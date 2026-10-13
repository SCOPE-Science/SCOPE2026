#!/usr/bin/env python3
"""Exact-arithmetic finite checks for a discrete path observation determinant theorem.

Usage: python3 checker.py. No external packages required.
This does not replace the all-dimensional proof.
"""
from fractions import Fraction as F
from math import gcd


def matrix_det(m):
    a = [row[:] for row in m]
    n = len(a)
    ans = F(1)
    for i in range(n):
        pivot = next((p for p in range(i, n) if a[p][i] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            ans = -ans
        x = a[i][i]
        ans *= x
        for p in range(i + 1, n):
            if a[p][i]:
                q = a[p][i] / x
                for c in range(i + 1, n):
                    a[p][c] -= q * a[i][c]
                a[p][i] = F(0)
    return ans


def matrix_rank(m):
    a = [row[:] for row in m]
    n = len(a)
    r = 0
    for c in range(n):
        p = next((j for j in range(r, n) if a[j][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        v = a[r][c]
        for q in range(r + 1, n):
            if a[q][c]:
                t = a[q][c] / v
                for k in range(c, n):
                    a[q][k] -= t * a[r][k]
        r += 1
        if r == n:
            break
    return r


def multiply(A, x):
    return [sum((a * v for a, v in zip(row, x)), F(0)) for row in A]


def compute(n, alpha, beta, j, H):
    a = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        a[i][i] = alpha
        if i + 1 < n:
            a[i][i + 1] = beta
            a[i + 1][i] = beta
    v = [F(int(i == j)) for i in range(n)]
    W = [[F(0)] * n for _ in range(n)]
    for _ in range(H):
        for x in range(n):
            for y in range(n):
                W[x][y] += v[x] * v[y]
        v = multiply(a, v)
    return W


def check():
    instances = 0
    determinants = 0
    ranks = 0
    for n in range(2, 9):
        for alpha in (F(0), F(3, 5), F(-1, 3)):
            for beta in (F(1, 5), F(-2, 7)):
                baseline = {}
                for H in (n, n + 1, n + 2):
                    for j in range(1, n + 1):
                        W = compute(n, alpha, beta, j - 1, H)
                        g = gcd(j, n + 1)
                        d = matrix_det(W)
                        rank = matrix_rank(W)
                        assert rank == n - g + 1, (n, alpha, beta, j, H, rank, g)
                        ranks += 1
                        if g == 1:
                            if H == n:
                                assert d == beta ** (n * (n - 1)), (n, alpha, beta, j, d)
                            if H not in baseline:
                                baseline[H] = d
                            assert d == baseline[H] and d > 0, (n, alpha, beta, j, H)
                        else:
                            assert d == 0, (n, alpha, beta, j, H)
                        determinants += 1
                        instances += 1
    n = 4
    a, b, H = F(3, 5), F(1, 5), 4
    W1 = compute(n, a, b, 0, H)
    W2 = compute(n, a, b, 1, H)
    assert matrix_det(W1) == matrix_det(W2) == F(1, 5 ** 12)
    assert sum(W1[i][i] for i in range(n)) == F(27519, 15625)
    assert sum(W2[i][i] for i in range(n)) == F(31197, 15625)
    print('VERIFY_OK', instances, 'exact-rational finite tests;',
          determinants, 'determinants;', ranks, 'ranks; n=4 trace contrast.')


if __name__ == '__main__':
    check()
