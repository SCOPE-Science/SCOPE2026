"""Independent finite checks of the exact cycle--clique mixing theorem.

Run: python3 verify.py  (requires NumPy).  Analytic proofs for all orders are
in RESULT.md; the finite calculations here are corroboration only.
"""
from fractions import Fraction
import math
import numpy as np


def spectral_modes(n, q):
    """Exact rational predicted Fourier eigenvalues as Python Fractions."""
    assert n >= 3 and q >= 3
    vals = {}
    for h in range(n):
        if h == 0:
            B = n
        elif n % 2:
            B = 1
        elif h % 2 == 0:
            B = 2
        else:
            B = 0
        C = 0
        if q == 3 and n % 3 == 0 and h in (n // 3, 2 * n // 3):
            C = 1 if n % 2 else 2
        if q == 4 and n % 2 == 0 and h == n // 2:
            C = 1
        for j in range(q):
            vals[h, j] = Fraction(B, n) if j == 0 else Fraction((q-2)*B+2*C, n*q)
    return vals


def predicted_rank(n, q):
    return n*q if n % 2 else n*q//2 + (3 if q == 4 and n % 4 == 2 else 0)


def explicit_matrices(n, q):
    """Build full adjacency independently, diagonalize it, and average projectors."""
    A_cycle = np.zeros((n, n))
    for a in range(n):
        A_cycle[a, (a+1) % n] = 1
        A_cycle[(a+1) % n, a] = 1
    A_clique = np.ones((q, q)) - np.eye(q)
    A = np.kron(A_cycle, np.eye(q)) + np.kron(np.eye(n), A_clique)
    spectrum, vectors = np.linalg.eigh(A)
    groups = []
    for k, energy in enumerate(spectrum):
        if not groups or abs(energy - spectrum[k-1]) > 1.0e-7:
            groups.append([])
        groups[-1].append(k)
    mixing = np.zeros((n*q, n*q))
    for group in groups:
        projection = vectors[:, group] @ vectors[:, group].T
        mixing += projection * projection
    return mixing


def factor_matrices(n, q):
    """Known factor averages and exact spectral correction in the group basis."""
    modes = spectral_modes(n, q)
    base = {}
    for h in range(n):
        B = n if h == 0 else (1 if n % 2 else 2 if h % 2 == 0 else 0)
        for j in range(q):
            base[h, j] = Fraction(B, n) if j == 0 else Fraction((q-2)*B, n*q)
    correction = np.zeros((n, q))
    full = np.zeros((n, q))
    for (h, j), value in modes.items():
        full[h, j] = float(value)
        correction[h, j] = float(value - base[h, j])
    return np.fft.ifftn(full).real, np.fft.ifftn(correction).real


def explicit_factor_correction(n, q):
    """Evaluate the claimed factor projector identity separately from modes."""
    if n % 2:
        cycle = (n-1)/n**2*np.ones((n, n)) + np.eye(n)/n
    else:
        reverse = np.zeros((n, n))
        for a in range(n):
            reverse[a, (a + n//2) % n] = 1
        cycle = (n-2)/n**2*np.ones((n, n)) + (np.eye(n)+reverse)/n
    clique = (1-2/q)*np.eye(q) + 2/q**2*np.ones((q, q))
    correction = np.zeros((n*q, n*q), dtype=complex)
    transverse = np.eye(q) - np.ones((q, q))/q
    frequencies = []
    coefficient = 0
    if q == 3 and n % 3 == 0:
        frequencies = [n//3, 2*n//3]
        coefficient = 2*(1 if n % 2 else 2)/(3*n)
    elif q == 4 and n % 2 == 0:
        frequencies = [n//2]
        coefficient = 1/(2*n)
    for h in frequencies:
        z = np.exp(2j*np.pi*h*np.arange(n)/n)
        projection = np.outer(z, np.conj(z))/n
        correction += coefficient*np.kron(projection, transverse)
    return np.kron(cycle, clique)+correction, correction


def verify():
    graphs = modes = matrix_entries = 0
    corrections = 0
    worst = 0.
    for n in range(3, 17):
        for q in range(3, 9):
            predicted = spectral_modes(n, q)
            expected_rank = predicted_rank(n, q)
            assert sum(value > 0 for value in predicted.values()) == expected_rank
            average = explicit_matrices(n, q)
            # Translation invariance tested directly, not assumed from the formula.
            expected_first_row, extra = factor_matrices(n, q)
            translated = np.array([
                [expected_first_row[(y//q - x//q) % n, (y%q - x%q) % q]
                 for y in range(n*q)]
                for x in range(n*q)
            ])
            error = float(np.max(np.abs(average - translated)))
            separate, correction = explicit_factor_correction(n, q)
            error2 = float(np.max(np.abs(average - separate)))
            assert error2 < 1e-9, (n, q, error2)
            assert float(np.max(np.abs(correction.imag))) < 1e-9
            worst = max(worst, error, error2)
            assert error < 1e-9, (n, q, error)
            modes_actual = np.fft.fftn(average[0].reshape(n, q))
            assert float(np.max(np.abs(modes_actual.imag))) < 1e-9
            for (h, j), value in predicted.items():
                assert abs(modes_actual[h, j].real - float(value)) < 1e-9
            # Exact exception criteria, tested independently of rank.
            has_extra = float(np.max(np.abs(extra))) > 1e-12
            expected_extra = ((q == 3 and n % 3 == 0) or (q == 4 and n % 2 == 0))
            assert has_extra == expected_extra, (n, q)
            assert (float(np.max(np.abs(correction))) > 1e-12) == expected_extra
            if expected_extra:
                corrections += 1
            assert abs(average.sum(axis=1)-1).max() < 1e-9
            graphs += 1
            modes += n*q
            matrix_entries += (n*q)**2
    assert predicted_rank(6, 4) == 15
    assert predicted_rank(10, 4) == 23
    assert predicted_rank(12, 4) == 24
    assert predicted_rank(6, 3) == 9
    assert spectral_modes(6, 4)[3, 1] == Fraction(1, 12)
    assert spectral_modes(10, 4)[5, 1] == Fraction(1, 20)
    assert spectral_modes(6, 3)[2, 1] == Fraction(1, 3)
    print('VERIFY_OK graphs=%d Fourier_modes=%d matrix_entries=%d correction_cases=%d worst_abs=%.3e C6_K4_rank=15/24 C10_K4_rank=23/40' %
          (graphs, modes, matrix_entries, corrections, worst))


if __name__ == '__main__':
    verify()
