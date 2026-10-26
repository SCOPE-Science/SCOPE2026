#!/usr/bin/env python3
"""Reproducible checks for the negative-binomial branching crossover theorem.
Only diagnostic numerical checks; the proof in RESULT.md is analytic.
"""
import math
import random
from scipy.optimize import brentq


def needed_scale(t, R, k):
    if t == 0:
        return 1.0 / R
    return k * math.expm1(t / k) / (-math.expm1(-t)) / R


def survival(scale, R, k):
    if scale * R <= 1:
        return 0.0
    hi = 1.0
    while needed_scale(hi, R, k) < scale:
        hi *= 2
    t = brentq(lambda z: needed_scale(z, R, k) - scale, 0.0, hi, xtol=1e-13)
    return -math.expm1(-t)


def crossing(R1, k1, R2, k2):
    assert R1 > R2 and 0 < k1 < k2
    target = math.log(R1 / R2)

    def lr(t):
        if t == 0:
            return 0.0
        return math.log(k1 / k2) + math.log(math.expm1(t / k1)) - math.log(math.expm1(t / k2))

    hi = .5
    while lr(hi) <= target:
        hi *= 2
    t = brentq(lambda x: lr(x) - target, 0.0, hi, xtol=1e-13)
    return t, needed_scale(t, R1, k1)


def main():
    R1, k1, R2, k2 = 4., .5, 3., 1.
    t, p = crossing(R1, k1, R2, k2)
    assert abs(p - 5 / 9) < 1e-12
    assert abs(t - math.log(5 / 3)) < 1e-12
    assert abs(survival(p, R1, k1) - .4) < 1e-11
    assert abs(survival(p, R2, k2) - .4) < 1e-11
    a = survival(.5, R1, k1)
    b = survival(.5, R2, k2)
    assert abs(a - (1 - (1 + math.sqrt(17)) / 8)) < 1e-12
    assert abs(b - 1 / 3) < 1e-12
    assert a > b
    a = survival(1., R1, k1)
    b = survival(1., R2, k2)
    assert abs(a - (1 - (1 + math.sqrt(33)) / 16)) < 1e-12
    assert abs(b - 2 / 3) < 1e-12
    assert a < b
    rng = random.Random(360726)
    tests = 0
    for j in range(2500):
        k1 = rng.uniform(.4, 1.1)
        k2 = rng.uniform(k1 + .2, 2.3)
        R2 = rng.uniform(1.1, 2.2)
        R1 = R2 * rng.uniform(1.02, 2.)
        t, p = crossing(R1, k1, R2, k2)
        assert p > 1 / R2
        s1, s2 = survival(p, R1, k1), survival(p, R2, k2)
        assert abs(s1 - s2) < 2e-10, (j, k1, k2, R1, R2, p, s1, s2)
        a, b = survival((1 / R1 + p) / 2, R1, k1), survival((1 / R1 + p) / 2, R2, k2)
        assert a > b + 1e-13, (j,a,b)
        a, b = survival(1.35 * p, R1, k1), survival(1.35 * p, R2, k2)
        assert b > a + 1e-13, (j,a,b)
        tests += 1
    for j in range(2000):
        k1 = rng.uniform(.35, 1.1)
        k2 = rng.uniform(k1+.1, 2.)
        R1 = rng.uniform(1.3, 2.)
        R2 = rng.uniform(R1+.1, 4.)
        p = rng.uniform(1/R1 + 0.05, 3.)
        assert survival(p, R1, k1) < survival(p, R2, k2)
    print('EXACT EXAMPLE: PASS')
    print('CROSSING RANDOMIZED CASES:',tests,'PASS')
    print('SAME-ORDER RANDOMIZED CASES: 2000 PASS')
    print('Finite computations supplement, not establish, the universal theorem.')


if __name__ == '__main__':
    main()
