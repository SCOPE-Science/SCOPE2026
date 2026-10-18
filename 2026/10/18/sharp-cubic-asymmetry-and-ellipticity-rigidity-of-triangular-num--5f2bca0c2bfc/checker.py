"""Finite supplementary numerical checks for triangular spatial numerical-range curvature.

Run: python3 checker.py
All universal mathematical statements are proved in RESULT.md; these tests
check finite cases and do not certify an infinite family by enumeration.
"""
import cmath
import math
import random


def f(t, a):
    return t ** a * (1.0 - t) ** (1.0 - a)


def deriv(t, a):
    return f(t, a) * (a - t) / (t * (1 - t))


def second(t, a):
    b = 1.0 - a
    return -a * b * f(t, a) / (t * t * (1 - t) ** 2)


def optimizer(c, p, B):
    a = 1.0 - 1.0 / p
    lo, hi = 1e-12, 1.0 - 1e-12
    for _ in range(75):
        t = (lo + hi) / 2.0
        if c + B * deriv(t, a) > 0:
            lo = t
        else:
            hi = t
    return (lo + hi) / 2.0


def envelope(c, p, B):
    a = 1.0 - 1.0 / p
    t = optimizer(c, p, B)
    return c * t + B * f(t, a)


def check():
    rng = random.Random(572019)
    checks = 0
    for p in (1.35, 1.5, 2.0, 2.75, 4.0, 7.0):
        a = 1.0 - 1.0 / p
        b = 1.0 / p
        F = f(a, a)
        for B in (0.8, 1.7):
            # Unique optimizer, positive radius of curvature, exact support.
            for j in range(100):
                theta = 2.0 * math.pi * j / 100.0
                L = 1.25
                c = L * math.cos(theta)
                t = optimizer(c, p, B)
                assert 0.0 < t < 1.0
                assert abs(c + B * deriv(t, a)) < 1e-8
                curvature_radius = B * f(t, a) + L * L * math.sin(theta) ** 2 / (-B * second(t, a))
                assert curvature_radius > 0.0
                G = envelope(c, p, B)
                for _ in range(12):
                    q = rng.uniform(0.0, 1.0)
                    assert G + 1e-11 >= c * q + B * f(q, a)
                    checks += 1
                checks += 3
            # Exact dual reflection and direct spatial range point.
            for _ in range(300):
                t = rng.uniform(0.0001, 0.9999)
                phi = rng.uniform(-math.pi, math.pi)
                diag1 = 1.2 - 0.7j
                diag2 = -0.3 + 0.2j
                off = B * cmath.exp(1j * 0.59)
                x1 = t ** (1.0 / p)
                x2 = (1.0 - t) ** (1.0 / p) * cmath.exp(1j * phi)
                dot = ((diag1 * x1 + off * x2) * x1 ** (p - 1) +
                       diag2 * x2 * abs(x2) ** (p - 2) * x2.conjugate())
                want = diag1 * t + diag2 * (1.0 - t) + off * f(t, a) * cmath.exp(1j * phi)
                assert abs(dot - want) < 1e-11
                dual_exp = 1.0 / p
                assert abs(f(t, a) - f(1.0 - t, dual_exp)) < 1e-12
                checks += 2
            # Third derivative via odd differences of the support envelope.
            h = 0.01
            D = lambda v: envelope(v, p, B) - envelope(-v, p, B)
            numeric = (D(2 * h) - 2.0 * D(h)) / (2.0 * h ** 3)
            analytic = 2.0 * a * b * (b - a) / (B * B * F * F)
            assert abs(numeric - analytic) < 1e-3, (p, B, numeric, analytic)
            checks += 1
    # Small-gap Hausdorff reflection defect: numerically minimize over real centres.
    for p in (1.5, 4.0):
        a = 1.0 - 1.0 / p
        b = 1.0 / p
        B = 1.7
        L = 0.15
        xs = [j / 200.0 for j in range(-200, 201)]
        differences = [envelope(L * x, p, B) - envelope(-L * x, p, B) for x in xs]
        def error(slope):
            return max(abs(d - slope * x) for d, x in zip(differences, xs))
        central = 2.0 * a * L
        left, right = central - 0.002, central + 0.002
        # Golden-section minimax of the one-parameter convex objective.
        ratio = (math.sqrt(5.0) - 1.0) / 2.0
        c = right - ratio * (right - left)
        d = left + ratio * (right - left)
        for _ in range(80):
            if error(c) <= error(d):
                right, d = d, c
                c = right - ratio * (right - left)
            else:
                left, c = c, d
                d = left + ratio * (right - left)
        empirical = error((left + right) / 2.0)
        asymptotic = abs(a * b * (b - a)) * L ** 3 / (6.0 * B ** 2 * f(a, a) ** 2)
        assert abs(empirical / asymptotic - 1.0) < 0.015
        checks += 1
    # The exact quartic sample coefficient.
    p, B = 4.0, 1.0
    a, b = 1.0 - 1.0 / p, 1.0 / p
    cubic = 2.0 * a * b * (b - a) / (B * B * f(a, a) ** 2)
    assert abs(cubic + 1.0 / math.sqrt(3.0)) < 1e-13
    checks += 1
    print('CHECKS_OK:', checks)


if __name__ == '__main__':
    check()
