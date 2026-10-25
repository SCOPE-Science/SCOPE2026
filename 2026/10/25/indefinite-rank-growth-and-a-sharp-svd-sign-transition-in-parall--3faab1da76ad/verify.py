"""Reproduce the spectral assertions for a parallel rank-adaptive low-rank step.

Run with: python verify.py
Requires NumPy (see requirements.txt). This checks finite-dimensional
identities and sample parameter values; the proofs of the universal
statements and sharp thresholds are in RESULT.md.
"""
import math
import numpy as np


def evaluated_step(gamma, h):
    """Exactly integrated K/L/S substeps in orthonormal augmented coordinates."""
    q = -math.expm1(-h)
    p = q * gamma
    augmented = np.array([[1.0, 0.0, p],
                          [0.0, 1.0, 0.0],
                          [p,   0.0, 0.0]])
    forcing = np.array([[1.0, 0.0, gamma],
                        [0.0, 1.0, 0.0],
                        [gamma, 0.0, gamma * gamma + 1.0]])
    initial = np.diag([1.0, 1.0, 0.0])
    exact = math.exp(-h) * initial + q * forcing
    d = (math.sqrt(1.0 + 4.0 * p * p) - 1.0) / 2.0
    return augmented, exact, d, forcing


def rank_truncate_symmetric(matrix, rank):
    vals, vectors = np.linalg.eigh(matrix)
    selected = sorted(range(len(vals)), key=lambda i: abs(vals[i]), reverse=True)[:rank]
    return (vectors[:, selected] * vals[selected]) @ vectors[:, selected].T


def check():
    checks = 0
    for gamma in (0.5, 1.0, 2.0, 3.0, 5.0):
        for h in (0.1, 0.75, 1.5, 2.0, 3.0):
            matrix, exact, d, forcing = evaluated_step(gamma, h)
            assert np.linalg.eigvalsh(forcing)[0] > 0
            assert np.linalg.eigvalsh(exact)[0] > 0
            actual = np.linalg.eigvalsh(matrix)
            expected = np.array([-d, 1.0, 1.0 + d])
            assert np.allclose(actual, expected, rtol=1e-12, atol=1e-12)
            checks += 3
            if abs(d-1.0) > 1e-5:
                t2 = rank_truncate_symmetric(matrix, 2)
                eigs2 = np.linalg.eigvalsh(t2)
                assert (eigs2[0] < -1e-8) == (d > 1.0)
                assert math.isclose(np.linalg.norm(matrix-t2, 'fro'),
                                    min(1.0, d), rel_tol=1e-11, abs_tol=1e-11)
                checks += 2
    gamma, h, theta, reject_factor = 2.0, 1.5, 1.2, 10.0
    matrix, exact, d, forcing = evaluated_step(gamma, h)
    sigmas = sorted(np.linalg.svd(matrix, compute_uv=False), reverse=True)
    assert d > 1.0 and sigmas[0] > sigmas[1] > sigmas[2]
    assert sigmas[2] < theta < math.sqrt(sigmas[1]**2 + sigmas[2]**2)
    assert math.sqrt(sigmas[1]**2 + sigmas[2]**2) > theta
    assert h * (gamma**2 + 1.0) < reject_factor * theta
    rank2 = rank_truncate_symmetric(matrix, 2)
    assert np.linalg.eigvalsh(rank2)[0] < -1.0
    assert np.linalg.eigvalsh(exact)[0] > 0.0
    checks += 7
    print(f'VERIFY_OK {checks}')
    print(f'd={d:.12f}, h_eta={h*(gamma**2+1):.12f}, '
          f'exact_lambda_min={np.linalg.eigvalsh(exact)[0]:.12f}, '
          f'truncated_lambda_min={np.linalg.eigvalsh(rank2)[0]:.12f}')

if __name__ == '__main__':
    check()
