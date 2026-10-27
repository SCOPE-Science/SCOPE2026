"""Reproduce the finite-dimensional weak-flux absorption checks.

Requires numpy and scipy. This program checks finite cases; the general
result follows from the analytic proof in RESULT.md.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def coefficient(n, a, gamma):
    if n % 2:
        return gamma * a * (n - a) / 4
    m = n // 2
    b = a % m
    return gamma * b * (m - b) / 2


def mean_lifetime(n, a, phi, gamma):
    H = np.zeros((n, n), dtype=complex)
    for j in range(n):
        k = (j + 1) % n
        H[j, k] += np.exp(1j * phi / n)
        H[k, j] += np.exp(-1j * phi / n)
    A = -1j * H
    A[0, 0] -= gamma
    initial = np.eye(n)[:, a]
    X = solve_continuous_lyapunov(A, -np.outer(initial, initial.conj()))
    assert np.linalg.norm(A @ X + X @ A.conj().T + np.outer(initial, initial.conj())) < 1e-7
    assert abs(X.trace().imag) < 1e-7
    return X.trace().real


def sine_sum(n, a):
    return sum(
        (np.sin(2 * np.pi * k * a / n) / np.sin(2 * np.pi * k / n)) ** 2
        for k in range(1, (n - 1) // 2 + 1)
    )


def run():
    checks = 0
    for n in range(3, 18):
        for a in range(n):
            for gamma in (0.8, 1.3, 2.6):
                wanted = coefficient(n, a, gamma)
                got = gamma * sine_sum(n, a) / 2
                assert abs(got - wanted) < 1e-8, (n, a, gamma, wanted, got)
                checks += 1
    for n in (5, 6, 7, 8, 9, 10, 11):
        for a in range(n):
            for gamma in (0.9, 1.7):
                wanted = coefficient(n, a, gamma)
                coarse = 0.09 ** 2 * mean_lifetime(n, a, 0.09, gamma)
                fine = 0.035 ** 2 * mean_lifetime(n, a, 0.035, gamma)
                # A bounded-lifetime case has vanishing rescaled limit.
                assert abs(fine - wanted) < max(0.13, 0.07 * wanted), (n, a, gamma, fine, wanted)
                assert abs(coarse - wanted) < max(0.25, 0.15 * wanted), (n, a, gamma, coarse, wanted)
                checks += 2
    print(f"PASS: {checks} identity and independent finite-matrix/flux checks")


if __name__ == "__main__":
    run()
