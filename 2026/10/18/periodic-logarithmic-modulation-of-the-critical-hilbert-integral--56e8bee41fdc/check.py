"""Finite Fourier-section diagnostics for a periodic positive Green kernel.

A numerical diagnostic, not a substitute for the operator-theoretic proof.
Run: python check.py (requires numpy).
"""
import numpy as np


def top_norm(frequency, amplitude, n_modes=30, n_grid=8192):
    grid = np.arange(n_grid) * (2 * np.pi / n_grid)
    a = 1.0 / (1.0 + amplitude * np.cos(grid))
    fourier = np.fft.fft(a) / n_grid
    modes = np.arange(-n_modes, n_modes + 1)
    a_matrix = fourier[(modes[:, None] - modes[None, :]) % n_grid]
    multiplier = 1.0 / (0.25 + (modes * frequency)**2)
    gram = (a_matrix * multiplier[None, :]) @ a_matrix
    gram = (gram + gram.conj().T) / 2.0
    return float(np.sqrt(np.linalg.eigvalsh(gram)[-1]))


def run():
    for w in (0.8, 1.0, 2.0):
        assert abs(top_norm(w, 0.0) - 2.0) < 1e-12
        coefficient = 1.5 + 0.5 / w**2
        errors = []
        for amplitude in (0.02, 0.04, 0.08):
            found = top_norm(w, amplitude)
            opposite = top_norm(w, -amplitude)
            lower = 2.0 / np.sqrt(1.0 - amplitude**2)
            predicted = 2.0 + coefficient * amplitude**2
            assert abs(found - opposite) < 1e-10
            assert found + 1e-9 >= lower
            assert abs(found - predicted) < 0.001
            errors.append(abs(found - predicted))
            print('omega', w, 'epsilon', amplitude,
                  'norm', round(found, 10), 'quadratic', round(predicted, 10))
        assert errors[0] < errors[-1]
    print('FINITE_DIAGNOSTICS_OK')


if __name__ == '__main__':
    run()
