#!/usr/bin/env python3
"""Numerical and exact-arithmetic consistency checks for two-switch intermittent escape.

This is a finite verification aid. It is not a proof of the stated limit laws.
Requires Python 3 standard library only.
"""
from fractions import Fraction
from math import isclose, sqrt, log
import random


def next_z(z, alpha, exponent):
    return z * (1.0 + z ** (-exponent / alpha)) ** (-alpha)


def escape(z_initial, alpha, beta, p, rng):
    z = float(z_initial)
    fast_count = 0
    slow_weight = 0.0
    n = 0
    s = beta / alpha - 1.0
    while z > 1.0:
        if rng.random() < p:
            fast_count += 1
            z = next_z(z, alpha, alpha)
        else:
            slow_weight += z ** (-s)
            z = next_z(z, alpha, beta)
        n += 1
        if n > 5000000:
            raise AssertionError('Unexpectedly long finite trajectory')
    residual = z - z_initial + alpha * fast_count + alpha * slow_weight
    # This is an identity for the one-step Taylor residual, not an asymptotic theorem.
    rec = z_initial / (alpha * p) - slow_weight / p - (fast_count - p * n) / p + residual / (alpha * p) - z / (alpha * p)
    assert isclose(float(n), rec, abs_tol=1e-7, rel_tol=2e-12)
    return n, residual


def check_exact():
    for k in range(1, 40):
        z = Fraction(k, 1)
        # alpha=1 and beta=2: the two transformed branches are rational.
        f = z * z / (z + 1)
        g = z * z * z / (z * z + 1)
        assert z - f == z / (z + 1)
        assert z - g == z / (z * z + 1)
        assert Fraction(1, 2) <= z - f <= 1
        assert 0 < z - g <= Fraction(1, k)


def check_conjugacy():
    for alpha, beta in ((0.3, 0.45), (0.4, 0.8), (0.65, 0.9)):
        for z in (1.001, 1.3, 2, 9, 100, 3000):
            x = 0.5 * z ** (-1.0 / alpha)
            for exponent in (alpha, beta):
                xp = x * (1 + (2 * x) ** exponent)
                zp = (2 * xp) ** (-alpha)
                expected = next_z(z, alpha, exponent)
                assert isclose(zp, expected, rel_tol=3e-12, abs_tol=1e-12)
                decrease = z - expected
                assert decrease > 0
                if exponent == alpha:
                    assert decrease <= alpha * (1 + 1e-9)
                    assert decrease >= alpha * 2 ** (-alpha - 1) - 1e-9
                else:
                    assert decrease <= alpha * z ** (1 - beta / alpha) + 1e-9


def check_finite_distribution():
    rng = random.Random(20260317)
    alpha = 0.4
    p = 0.6
    q = 1 - p
    start = 1200
    samples = 600
    for beta, regime in ((0.52, 'deterministic'), (0.60, 'critical'), (0.80, 'gaussian')):
        s = beta / alpha - 1
        t = [escape(start, alpha, beta, p, rng)[0] for _ in range(samples)]
        scale = start ** (1-s) if regime == 'deterministic' else sqrt(start)
        values = [(v - start/(alpha*p)) / scale for v in t]
        avg = sum(values)/samples
        std = sqrt(sum((v-avg)**2 for v in values)/samples)
        if regime == 'deterministic':
            expected = -q/(alpha*p*p*(1-s))
            assert abs(avg - expected) < 1.3
        elif regime == 'critical':
            expected = -2*q/(alpha*p*p)
            assert abs(avg - expected) < 1.5
            assert abs(std - sqrt(q/(alpha*p*p))) < 0.65
        else:
            assert abs(avg) < 0.9
            assert abs(std - sqrt(q/(alpha*p*p))) < 0.65
        print('finite-sample', regime, 'mean', round(avg, 4), 'sd', round(std, 4))


if __name__ == '__main__':
    check_exact()
    check_conjugacy()
    check_finite_distribution()
    print('VERIFY_OK')
