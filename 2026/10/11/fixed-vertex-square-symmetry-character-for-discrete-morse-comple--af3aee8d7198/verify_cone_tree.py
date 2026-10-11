"""Exact finite checks for the cone-over-tree Morse-complex character theorem.
Uses only Python's standard library; theorem for all finite trees is proved separately.
Run: python verify_cone_tree.py
"""
from itertools import product, permutations
from collections import Counter
from heapq import heapify, heappop, heappush


def tree_from_prufer(seq, n):
    degrees = [1] * n
    for x in seq:
        degrees[x] += 1
    leaves = [i for i in range(n) if degrees[i] == 1]
    heapify(leaves)
    edges = []
    for x in seq:
        u = heappop(leaves)
        edges.append((min(u, x), max(u, x)))
        degrees[u] -= 1
        degrees[x] -= 1
        if degrees[x] == 1:
            heappush(leaves, x)
    u = heappop(leaves); v = heappop(leaves)
    edges.append((min(u, v), max(u, v)))
    return tuple(sorted(edges))


def rooted_code(edges, n, v, par=-1):
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b); adjacency[b].append(a)
    def rec(x, parent):
        return '(' + ''.join(sorted(rec(y, x) for y in adjacency[x] if y != parent)) + ')'
    return rec(v, par)


def unlabelled_trees(n):
    representatives = {}
    for seq in product(range(n), repeat=n-2):
        E = tree_from_prufer(seq, n)
        key = min(rooted_code(E, n, r) for r in range(n))
        representatives.setdefault(key, E)
    return list(representatives.values())


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 else 1


def automorphisms(E, n):
    Es = set(E)
    deg = [0] * n
    for u, v in E:
        deg[u] += 1; deg[v] += 1
    for p in permutations(range(n)):
        if any(deg[i] != deg[p[i]] for i in range(n)):
            continue
        if all((min(p[u], p[v]), max(p[u], p[v])) in Es for u, v in E):
            yield p


def signed_fixed_forest_sum(E, n, perm):
    hub = n
    p = tuple(perm) + (hub,)
    adjacency = [set() for _ in range(n + 1)]
    for u, v in E:
        adjacency[u].add(v); adjacency[v].add(u)
    for u in range(n):
        adjacency[u].add(hub); adjacency[hub].add(u)
    orbit_list = []
    visited = set()
    for v in range(n + 1):
        if v in visited:
            continue
        orb = []
        a = v
        while a not in visited:
            visited.add(a); orb.append(a); a = p[a]
        assert a == v
        orbit_list.append(orb)
    possibilities = []
    for orb in orbit_list:
        q = len(orb)
        choices = [()]
        for t in adjacency[orb[0]]:
            destinations = []
            w = t
            for _ in range(q):
                destinations.append(w); w = p[w]
            if w != t:
                continue
            if all(destinations[j] in adjacency[orb[j]] for j in range(q)):
                choices.append(tuple(zip(orb, destinations)))
        possibilities.append(choices)
    total = 0
    for selection in product(*possibilities):
        f = {a: b for choice in selection for a, b in choice}
        acyclic = True
        for start in f:
            chain = set(); a = start
            while a in f and a not in chain:
                chain.add(a); a = f[a]
            if a in chain:
                acyclic = False; break
        if acyclic:
            total += (-1) ** sum(bool(choice) for choice in selection)
    return (-1)**n * total


def rank_mod2(columns):
    basis = {}
    for x in columns:
        while x:
            pivot = x.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = x
                break
            x ^= basis[pivot]
    return len(basis)


def check_homology(E, n):
    # Include the empty face and all oriented rooted forests explicitly.
    hub = n
    arcs = sorted({(v, w) for u, t in list(E)+[(i, hub) for i in range(n)]
                   for v, w in ((u, t), (t, u))})
    faces = [set() for _ in range(n + 1)]
    faces[0].add(())
    def acyclic_set(arcs_chosen):
        m = {u: v for u, v in arcs_chosen}
        if len(m) != len(arcs_chosen):
            return False
        for z in m:
            seen = set(); a = z
            while a in m and a not in seen:
                seen.add(a); a = m[a]
            if a in seen:
                return False
        return True
    for k in range(1, n + 1):
        from itertools import combinations
        for s in combinations(arcs, k):
            if acyclic_set(s):
                faces[k].add(s)
    # The simplicial dimension is n-1; a k-arrow forest is a (k-1)-face.
    fcounts = [len(x) for x in faces]
    ranks = [0] * (n + 1)
    for k in range(1, n + 1):
        order = {face: i for i, face in enumerate(sorted(faces[k-1]))}
        cols = []
        for face in sorted(faces[k]):
            mask = 0
            for i in range(k):
                smaller = face[:i] + face[i+1:]
                mask ^= 1 << order[smaller]
            cols.append(mask)
        ranks[k] = rank_mod2(cols)
    bettis = [fcounts[k] - ranks[k] - (ranks[k+1] if k < n else 0) for k in range(n+1)]
    expected = [0] * (n+1)
    expected[n] = n*n
    assert bettis == expected, (E, fcounts, ranks, bettis, expected)
    return fcounts, bettis


def main():
    tested = 0; types = 0; homology_tests = 0
    for n in range(2, 8):
        trees = unlabelled_trees(n)
        for E in trees:
            types += 1
            for p in automorphisms(E, n):
                actual = signed_fixed_forest_sum(E, n, p)
                fixed = sum(p[i] == i for i in range(n))
                expected = parity(p) * fixed**2
                assert actual == expected, (E, n, p, actual, expected)
                tested += 1
            if n <= 4:
                check_homology(E, n)
                homology_tests += 1
        print('n=%d unlabeled_trees=%d' % (n, len(trees)))
    assert tested == 967, tested
    assert types == 24, types
    assert homology_tests == 4, homology_tests
    print('VERIFY_OK trees=%d automorphisms=%d homology_cases=%d' % (types, tested, homology_tests))

if __name__ == '__main__':
    main()
