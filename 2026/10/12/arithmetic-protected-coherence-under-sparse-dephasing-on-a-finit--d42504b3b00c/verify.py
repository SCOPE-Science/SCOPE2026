"""Numerical checks for the finite path under site-selective pure dephasing.

Requires NumPy and SciPy; calculations are checks, not proofs for all sizes.
Run: python verify.py
"""
import itertools
from math import gcd
import numpy as np
from scipy.linalg import eig


def path_generator(n, monitored):
    h = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    eye = np.eye(n)
    generator = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    for vertex, rate in monitored:
        p = np.zeros((n, n))
        p[vertex - 1, vertex - 1] = 1.0
        generator += rate * (
            np.kron(p.T, p)
            - 0.5 * np.kron(eye, p)
            - 0.5 * np.kron(p.T, eye)
        )
    return h, generator


def predicted_projection(n, positions, initial):
    length = n + 1
    g = gcd(length, *positions)
    r = n - g + 1
    j = np.arange(1, n + 1)
    dark = np.array([
        np.sqrt(2.0 / length) * np.sin(np.pi * m * j / g)
        for m in range(1, g)
    ]).T.reshape(n, g - 1)
    pd = dark @ dark.T
    b = np.eye(n) - pd
    predicted = (np.trace(b @ initial) / r) * b
    for col in dark.T:
        q = np.outer(col, col)
        predicted += q @ initial @ q
    return predicted, pd, dark


def predicted_positions(n, positions, start):
    length = n + 1
    g = gcd(length, *positions)
    r = n - g + 1
    w = lambda site: g / length if site % g else 0.0
    return np.array([
        (1 - w(start)) * (1 - w(target)) / r
        + (g / length ** 2) * (1 + 0.5 * (start % g == target % g)
                                + 0.5 * (start % g == (-target) % g))
        if (start % g and target % g) else
        (1 - w(start)) * (1 - w(target)) / r
        for target in range(1, n + 1)
    ], dtype=float)


def vec(matrix):
    return matrix.reshape(-1, order="F")


def mat(vector, n):
    return vector.reshape((n, n), order="F")


cases = 0
localized = 0
peripheral = 0
for n in range(2, 8):
    sites = range(1, n + 1)
    for count in (1, 2):
        for subset in itertools.combinations(sites, count):
            monitored = [(site, 0.75 + 0.13 * idx)
                         for idx, site in enumerate(subset)]
            h, lindblad = path_generator(n, monitored)
            eigenvalues, vectors = eig(lindblad)
            zero = np.flatnonzero(np.abs(eigenvalues) < 1e-8)
            inverse = np.linalg.inv(vectors)
            _, _, dark = predicted_projection(n, subset, np.eye(n) / n)
            # Every peripheral Bohr frequency arises from two protected modes.
            expected = [0.0]
            g = gcd(n + 1, *subset)
            energies = [2 * np.cos(np.pi * m / g) for m in range(1, g)]
            expected += [float(e1 - e2) for e1 in energies for e2 in energies]
            actual = [float(z.imag) for z in eigenvalues if z.real > -1e-8]
            for frequency in actual:
                assert min(abs(frequency - f) for f in expected) < 2e-7
            for frequency in expected:
                assert min(abs(frequency - f) for f in actual) < 2e-7
            peripheral += len(actual)
            for start in sites:
                state = np.zeros((n, n), dtype=complex)
                state[start - 1, start - 1] = 1.0
                direct = mat(vectors[:, zero] @ (inverse[zero] @ vec(state)), n)
                predicted, _, _ = predicted_projection(n, subset, state)
                assert np.max(np.abs(direct - predicted)) < 2e-7, (n, subset, start)
                assert np.max(np.abs(np.real(np.diag(direct))
                                     - predicted_positions(n, subset, start))) < 2e-7
                assert abs(sum(predicted_positions(n, subset, start)) - 1) < 2e-12
                localized += 1
            cases += 1
print(f"VERIFY_OK monitor_sets={cases} initial_sites={localized} peripheral_eigenvalues={peripheral}")
