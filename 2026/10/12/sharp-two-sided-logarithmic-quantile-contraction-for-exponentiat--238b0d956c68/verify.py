#!/usr/bin/env python3
"""Finite numerical checks of a sharp two-sided quantile theorem.

The general proof is analytic. This program makes no universal certification claim.
"""
import math
import random


def quantile(a, u):
    assert a > 0 and 0 < u < 1
    return math.log(-math.log1p(-u ** (1.0 / a)))


def B(w):
    assert w > 0
    return math.expm1(w) * (-math.log1p(-math.exp(-w)))


def derivative_ratio(r, s, u):
    assert 0 < r < s and 0 < u < 1
    t = -math.log(u)
    return (r / s) * B(t / r) / B(t / s)


def check(r, s, u, v):
    assert 0 < r < s and 0 < u < v < 1
    g_r = quantile(r, v) - quantile(r, u)
    g_s = quantile(s, v) - quantile(s, u)
    if not ((r / s) * g_r < g_s < g_r):
        raise AssertionError((r, s, u, v, g_r, g_s))
    return g_s / g_r


def main():
    ratio = check(1.0, 2.0, 0.2, 0.8)
    assert abs(ratio - 0.674717885639053) < 1e-12
    rng = random.Random(20201008)
    cases = 0
    for _ in range(40000):
        r = math.exp(rng.uniform(-2.0, 2.0))
        s = r * math.exp(rng.uniform(0.1, 2.0))
        u = rng.uniform(0.005, 0.7)
        v = u + (1.0 - u) * rng.uniform(0.01, 0.8)
        check(r, s, u, v)
        cases += 1
    for r, s in ((0.25, 1.5), (1, 2), (0.8, 4.5), (2.5, 3.7)):
        for u in (0.00001, 0.001, 0.05, 0.2, 0.5, 0.8, 0.95, 0.99999):
            rat = derivative_ratio(r, s, u)
            assert (r / s) < rat < 1, (r, s, u, rat)
            # Finite-difference derivative ratio, away from endpoints.
            if 0.001 < u < 0.999:
                h = min(1e-6, u / 5, (1-u)/5)
                dr = (quantile(r, u+h) - quantile(r, u-h))/(2*h)
                ds = (quantile(s, u+h) - quantile(s, u-h))/(2*h)
                assert abs(ds/dr - rat) < 3e-5
            cases += 1
    for u in (1e-10, 1e-8, 1e-5, 1e-3):
        assert abs(derivative_ratio(1., 2., u) - .5) < .15
    for u in (1-1e-4, 1-1e-6, 1-1e-8):
        assert abs(derivative_ratio(1., 2., u) - 1) < .08
    print('VERIFY_OK finite_cases=%d r1s2_gap_ratio=%.12f' % (cases, ratio))


if __name__ == '__main__':
    main()
