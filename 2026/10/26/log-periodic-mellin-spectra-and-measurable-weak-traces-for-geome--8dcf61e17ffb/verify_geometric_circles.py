"""Reproduce finite checks for geometric-circle Bergman Toeplitz spectra.

The infinite spectral and weak-trace assertions require the accompanying proof;
these finite checks do not certify asymptotic statements.
"""
from __future__ import annotations
import math


def profile(alpha: float, base: float, t: float, radius: int = 36) -> float:
    """Two-sided discrete Mellin profile, truncated with controlled tails."""
    return sum(base ** (alpha * (t - ell)) *
               math.exp(-base ** (t - ell))
               for ell in range(-radius, radius + 1))


def eigenvalue(alpha: float, base: float, n: int, radius: int = 50) -> float:
    """Circle-measure diagonal coefficient, truncated only in geometric tail."""
    if n < 0:
        raise ValueError('n must be nonnegative')
    return (n + 1) * sum(base ** (-alpha * j) *
                         (1 - base ** (-j)) ** n
                         for j in range(1, radius + 1))


def check() -> int:
    tested = 0
    for alpha in (1.2, 1.5, 2.0, 2.7, 3.5):
        for base in (2.0, 3.0, 4.0, 7.0):
            for t in (0.0, 0.13, 0.31, 0.5, 0.73, 0.99):
                p = profile(alpha, base, t)
                assert p > 0
                assert abs(profile(alpha, base, t + 1) - p) < 5e-10 * p
                tested += 2
    for alpha, base in ((2.0, 4.0), (1.5, 3.0), (2.7, 2.0)):
        beta = alpha - 1
        for k in range(7, 12):
            for m in (1, 2):
                n = int(m * base ** k)
                expected = profile(alpha, base, (math.log(n) / math.log(base)) % 1)
                observed = n ** beta * eigenvalue(alpha, base, n)
                relative = abs(observed / expected - 1)
                assert relative < 0.06, (alpha, base, n, relative)
                tested += 1
    # For the trace-class boundary alpha=2, the Mellin mean is Gamma(2)/ln b.
    for base in (2., 3., 4., 7.):
        nquad = 4096
        average = sum(profile(2, base, (k + 0.5) / nquad)
                      for k in range(nquad)) / nquad
        assert abs(average - 1 / math.log(base)) < 1e-10
        tested += 1
    # The weak-trace logarithmic finite means converge much more slowly;
    # these values are evidence for scale, not infinite-dimensional proof.
    for base in (2., 4.):
        N = 20000
        prefix = sum(eigenvalue(2, base, n) for n in range(N + 1))
        average = prefix / math.log(N + 1)
        assert abs(average - 1 / math.log(base)) < 0.17
        tested += 1
    return tested


if __name__ == '__main__':
    print(f'Finite geometric-circle spectral tests passed: {check()}')
