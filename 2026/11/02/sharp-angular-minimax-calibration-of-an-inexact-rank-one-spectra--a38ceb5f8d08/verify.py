#!/usr/bin/env python3
"""Independent exact-rational and floating-point checks for the stated 2x2 spectral-LMP formulas.

This is a finite reproducibility check, not a substitute for the analytic proof.
"""
from fractions import Fraction
from math import sqrt, isclose, sin, asin, pi, hypot
from random import Random


def condition(kappa, r, theta):
    """Condition number of the specified SPD-congruence in its orthonormal Ritz basis."""
    rho = kappa - (kappa - 1) * r
    sig = 1 + (kappa - 1) * r
    off = (kappa - 1) * sqrt(r * (1 - r) * theta / rho)
    halfdiff = (theta - sig) / 2
    halfsum = (theta + sig) / 2
    radical = hypot(halfdiff, off)
    return (halfsum + radical) / (halfsum - radical)


def optimum(kappa, R):
    z = (kappa - 1) ** 2 * R * (1 - R) / kappa
    return (sqrt(1 + z) + sqrt(z)) ** 2


def critical(kappa):
    return 2 / (3 + sqrt(4 * kappa + 5))


def run():
    tests = 0
    # The factorization determining precisely when unscaled preconditioning worsens.
    for k in range(2, 75):
        for j in range(0, 81):
            r = Fraction(j, 160)
            d = Fraction(k - 1)
            lhs = (2 + d * r) ** 2 * (k - d * r) - (k + 1) ** 2
            rhs = d ** 2 * (1 - r) * (d * r * r + 3 * r - 1)
            assert lhs == rhs
            tests += 1
    rng = Random(574903)
    # Check the analytical minimax and the monotonicity of the worst-case angle.
    for i in range(2100):
        k = 1 + 10 ** rng.uniform(-2.5, 3.0)
        R = rng.random() * .5
        theta = 1 + (k - 1) * R
        target = optimum(k, R)
        actual = condition(k, R, theta)
        assert isclose(actual, target, rel_tol=3e-9, abs_tol=1e-9), (k, R, target, actual)
        for t in (0, .05, .25, .5, .75, 1):
            assert condition(k, t * R, theta) <= target * (1 + 1e-8)
        for t in (.001, .02, .2, 1, 5, 50):
            candidate = condition(k, R, theta * t)
            assert candidate >= target * (1 - 3e-9)
        tests += 13
    # The exact worsening frontier for theta=1.
    for i in range(1700):
        k = 1 + 10 ** rng.uniform(-2, 4)
        rc = critical(k)
        assert 0 < rc < .5
        for factor in (.1, .8, 1.0, 1.2):
            r = min(.5, factor * rc)
            c = condition(k, r, 1)
            if factor < 1:
                assert c <= k * (1 + 1e-9)
            elif factor > 1:
                assert c > k * (1 - 1e-9)
            else:
                assert isclose(c, k, rel_tol=3e-9)
        tests += 5
    # Deterministic 2-by-2 matrices and similarity eigenvalue checks using trace/determinant.
    for i in range(800):
        k = 1 + 10 ** rng.uniform(-1, 3)
        phi = rng.uniform(0, pi / 4)
        r = sin(phi) ** 2
        theta = 10 ** rng.uniform(-2, 3)
        rho = k - (k - 1) * r
        sigma = 1 + (k - 1) * r
        t = theta + sigma
        determinant = theta * k / rho
        eigenplus = (t + sqrt(max(0, t*t-4*determinant))) / 2
        eigenminus = determinant / eigenplus
        assert isclose(eigenplus / eigenminus, condition(k, r, theta), rel_tol=3e-9)
        tests += 1
    # Sharp large-condition-number scales.
    for c in (0, .25, 1, 3):
        for k in (10**5, 10**7):
            R = sin(c / sqrt(k)) ** 2
            ref = (sqrt(1 + c*c) + c) ** 2
            got = optimum(k, R)
            assert abs(got - ref) / ref < .01
            tests += 1
    print('VERIFY_OK', tests)
    return tests


if __name__ == '__main__':
    run()
