"""Reproduce numerical stress checks for a sharp commuting-modulus Schatten inequality.

Requires: Python 3 and NumPy. Exact analytic proof is in RESULT.md.
"""
import numpy as np

rng = np.random.default_rng(13071)
for m in (2, 3, 4, 6):
    for n in (2, 4, 7):
        for trial in range(120):
            weights = rng.lognormal(0, 2, size=(m, n))
            unitary = []
            for k in range(m):
                raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
                q, _ = np.linalg.qr(raw)
                unitary.append(q)
            total = sum(unitary[k] @ np.diag(weights[k]) for k in range(m))
            sv = np.linalg.svd(total, compute_uv=False)
            s = weights.sum(axis=0)
            for p in (1, 1.05, 1.5, 1.99, 2, 2.5, 4, 10):
                ratio = (sum(sv**p) / sum(s**p)) ** (1 / p)
                target = 1 if p <= 2 else m ** (0.5 - 1 / p)
                assert ratio <= target + 1e-9, (m, n, trial, p, ratio, target)
    print('RANDOM_COMMUTING_MODULI_OK', m)
for m in (2, 3, 4, 7):
    witness = np.zeros((m, m))
    witness[0, :] = 1
    sv = np.linalg.svd(witness, compute_uv=False)
    assert np.isclose(sv[0], np.sqrt(m))
    assert np.all(np.abs(sv[1:]) < 1e-12)
    for p in (2, 2.5, 3, 10):
        ratio = (sum(sv**p) / m) ** (1 / p)
        assert abs(ratio - m ** (0.5 - 1 / p)) < 1e-12
    print('SHARP_ORTHOGONAL_RIGHT_SUPPORTS_OK', m)
