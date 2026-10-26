"""Exact census for the first failure of degree-first weak positional bias on trees.
Only the Python standard library is used.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import defaultdict
from heapq import heapify, heappop, heappush


def from_prufer(n, code):
    d = [1] * n
    for v in code: d[v] += 1
    leaves = [u for u in range(n) if d[u] == 1]
    heapify(leaves)
    edges = []
    for v in code:
        u = heappop(leaves)
        edges.append((u, v))
        d[u] -= 1
        d[v] -= 1
        if d[v] == 1: heappush(leaves, v)
    u = heappop(leaves)
    v = heappop(leaves)
    edges.append((u, v))
    return tuple(edges)


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return tuple(tuple(sorted(a)) for a in adj)


def canonical(adj):
    n = len(adj)
    d = [len(a) for a in adj]
    leaves = [i for i, z in enumerate(d) if z <= 1]
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new = []
        for u in leaves:
            for v in adj[u]:
                d[v] -= 1
                if d[v] == 1:
                    new.append(v)
            d[u] = 0
        leaves = new
    def rooted(u, parent):
        return '(' + ''.join(sorted(rooted(v, u) for v in adj[u] if v != parent)) + ')'
    return min(rooted(u, -1) for u in leaves)


def linear_solve(A, b):
    n = len(b)
    A = [list(row) + [b[i]] for i, row in enumerate(A)]
    for j in range(n):
        k = next((k for k in range(j, n) if A[k][j]), None)
        assert k is not None, 'coalescence system singular'
        A[j], A[k] = A[k], A[j]
        t = A[j][j]
        if t != 1:
            A[j][j:] = [v / t for v in A[j][j:]]
        for i in range(n):
            if i == j or A[i][j] == 0: continue
            t = A[i][j]
            A[i][j:] = [a - t * c for a, c in zip(A[i][j:], A[j][j:])]
    return [row[-1] for row in A]


def weak_scores(adj):
    n = len(adj)
    m = sum(map(len, adj)) // 2
    deg = [len(a) for a in adj]
    pairs = list(combinations(range(n), 2))
    ix = {p: i for i, p in enumerate(pairs)}
    M = [[Q(0) for _ in pairs] for _ in pairs]
    for k, (u, v) in enumerate(pairs):
        M[k][k] = Q(2)
        for z in adj[u]:
            if z != v:
                M[k][ix[tuple(sorted((z, v)))]] -= Q(1, deg[u])
        for z in adj[v]:
            if z != u:
                M[k][ix[tuple(sorted((u, z)))]] -= Q(1, deg[v])
    psi = linear_solve(M, [Q(1) for _ in pairs])
    assert all(z > 0 for z in psi)
    assert all(sum(M[i][j] * psi[j] for j in range(len(pairs))) == 1 for i in range(len(pairs)))
    out = []
    for u in range(n):
        h = sum((psi[ix[(v, w)]] for v, w in combinations(adj[u], 2)), Q(0))
        out.append(h / (n * m * deg[u]))
    return out


def census():
    expected = {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23}
    for n in range(2, 9):
        classes = {}
        for code in product(range(n), repeat=n-2):
            edges = from_prufer(n, code)
            adj = adjacency(n, edges)
            classes.setdefault(canonical(adj), adj)
        assert len(classes) == expected[n], (n, len(classes))
        bad = 0
        for adj in classes.values():
            h = weak_scores(adj)
            degrees = [len(x) for x in adj]
            dmax = max(degrees)
            max_degree_best = max(h[u] for u in range(n) if degrees[u] == dmax)
            if max(h) > max_degree_best:
                bad += 1
        print('n=', n, 'tree_isomorphism_classes=', len(classes), 'strict_degree_failures=', bad)
        assert bad == 0


def witness():
    # 0 is a degree-three hub. 1 is the unique degree-four hub.
    edges = ((0, 5), (0, 7), (1, 0), (1, 2), (1, 3), (1, 4), (5, 6), (7, 8))
    adj = adjacency(9, edges)
    h = weak_scores(adj)
    print('witness_edges=', edges)
    for i, z in enumerate(h): print('vertex=', i, 'degree=', len(adj[i]), 'weak_slope=', z, 'decimal=', float(z))
    gap = h[0] - h[1]
    print('strict_gap=', gap, 'decimal=', float(gap))
    assert len(adj[0]) == 3 and len(adj[1]) == 4
    assert gap > 0 and all(h[0] > h[i] for i in range(1, 9))

if __name__ == '__main__':
    census()
    witness()
    print('ALL EXACT CHECKS PASSED')
