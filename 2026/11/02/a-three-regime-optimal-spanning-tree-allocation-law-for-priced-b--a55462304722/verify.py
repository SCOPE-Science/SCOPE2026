#!/usr/bin/env python3
"""Standalone independent arithmetic checks of the weighted-cube tree-design formulas.

This code checks finite instances only; the theorem's all-dimension assertion
rests on the accompanying proof.
"""
from fractions import Fraction
from math import comb, fsum


def determinant_integer(a):
    a = [row[:] for row in a]
    n = len(a)
    previous, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1] if n else 1


def independent_tree_det(d, x, y):
    v = 1 << d
    a = [[0] * (v - 1) for _ in range(v - 1)]
    for u in range(v):
        for j in range(d):
            z = u ^ (1 << j)
            if u > z:
                continue
            w = x if j == 0 else y
            if u != v - 1:
                a[u][u] += w
            if z != v - 1:
                a[z][z] += w
            if u != v - 1 and z != v - 1:
                a[u][z] -= w
                a[z][u] -= w
    return determinant_integer(a)


def spectral_tree_count(d, x, y):
    m = d - 1
    numerator = 1
    for k in range(1, m + 1):
        numerator *= (2 * k * y) ** comb(m, k)
    for k in range(m + 1):
        numerator *= (2 * (x + k * y)) ** comb(m, k)
    assert numerator % (1 << d) == 0
    return numerator // (1 << d)


def derivative(d, t, p, q):
    m = d - 1
    s = fsum(comb(m, k) / (t + k) for k in range(m + 1))
    return (p * t + m * q) * s - p * ((1 << d) - 1)


def root(d, p, q):
    low, high = 0.0, max(d, 1.0)
    while derivative(d, high, p, q) >= 0.0:
        high *= 2.0
        assert high < 1e12
    for _ in range(170):
        mid = (low + high) * 0.5
        if derivative(d, mid, p, q) > 0.0:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def verify():
    checks = 0
    for d in (2, 3, 4):
        for x, y in ((1, 1), (1, 2), (2, 1), (2, 3), (3, 4), (5, 7)):
            assert independent_tree_det(d, x, y) == spectral_tree_count(d, x, y)
            checks += 1
    for d in range(2, 42):
        m = d - 1
        s = sum((Fraction(comb(m, k), 1 + k) for k in range(m + 1)), Fraction())
        assert s == Fraction((1 << d) - 1, d)
        checks += 1
    for d in range(2, 30):
        for p, q in ((1, 1), (1, 2), (2, 1), (3, 2), (2, 5), (5, 2)):
            r = root(d, p, q)
            if p == q:
                assert abs(r - 1.0) < 1e-5
            else:
                assert r < 1.0 if p > q else r > 1.0
            assert derivative(d, r * 0.99, p, q) > -1e-7
            assert derivative(d, r * 1.01, p, q) < 1e-7
            checks += 3
    for p, q in ((2, 1), (3, 1)):
        d = 27
        r = root(d, p, q)
        expected = q / (p - q)
        scaled = (1 << d) * r / (d - 1)
        assert abs(scaled / expected - 1) < 0.08, (d, p, q, scaled, expected)
        checks += 1
    for p, q in ((1, 2), (1, 3)):
        d = 27
        r = root(d, p, q)
        expected = q / p - 1
        scaled = r / (d - 1)
        assert abs(scaled / expected - 1) < 0.05, (d, p, q, scaled, expected)
        checks += 1
    print('PASS:', checks, 'independent matrix-tree, exact combinatorial, root-sign, and asymptotic spot checks')


if __name__ == '__main__':
    verify()
