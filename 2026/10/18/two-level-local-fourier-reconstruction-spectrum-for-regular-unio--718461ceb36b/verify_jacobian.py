"""Numerical, independent check of regular-arc Fourier endpoint spectra.

Requires Python 3, NumPy and SciPy. This is a finite numerical test,
not a substitute for the all-integer analytic singular-value calculation.
"""
import numpy as np
from scipy.linalg import null_space


def positive_moments(starts, ends):
    m = len(starts)
    return np.array([
        np.sum(np.exp(-1j * k * starts) - np.exp(-1j * k * ends))
        / (2j * np.pi * k)
        for k in range(1, m)
    ])


rng = np.random.default_rng(734311)
checks = 0
for m in range(2, 11):
    for alpha in (0.13, 0.28, 0.50, 0.74, 0.93):
        starts = 2 * np.pi * np.arange(m) / m
        ends = starts + 2 * np.pi * alpha / m
        J = np.zeros((2 * m - 2, 2 * m), dtype=float)
        for k in range(1, m):
            row = np.r_[-np.exp(-1j * k * starts),
                        np.exp(-1j * k * ends)] / (2 * np.pi)
            J[2 * k - 2] = row.real
            J[2 * k - 1] = row.imag
        constraints = np.zeros((2, 2 * m))
        constraints[0] = np.r_[-np.ones(m), np.ones(m)]
        constraints[1] = 1
        Q = null_space(constraints)
        observed = np.sort(np.linalg.svd(J @ Q, compute_uv=False))
        common = m / (4 * np.pi ** 2)
        low = np.sqrt(common * (1 - abs(np.cos(np.pi * alpha))))
        high = np.sqrt(common * (1 + abs(np.cos(np.pi * alpha))))
        predicted = np.sort([low] * (m - 1) + [high] * (m - 1))
        assert np.max(np.abs(observed - predicted)) < 2e-12
        assert np.max(np.abs(positive_moments(starts, ends))) < 2e-14
        z = Q @ rng.normal(size=2 * m - 2)
        z /= np.linalg.norm(z)
        t = 1e-7
        actual = (positive_moments(starts + t * z[:m],
                                   ends + t * z[m:])
                  - positive_moments(starts, ends)) / t
        linear = np.array([
            (J[2 * j] + 1j * J[2 * j + 1]) @ z
            for j in range(m - 1)
        ])
        assert np.linalg.norm(actual - linear) < 3e-6
        checks += 1
print('PASS:', checks, 'Fourier-Jacobian spectra, zero moments, and finite differences.')
