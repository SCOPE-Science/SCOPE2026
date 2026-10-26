#!/usr/bin/env python3
"""Finite sanity checks for the local UTR-Adaptive power-minimum recurrence."""
import math


def one_step(x, p, rho):
    a = abs(x)
    if a == 0:
        return 0.0
    grad = a ** (p - 1)
    hess = (p - 1) * a ** (p - 2)
    root_grad = a ** ((p - 1) / 2)
    if hess >= rho * root_grad:
        radius = root_grad / (2 * rho)
        unconstrained = grad / hess
    else:
        radius = root_grad / (4 * rho)
        unconstrained = grad / (hess + rho * root_grad)
    magnitude = min(radius, unconstrained)
    return x - math.copysign(magnitude, x)


def q3(rho):
    if rho <= 1:
        return 0.5
    if rho <= 2:
        return 1.0 - 1.0 / (2.0 * rho)
    return 1.0 - 1.0 / (4.0 * rho)


def main():
    for rho in (0.5, 1.0, 1.5, 2.0, 3.0):
        x0 = 1.0e-3
        observed = one_step(x0, 3.0, rho) / x0
        expected = q3(rho)
        assert abs(observed - expected) < 1e-12, (rho, observed, expected)
        print(f"p=3 rho={rho:g}: factor={observed:.12g} PASS")

    for p in (4.0, 5.0):
        rho = 1.0
        x = 1.0e-2
        n = 100000
        for _ in range(n):
            x = one_step(x, p, rho)
        s = (p - 3.0) / 2.0
        observed = abs(x) ** (-s) / n
        expected = (p - 3.0) / (8.0 * rho)
        relative_error = abs(observed - expected) / expected
        assert relative_error < 0.02, (p, observed, expected, relative_error)
        print(f"p={p:g}: scaled inverse-power={observed:.8g}, limit={expected:.8g}, relative_error={relative_error:.4%} PASS")
    print("Finite checks passed; analytic proof remains in RESULT.md.")


if __name__ == "__main__":
    main()
