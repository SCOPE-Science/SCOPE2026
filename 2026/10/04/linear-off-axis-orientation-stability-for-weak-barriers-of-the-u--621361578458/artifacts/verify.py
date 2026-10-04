#!/usr/bin/env python3
"""Consistency checks for the unit-cube weak-barrier stability proof."""
from fractions import Fraction
from itertools import product
from math import sqrt, cos, sin, pi


def exact_sign_moments(a):
    n = len(a)
    vals = []
    for eps in product((-1, 1), repeat=n):
        vals.append(sum(e*x for e, x in zip(eps, a)))
    den = 1 << n
    e2 = Fraction(sum(x*x for x in vals), den)
    e4 = Fraction(sum(x**4 for x in vals), den)
    s2 = sum(x*x for x in a)
    s4 = sum(x**4 for x in a)
    assert e2 == s2
    assert e4 == 3*s2*s2 - 2*s4


def normalized_checks(a):
    n = len(a)
    s2 = sum(x*x for x in a)
    if s2 == 0:
        return
    norm = sqrt(s2)
    v = [x/norm for x in a]
    vals = []
    for eps in product((-1, 1), repeat=n):
        vals.append(abs(sum(e*x for e, x in zip(eps, v))))
    phi = sum(vals) / len(vals)
    q = sum(x**4 for x in v)
    rhs = (1.0-q)/(sqrt(n)+1.0)**2
    assert 1.0-phi + 2e-14 >= rhs

    for beta in (0.15, 0.35, 0.65):
        if beta >= pi/4:
            continue
        c = cos(beta)
        if max(abs(x) for x in v) < c - 1e-13:
            cap = c**4 + (1.0-c*c)**2
            assert q <= cap + 2e-13
            assert 1.0-q + 2e-13 >= 2.0*sin(beta)**2*cos(beta)**2


def main():
    # Exact moment identities on a complete bounded integer grid.
    for n in range(1, 6):
        for a in product(range(-2, 3), repeat=n):
            if any(a):
                exact_sign_moments(a)

    # Pointwise normalized inequalities on deterministic coefficient grids.
    for n in range(3, 8):
        samples = []
        for a in product((-2, -1, 0, 1, 2), repeat=n):
            if any(a):
                samples.append(a)
            if len(samples) >= 400:
                break
        # Include structured vectors spanning axis-near, flat, and two-level cases.
        samples.extend([
            tuple([2] + [1]*(n-1)),
            tuple([3, 2] + [0]*(n-2)),
            tuple([1]*n),
            tuple([n] + [1]*(n-1)),
        ])
        for a in samples:
            normalized_checks(a)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
