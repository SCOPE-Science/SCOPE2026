#!/usr/bin/env python3
"""Reproducibility checks for the two-defect cycle spectral formulas.

The analytic proof is in RESULT.md. This script checks Green-kernel identities,
threshold limits, and the finite-size scaling equations using only Python's
standard library. Numerical checks are corroborative, not proofs of limits.
"""
import math

TOL = 2e-10

def green_sum(N, d, kappa):
    E = 2.0 * math.cosh(kappa)
    return sum(
        math.cos(2.0 * math.pi * j * d / N) / (E - 2.0 * math.cos(2.0 * math.pi * j / N))
        for j in range(N)
    ) / N

def green_formula(N, d, kappa):
    g0 = math.sinh(N * kappa) / (
        2.0 * math.sinh(kappa) * (math.cosh(N * kappa) - 1.0)
    )
    gd = math.cosh((N / 2.0 - d) * kappa) / (
        2.0 * math.sinh(kappa) * math.sinh(N * kappa / 2.0)
    )
    return g0, gd

def scaled_lambda(N, d, branch, y):
    sign = 1.0 if branch == "symmetric" else -1.0
    denominator = math.cosh(y / 2.0) + sign * math.cosh((0.5 - d / N) * y)
    return 2.0 * N * math.sinh(y / N) * math.sinh(y / 2.0) / denominator

def limiting_lambda(rho, branch, y):
    sign = 1.0 if branch == "symmetric" else -1.0
    denominator = math.cosh(y / 2.0) + sign * math.cosh((0.5 - rho) * y)
    return 2.0 * y * math.sinh(y / 2.0) / denominator

def bisect_increasing(f, target, lo, hi):
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

def root_scaled(N, d, branch, lam):
    lo = 1e-8
    if branch == "antisymmetric":
        threshold = 2.0 * N * N / (d * (N - d))
        if lam <= threshold:
            return None
        lo = 1e-6
    hi = 1.0
    while scaled_lambda(N, d, branch, hi) < lam:
        hi *= 2.0
        if hi > 100.0:
            raise RuntimeError("failed to bracket scaled root")
    return bisect_increasing(lambda y: scaled_lambda(N, d, branch, y), lam, lo, hi)

def root_limit(rho, branch, lam):
    threshold = 2.0 / (rho * (1.0 - rho))
    if branch == "antisymmetric" and lam <= threshold:
        return None
    lo = 1e-8
    hi = 1.0
    while limiting_lambda(rho, branch, hi) < lam:
        hi *= 2.0
        if hi > 100.0:
            raise RuntimeError("failed to bracket limiting root")
    return bisect_increasing(lambda y: limiting_lambda(rho, branch, y), lam, lo, hi)

def main():
    checks = 0
    for N, d, kappa in [(7, 2, 0.17), (10, 5, 0.2), (17, 4, 0.07), (24, 9, 0.11)]:
        g0, gd = green_formula(N, d, kappa)
        assert abs(g0 - green_sum(N, 0, kappa)) < TOL
        assert abs(gd - green_sum(N, d, kappa)) < TOL
        assert g0 > gd > 0.0
        checks += 3

    for N, d in [(8, 2), (10, 5), (17, 4), (24, 9)]:
        Vc = 2.0 * N / (d * (N - d))
        for kappa in [1e-5, 3e-5]:
            # Stable identity for the antisymmetric resolvent channel.
            gap = (math.sinh(d * kappa / 2.0) * math.sinh((N - d) * kappa / 2.0)
                   / (math.sinh(kappa) * math.sinh(N * kappa / 2.0)))
            assert abs(gap - d * (N - d) / (2.0 * N)) < 2e-3
            checks += 1
        assert abs(Vc * d * (N - d) / (2.0 * N) - 1.0) < 1e-14
        checks += 1

    # The two branches have the predicted number of roots across the threshold.
    N, d = 80, 20
    lam_c_N = 2.0 * N * N / (d * (N - d))
    assert root_scaled(N, d, "symmetric", 8.0) is not None
    assert root_scaled(N, d, "antisymmetric", lam_c_N - 0.1) is None
    assert root_scaled(N, d, "antisymmetric", lam_c_N + 0.1) is not None
    checks += 3

    # Double-scaling roots converge to the stated limiting equations.
    rho = 0.25
    lam = 14.0
    y_lim_plus = root_limit(rho, "symmetric", lam)
    y_lim_minus = root_limit(rho, "antisymmetric", lam)
    errors = []
    for N in [80, 160, 320]:
        d = N // 4
        for branch, y_lim in [("symmetric", y_lim_plus), ("antisymmetric", y_lim_minus)]:
            y_N = root_scaled(N, d, branch, lam)
            assert y_N is not None
            errors.append(abs(y_N - y_lim))
            assert abs(scaled_lambda(N, d, branch, y_N) - lam) < 1e-8
            checks += 2
    assert errors[-1] < errors[0]
    checks += 1
    print(f"PASS: {checks} checks; max finite-size scaling error={max(errors):.6g}; final error={errors[-1]:.6g}")

if __name__ == "__main__":
    main()
