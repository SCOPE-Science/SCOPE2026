"""Independent exhaustive checks for edge general-position counting on trees.

Python >=3.8, standard library only. No network or external data.
"""
from collections import deque
from itertools import product
from math import comb
from random import Random


def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    return out


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def edge_gp_polynomial(n, edges):
    assert n >= 1 and len(edges) == n - 1
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def descend(v, parent):
        # Polynomials indexed by greatest root-to-vertex selected-edge count 0,1,2.
        states = [[1], [], []]
        for w in graph[v]:
            if w == parent:
                continue
            child = descend(w, v)
            branches = [[], [], []]
            for a in range(3):
                if not child[a]:
                    continue
                for b in (0, 1):
                    h = a + b
                    if h <= 2:
                        shifted = ([0] if b else []) + child[a]
                        branches[h] = add(branches[h], shifted)
            nxt = [[], [], []]
            for a in range(3):
                if not states[a]:
                    continue
                for h in range(3):
                    if not branches[h] or a + h > 2:
                        continue
                    k = max(a, h)
                    nxt[k] = add(nxt[k], mul(states[a], branches[h]))
            states = nxt
        return states

    states = descend(0, -1)
    out = []
    for s in states:
        out = add(out, s)
    return out


def independent_path_masks(n, edges):
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
    masks = []
    for start in range(n):
        parent = [-1] * n
        ein = [-1] * n
        parent[start] = start
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for w, i in graph[v]:
                if parent[w] == -1:
                    parent[w] = v
                    ein[w] = i
                    queue.append(w)
        for finish in range(start + 1, n):
            x, mask = finish, 0
            while x != start:
                mask |= 1 << ein[x]
                x = parent[x]
            masks.append(mask)
    return masks


def brute(n, edges):
    pm = independent_path_masks(n, edges)
    result = [0] * n
    for subset in range(1 << (n - 1)):
        if all((subset & mask).bit_count() <= 2 for mask in pm):
            result[subset.bit_count()] += 1
    return result


def prufer_edges(seq):
    n = len(seq) + 2
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = [i for i, d in enumerate(degree) if d == 1]
    edges.append((a, b))
    return edges


def check(n, edges):
    got = edge_gp_polynomial(n, edges)
    want = brute(n, edges)
    assert got == want[:len(got)] and not any(want[len(got):]), (n, edges, got, want)
    assert got[0] == 1
    if n >= 2:
        assert got[1] == n - 1
    if n >= 3:
        assert got[2] == comb(n - 1, 2)
    return 1 << (n - 1)


def main():
    cases = 0
    subsets = 0
    for n in range(1, 8):
        for seq in product(range(n), repeat=max(0, n - 2)) if n >= 2 else [()]:
            e = prufer_edges(seq) if n >= 2 else []
            subsets += check(n, e)
            cases += 1
    rng = Random(15032026)
    for n, reps in [(8, 200), (9, 120), (10, 80), (11, 50), (12, 30), (13, 15)]:
        for _ in range(reps):
            e = prufer_edges([rng.randrange(n) for _ in range(n - 2)])
            subsets += check(n, e)
            cases += 1

    for m in range(0, 60):
        # Star and path are independent exact-combinatorial boundary checks.
        star = [(0, i + 1) for i in range(m)]
        path = [(i, i + 1) for i in range(m)]
        assert edge_gp_polynomial(m + 1, star) == [comb(m, k) for k in range(m + 1)]
        assert edge_gp_polynomial(m + 1, path) == (
            [1] if m == 0 else [1, m] if m == 1 else [1, m, comb(m, 2)]
        )
    for a in range(1, 11):
        for b in range(1, 11):
            # Two nonleaf centers joined by one edge.
            edges = [(0, 1)] + [(0, i + 2) for i in range(a)] + [
                (1, a + 2 + i) for i in range(b)
            ]
            numerator = [comb(a + b, k) for k in range(a + b + 1)]
            supplementary = add([comb(a, k) for k in range(a + 1)],
                                [comb(b, k) for k in range(b + 1)])
            supplementary[0] -= 1
            expected = add(numerator, [0] + supplementary)
            assert edge_gp_polynomial(a + b + 2, edges) == expected
    print('VERIFICATION_OK', 'tree_cases=' + str(cases), 'edge_subsets=' + str(subsets),
          'star_path_orders=1..60', 'double_star_profiles=100')

if __name__ == '__main__':
    main()
