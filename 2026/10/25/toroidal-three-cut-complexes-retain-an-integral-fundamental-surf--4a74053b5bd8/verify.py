#!/usr/bin/env python3
"""Reproduce exact simplicial-collapse checks for periodic square grids.

Only Python's standard library is required.  This checker examines the
combinatorial Alexander dual of the ordinary three-cut complex.  The
uniform statement rests on a separate structural proof, not extrapolation
from finitely many grids.
"""
from itertools import combinations
from collections import Counter


def grid(m, n):
    assert m >= 5 and n >= 5
    v = tuple(range(m * n))
    at = lambda i, j: (i % m) * n + (j % n)
    edges = set()
    squares = []
    for i in range(m):
        for j in range(n):
            a = at(i, j)
            b = at(i + 1, j)
            c = at(i + 1, j + 1)
            d = at(i, j + 1)
            edges.add(tuple(sorted((a, b))))
            edges.add(tuple(sorted((a, d))))
            squares.append((a, b, c, d))
    return v, edges, squares


def dist2_pairs(vertices, edges):
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    common = {}
    for a, b in combinations(vertices, 2):
        if (a, b) not in edges:
            common[(a, b)] = adj[a] & adj[b]
    return adj, common


def check(m, n):
    vertices, graph_edges, squares = grid(m, n)
    N = len(vertices)
    assert len(graph_edges) == 2 * N
    assert len({frozenset(s) for s in squares}) == N
    adj, common = dist2_pairs(vertices, graph_edges)
    assert all(len(adj[v]) == 4 for v in vertices)
    assert not any((b in adj[a] and c in adj[a] and c in adj[b])
                   for a, b, c in combinations(vertices, 3))
    dist2 = {p for p, C in common.items() if C}
    straight = {p for p, C in common.items() if len(C) == 1}
    diagonals = {p for p, C in common.items() if len(C) == 2}
    distant = {p for p, C in common.items() if not C}
    assert len(straight) == 2 * N
    assert len(diagonals) == 2 * N
    assert len(distant) == N * (N - 13) // 2
    assert len(dist2) == 4 * N
    assert len(common) == N * (N - 1) // 2 - 2 * N
    assert all(len(c) in (0, 1, 2) for c in common.values())

    # Construct dual faces directly from the connectivity criterion.
    triangles = set()
    for t in combinations(vertices, 3):
        e = sum((a in adj[b]) for a, b in combinations(t, 2))
        if e >= 2:
            assert e == 2
            triangles.add(t)
    tet = set()
    for z in combinations(vertices, 4):
        if all(tuple(sorted(t)) in triangles for t in combinations(z, 3)):
            tet.add(z)
    expected_tet = {tuple(sorted(s)) for s in squares}
    assert tet == expected_tet
    assert len(triangles) == 6 * N
    assert len(tet) == N
    if N <= 30:
        for z in combinations(vertices, 5):
            assert not all(tuple(sorted(t)) in triangles for t in combinations(z, 3))

    layers = {0: set((v,) for v in vertices),
              1: set(combinations(vertices, 2)),
              2: triangles.copy(), 3: tet.copy()}

    def collapse(low, high):
        low, high = tuple(sorted(low)), tuple(sorted(high))
        a, b = len(low) - 1, len(high) - 1
        assert b == a + 1 and set(low) <= set(high)
        assert low in layers[a] and high in layers[b]
        assert sum(set(low) <= set(z) for z in layers[b]) == 1
        assert all(not set(low) <= set(z) for d in range(b + 1, 4)
                   for z in layers[d])
        layers[a].remove(low)
        layers[b].remove(high)

    # Collapse every square tetrahedron across an exclusive triangular face.
    # Then remove its a--c diagonal across the other path triangle.
    for a, b, c, d in squares:
        collapse((a, b, c), (a, b, c, d))
    assert not layers[3]
    for a, b, c, d in squares:
        collapse((a, c), (a, c, d))
    for (a, c) in sorted(straight):
        w, = common[(a, c)]
        collapse((a, c), (a, w, c))
    assert len(layers[2]) == 2 * N
    assert len(layers[1]) == 3 * N + len(distant)
    expected_triangles = {
        tuple(sorted(t))
        for a, b, c, d in squares
        for t in ((a, b, d), (b, c, d))
    }
    retained_diagonals = {tuple(sorted((b, d))) for a, b, c, d in squares}
    assert len(retained_diagonals) == N
    assert layers[2] == expected_triangles
    assert layers[1] == graph_edges | retained_diagonals | distant
    assert len(layers[0]) == N

    # The squares have exactly two incident sides per graph edge and a
    # connected square-adjacency graph, as in a closed orientable torus.
    square_boundary = Counter()
    for a, b, c, d in squares:
        for x, y in ((a, b), (b, c), (c, d), (d, a)):
            square_boundary[tuple(sorted((x, y)))] += 1
    assert set(square_boundary) == graph_edges
    assert set(square_boundary.values()) == {2}
    # Global oriented two-cycle: positive-oriented triangle sum has zero
    # simplicial boundary, including cancellation along retained diagonals.
    boundary = Counter()
    for a, b, c, d in squares:
        for x, y, z in ((a, b, d), (b, c, d)):
            for p, q, sign in ((y, z, 1), (x, z, -1), (x, y, 1)):
                u, v = sorted((p, q))
                boundary[(u, v)] += sign * (1 if (p, q) == (u, v) else -1)
    assert all(z == 0 for z in boundary.values())
    assert len(boundary) == len(graph_edges) + N

    print('PASS', m, n, 'N', N,
          'dual_f', (N, N*(N-1)//2, 6*N, N),
          'collapses', 4*N,
          'torus_triangles', 2*N,
          'long_edges', len(distant),
          'cut_homology_degrees', (N-5, N-4),
          'cut_homology_ranks', (1, 2+len(distant)))


if __name__ == '__main__':
    for parameters in ((5, 5), (5, 6), (6, 6), (5, 7)):
        check(*parameters)
    print('VERIFY_OK')
