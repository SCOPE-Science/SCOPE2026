#!/usr/bin/env python3
"""Finite-truncation sanity checks for the power-law quantum-walk radial law.

The analytic proof of the infinite-dimensional theorem is in RESULT.md.
"""
from math import cos, gamma, pi, sin, isclose


def k_alpha(alpha):
    beta = 1.0 / alpha
    return 2.0 ** (beta - 1.0) * gamma(1.0 - beta) * cos(pi * beta / 2.0)


def sums(alpha, n, multiple=300):
    # Choose the time so that (ct)^(1/alpha)=n, with c=1.
    t = float(n) ** alpha
    mean = var = twice = 0.0
    for k in range(1, multiple * n + 1):
        phase = t / (float(k) ** alpha)
        p = sin(phase) ** 2
        mean += p
        var += p * (1.0 - p)
        twice += sin(2.0 * phase) ** 2
    return mean, var, twice


def main():
    for alpha in (1.5, 2.0, 3.0):
        beta = 1.0 / alpha
        constant = k_alpha(alpha)
        for n in (150, 500):
            mean, var, twice = sums(alpha, n)
            assert isclose(4.0 * var, twice, rel_tol=3e-11, abs_tol=3e-10)
            assert abs(mean / (constant * n) - 1.0) < 0.045
            assert abs(var / mean - 2.0 ** (beta - 2.0)) < 0.035
            print(f"alpha={alpha:g} N={n:d} mean/limit={mean/(constant*n):.6f} "
                  f"Fano={var/mean:.6f} target={2.0**(beta-2.0):.6f}")
    print("PASS: finite-truncation sanity checks; no infinite-proof certification")


if __name__ == "__main__":
    main()
