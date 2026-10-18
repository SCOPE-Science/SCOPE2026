#!/usr/bin/env python3
"""Exact-integer sample checks for a cyclic Euler polar matrix.

Requires Python 3 and SymPy >= 1.12.  These finite calculations are
examples and regression tests, not a substitute for the general proof.
"""
from math import gcd
from sympy import ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form


def polar(n, a):
    H = zeros(n)
    for i in range(n):
        for offset, coefficient in ((0, 2), (1, -1), (-1, -1),
                                    (a, -1), (-a, -1),
                                    (a + 1, 1), (-a - 1, 1)):
            H[i, (i + offset) % n] += coefficient
    assert H == H.T
    return H


def predicted(n, a):
    g = gcd(n, a + 1)
    m = n // g
    if m % 2:
        if g == 1:
            return [n], 1
        return [2] * (g - 2) + [2 * n], 1
    return [n // 2], g + 1


def check(n, a):
    assert n >= 3 and 1 <= a < n and gcd(n, a) == 1
    H = polar(n, a)
    D = smith_normal_form(H, domain=ZZ)
    entries = [abs(int(D[i, i])) for i in range(n)]
    torsion = [entry for entry in entries if entry > 1]
    free_rank = entries.count(0)
    expected_torsion, expected_free_rank = predicted(n, a)
    assert torsion == expected_torsion, (n, a, torsion, expected_torsion)
    assert free_rank == expected_free_rank, (n, a, free_rank, expected_free_rank)
    return len(torsion), free_rank


def main():
    cases = [(n, a) for n in range(3, 23) for a in range(1, n)
             if gcd(n, a) == 1]
    cases += [(24, 5), (24, 7), (24, 11), (28, 3), (30, 11), (36, 5)]
    tested = 0
    for n, a in cases:
        check(n, a)
        tested += 1
    print('EXACT_SMITH_CHECK_OK', tested, 'cases')
    print('MAX_N', max(n for n, a in cases))
    print('EXAMPLES', [(n, a, predicted(n, a)) for n, a in
                       ((9, 2), (10, 3), (12, 5), (15, 4), (24, 7))])


if __name__ == '__main__':
    main()
