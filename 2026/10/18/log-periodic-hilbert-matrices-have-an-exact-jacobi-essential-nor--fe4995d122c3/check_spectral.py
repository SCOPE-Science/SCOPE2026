"""Finite spectral diagnostics for a log-periodically modulated Hilbert matrix.

The analytical arguments, not this finite checker, prove the infinite theorem.
"""
import math
import numpy as np


def finite_section(omega, eps, radius):
    indices = np.arange(-radius, radius + 1, dtype=float)
    c = np.pi / np.cosh(np.pi * omega * indices)
    size = 2 * radius + 1
    b = np.diag(c)
    for j in range(size - 1):
        b[j + 1, j] = eps * c[j] / 2
        b[j, j + 1] = eps * c[j + 1] / 2
    return b


def certified_error(omega, eps, radius):
    c_n = np.pi / math.cosh(math.pi * omega * radius)
    c_next = np.pi / math.cosh(math.pi * omega * (radius + 1))
    return (1 + abs(eps)) * c_next + abs(eps) * c_n / 2


def curvature(omega):
    r = 1 / math.cosh(math.pi * omega)
    return (1 + 3 * r * r) / (4 * (1 - r * r))


def main():
    count = 0
    for omega in [0.35, 0.8, 1.4]:
        radius = 36
        for eps in [-0.08, -0.04, -0.02, 0.0, 0.02, 0.04, 0.08]:
            b = finite_section(omega, eps, radius)
            sigma = float(np.linalg.svd(b, compute_uv=False)[0])
            lower = np.pi * math.sqrt(1 + eps * eps / 2)
            upper = np.pi * (1 + abs(eps))
            err = certified_error(omega, eps, radius)
            assert sigma + err >= lower - 1e-11
            assert sigma <= upper + 1e-11
            assert sigma >= lower - 1e-9
            if eps != 0:
                ratio = (sigma / math.pi - 1) / eps ** 2
                expected = curvature(omega)
                # Fourth-order truncation error after dividing by eps^2 is O(eps^2).
                assert abs(ratio - expected) < 0.015
                print(f"omega={omega:.2f}; eps={eps:+.3f}; curvature={ratio:.9f}; analytic={expected:.9f}; norm={sigma:.10f}; cert_tail={err:.2e}")
            count += 1
        plus = np.linalg.svd(finite_section(omega, 0.04, radius), compute_uv=False)[0]
        minus = np.linalg.svd(finite_section(omega, -0.04, radius), compute_uv=False)[0]
        assert abs(plus - minus) < 1e-10
    assert count == 21
    print(f"PASS: {count} parameter tests and 3 evenness checks.")


if __name__ == "__main__":
    main()
