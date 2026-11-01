#!/usr/bin/env python3
"""Exact-integer super-solution certificate for centered graph-ball maxima.

Requires Python 3 and NumPy. Floating point is used ONLY to propose
positive integer witnesses; every accepted spectral bound is independently
checked with unbounded Python integers. The finite ranges are exhaustive.
"""
import itertools
import math
from fractions import Fraction

import numpy as np


def check_case(m):
    n = 2 * m
    q = 4 if m == 5 else 2
    r = n - q
    L = math.lcm(n, n - 1)
    threshold_scaled = {2: 210, 3: 1275, 4: 4350, 5: 11178}[m]
    # Polynomial satisfied by the exceptional maximum squared norm.
    a = (n - 1) ** 2
    b = -(a + q * r + (r - 1) ** 2)
    c = (r - 1) ** 2
    T = Fraction(threshold_scaled, L * L)
    assert T > 1 and a * T * T + b * T + c < 0
    # Exactly these q/2 antipodal pairs take radius zero;
    # every remaining vertex takes radius one.
    winners = set()
    for chosen in itertools.combinations(range(m), q // 2):
        z = [1] * n
        for pair in chosen:
            z[2 * pair] = z[2 * pair + 1] = 0
        winners.add(tuple(z))

    # H[i, z, j] = L times the averaging-row coefficient.
    H = np.zeros((n, 3, n), dtype=np.int64)
    for i in range(n):
        H[i, 0, i] = L
        H[i, 1, :] = L // (n - 1)
        H[i, 1, i ^ 1] = 0
        H[i, 2, :] = L // n

    strict = 0
    exceptional = 0
    min_exact_margin = None
    max_abs_integer_product = 0
    for z in itertools.product(range(3), repeat=n):
        if z in winners:
            exceptional += 1
            continue
        A = H[np.arange(n), z, :]
        K = (A.T @ A).tolist()  # Exact: entries are small integers.
        D = threshold_scaled * np.eye(n) - np.array(K, dtype=float)
        # A proposed resolvent super-solution, not trusted as evidence.
        w = np.linalg.solve(D, np.ones(n))
        v = [int(round(float(y) * 10**9)) for y in w]
        assert all(y > 0 for y in v), (m, z, 'nonpositive witness')
        # EXACT certificate: (threshold_scaled I - K)v > 0.
        # Python int arithmetic prevents floating/NumPy overflow.
        for i in range(n):
            dot = sum(int(K[i][j]) * v[j] for j in range(n))
            max_abs_integer_product = max(max_abs_integer_product, abs(dot))
            margin = threshold_scaled * v[i] - dot
            assert margin > 0, (m, z, i, margin)
            min_exact_margin = margin if min_exact_margin is None else min(min_exact_margin, margin)
        strict += 1
    assert strict + exceptional == 3 ** n
    assert exceptional == math.comb(m, q // 2)
    return {
        'm': m, 'rows': n, 'selections': 3 ** n,
        'strict': strict, 'exceptional': exceptional,
        'threshold': str(T), 'quadratic': (a, b, c),
        'min_integer_margin': min_exact_margin,
        'max_integer_product': max_abs_integer_product,
    }


def main():
    rows = [check_case(m) for m in (2, 3, 4, 5)]
    assert [x['strict'] for x in rows] == [79, 726, 6557, 59039]
    assert [x['exceptional'] for x in rows] == [2, 3, 4, 10]
    for row in rows:
        print('EXACT_CERTIFICATE', row)
    print('CERTIFICATE_OK selections=66420 strict=66401 exceptional=19')


if __name__ == '__main__':
    main()
