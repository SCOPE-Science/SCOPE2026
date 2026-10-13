"""Independent finite-matrix checks for the critical-point survival formula.

Run with: python verify.py
Requires numpy and scipy as in requirements.txt.
The calculation is finite and does not prove the stated infinite theorem.
"""
import numpy as np
from scipy.linalg import expm
from numpy.polynomial import Polynomial


def check(v, g, gamma, eps, rng):
    v = np.asarray(v, dtype=float)
    k = len(v)
    p = Polynomial.fromroots(v)
    critical = np.sort(p.deriv().roots().real)
    scale = np.array([sum(1 / (x - v) ** 2) for x in critical])
    rates = gamma / (g * g * scale)
    vectors = np.column_stack(
        [(x - v) ** (-1) / np.sqrt(ss) for x, ss in zip(critical, scale)]
    )
    np.testing.assert_allclose(vectors.T @ vectors, np.eye(k - 1), atol=1e-9)

    h = np.zeros((k + 1, k + 1), dtype=complex)
    h[0, 0] = -0.5j * gamma
    h[0, 1:] = g
    h[1:, 0] = g
    h[1:, 1:] = np.diag(eps * v)

    # Direct full-Hamiltonian eigenvalues, not the secular-polynomial expansion.
    spectrum = np.linalg.eigvals(h)
    small = sorted(sorted(spectrum, key=abs)[: k - 1], key=lambda x: x.real)
    for j, eigenvalue in enumerate(small):
        assert abs(eigenvalue.real / eps - critical[j]) < 0.2
        assert abs(-2 * eigenvalue.imag / (eps * eps) - rates[j]) < 0.04

    # Direct finite-dimensional propagation, tested against the asymptotic
    # expression computed only from real roots of the detuning polynomial.
    for trial in range(4):
        initial = rng.normal(size=k + 1) + 1j * rng.normal(size=k + 1)
        initial /= np.linalg.norm(initial)
        for tau in (0.4, 1.0):
            final = expm(-1j * h * tau / (eps * eps)) @ initial
            exact = np.vdot(final, final).real
            projected = np.abs(vectors.T @ initial[1:]) ** 2
            predicted = np.sum(projected * np.exp(-rates * tau))
            assert abs(exact - predicted) < 0.01, (
                k, eps, trial, tau, exact, predicted
            )
    # Any real eigenvalue would imply a nonzero perfectly dark state.
    assert np.max(spectrum.imag) < 0


def main():
    rng = np.random.default_rng(101)
    sets = (
        [-1.0, 0.0, 1.0],
        [-1.3, -0.1, 0.7, 2.0],
        [-2.0, -0.9, 0.3, 0.6, 2.4],
        [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0],
    )
    for v in sets:
        for eps in (0.015, 0.006):
            check(v, 1.2, 1.7, eps, rng)
    print("VERIFY_OK models=8 survival_comparisons=64 rate_checks=30")


if __name__ == "__main__":
    main()
