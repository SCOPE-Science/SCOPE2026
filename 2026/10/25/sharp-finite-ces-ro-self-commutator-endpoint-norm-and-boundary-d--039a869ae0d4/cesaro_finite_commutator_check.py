#!/usr/bin/env python3
"""Exact finite-dimensional checks for a Cesaro self-commutator norm theorem.

Only the Python standard library is required. Finite checks are not used as
proof of the all-dimensional formulas or of the asymptotic expansion.
"""
from fractions import Fraction
from math import sqrt, fsum


def cesaro_matrix(n):
    return [[Fraction(1, i + 1) if j <= i else Fraction(0)
             for j in range(n)] for i in range(n)]


def exact_commutator(h):
    n = len(h)
    return [[sum((h[k][i] * h[k][j] - h[i][k] * h[j][k]
                   for k in range(n)), Fraction(0))
             for j in range(n)] for i in range(n)]


def closed_norm(n):
    # The kth coefficient of HH^T - H^TH is a_k.
    tails = [Fraction(0)] * (n + 2)
    for j in range(n, 0, -1):
        tails[j] = tails[j + 1] + Fraction(1, j * j)
    a = [Fraction(1, j) - tails[j] for j in range(1, n + 1)]
    neg = [j for j in range(1, n + 1) if a[j-1] < 0]
    m = max(neg)
    value = 2 * m * tails[m + 1]
    return value, m, a


def run():
    for n in range(2, 25):
        h = cesaro_matrix(n)
        k = exact_commutator(h)
        sharp, m, a = closed_norm(n)
        assert k == [[-a[max(i, j)] for j in range(n)] for i in range(n)]
        rows = [sum((abs(z) for z in row), Fraction(0)) for row in k]
        assert max(rows) == sharp, (n, max(rows), sharp)
        assert rows[0] == sharp
        if n >= 3:
            assert all(row < sharp for row in rows[1:]), n
        assert all(a[i] < a[i + 1] for i in range(n - 1))
        x = [Fraction(-1) if j < m else Fraction(1) for j in range(n)]
        # If there is a zero entry, the corresponding sign does not matter.
        top = sum((k[0][j] * x[j] for j in range(n)), Fraction(0))
        assert abs(top) == sharp
    for n in (200, 500, 1000, 2000, 5000, 10000, 50000):
        tail = 0.0
        vals = [0.0] * (n + 1)
        for j in range(n, 0, -1):
            tail += 1.0 / (j*j)
            vals[j] = tail
        m = max(j for j in range(1, n+1) if 1/j - vals[j] < 0)
        sharp = 2*m*vals[m+1]
        approx = 2 - 2*sqrt(2/n) + 2/(3*n)
        assert abs(sharp - approx) < 10/n**1.5, (n, sharp, approx)
        assert abs(m - sqrt(n/2)) < 3, (n, m)
    print('PASS: exact matrices, first-row maximizers, step witnesses,')
    print('and finite numerical checks of two-term boundary asymptotics.')


if __name__ == '__main__':
    run()
