#!/usr/bin/env python3
"""Finite consistency checks for three-cut complexes and their Alexander duals.

Uses only the Python standard library. These tests support, but do not replace,
the all-graphs elementary-collapse proof in RESULT.md.
"""
from itertools import combinations
from math import comb


def cycle_squares(edges, vertices):
    edge_set = {frozenset(e) for e in edges}
    squares = set()
    for a, b, c, d in combinations(range(vertices), 4):
        for order in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            sides = frozenset(frozenset((order[i], order[(i + 1) % 4])) for i in range(4))
            if sides <= edge_set:
                squares.add(sides)
    assert all(not (u & v) for u, v in combinations(squares, 2))
    return len(squares)


def finite_example(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    assert all(not (adj[a] & adj[b]) for a, b in edges), 'triangle-free input required'
    q = cycle_squares(edges, n)
    paths = sum(comb(len(nei), 2) for nei in adj)
    expected = comb(n - 1, 2) - paths + q
    disconnected = []
    for t in combinations(range(n), 3):
        edge_count = sum(b in adj[a] for a, b in combinations(t, 2))
        if edge_count < 2:
            disconnected.append(sum(1 << x for x in t))
    faces = set()
    for deleted in disconnected:
        f = ((1 << n) - 1) ^ deleted
        sub = f
        while sub:
            faces.add(sub)
            sub = (sub - 1) & f
    dimfaces = {d: sorted(v for v in faces if v.bit_count() == d + 1) for d in range(n)}
    pivots = []
    for d in range(n - 1):
        lower, upper = dimfaces[d], dimfaces[d + 1]
        columns = []
        idx = {v: i for i, v in enumerate(lower)}
        for mask in upper:
            col = 0
            for v in range(n):
                if (mask >> v) & 1:
                    col ^= 1 << idx[mask ^ (1 << v)]
            columns.append(col)
        basis = {}
        for col in columns:
            while col:
                p = col.bit_length() - 1
                if p in basis:
                    col ^= basis[p]
                else:
                    basis[p] = col
                    break
        pivots.append(len(basis))
    reduced = {}
    for d in range(n - 2):
        b = len(dimfaces[d]) - pivots[d] - (pivots[d - 1] if d else 1)
        if b:
            reduced[d] = b
    assert reduced == ({n - 4: expected} if expected else {}), (n, reduced, expected)
    # Dual triangle/tetrahedron count is a separate consistency condition.
    dual_tris = sum(
        sum(b in adj[a] for a, b in combinations(t, 2)) == 2
        for t in combinations(range(n), 3)
    )
    assert dual_tris == paths
    assert expected == comb(n - 1, 2) - dual_tris + q
    print('n=', n, 'squares=', q, 'faces=', len(faces),
          'reduced_Betti=', reduced, 'PASS')


if __name__ == '__main__':
    finite_example(8, [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),(6,7)])
    finite_example(8, [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),(6,3),(6,7)])
    finite_example(9, [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),(6,7),(7,8)])
    finite_example(8, [(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,2),(5,6),(6,7)])
    print('VERIFY_OK')
