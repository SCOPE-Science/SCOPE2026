#!/usr/bin/env python3
"""Finite exact checks for separated two-frame observation covering designs.

Analytic proofs, not this finite program, establish the theorem for all d.
"""
from fractions import Fraction


def pattern(d):
    assert d >= 1
    if d % 2 == 0:
        period = 2*d
        starts = set(range(0, d, 2))
    else:
        period = 2*d+1
        starts = set(range(0, d, 2))
    return period, starts


def rate(d):
    return Fraction(1, 4) if d % 2 == 0 else Fraction(d+1, 4*d+2)


def check(d):
    period, starts = pattern(d)
    F = {0, 1, d, d+1}
    assert len(starts) * rate(d).denominator == rate(d).numerator * period
    union = {(s+f) % period for s in starts for f in F}
    assert union == set(range(period)), (d, period, starts, union)
    J = set(range(d+1, 2*d+1))
    for a in range(2*d+1):
        assert len({a+f for f in F} & J) <= 2


if __name__ == '__main__':
    for d in range(1, 501):
        check(d)
    for d in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        p, A = pattern(d)
        print(f'd={d} period={p} residues={sorted(A)} cost={rate(d)}')
    print('PASS: 500 periodic covers and interval-incidence bounds checked.')
