#!/usr/bin/env python3
"""Exact GF(2) checker for periodic square-cluster checkerboard entanglement.
Uses bit-mask elimination; no quantum-state or scientific-analysis dependencies.
"""
from math import gcd


def rank2(rows, ncols):
    a = list(rows)
    r = 0
    for col in range(ncols):
        p = next((i for i in range(r, len(a)) if (a[i] >> col) & 1), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(r + 1, len(a)):
            if (a[i] >> col) & 1:
                a[i] ^= a[r]
        r += 1
    return r


def torus_biadjacency(m, n):
    assert m >= 4 and n >= 4 and m % 2 == 0 and n % 2 == 0
    black = [(i, j) for i in range(m) for j in range(n) if (i + j) % 2 == 0]
    white = [(i, j) for i in range(m) for j in range(n) if (i + j) % 2 == 1]
    wi = {z: i for i, z in enumerate(white)}
    rows = []
    edges = []
    for u, (i, j) in enumerate(black):
        neighbors = [((i+1) % m, j), ((i-1) % m, j),
                     (i, (j+1) % n), (i, (j-1) % n)]
        assert len(set(neighbors)) == 4
        row = 0
        for x in neighbors:
            v = wi[x]
            row ^= 1 << v
            edges.append((u, v))
        rows.append(row)
    return rows, edges, len(white)


def check():
    test_count = edge_count = 0
    print('Checker: periodic cluster-state bipartition, exact GF(2)')
    for m in range(4, 19, 2):
        for n in range(4, 19, 2):
            rows, edges, width = torus_biadjacency(m, n)
            expected = m*n//2 - gcd(m, n)
            got = rank2(rows, width)
            assert got == expected, (m, n, expected, got)
            test_count += 1
            for u,v in (edges if m <= 8 and n <= 8 else edges[:1]):
                altered = rows.copy()
                assert (altered[u] >> v) & 1
                altered[u] ^= 1 << v
                assert rank2(altered, width) == expected + 1, (m,n,u,v)
                edge_count += 1
    print('Exact grid cases:', test_count)
    print('Exact one-edge deletion cases:', edge_count)
    for m, n in [(4,4),(4,6),(6,6),(6,10),(8,12),(10,10)]:
        rows, _, width = torus_biadjacency(m,n)
        print('m={}, n={}, cut-rank={}, defect={}, post-one-edge={}'.format(
            m,n,rank2(rows,width),gcd(m,n),rank2(rows,width)+1))
    print('PASS')

if __name__ == '__main__':
    check()
