#!/usr/bin/env python3
"""Exact rational checks for finite equilateral Lipschitz-free Hilbert distortion.

This program tests finite samples only; the accompanying analytic proof
establishes the formulas for all dimensions and all real vectors.
"""
from fractions import Fraction as F
from itertools import product


def varsum(values):
    n = len(values)
    z = sum(values)
    return sum(x * x for x in values) - z * z / n


def diam(values):
    return max(values) - min(values)


def check():
    tested = 0
    for n in range(2, 17):
        u = F((n * n) // 4, n)
        low = F(1, 2)
        assert F(2 * (n * n // 4), n) == u / low
        assert varsum([F(0), F(1)] + [F(1, 2)] * (n - 2)) == low
        max_binary = F(0)
        for k in range(n + 1):
            v = [F(1)] * k + [F(0)] * (n - k)
            assert varsum(v) == F(k * (n - k), n)
            if k > 0 and k < n:
                assert diam(v) == 1
            max_binary = max(max_binary, varsum(v))
            tested += 1
        assert max_binary == u
        if n <= 8:
            for vals in product([F(0), F(1, 2), F(1)], repeat=n):
                d = diam(vals)
                if not d:
                    continue
                q = varsum(vals) / (d * d)
                assert low <= q <= u, (n, vals, q)
                # The exact Lagrange pairwise identity defining variance.
                assert sum((vals[i] - vals[j])**2
                           for i in range(n) for j in range(i + 1, n)) == n * varsum(vals)
                tested += 1
    print(f'EQUILATERAL_EUCLIDEAN_EXACT_OK {tested}')


if __name__ == '__main__':
    check()
