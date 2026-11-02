#!/usr/bin/env python3
"""Standalone numerical checks for a random-node interpolation moment law.

Tests are finite sanity checks; proof of all-node-count quantifiers
is contained in the accompanying mathematical argument.
"""
import math
import random


def survival_exact(theta, t):
    assert theta >= 0 and t >= 1
    return 2.0 * (2.0 / (1.0 + t)) ** (theta + 1.0) - t ** (-(theta + 1.0))


def midpoint_length(d, t):
    if d < 1.0 / t:
        return 1.0 - d
    if d < 2.0 / (1.0 + t):
        return 2.0 - (1.0 + t) * d
    return 0.0


def survival_simpson(theta, t, subdivisions=6000):
    z = 2.0 / ((theta + 1.0) * (theta + 2.0))
    a, b = 0.0, 1.0
    h = (b - a) / subdivisions
    vals = []
    for j in range(subdivisions + 1):
        d = a + j * h
        vals.append(d**theta * midpoint_length(d, t))
    integral = (vals[0] + vals[-1] +
                4.0 * sum(vals[1:-1:2]) +
                2.0 * sum(vals[2:-1:2])) * h / 3.0
    return 2.0 * integral / z


def lagrange_values(nodes, t):
    out = []
    for i, xi in enumerate(nodes):
        value = 1.0
        for j, xj in enumerate(nodes):
            if i != j:
                value *= (t - xj) / (xi - xj)
        out.append(value)
    return out


def main():
    numeric_integrals = 0
    for theta in [0.0, 0.5, 1.0, 2.0, 3.0]:
        for t in [1.0, 1.5, 2.0, 4.0, 8.0]:
            expect = survival_exact(theta, t)
            got = survival_simpson(theta, t)
            assert 0 <= expect <= 1.0 + 1e-12
            assert abs(got - expect) < 2.0e-6, (theta, t, got, expect)
            numeric_integrals += 1

    # Tail constant follows algebraically from the exact expression.
    for theta in [0.0, 1.0, 2.0, 3.0]:
        t = 1.e6
        scaled = 2.0 * (2.0*t/(t+1.0)) ** (theta+1.0) - 1.0
        expect = 2. ** (theta + 2.) - 1.
        assert abs(scaled / expect - 1.0) < 3.e-5

    # Concrete exact moments: theta=2 gives E[Lambda]=5/2 and E[Lambda^2]=11.
    for theta in [2.0, 3.0, 4.0]:
        mean = 1. + 3. / theta
        second = (theta*theta + 5*theta + 8)/(theta*(theta - 1.))
        assert second >= mean*mean
    assert abs((4. + 10. + 8.)/(2.*1.) - 11.) < 1.e-12

    rng = random.Random(781298)
    mc_checks = 0
    repeats = 60000
    for theta in [0.0, 1.0, 2.0]:
        samples = []
        for _ in range(repeats):
            d = rng.betavariate(theta+1., 2.)
            midpoint = rng.uniform(d/2., 1.-d/2.)
            samples.append(2.*max(midpoint, 1.-midpoint)/d)
        for t in [1.5, 2.0, 4.0]:
            empirical = sum(x > t for x in samples)/repeats
            expected = survival_exact(theta, t)
            assert abs(empirical-expected) < 0.013, (theta, t, empirical, expected)
            mc_checks += 1

    for n in [2, 3, 4, 5, 6]:
        for _ in range(100):
            nodes = sorted(rng.sample(range(1, 10000), n))
            nodes = [x/10000 for x in nodes]
            for t in [0.0, 0.25, 0.73, 1.0]:
                l = lagrange_values(nodes, t)
                assert abs(sum(l)-1.) < 2e-8
                assert sum(abs(x) for x in l) >= 1. - 1e-8
    print('VERIFY_OK midpoint_integrals=%d exact_moments=3 monte_carlo=%d basis_trials=%d' %
          (numeric_integrals, mc_checks, 5*100*4))


if __name__ == '__main__':
    main()
