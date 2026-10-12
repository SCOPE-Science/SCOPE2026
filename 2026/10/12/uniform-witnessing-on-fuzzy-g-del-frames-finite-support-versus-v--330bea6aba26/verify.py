#!/usr/bin/env python3
"""Exact finite sanity checks for the rowwise Gödel witness criteria.

Finite enumerations supplement, but do not prove, statements about infinite frames.
"""
from fractions import Fraction
from itertools import product

Q = tuple(Fraction(j, 3) for j in range(4))


def impl(a, b):
    return Fraction(1) if a <= b else b


def box_terms(r, v):
    return tuple(impl(a, b) for a, b in zip(r, v))


def diamond_terms(r, v):
    return tuple(min(a, b) for a, b in zip(r, v))


def run():
    total = 0
    for n in (1, 2, 3):
        tuples = list(product(Q, repeat=n))
        for r in tuples:
            for v in tuples:
                b = box_terms(r, v)
                d = diamond_terms(r, v)
                assert min(b) in b
                assert max(d) in d
                assert all(x == 1 for x, a in zip(b, r) if a == 0)
                assert all(x == 0 for x, a in zip(d, r) if a == 0)
                total += 1
    assert total == 16 + 256 + 4096

    # Prefixes of an infinite c0 row: no box witness in the infinite limit.
    for n in (4, 8, 16, 32, 64, 128):
        r = tuple(Fraction(1, j + 1) for j in range(n))
        p = tuple(a / 2 for a in r)
        b = box_terms(r, p)
        assert b == p
        assert min(b) == Fraction(1, 2 * n)
        assert min(b) > 0
        assert max(diamond_terms(r, p)) == Fraction(1, 2)
    # Prefixes of an infinite non-c0 row: diamond sup tends to 1 unattained.
    for n in (4, 8, 16, 32, 64, 128):
        r = (Fraction(1),) * n
        p = tuple(Fraction(j + 1, j + 2) for j in range(n))
        assert max(diamond_terms(r, p)) == Fraction(n, n + 1) < 1
        assert max(diamond_terms(r, p)) not in (Fraction(1),)
    print(f'PASS: {total} exact finite row/valuation cases; '
          '12 rational increasing-prefix checks; no infinite inference from enumeration')


if __name__ == '__main__':
    run()
