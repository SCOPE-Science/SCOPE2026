"""Finite-dimensional checks of Dicke dark-spectrum and passive rearrangement.
Run: python3 artifacts/verify.py ; dependency: NumPy >=1.24.
The universal asymptotic theorem is analytic, not certified by finite tests.
"""
from math import comb, isclose, sqrt, log
import numpy as np


def spin_data(n):
    M = n // 2
    multiplicity = [comb(n, k) - (comb(n, k-1) if k else 0) for k in range(M+1)]
    eigenvalue = [(n-2*k+1) / (2**n) for k in range(M+1)]
    assert sum(multiplicity[k] * eigenvalue[k] for k in range(M+1)) == 1
    return multiplicity, eigenvalue


def ergotropy_exact(n):
    mult, vals = spin_data(n)
    eraw = sum(k * mult[k] * vals[k] for k in range(len(mult)))
    passive = 0.0
    level, available = 0, comb(n, 0)
    for g, weight in zip(mult, vals):
        while g:
            if not available:
                level += 1
                available = comb(n, level)
            used = min(g, available)
            passive += used * weight * level
            g -= used
            available -= used
    return eraw - passive, eraw, passive


def dark_sector_matrices(n):
    dim = 2**n
    lower = np.zeros((dim, dim), dtype=float)
    exc = np.zeros(dim, dtype=float)
    for state in range(dim):
        exc[state] = state.bit_count()
        for bit in range(n):
            if (state >> bit) & 1:
                lower[state ^ (1 << bit), state] += 1.0
    jz = np.diag(exc - n/2)
    J2 = lower.T @ lower + jz @ (jz - np.eye(dim))
    _, s, vh = np.linalg.svd(lower)
    vectors = vh.T[:, s < 1e-8]
    assert np.linalg.norm(lower @ vectors) < 1e-7
    J2dark = vectors.T @ J2 @ vectors
    spinsq, frame = np.linalg.eigh(J2dark)
    coords = vectors @ frame
    j = (np.sqrt(1.0 + 4.0 * spinsq) - 1.0) / 2.0
    weights = (2*j + 1)/(2**n)
    rho = (coords * weights) @ coords.T
    assert abs(np.trace(rho)-1) < 1e-9
    assert np.linalg.norm(lower @ rho) < 1e-8
    h = np.diag(exc)
    assert np.linalg.norm(h @ rho - rho @ h) < 1e-8
    actual = np.trace(rho @ h)
    return j, actual


def verify():
    for n in range(1, 8):
        g, w = spin_data(n)
        j, energy = dark_sector_matrices(n)
        predicted = sorted([n/2-k for k in range(len(g)) for _ in range(g[k])])
        assert np.allclose(sorted(j), predicted, atol=1e-7), (n, j, predicted)
        _, expected_energy, _ = ergotropy_exact(n)
        assert isclose(energy, expected_energy, abs_tol=5e-9)
    for n in range(1, 40):
        work, initial, passive = ergotropy_exact(n)
        assert work >= -1e-9
        if n <= 3:
            assert abs(work) < 1e-10
        if n >= 4:
            assert work > 1e-12
    assert abs(ergotropy_exact(4)[0] - 1/16) < 1e-12
    print('VERIFY_OK: dark spaces n<=7, passive rearrangement n<=39, W_4=1/16')
    for n in (50, 100, 300, 600):
        work, _, _ = ergotropy_exact(n)
        print(f'n={n} W={work:.9g}, normalized={work/sqrt(n*log(n)):.9g}')

if __name__ == '__main__':
    verify()
