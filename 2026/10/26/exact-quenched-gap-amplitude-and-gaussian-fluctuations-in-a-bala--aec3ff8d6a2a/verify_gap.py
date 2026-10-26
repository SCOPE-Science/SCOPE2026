#!/usr/bin/env python3
"""Finite-matrix consistency checks of the exact string reduction and predicted gap limits.

These finite computations are not proofs of infinite-system limit laws.
Requirements: numpy, scipy. Run: python verify_gap.py
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def energy_gap(j):
    j = np.asarray(j, dtype=float)
    h = np.append(j, 1.0)
    diag = h * h
    diag[1:] += j * j
    offdiag = j * h[:-1]
    eigmin = eigh_tridiagonal(diag, offdiag, select='i', select_range=(0, 0), check_finite=False)[0][0]
    assert eigmin > 0
    return math.sqrt(eigmin)


def exact_matrix_check():
    rng = np.random.default_rng(321)
    for n in (3, 7, 12):
        j = rng.uniform(0.5, 1.0, n - 1)
        h = np.append(j, 1.0)
        m = np.diag(h) + np.diag(j, k=-1)
        w = 1.0 / (h * h)
        coordinates = np.arange(1, n + 1)
        green = np.minimum.outer(coordinates, coordinates)
        b = (np.sqrt(w)[:, None] * green * np.sqrt(w)[None, :])
        eigen_gap = 1.0 / math.sqrt(np.linalg.eigvalsh(b)[-1])
        original_gap = np.linalg.svd(m, compute_uv=False)[-1]
        assert np.isclose(original_gap, eigen_gap, rtol=1e-11, atol=1e-11)
        assert np.isclose(energy_gap(j), original_gap, rtol=1e-10, atol=1e-10)
    print('Exact matrix reduction: PASS for 3, 7 and 12 sites')


def monte_carlo():
    rng = np.random.default_rng(41022)
    mean = math.pi / (2 * math.sqrt(2))
    variance = math.pi**2 / 128
    print('J uniform on [1/2,1]: predicted amplitude', mean, 'predicted CLT variance', variance)
    for n, trials in ((100, 800), (300, 500), (1000, 180)):
        samples = []
        for _ in range(trials):
            j = rng.uniform(0.5, 1.0, n - 1)
            samples.append(n * energy_gap(j))
        samples = np.array(samples)
        print('N', n, 'trials', trials, 'empirical_N_gap_mean', samples.mean(),
              'empirical_scaled_variance', n * samples.var(ddof=1))


if __name__ == '__main__':
    exact_matrix_check()
    monte_carlo()
