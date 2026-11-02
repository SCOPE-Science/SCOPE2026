"""Finite checks of the Hilbert-corner comparison for critical periodic Fourier systems.

Run: python checker.py
Requires numpy. All checks are finite, not a proof of asymptotics.
"""
import math
import numpy as np


def finite_test(period: int) -> int:
    p = period
    m = (p + 1) // 2
    L = p // 2
    signs = np.array([1] * m + [-1] * (p - m))
    rows = np.arange(p)[:, None]
    cols = np.arange(p)[None, :]
    mat = np.exp(-2j * np.pi * rows * (cols + signs / 4.0) / p) / math.sqrt(p)
    gram = mat.conj().T @ mat
    cross = gram[m:p, 0:m]
    full_norm = np.linalg.svd(cross, compute_uv=False)[0]
    corner = cross[np.ix_(np.arange(L), m - 1 - np.arange(L))]
    a = np.add.outer(np.arange(L), np.arange(L)) + 0.5
    positive_corner = 1.0 / (p * np.sin(np.pi * a / p))
    phase = np.exp(1j * np.pi * (p - 1) * a / p) * (-1) ** (a - 0.5)
    # Cross entries are conjugates of the geometric series according to row order.
    err = min(np.max(np.abs(corner - phase * positive_corner)),
              np.max(np.abs(corner - np.conj(phase) * positive_corner)))
    assert err < 4e-12, (p, err)
    Hil = 1.0 / (np.add.outer(np.arange(L), np.arange(L)) + 1.0)
    hil_lambda = np.linalg.eigvalsh(Hil)[-1]
    corner_norm = np.linalg.svd(positive_corner, compute_uv=False)[0]
    assert np.all(positive_corner >= Hil / math.pi - 2e-14)
    assert corner_norm + 1e-12 >= hil_lambda / math.pi
    assert full_norm + 1e-12 >= corner_norm
    gram_min = np.linalg.eigvalsh(gram)[0]
    assert abs(gram_min - (1.0 - full_norm)) < 5e-12
    assert gram_min <= 1.0 - hil_lambda / math.pi + 2e-12
    assert gram_min >= -5e-12
    return 7


def main() -> None:
    cases = list(range(4, 49)) + [64, 72, 96, 128]
    count = sum(finite_test(p) for p in cases)
    print(f"PASS: {len(cases)} periods, {count} finite checks; no asymptotic proof claimed.")


if __name__ == '__main__':
    main()
