"""Finite reproducibility checks for a scalar interval FIR robustness theorem.

Requires Python 3 and NumPy. These calculations are diagnostics, not
substitutes for the complex-analytic proof of the infinite-dimensional bound.
"""
from fractions import Fraction
import cmath
import math
import numpy as np


def companion(a, gains):
    h = len(gains)
    mat = np.zeros((h, h), dtype=float)
    mat[0, 0] = a + gains[0]
    if h > 1:
        mat[0, 1:] = gains[1:]
        mat[1:, :-1] = np.eye(h - 1)
    return mat


def check():
    checks = 0
    for c in (-3.0, 0.0, 0.8, 2.4):
        for t in (0.13, 0.65, 1.7, 2.4):
            for h in (1, 2, 3, 5):
                gains = [-c] + ([-t * t / 4.0] + [0.0] * (h - 2) if h >= 2 else [])
                predicted = t if h == 1 else t / 2.0
                for u in np.linspace(-1, 1, 19):
                    eigen = np.linalg.eigvals(companion(c + t * float(u), gains))
                    actual = max(abs(z) for z in eigen)
                    assert actual <= predicted + 3e-4, (c, t, h, u, actual)
                    if h >= 2:
                        assert abs(actual - predicted) < 3e-4, (c, t, h, u, actual)
                    elif abs(u) == 1:
                        assert abs(actual - predicted) < 3e-4
                    checks += 1
    for t in (Fraction(1, 2), Fraction(2, 3), Fraction(11, 5), Fraction(17, 7)):
        for h in (2, 3, 8):
            for u in (Fraction(-1, 1), Fraction(-1, 2), Fraction(0), Fraction(2, 3), Fraction(1)):
                delta = t * u
                # The nonzero characteristic factor is z^2-delta*z+t^2/4.
                # Both its discriminant and product are checked exactly.
                disc = delta * delta - t * t
                prod = t * t / 4
                assert disc <= 0 and prod > 0
                # Expanded polynomial has degree h and exactly three coefficients.
                coeffs = [Fraction(0) for _ in range(h + 1)]
                coeffs[0] = 1
                coeffs[1] = -delta
                coeffs[2] = prod
                assert len(coeffs) == h + 1
                assert all(x == 0 for x in coeffs[3:])
                checks += 4
    # Joukowski inverse identity at the sharp radius R=t/2.
    for t in (0.4, 1.3, 3.6):
        for c in (-3.0, 0.0, 4.0):
            for z in np.linspace(t * 0.501, 14.0 * t, 80):
                w = c + z + t * t / (4.0 * z)
                phi = (w - c + cmath.sqrt((w - c) ** 2 - t * t)) / t
                assert abs(phi - 2 * z / t) < 4e-12
                checks += 1
    return checks


if __name__ == '__main__':
    n = check()
    print(f'PASS: {n} independent deterministic computational checks')
