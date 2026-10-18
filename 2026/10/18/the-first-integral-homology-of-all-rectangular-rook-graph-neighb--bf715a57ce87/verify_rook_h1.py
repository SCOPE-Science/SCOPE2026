#!/usr/bin/env python3
"""Finite computational consistency checks for the integral H_1 theorem for rook neighborhoods.

Uses only the Python standard library. The all-parameter theorem is proved
algebraically; these computations check examples and proposed cochains.
"""
from itertools import combinations
import json


def neighborhood_triangles(rows, columns):
    positions = [(r, c) for r in range(rows) for c in range(columns)]
    neighborhoods = [
        {v for v, (s, d) in enumerate(positions)
         if (s == r) != (d == c)}
        for r, c in positions
    ]
    assert all(len(t) == rows + columns - 2 for t in neighborhoods)
    edge_set = {
        pair for pair in combinations(range(len(positions)), 2)
        if any(set(pair) <= N for N in neighborhoods)
    }
    assert len(edge_set) == len(positions) * (len(positions) - 1) // 2
    triangles = [
        triple for triple in combinations(range(len(positions)), 3)
        if any(set(triple) <= N for N in neighborhoods)
    ]
    return positions, triangles


def raw_label(rows, columns, x, y, t=1, s=0):
    """Oriented integer cocycle for 3-row cases or mod-2 for large cases."""
    if x == y:
        return 0
    if x > y:
        return -raw_label(rows, columns, y, x, t, s)
    (i, j), (k, l) = divmod(x, columns), divmod(y, columns)
    if rows >= 4 and columns >= 4:
        # Values are interpreted modulo 2. Orientation is immaterial.
        return int(i != k and j != l)
    if rows != 3:
        raise ValueError("This independent cocycle constructor uses rows=3")
    if x == 0:
        return 0
    cat = lambda a, b: 'A' if a == 0 else ('B' if b == 0 else 'C')
    X, Y = cat(i, j), cat(k, l)
    if columns >= 4:
        trow = {1: t, 2: -t}
        if (X, Y) == ('A', 'A'): return 0
        if (X, Y) == ('B', 'B'): return -2*t
        if (X, Y) == ('A', 'B'): return trow[k]
        if (X, Y) == ('B', 'A'): return -trow[i]
        if (X, Y) == ('A', 'C'): return -trow[k] if j == l else 0
        if (X, Y) == ('C', 'A'): return trow[i] if j == l else 0
        if (X, Y) == ('B', 'C'): return -trow[i] if i == k else 0
        if (X, Y) == ('C', 'B'): return trow[k] if i == k else 0
        if (X, Y) == ('C', 'C'):
            if j == l or i == k: return 0
            return t if (i, k) == (1, 2) else -t
        raise AssertionError((X, Y))
    # 3x3. Here t=t_{22}, s=u(b_2,b_3), p=2t+s.
    tval = {(1, 1): t, (1, 2): -t-s,
            (2, 1): t+s, (2, 2): -t}
    if (X, Y) == ('A', 'A'): return 2*t+s
    if (X, Y) == ('B', 'B'): return s
    if (X, Y) == ('A', 'B'): return tval[k, j]
    if (X, Y) == ('B', 'A'): return -tval[i, l]
    if (X, Y) == ('A', 'C'): return tval[3-k, j] if j == l else 0
    if (X, Y) == ('C', 'A'): return -tval[3-i, l] if j == l else 0
    if (X, Y) == ('B', 'C'): return -tval[i, 3-l] if i == k else 0
    if (X, Y) == ('C', 'B'): return tval[k, 3-j] if i == k else 0
    if (X, Y) == ('C', 'C'):
        return -tval[3-i, j] if (i != k and j != l) else 0
    raise AssertionError((X, Y))


def rank_mod(rows, modulus):
    """Rank of sparse column vectors over a prime field."""
    pivots = {}
    for vec in rows:
        vec = {k: v % modulus for k, v in vec.items() if v % modulus}
        while vec:
            k = min(vec)
            if k not in pivots:
                inv = pow(vec[k], -1, modulus)
                pivots[k] = {j: v * inv % modulus for j, v in vec.items()}
                break
            factor = vec[k]
            for j, value in pivots[k].items():
                new = (vec.get(j, 0) - factor * value) % modulus
                if new:
                    vec[j] = new
                else:
                    vec.pop(j, None)
    return len(pivots)


def verify_case(m, n):
    positions, triangles = neighborhood_triangles(m, n)
    schemes = ((1, 0), (0, 1)) if (m, n) == (3, 3) else ((1, 0),)
    for t, s in schemes:
        for a, b, c in triangles:
            defect = (raw_label(m,n,a,b,t,s) +
                      raw_label(m,n,b,c,t,s) +
                      raw_label(m,n,c,a,t,s))
            if m >= 4: defect %= 2
            assert defect == 0, (m, n, (a,b,c), t,s,defect)
    N = len(positions)
    free_edges = list(combinations(range(1, N), 2))
    edge_ids = {e:i for i,e in enumerate(free_edges)}
    columns = []
    for a,b,c in triangles:
        vec = {}
        for edge, sign in (((b,c),1), ((a,c),-1), ((a,b),1)):
            if edge[0] != 0: vec[edge_ids[edge]] = sign
        columns.append(vec)
    h1_dims = {
        str(p): len(free_edges) - rank_mod(columns, p)
        for p in (2, 3, 5)
    }
    if m == n == 3: target = {'2': 2, '3': 2, '5': 2}
    elif min(m,n) == 3: target = {'2': 1, '3': 1, '5': 1}
    else: target = {'2': 1, '3': 0, '5': 0}
    assert h1_dims == target, (m,n,h1_dims,target)
    return {'board':[m,n], 'vertices':N, 'edges':N*(N-1)//2,
            'triangles':len(triangles), 'H1_field_dimensions':h1_dims,
            'explicit_cocycles':'passed'}


def main():
    tests = [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5)]
    values = [verify_case(*shape) for shape in tests]
    print(json.dumps({'status':'ROOK_H1_FINITE_CHECKS_OK',
                      'interpretation':'finite consistency checks, not proof for all m,n',
                      'cases':values}, separators=(',',':')))

if __name__ == '__main__':
    main()
