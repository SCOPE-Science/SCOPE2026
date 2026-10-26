#!/usr/bin/env python3
"""Finite exact checks for the high-index nilpotency law in truncated polynomial rings.

Run with Python 3 using only the standard library. All arithmetic is exact.
"""
from itertools import product
from collections import Counter
from random import Random


def trim(a, m):
    return (a + (0,) * m)[:m]


def ring_mul(a, b, p, e):
    out = [0] * e
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[:e - i]):
            out[i + j] = (out[i + j] + x * y) % p
    return tuple(out)


def poly_reduce(t, coeff, p, e, m):
    """Companion-module multiplication by t, polynomial f=t^m-sum c_j t^j."""
    z = [tuple([0] * e) for _ in range(m)]
    for i in range(1, m):
        z[i] = t[i - 1]
    for i in range(m):
        for d, x in enumerate(t[m - 1]):
            if not x:
                continue
            for h, y in enumerate(coeff[i][:e - d]):
                z[i] = tuple((z[i][k] + (x * y if k == d + h else 0)) % p for k in range(e))
    return tuple(z)


def companion_index(coeff, p, e, m):
    one = tuple([1] + [0] * (e - 1))
    z = tuple([one] + [tuple([0] * e) for _ in range(m - 1)])
    for k in range(1, e * m + 1):
        z = poly_reduce(z, coeff, p, e, m)
        if not any(any(x) for x in z):
            return k
    raise AssertionError('Companion was not nilpotent')


def expected_index(a1, m, e):
    valuation = next((j for j, x in enumerate(a1) if x), m)
    return e * m - (e - 1) * valuation if (e - 1) * valuation < m else None


def exhaustive_companion(p, e, m):
    observed = Counter()
    unclassified = 0
    for digits in product(range(p), repeat=(e - 1) * m):
        coeff = [tuple([0] + list(digits[j * (e - 1):(j + 1) * (e - 1)])) for j in range(m)]
        a1 = [z[1] for z in coeff]
        t = companion_index(coeff, p, e, m)
        expected = expected_index(a1, m, e)
        if expected is None:
            assert t <= (e - 1) * m, (p, e, m, coeff, t)
            unclassified += 1
        else:
            assert t == expected, (p, e, m, coeff, t, expected)
            observed[t] += 1
    assert sum(observed.values()) + unclassified == p ** ((e - 1) * m)
    for v in range((m - 1) // (e - 1) + 1):
        idx = e * m - (e - 1) * v
        predicted = (p - 1) * p ** ((e - 1) * m - v - 1)
        assert observed[idx] == predicted, (p, e, m, idx, observed[idx], predicted)
    cutoff = (m - 1) // (e - 1) + 1
    assert unclassified == p ** ((e - 1) * m - cutoff)
    return (p, e, m, dict(sorted(observed.items())), unclassified)


def matrix_multiply(A, B, p, e):
    m = len(A)
    return [[tuple(sum((A[i][h][x] * B[h][j][d - x] for h in range(m) for x in range(d + 1)), 0) % p for d in range(e)) for j in range(m)] for i in range(m)]


def matrix_index(Bs, p, e, m):
    A = [[tuple(([int(i == j + 1)] + [Bs[d - 1][i][j] for d in range(1, e)])) for j in range(m)] for i in range(m)]
    P = [[tuple([int(i == j)] + [0] * (e - 1)) for j in range(m)] for i in range(m)]
    for k in range(1, e * m + 1):
        P = matrix_multiply(P, A, p, e)
        if all(all(not any(x) for x in row) for row in P):
            return k
    raise AssertionError('Original lift was not nilpotent')


def first_coefficient(B, p, m):
    return [sum(B[i][i + m - 1 - j] for i in range(j + 1)) % p for j in range(m)]


def direct_matrix_checks(p, e, m, count, rng):
    checked = 0
    for _ in range(count):
        Bs = [[[rng.randrange(p) for _ in range(m)] for _ in range(m)] for _ in range(e - 1)]
        a1 = first_coefficient(Bs[0], p, m)
        expected = expected_index(a1, m, e)
        index = matrix_index(Bs, p, e, m)
        if expected is None:
            assert index <= (e - 1) * m, (p, e, m, Bs, index)
        else:
            assert index == expected, (p, e, m, Bs, index, expected)
        checked += 1
    return checked


def main():
    tests = [(2, 3, 2), (3, 3, 2), (2, 3, 3), (2, 4, 2), (2, 4, 3), (2, 5, 2), (2, 3, 4)]
    for test in tests:
        print('COMPANION', exhaustive_companion(*test))
    rng = Random(403672)
    for test in [(2, 3, 2), (2, 3, 3), (3, 3, 2), (2, 4, 3), (3, 4, 2)]:
        print('MATRIX', test, direct_matrix_checks(*test, 150, rng))
    print('HIGH_TAIL_OK')


if __name__ == '__main__':
    main()
