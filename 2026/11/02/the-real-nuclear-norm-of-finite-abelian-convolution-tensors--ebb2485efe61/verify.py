"""Numerical checks for the real Fourier block decomposition of finite-group convolution tensors.

Requires Python 3 and NumPy. All universal norm equalities have separate analytical proofs.
"""
import itertools
import math
import numpy as np


def group_data(factors):
    els = list(itertools.product(*(range(d) for d in factors)))
    ix = {v: i for i, v in enumerate(els)}
    n = len(els)
    C = np.zeros((n, n, n), dtype=float)
    for i, a in enumerate(els):
        for j, b in enumerate(els):
            C[i, j, ix[tuple((x + y) % d for x, y, d in zip(a, b, factors))]] = 1.0
    rows = []
    blocks = []
    seen = set()
    for character in els:
        if character in seen:
            continue
        negative = tuple((-v) % d for v, d in zip(character, factors))
        angles = np.array([2 * math.pi * sum(k * g / d for k, g, d in zip(character, x, factors)) for x in els])
        charvals = np.exp(1j * angles)
        first = len(rows)
        if negative == character:
            rows.append(np.real(charvals) / math.sqrt(n))
            blocks.append((first,))
        else:
            seen.add(negative)
            rows.append(math.sqrt(2 / n) * np.real(charvals))
            rows.append(math.sqrt(2 / n) * np.imag(charvals))
            blocks.append((first, first + 1))
        seen.add(character)
    U = np.array(rows)
    B = np.einsum('ai,bj,ck,ijk->abc', U, U, U, C, optimize=True)
    return C, U, B, blocks


def check(factors):
    A, U, B, blocks = group_data(factors)
    n = A.shape[0]
    r = sum(len(b) == 1 for b in blocks)
    assert r == math.prod(math.gcd(d, 2) for d in factors)
    assert sum(map(len, blocks)) == n
    assert np.allclose(U @ U.T, np.eye(n), atol=1e-12)
    assert np.allclose(np.linalg.norm(A), n, atol=1e-10)
    assert np.allclose(np.linalg.norm(B), n, atol=1e-10)
    # The complex character basis diagonalizes the same structure tensor into n
    # disjoint pure Fourier terms, each of absolute coefficient sqrt(n).
    group_elements = list(itertools.product(*(range(d) for d in factors)))
    Fourier = np.array([
        [np.exp(-2j * math.pi * sum(k * g / d for k, g, d in zip(character, x, factors))) / math.sqrt(n)
         for x in group_elements]
        for character in group_elements
    ])
    assert np.allclose(Fourier @ Fourier.conj().T, np.eye(n), atol=1e-12)
    complex_form = np.einsum('ai,bj,ck,ijk->abc', Fourier, Fourier, Fourier, A, optimize=True)
    support = np.abs(complex_form) > 1e-9
    assert support.sum() == n
    assert np.allclose(np.abs(complex_form[support]), math.sqrt(n), atol=1e-10)
    assert np.allclose(complex_form[~support], 0, atol=1e-10)
    within = np.zeros_like(B)
    witness = np.zeros_like(B)
    upper_bound = 0.0
    for block in blocks:
        s = np.ix_(block, block, block)
        within[s] = B[s]
        amplitude = math.sqrt(n / len(block))
        expected_magnitude = amplitude
        nonzero = np.abs(B[s]) > 1e-9
        assert nonzero.sum() == (1 if len(block) == 1 else 4)
        assert np.allclose(np.abs(B[s][nonzero]), expected_magnitude, atol=1e-10)
        assert np.allclose(B[s][~nonzero], 0, atol=1e-10)
        witness[s] = B[s] / amplitude
        upper_bound += float(np.abs(B[s]).sum())
    assert np.allclose(B, within, atol=1e-10)
    pairing = float(np.sum(B * witness))
    witness_original = np.einsum('ai,bj,ck,abc->ijk', U, U, U, witness, optimize=True)
    assert np.allclose(float(np.sum(A * witness_original)), pairing, atol=1e-9)
    predicted = math.sqrt(n) * (r + math.sqrt(2) * (n - r))
    assert math.isclose(pairing, upper_bound, rel_tol=2e-11, abs_tol=1e-10)
    assert math.isclose(pairing, predicted, rel_tol=2e-11, abs_tol=1e-10)
    # Each witness block acts as scalar multiplication or real complex multiplication
    # (up to sign reversal), hence has trilinear spectral norm 1. We check sampled
    # unit inputs; the proof supplies the universal upper bound.
    rng = np.random.default_rng(n * 101 + r)
    for _ in range(500):
        X = rng.normal(size=(3, n))
        X /= np.linalg.norm(X, axis=1)[:, None]
        val = float(np.einsum('abc,a,b,c', witness, *X, optimize=True))
        assert abs(val) <= 1 + 1e-11
    complex_predicted = n * math.sqrt(n)
    assert math.isclose(float(np.sum(np.abs(complex_form))), complex_predicted, rel_tol=1e-11)
    print(f'{factors}: order={n}, two_torsion={r}, pi_R={predicted:.12f}, pi_C={complex_predicted:.12f}, ratio={predicted/complex_predicted:.12f}, witness={pairing:.12f}')


if __name__ == '__main__':
    for fs in [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (2, 2), (2, 3), (2, 4), (3, 3), (2, 2, 2)]:
        check(fs)
    print('All finite Fourier decomposition and witness checks passed.')
