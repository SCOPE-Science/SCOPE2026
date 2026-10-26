#!/usr/bin/env python3
"""Independent exact-rational checks of the entropy–quadratic diversity covariance."""
from fractions import Fraction as F


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def tilted_moment_covariance(alpha):
    """Compute E[H Q] - E[H] E[Q] by Dirichlet quadratic tilting."""
    assert len(alpha) >= 2 and all(type(v) is int and v > 0 for v in alpha)
    A = sum(alpha)
    entropy_mean = harmonic(A) - sum((F(a, A) * harmonic(a) for a in alpha), F(0))
    q_mean = sum((F(a * (a + 1), A * (A + 1)) for a in alpha), F(0))
    hq = F(0)
    for i, a in enumerate(alpha):
        shifted = list(alpha)
        shifted[i] += 2
        entropy_shifted = harmonic(A + 2) - sum(
            (F(b, A + 2) * harmonic(b) for b in shifted), F(0)
        )
        hq += F(a * (a + 1), A * (A + 1)) * entropy_shifted
    return hq - entropy_mean * q_mean


def structural_covariance(alpha):
    """Compute closed form via weighted pairwise harmonic differences."""
    A = sum(alpha)
    kappa = sum((F(alpha[i] * alpha[j]) for i in range(len(alpha))
                 for j in range(i + 1, len(alpha))), F(0))
    correction = sum((F(alpha[i] * alpha[j], A * A) *
                      (alpha[i] - alpha[j]) *
                      (harmonic(alpha[i]) - harmonic(alpha[j]))
                      for i in range(len(alpha))
                      for j in range(i + 1, len(alpha))), F(0))
    return -F(2, A * (A + 1) * (A + 2)) * (kappa / (A + 1) + A * correction)


def run():
    checks = {
        (1, 1): F(-1, 36),
        (1, 3): F(-37, 1200),
        (2, 2): F(-1, 75),
        (1, 2, 3): F(-61, 3528),
    }
    for alpha, expected in checks.items():
        from_moments = tilted_moment_covariance(alpha)
        from_structure = structural_covariance(alpha)
        assert from_moments == from_structure == expected, (
            alpha, from_moments, from_structure, expected)
        print(alpha, '=', from_moments)
    assert abs(checks[(1, 3)]) > 2 * abs(checks[(2, 2)])
    print('All independent exact-fraction checks passed.')


if __name__ == '__main__':
    run()
