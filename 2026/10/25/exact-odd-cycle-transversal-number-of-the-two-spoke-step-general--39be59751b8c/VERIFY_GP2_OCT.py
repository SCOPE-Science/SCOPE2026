#!/usr/bin/env python3
"""Reproduce a finite dual certificate for the odd-cycle transversal of GP(n,2).

No third-party packages are required.  Values -1 and +1 are bipartition
colours; 0 denotes a vertex deleted from the induced bipartite subgraph.
"""

from itertools import combinations

COLUMNS = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)
           if a == 0 or b == 0 or a != b]
STATES = [(p, q) for p in range(len(COLUMNS))
          for q in range(len(COLUMNS))
          if 0 in (COLUMNS[p][0], COLUMNS[q][0])
          or COLUMNS[p][0] != COLUMNS[q][0]]

# Integer potentials in the lexicographic 41-state order established above.
POTENTIAL = [0, 0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -2, 0, 0,
             0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0,
             -2, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0, 0]

# The sole recurrent strongly connected component of zero-reduced-cost arcs.
RECURRENT = {2, 3, 4, 5, 7, 8, 9, 11, 14, 15, 16,
             24, 25, 26, 29, 31, 32, 33, 35, 36, 37, 38}
LEVEL = {2: 0, 3: 3, 4: 0, 5: 2, 7: 1, 8: 2,
         9: 1, 11: 0, 14: 0, 15: 3, 16: 0,
         24: 2, 25: 1, 26: 2, 29: 2, 31: 3,
         32: 0, 33: 3, 35: 0, 36: 2, 37: 1, 38: 2}

# Each tuple is an (outer, inner) column.  All words start at the same
# automaton state: last column (-1,0), first column (0,1).
WORDS = {
    4: [(0, 1), (-1, 1), (1, -1), (-1, 0)],
    5: [(0, 1), (-1, 1), (1, -1), (0, -1), (-1, 0)],
    6: [(0, 1), (-1, 1), (1, -1), (-1, 0), (1, 0), (-1, 0)],
    7: [(0, 1), (-1, 1), (1, -1), (-1, 0), (0, 1), (1, -1), (-1, 0)],
    8: [(0, 1), (-1, 1), (1, -1), (-1, 0), (0, 1),
        (-1, 1), (1, -1), (-1, 0)],
}


def arcs():
    idx = {s: i for i, s in enumerate(STATES)}
    a = []
    for i, (p, q) in enumerate(STATES):
        for r, (outer, inner) in enumerate(COLUMNS):
            # Outer rim constraint at positions i+1 and i+2.
            if outer and COLUMNS[q][0] and outer == COLUMNS[q][0]:
                continue
            # Inner rim constraint at positions i and i+2.
            if inner and COLUMNS[p][1] and inner == COLUMNS[p][1]:
                continue
            j = idx[(q, r)]
            w = (outer == 0) + (inner == 0)
            a.append((i, j, w))
    return a


def scc(n, edges):
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j)
        rev[j].append(i)
    seen, order = set(), []
    def dfs(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                dfs(w)
        order.append(v)
    for v in range(n):
        if v not in seen:
            dfs(v)
    seen.clear()
    comps = []
    def reverse_dfs(v, comp):
        seen.add(v)
        comp.add(v)
        for w in rev[v]:
            if w not in seen:
                reverse_dfs(w, comp)
    for v in reversed(order):
        if v not in seen:
            c = set()
            reverse_dfs(v, c)
            comps.append(c)
    return comps


def check_cyclic_word(w):
    n = len(w)
    if n < 4 or not all(c in COLUMNS for c in w):
        return False
    for i in range(n):
        ai, bi = w[i]
        aj = w[(i + 1) % n][0]
        bk = w[(i + 2) % n][1]
        if ai and aj and ai == aj:
            return False
        if bi and bk and bi == bk:
            return False
    return True


def candidate_cost(w):
    return sum((x == 0) + (y == 0) for x, y in w)


def claim(n):
    assert n >= 5
    return (n + 1) // 2 + (n % 4 == 2)


def certificate():
    assert len(COLUMNS) == 7 and len(STATES) == 41
    assert len(POTENTIAL) == len(STATES)
    E = arcs()
    assert len(E) == len(set(E))
    assert all(2 * w - 1 + POTENTIAL[i] - POTENTIAL[j] >= 0
               for i, j, w in E)
    tight = [(i, j) for i, j, w in E
             if 2 * w - 1 + POTENTIAL[i] - POTENTIAL[j] == 0]
    comps = scc(len(STATES), tight)
    tight_set = set(tight)
    cyclic = [c for c in comps
              if len(c) > 1 or any((i, i) in tight_set for i in c)]
    assert len(cyclic) == 1 and cyclic[0] == RECURRENT
    assert set(LEVEL) == RECURRENT
    assert all((LEVEL[j] - LEVEL[i]) % 4 == 1
               for i, j in tight if i in RECURRENT and j in RECURRENT)

    # Every minimum cost closed walk of even length with total cost n/2
    # consists exclusively of tight arcs.  Thus it must remain in RECURRENT
    # and its length is 0 modulo 4 by the LEVEL labelling.
    for k, w in WORDS.items():
        assert len(w) == k and check_cyclic_word(w)
        assert w[-1] == (-1, 0) and w[0] == (0, 1)
        assert candidate_cost(w) == (2 if k == 4 else claim(k))
    for base in (5, 6, 7, 8):
        for blocks in range(7):
            word = WORDS[base] + WORDS[4] * blocks
            n = len(word)
            assert check_cyclic_word(word), (base, blocks)
            assert candidate_cost(word) == claim(n), (base, blocks)
    print('CERTIFICATE_OK states=41 tight_arcs=%d recurrent_states=%d'
          % (len(tight), len(RECURRENT)))


def brute_check(n):
    # Independent check based directly on deleting subsets of vertices and
    # testing each residual graph for bipartiteness.  No transfer states.
    m = 2 * n
    adj = [[] for _ in range(m)]
    for i in range(n):
        for a, b in ((i, (i + 1) % n),
                     (i, n + i),
                     (n + i, n + (i + 2) % n)):
            adj[a].append(b)
            adj[b].append(a)
    def bipartite_without(removed):
        removed = set(removed)
        side = [-1] * m
        for start in range(m):
            if start in removed or side[start] != -1:
                continue
            side[start] = 0
            queue = [start]
            for v in queue:
                for u in adj[v]:
                    if u in removed:
                        continue
                    if side[u] == -1:
                        side[u] = 1 - side[v]
                        queue.append(u)
                    elif side[u] == side[v]:
                        return False
        return True
    k = claim(n)
    assert not any(bipartite_without(s)
                   for s in combinations(range(m), k - 1)), n
    count = sum(bipartite_without(s)
                for s in combinations(range(m), k))
    assert count > 0
    print('INDEPENDENT_BRUTE_OK n=%d minimum=%d attaining_sets=%d'
          % (n, k, count))


if __name__ == '__main__':
    certificate()
    for n in range(5, 13):
        brute_check(n)
    print('VERIFY_OK')
