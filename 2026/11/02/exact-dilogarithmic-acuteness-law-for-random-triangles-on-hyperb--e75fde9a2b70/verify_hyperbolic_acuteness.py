"""Independent numerical checks for the hyperbolic-circle acuteness theorem.

Python 3 standard library only.  The universal result requires the analytic proof;
these calculations check its main normalization and sampling identities.
"""
import math
import random

PI = math.pi


def odd_dilog_difference(z, terms=4500):
    """Return Li_2(z)-Li_2(-z) using its absolutely convergent odd series."""
    assert 0 <= z < 1
    acc = 0.0
    power = z
    for k in range(terms):
        m = 2 * k + 1
        acc += 2 * power / (m * m)
        power *= z * z
        if abs(power) < 1e-17:
            break
    return acc


def probability_formula(R):
    s = math.sinh(R)
    z = s * s / (2 + s * s)
    return 0.25 + 3 / PI**2 * odd_dilog_difference(z)


def composite_simpson(f, a, b, n=24000):
    assert n % 2 == 0
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + h * i)
    return total * h / 3


def probability_integral(R):
    s = math.sinh(R)
    kappa = 1 + 2 / (s * s)
    start = math.acos(1 / kappa)
    integrand = lambda t: math.acos(max(-1.0, min(1.0, kappa * math.cos(t))))
    return 0.25 + 6 / PI**2 * composite_simpson(integrand, start, PI / 2)


def tangent_to(z, w):
    """Initial oriented Euclidean tangent of the Poincare geodesic from z to w."""
    zx, zy = z
    wx, wy = w
    determinant = zx * wy - zy * wx
    if abs(determinant) < 1e-11:
        raise ArithmeticError("near-diameter configuration")
    k = (1.0 + zx * zx + zy * zy) / 2.0
    cx = k * (wy - zy) / determinant
    cy = k * (zx - wx) / determinant
    tx, ty = -(zy - cy), zx - cx
    if tx * (wx - zx) + ty * (wy - zy) < 0:
        tx, ty = -tx, -ty
    return tx, ty


def direct_acute_triangle(R, rng):
    rho = math.tanh(R / 2)
    while True:
        angles = [2 * PI * rng.random() for _ in range(3)]
        pts = [(rho * math.cos(t), rho * math.sin(t)) for t in angles]
        try:
            for i in range(3):
                t1 = tangent_to(pts[i], pts[(i + 1) % 3])
                t2 = tangent_to(pts[i], pts[(i + 2) % 3])
                if t1[0] * t2[0] + t1[1] * t2[1] <= 0:
                    return False
            return True
        except ArithmeticError:
            continue


def run():
    radii = [0.2, 0.5, 1.0, 2.0, 3.0]
    for R in radii:
        p1, p2 = probability_formula(R), probability_integral(R)
        assert abs(p1 - p2) < 4e-8, (R, p1, p2)
        assert 0.25 < p1 < 1
    assert all(probability_formula(a) < probability_formula(b)
               for a, b in zip(radii, radii[1:]))
    print('INDEPENDENT_GAP_INTEGRALS_AND_ODD_DILOG_SERIES_PASSED', len(radii))

    rng = random.Random(20261029)
    trials = 25000
    for R in [0.3, 1.0, 2.0, 3.0]:
        expected = probability_formula(R)
        observed = sum(direct_acute_triangle(R, rng) for _ in range(trials)) / trials
        sigma = math.sqrt(expected * (1 - expected) / trials)
        assert abs(expected - observed) < max(5.0 * sigma, 0.012), (R, expected, observed)
        print('DIRECT_POINCARE_GEODESIC_TANGENT_MONTE_CARLO_PASSED', R, trials)

    for R in [0.03, 0.05, 0.08]:
        p = probability_formula(R)
        small = 0.25 + 3 * R**2 / PI**2 - R**4 / (2 * PI**2)
        assert abs(p - small) < 0.3 * R**6
    print('SMALL_RADIUS_COEFFICIENT_DIAGNOSTICS_PASSED')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    run()
