#!/usr/bin/env python3
"""Supplementary finite checks for chiral Brownian escape susceptibility.

Uses NumPy and SciPy. The exact infinite-dimensional claims are proved in
RESULT.md; a finite grid cannot certify those universal conclusions.
"""

import math
import numpy as np
from scipy.integrate import quad
from scipy.sparse import csr_matrix, diags, eye, kron
from scipy.sparse.linalg import spsolve


def interval_series(omega, dr, D=1.0, L=1.0, terms=10000):
    n = np.arange(1, terms + 1, dtype=np.float64)
    a = D * (np.pi * n / L) ** 2 + dr
    return (L * L / (D * D * np.pi**2)) * np.sum(
        a / (n * n * (a * a + omega * omega))
    )


def interval_derivative(s, dr, order, D=1.0, L=1.0, terms=10000):
    """Return (-1)^order d^order_s chi(sqrt(s)), truncated."""
    n = np.arange(1, terms + 1, dtype=np.float64)
    a = D * (np.pi * n / L) ** 2 + dr
    return (L * L / (D * D * np.pi**2)) * math.factorial(order) * np.sum(
        a / (n * n * (a * a + s) ** (order + 1))
    )


def discrete_interval(N=65, Q=36, D=1.0, L=1.0, dr=0.2, om=0.7, v=0.2):
    """Solve the finite-difference backward equation and its v=0 response."""
    dx = 2 * L / (N + 1)
    x = np.linspace(-L + dx, L - dx, N)
    th = 2 * np.pi * np.arange(Q) / Q
    dt = 2 * np.pi / Q
    Ix, It = eye(N, format="csr"), eye(Q, format="csr")
    Tx = diags(
        [-np.ones(N - 1), 2 * np.ones(N), -np.ones(N - 1)],
        [-1, 0, 1], format="csr"
    ) / dx**2
    Dx = diags(
        [-np.ones(N - 1), np.ones(N - 1)], [-1, 1], format="csr"
    ) / (2 * dx)
    angular_gradient = np.zeros((Q, Q))
    angular_laplacian = np.zeros((Q, Q))
    for j in range(Q):
        angular_gradient[j, (j + 1) % Q] = 1 / (2 * dt)
        angular_gradient[j, (j - 1) % Q] = -1 / (2 * dt)
        angular_laplacian[j, j] = 2 / dt**2
        angular_laplacian[j, (j + 1) % Q] = -1 / dt**2
        angular_laplacian[j, (j - 1) % Q] = -1 / dt**2
    angular = dr * csr_matrix(angular_laplacian) - om * csr_matrix(angular_gradient)
    A = kron(It, D * Tx) + kron(angular, Ix)
    B = kron(diags(np.cos(th), 0, format="csr"), Dx)
    passive = np.tile((L * L - x * x) / (2 * D), Q)
    f = B @ passive
    chi_grid = float(f @ spsolve(A, f) / (N * Q))
    M0 = float(np.mean(passive))
    Mp = float(np.mean(spsolve(A - v * B, np.ones(N * Q))))
    Mh = float(np.mean(spsolve(A - 0.5 * v * B, np.ones(N * Q))))
    Mn = float(np.mean(spsolve(A + v * B, np.ones(N * Q))))
    return chi_grid, M0, Mp, Mh, Mn


def main():
    checks = 0
    c0 = interval_series(0, 0)
    assert abs(c0 - 1/90) < 1e-10
    checks += 1
    # A separate disk calculation: integrate the polynomial
    # -<F,A_0^{-1}F> after averaging over a uniform initial direction.
    disk = quad(lambda r: (2 * r) * r * r * (1 - r * r) / 64, 0, 1, epsabs=1e-13)[0]
    assert abs(disk - 1/384) < 1e-12
    checks += 1
    for dr in [0.0, 0.2, 0.7, 2.0]:
        for s in [0.0, 0.1, 1.0, 10.0, 100.0]:
            for order in range(5):
                assert interval_derivative(s, dr, order) > 0
                checks += 1
        values = [interval_series(om, dr) for om in [0, 0.5, 1, 2, 5, 20, 100]]
        assert all(a > b > 0 for a, b in zip(values, values[1:]))
        checks += 1
    cases = [(0.0, 0.0), (0.2, 0.7), (0.7, 2.0), (0.0, 3.0)]
    for dr, om in cases:
        chi, M0, Mp, Mh, Mn = discrete_interval(dr=dr, om=om)
        c = interval_series(om, dr)
        assert abs(chi / c - 1) < 0.02, (dr, om, chi, c)
        assert abs((M0 - Mp) / 0.2**2 - chi) < 0.00005
        assert abs((M0 - Mh) / 0.1**2 - chi) < 0.00002
        assert abs(Mp - Mn) < 1e-10
        assert Mp < M0
        checks += 5
    print(f"PASS: {checks} deterministic checks")
    print("Interval at zero chirality:", c0, "= 1/90")
    print("Disk at zero angular dynamics:", disk, "= 1/384")
    print("Finite differences: four angular parameter pairs, two swim speeds each")
    print("Limit: numerical grids and series truncations do not prove universal statements")


if __name__ == "__main__":
    main()
