"""Deterministic numerical checks for the Rayleigh-residual distortion formulas.

The checks support, but do not replace, the exact proofs in RESULT.md.
"""
from __future__ import annotations

import sys
import numpy as np


def residual_norm_from_weights(lam: np.ndarray, w: np.ndarray) -> float:
    rho = np.sum(w * lam)
    return float(np.sqrt(np.sum(w * np.abs(lam - rho) ** 2)))


def filtered_ratio(lam: np.ndarray, w: np.ndarray, gains: np.ndarray) -> float:
    rin = residual_norm_from_weights(lam, w)
    s2 = float(np.sum(w * gains**2))
    q = w * gains**2 / s2
    rout = residual_norm_from_weights(lam, q)
    return rout / rin


def check_random_normal_filters() -> float:
    rng = np.random.default_rng(20260921)
    max_violation = 0.0
    for _ in range(5000):
        n = int(rng.integers(2, 10))
        lam = rng.normal(size=n) + 1j * rng.normal(size=n)
        gains = np.exp(rng.uniform(-3.0, 3.0, size=n))
        w = rng.dirichlet(np.ones(n))
        r = filtered_ratio(lam, w, gains)
        m = float(gains.min())
        M = float(gains.max())
        max_violation = max(max_violation, r - M / m, m / M - r, 0.0)
    assert max_violation < 2e-12
    return max_violation


def check_two_state_formula() -> float:
    lam = np.array([1.0 + 2.0j, -3.0 + 0.4j])
    m, M = 0.7, 5.0
    gains = np.array([m, M])
    max_error = 0.0
    for p in [1e-10, 0.1, 0.25, 0.8, 1.0 - 1e-10]:
        w = np.array([1.0 - p, p])
        measured = filtered_ratio(lam, w, gains)
        exact = m * M / ((1.0 - p) * m * m + p * M * M)
        max_error = max(max_error, abs(measured - exact))
    assert max_error < 2e-12
    return max_error


def check_power_corollary() -> float:
    max_error = 0.0
    for kappa in [2.0, 3.0, 10.0, 100.0]:
        lam = np.array([1.0, kappa])
        gains = lam.copy()
        for p in [1e-10, 1.0 / (kappa + 1.0), 0.5]:
            w = np.array([1.0 - p, p])
            measured = filtered_ratio(lam, w, gains)
            exact = kappa / (1.0 + p * (kappa * kappa - 1.0))
            max_error = max(max_error, abs(measured - exact))
    assert max_error < 2e-10
    return max_error


def check_exact_zero_barrier() -> float:
    # A=diag(0,1,3), phi(t)=t.  The filtered vector is independent of eps.
    max_error = 0.0
    for eps in [1e-2, 1e-4, 1e-8, 1e-12]:
        x = np.array([np.sqrt(1.0 - eps), np.sqrt(eps / 2.0), np.sqrt(eps / 2.0)])
        A = np.diag([0.0, 1.0, 3.0])
        rho = float(x @ (A @ x))
        rin = float(np.linalg.norm(A @ x - rho * x))
        y0 = A @ x
        y = y0 / np.linalg.norm(y0)
        rho_y = float(y @ (A @ y))
        rout = float(np.linalg.norm(A @ y - rho_y * y))
        exact_in = np.sqrt(eps * (5.0 - 4.0 * eps))
        exact_out = 0.6
        max_error = max(max_error, abs(rin - exact_in), abs(rout - exact_out))
    assert max_error < 2e-12
    return max_error


if __name__ == "__main__":
    print(f"python={sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"numpy={np.__version__}")
    print(f"random_normal_max_bound_violation={check_random_normal_filters():.3e}")
    print(f"two_state_max_formula_error={check_two_state_formula():.3e}")
    print(f"power_corollary_max_formula_error={check_power_corollary():.3e}")
    print(f"exact_zero_max_formula_error={check_exact_zero_barrier():.3e}")
    print("ALL_CHECKS_PASS")
