#!/usr/bin/env python3
"""Exact-rational independent reconstruction of two canonical graph projections.

No mathematical novelty or independent certification is asserted by this checker.
It tests finite cases, not the all-parameter group-representation argument.
"""
from fractions import Fraction as F


def inverse(A):
    n = len(A)
    H = [[F(A[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if H[i][k])
        H[k], H[p] = H[p], H[k]
        z = H[k][k]
        H[k] = [v / z for v in H[k]]
        for i in range(n):
            if i != k:
                z = H[i][k]
                if z:
                    H[i] = [x - z * y for x, y in zip(H[i], H[k])]
    return [v[n:] for v in H]


def verify(n):
    edges = [(i, n + j) for i in range(n) for j in range(n) if i != j]
    size = 2 * n - 1
    L = [[0 for _ in range(size)] for _ in range(size)]
    for a, b in edges:
        if a < size:
            L[a][a] += 1
        if b < size:
            L[b][b] += 1
        if a < size and b < size:
            L[a][b] -= 1
            L[b][a] -= 1
    H = inverse(L)
    m = len(edges)
    Q = [[F(0) for _ in range(m)] for _ in range(m)]
    for col, (a, b) in enumerate(edges):
        z = [F(int(i == a) - int(i == b)) for i in range(size)]
        p = [sum(H[i][j] * z[j] for j in range(size)) for i in range(size)] + [F(0)]
        for row, (c, d) in enumerate(edges):
            Q[row][col] = p[c] - p[d]
    C = [[F(int(i == j)) - Q[i][j] for j in range(m)] for i in range(m)]
    q = F(3 * n - 4, n)
    c = F(2 * (2 * n * n - 6 * n + 3), n * (n - 1))
    resistance = F(2 * n - 1, n * (n - 1))
    for i in range(m):
        assert sum(abs(Q[j][i]) for j in range(m)) == q, (n, i, 'Q')
        assert sum(abs(C[j][i]) for j in range(m)) == c, (n, i, 'C')
        assert Q[i][i] == resistance, (n, i, 'R')
        for j in range(m):
            assert Q[i][j] == Q[j][i], (n, i, j, 'symmetry')
    for col in range(m):
        for vertex in range(2 * n):
            flow = sum((int(a == vertex) - int(b == vertex)) * C[i][col]
                       for i, (a, b) in enumerate(edges))
            assert flow == 0, (n, col, vertex, 'cycle')
    if n <= 6:
        for i in range(m):
            for j in range(m):
                assert sum(Q[i][k] * Q[k][j] for k in range(m)) == Q[i][j]
    return m

if __name__ == '__main__':
    counts = [(n, verify(n)) for n in range(3, 11)]
    print('PASS exact rational crown-graph columns:', counts)
    print('TOTAL columns:', sum(count for _, count in counts))
    print('Finite tests are not a proof of the infinite-family theorem.')
