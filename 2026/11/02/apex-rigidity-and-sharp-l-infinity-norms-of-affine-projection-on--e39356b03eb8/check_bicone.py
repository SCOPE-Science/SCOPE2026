#!/usr/bin/env python3
"""Reproducible finite checks of exact affine-projector formulas on Euclidean bipyramids.

The analytical proof, not the finite Monte Carlo checks, establishes universality.
"""
from fractions import Fraction as F
from math import sqrt
import random


def apex_constant(d):
    c = F((d + 2) * (d + 3), 2)
    return F(1) + F(d + 3, 2) * (1 - 1 / c) ** (d + 2)


def axis_variance_inverse(d):
    return F((d + 2) * (d + 3), 2)


def transverse_variance_inverse(d):
    return F((d + 2) * (d + 3), d + 1)


def deterministic_checks(max_d=50):
    assert 3 * 10561 ** 2 > 20 * 4000 ** 2
    assert apex_constant(2) == F(10561, 4000)
    assert apex_constant(1) == 1 + F(2) * F(5, 6) ** 3
    checks = 3
    for d in range(1, max_d + 1):
        et2 = F(2, (d + 2) * (d + 3))
        ex2 = F(d + 1, (d + 2) * (d + 3))
        assert et2 * axis_variance_inverse(d) == 1
        assert ex2 * transverse_variance_inverse(d) == 1
        assert apex_constant(d) > F(d + 3, 2)
        checks += 3
        if d >= 3:
            assert F(d + 3, 2) ** 2 >= transverse_variance_inverse(d)
            assert d * d >= 5
            checks += 2
    return checks


def sample_uniform_bipyramid(d, rng):
    # |t|~Beta(1,d+1); X conditional on t is uniform in the d-ball radius 1-|t|.
    abs_t = rng.betavariate(1, d + 1)
    t = abs_t if rng.random() < 0.5 else -abs_t
    direction = [rng.gauss(0, 1) for _ in range(d)]
    r = sqrt(sum(z * z for z in direction))
    radius = (1 - abs_t) * rng.random() ** (1 / d)
    return radius * direction[0] / r, t


def sampling_checks(sample_count=40000):
    rng = random.Random(20261025)
    outcomes = []
    for d in (1, 2, 3, 4, 5, 8, 12):
        a = float(transverse_variance_inverse(d))
        c = float(axis_variance_inverse(d))
        apex_sum = 0.
        eq_sum = 0.
        for _ in range(sample_count):
            x1, t = sample_uniform_bipyramid(d, rng)
            apex_sum += abs(1 + c * t)
            eq_sum += abs(1 + a * x1)
        apex_est = apex_sum / sample_count
        eq_est = eq_sum / sample_count
        exact = float(apex_constant(d))
        assert abs(apex_est - exact) < 0.13, (d, apex_est, exact)
        if d >= 2:
            assert eq_est < exact - 0.15, (d, eq_est, exact)
        else:
            assert abs(eq_est - exact) < 0.13
        outcomes.append((d, round(exact, 8), round(apex_est, 8), round(eq_est, 8)))
    return outcomes


if __name__ == '__main__':
    print('exact_rational_checks', deterministic_checks())
    print('independent_random_samples_per_dimension', 40000)
    for outcome in sampling_checks():
        print('ambient_minus_one_d, apex_exact, sampled_apex, sampled_equator:', *outcome)
    print('PASS: finite checks corroborate, but do not establish, the universal theorem.')
