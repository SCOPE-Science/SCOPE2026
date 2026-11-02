#!/usr/bin/env python3
"""Exact finite checks of an explicit nine-good Pareto/EFX boundary witness."""
from fractions import Fraction
from itertools import product

GOODS = 'xyabcdepq'
BUNDLES = ({0, 3}, {1}, {4, 5, 7, 8}, {2, 6})

def matrix(k):
    return (
        (3*k, 2*k+2, k, k, 1, 1, k, 2, 1),
        (2*k+2, 3*k, 1, k, k, 1, k, 1, 2),
        (3*k, 2*k+2, 1, 1, k, k, k, 2, 1),
        (2*k+2, 3*k, k, 1, 1, k, k, 1, 2),
    )

def check(k, exhaustive):
    v = matrix(k)
    u = tuple(sum(v[i][g] for g in BUNDLES[i]) for i in range(4))
    assert u == (4*k, 3*k, 2*k+3, 2*k)
    target = Fraction(2*k+3, 3*k)
    observed = None
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for g in BUNDLES[j]:
                den = sum(v[i][h] for h in BUNDLES[j] if h != g)
                if den:
                    quotient = Fraction(u[i], den)
                    observed = quotient if observed is None else min(observed, quotient)
                    assert quotient >= target, (k, i, j, g)
    assert observed == target
    welfare_max = sum(max(v[i][g] for i in range(4)) for g in range(9))
    assert welfare_max == 11*k+4 and sum(u) == welfare_max-1
    if exhaustive:
        count = 0
        for assignments in product(range(4), repeat=9):
            util = [0, 0, 0, 0]
            for g, i in enumerate(assignments):
                util[i] += v[i][g]
            assert not (all(util[i] >= u[i] for i in range(4)) and
                        any(util[i] > u[i] for i in range(4))), (k, assignments)
            count += 1
        assert count == 4**9
    return u

if __name__ == '__main__':
    values = (6, 7, 8, 9, 10, 12, 20, 50, 100)
    for k in values:
        check(k, k in (6, 8, 12))
    print('VERIFY_OK parameters=%s exhaustive_instances=%d' %
          (','.join(map(str, values)), 3*4**9))
