#!/usr/bin/env python3
"""Exact determinant checks and reproducible importance sampling for random-simplex near-volume tails.

Requires only the Python standard library. The all-dimensional mathematical assertion is analytical; this program supplies finite, reproducible checks.
"""
from fractions import Fraction as F
from math import factorial
import itertools
import random


def coefficients(d):
    m = d * (d + 1)
    c = F(factorial(d + 1) * factorial(d) ** (d + 1), factorial(m))
    a = F(m * (d * d - 1), 2 * (m + 1))
    return m, c, a


def polynomial_det_of_I_plus_hE(E):
    n = len(E)
    coeff = [F(0)] * (n + 1)
    for pi in itertools.permutations(range(n)):
        inv = sum(pi[i] > pi[j] for i in range(n) for j in range(i + 1, n))
        poly = [F(1)]
        for i, j in enumerate(pi):
            zero, linear = (F(1) if i == j else F(0)), E[i][j]
            new = [F(0)] * (len(poly) + 1)
            for k, val in enumerate(poly):
                new[k] += val * zero
                new[k + 1] += val * linear
            poly = new
        sgn = -1 if inv & 1 else 1
        for k, val in enumerate(poly):
            coeff[k] += sgn * val
    return coeff


def exact_det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    value = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        v = a[j][j]
        value *= v
        for i in range(j + 1, n):
            ratio = a[i][j] / v
            for k in range(j + 1, n):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = F(0)
    return value


def exact_tests():
    tests = 0
    for d in (1, 2, 3, 4):
        n = d + 1
        for shift in range(8):
            E = [[F(0)] * n for _ in range(n)]
            for j in range(n):
                for i in range(n):
                    if i != j:
                        E[i][j] = F(1 + ((i * 13 + j * 7 + shift * 3) % 11), 1000)
                E[j][j] = -sum(E[i][j] for i in range(n) if i != j)
            series = polynomial_det_of_I_plus_hE(E)
            S = -sum(E[i][i] for i in range(n))
            s = [-E[i][i] for i in range(n)]
            b = sum((s[i] * s[j] - E[i][j] * E[j][i])
                    for i in range(n) for j in range(i + 1, n))
            assert series[0] == 1 and series[1] == -S and series[2] == b
            assert sum(series) == exact_det([[(F(1) if i==j else F(0))+E[i][j] for j in range(n)] for i in range(n)])
            tests += 4
    assert coefficients(1) == (2, F(1), F(0))
    assert coefficients(2) == (6, F(1, 15), F(9, 7))
    assert coefficients(3) == (12, F(1, 15400), F(48, 13))
    assert coefficients(4) == (20, F(1, 2546168625), F(50, 7))
    print('Exact determinant/constant checks:', tests + 4, 'passed')


def det_float(A):
    n = len(A)
    a = [r[:] for r in A]
    value = 1.0
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-15:
            return 0.0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = -value
        v = a[k][k]
        value *= v
        for i in range(k + 1, n):
            z = a[i][k] / v
            for j in range(k + 1, n):
                a[i][j] -= z * a[k][j]
    return value


def tail_sampling(d, eps, N, seed):
    rng = random.Random(seed)
    m, c, a = coefficients(d)
    R = eps * (1 + 2 * eps)
    accepted = 0
    for _ in range(N):
        g = [-__import__('math').log(rng.random()) for _ in range(m + 1)]
        total = sum(g)
        t = [R * v / total for v in g[:m]]
        B = [[0.0 for _ in range(d + 1)] for _ in range(d + 1)]
        k = 0
        for col in range(d + 1):
            s = 0.0
            for row in range(d + 1):
                if row == col:
                    continue
                B[row][col] = t[k]
                s += t[k]
                k += 1
            B[col][col] = 1 - s
        det = det_float(B)
        if 1 - det < eps:
            accepted += 1
    ratio = (R / eps) ** m * accepted / N
    pred = 1 + float(a) * eps
    print('d=%d eps=%.3f N=%d accepted=%d P/(C*eps^m)=%.6f first-order=%.6f' %
          (d, eps, N, accepted, ratio, pred))
    assert abs(ratio - pred) < 0.07


if __name__ == '__main__':
    exact_tests()
    for dim in (2, 3, 4):
        tail_sampling(dim, 0.015, 50000, 401 + dim)
    print('All checks passed.')
