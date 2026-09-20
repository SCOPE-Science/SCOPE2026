#!/usr/bin/env python3
"""Deterministic checks for the stagewise-safe Richardson frontier."""

from math import sqrt, isclose

THRESHOLD = 1.0 + sqrt(2.0)

def safe_optimum(kappa):
    """Return (factor, normalized steps L*tau_1, L*tau_2)."""
    if not kappa > 1.0:
        raise ValueError("kappa must exceed 1")
    a = 1.0 / kappa
    if kappa <= THRESHOLD:
        factor = (kappa - 1.0) ** 2 / (kappa * kappa + 6.0 * kappa + 1.0)
        up = 2.0 / (1.0 + a + (1.0 - a) / sqrt(2.0))
        um = 2.0 / (1.0 + a - (1.0 - a) / sqrt(2.0))
        return factor, up, um
    factor = (kappa - 2.0) / (kappa + 2.0)
    return factor, 2.0, 2.0 * kappa / (kappa + 2.0)

def polynomial_sup(kappa, u, v, n=200000):
    """Grid approximation to max_{x in [1/kappa,1]} |(1-u*x)(1-v*x)|."""
    a = 1.0 / kappa
    best = 0.0
    arg = None
    for j in range(n + 1):
        x = a + (1.0 - a) * j / n
        val = abs((1.0 - u * x) * (1.0 - v * x))
        if val > best:
            best, arg = val, x
    return best, arg

def chebyshev_two_factor(kappa):
    return (kappa - 1.0) ** 2 / (kappa * kappa + 6.0 * kappa + 1.0)

def repeated_gd_two_factor(kappa):
    return ((kappa - 1.0) / (kappa + 1.0)) ** 2

def main():
    samples = [1.5, 2.0, THRESHOLD, 3.0, 5.0, 10.0]
    print("kappa factor grid_sup L*tau_1 L*tau_2 argmax")
    for kappa in samples:
        factor, u, v = safe_optimum(kappa)
        grid, arg = polynomial_sup(kappa, u, v)
        assert u <= 2.0 + 1e-12 and v <= 2.0 + 1e-12
        assert abs(grid - factor) < 2e-9
        print(f"{kappa:.12g} {factor:.12g} {grid:.12g} "
              f"{u:.12g} {v:.12g} {arg:.12g}")

    # Exact algebraic comparison identities, evaluated numerically.
    for kappa in [3.0, 5.0, 10.0, 100.0]:
        safe = (kappa - 2.0) / (kappa + 2.0)
        gd2 = repeated_gd_two_factor(kappa)
        cheb = chebyshev_two_factor(kappa)
        rhs_gd = 4.0 / ((kappa + 1.0) ** 2 * (kappa + 2.0))
        rhs_cheb = 4.0 * (kappa * kappa - 2.0 * kappa - 1.0) / (
            (kappa + 2.0) * (kappa * kappa + 6.0 * kappa + 1.0)
        )
        assert isclose(gd2 - safe, rhs_gd, rel_tol=1e-13, abs_tol=1e-15)
        assert isclose(safe - cheb, rhs_cheb, rel_tol=1e-13, abs_tol=1e-15)

    # General m-stage barrier at the smallest eigenvalue.
    for kappa in [3.0, 5.0, 10.0]:
        for m in [1, 2, 5, 10]:
            lower = (1.0 - 2.0 / kappa) ** m
            upper = ((kappa - 1.0) / (kappa + 1.0)) ** m
            assert 0.0 <= lower <= upper <= 1.0

    print("all checks passed")

if __name__ == "__main__":
    main()
