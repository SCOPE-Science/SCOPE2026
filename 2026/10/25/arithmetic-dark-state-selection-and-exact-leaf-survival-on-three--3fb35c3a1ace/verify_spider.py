"""Reproducible finite checks of the three-arm spider absorption theorem.

Run: python verify_spider.py
Requires: numpy, sympy.  The proof for all positive arm lengths is mathematical;
these finite calculations are diagnostic, not a replacement for that proof.
"""
from itertools import product
from math import gcd
import numpy as np
import sympy as sp


def analytic(lengths):
    """Exact rational survival and dark dimension for a leaf on arm 1."""
    p, q, r = [int(L) + 1 for L in lengths]
    assert min(p, q, r) >= 2
    g12, g13, g23 = gcd(p, q), gcd(p, r), gcd(q, r)
    g123 = gcd(g12, r)
    h = lambda g: g if g >= 2 else 0
    S = (sp.Rational(h(g12), p + q)
         + sp.Rational(h(g13), p + r)
         + h(g123) * (
             sp.Rational(q + r, p*q + p*r + q*r)
             - sp.Rational(1, p + q) - sp.Rational(1, p + r)))
    d = g12 + g13 + g23 - g123 - 2
    return S, d


def adjacency(lengths, dtype=float):
    """Hub index zero; arm 1 then arm 2 then arm 3 outward."""
    size = 1 + sum(lengths)
    A = np.zeros((size, size), dtype=dtype)
    starts = []
    next_vertex = 1
    for L in lengths:
        starts.append(next_vertex)
        A[0, next_vertex] = A[next_vertex, 0] = 1
        for x in range(L - 1):
            A[next_vertex + x, next_vertex + x + 1] = 1
            A[next_vertex + x + 1, next_vertex + x] = 1
        next_vertex += L
    return A, starts


def spectral_survival(lengths):
    """Directly diagonalize the full Hermitian adjacency, without using gcds."""
    H, starts = adjacency(lengths)
    energy, basis = np.linalg.eigh(H)
    leaf = starts[0] + lengths[0] - 1
    survived, dark_dim = 0.0, 0
    left = 0
    while left < len(energy):
        right = left + 1
        while right < len(energy) and abs(energy[right] - energy[left]) < 1e-8:
            right += 1
        E = basis[:, left:right]
        hub_weights = E[0, :]
        leaf_weights = E[leaf, :]
        k = right - left
        sq_h = float(np.vdot(hub_weights, hub_weights).real)
        if sq_h < 1e-18:
            dark_dim += k
            survived += float(np.vdot(leaf_weights, leaf_weights).real)
        else:
            dark_dim += k - 1
            p = (np.vdot(leaf_weights, leaf_weights).real
                 - abs(np.vdot(hub_weights, leaf_weights))**2 / sq_h)
            survived += float(p)
        left = right
    return survived, dark_dim


def rational_dark_dimension(lengths):
    """Exact integer-arithmetic hub Krylov rank (alternative check)."""
    H_float, _ = adjacency(lengths)
    H = sp.Matrix([[int(v) for v in row] for row in H_float])
    size = H.rows
    v = sp.zeros(size, 1)
    v[0] = 1
    columns = []
    for j in range(size):
        columns.append(v)
        v = H * v
    return size - sp.Matrix.hstack(*columns).rank()


def check():
    count, max_diff = 0, 0.0
    for lengths in product(range(1, 9), repeat=3):
        if sum(lengths) > 20:
            continue
        expected, expected_dim = analytic(lengths)
        got, got_dim = spectral_survival(lengths)
        err = abs(float(expected) - got)
        if err > 2e-9 or expected_dim != got_dim:
            raise AssertionError((lengths, expected, expected_dim, got, got_dim, err))
        max_diff = max(max_diff, err)
        count += 1
    assert count == 492

    # Exact linear-algebra verification for characteristic mixed-length cases.
    exact_cases = [
        (1,1,1), (1,1,2), (1,2,2), (1,2,3), (1,2,4),
        (1,3,3), (1,3,4), (2,2,2), (2,2,3), (2,2,4),
        (2,3,3), (2,3,4), (2,4,4), (3,3,3), (3,3,4),
        (3,4,4), (3,4,5), (4,4,4), (4,4,5), (4,5,5),
        (4,5,6), (5,5,5), (5,5,6), (5,6,6)
    ]
    for lengths in exact_cases:
        _, dim = analytic(lengths)
        found = rational_dark_dimension(lengths)
        assert dim == found, (lengths, dim, found)

    # Alternative non-Hermitian eigenvalue test for positive loss strengths.
    loss_cases = [(1,2,3), (1,1,1), (1,3,4), (2,3,5), (3,5,7),
                  (4,5,11), (5,9,14)]
    loss_checks = 0
    for lengths in loss_cases:
        H, _ = adjacency(lengths)
        for gamma in (0.25, 1.0, 3.0):
            K = np.array(H, dtype=complex)
            K[0,0] -= 1j * gamma
            eigenvalues = np.linalg.eigvals(K)
            count_real = int(sum(abs(z.imag) < 1e-8 for z in eigenvalues))
            assert count_real == analytic(lengths)[1], (lengths, gamma, count_real)
            assert all(z.imag < 1e-7 for z in eigenvalues)
            loss_checks += 1
    print(f"PASS: {count} full-adjacency spectral comparisons")
    print(f"PASS: {len(exact_cases)} exact integer Krylov-rank comparisons")
    print(f"PASS: {loss_checks} dissipative eigenvalue checks")
    print(f"largest survival discrepancy: {max_diff:.3e}")
    print("examples: (1,2,3) ->", analytic((1,2,3)),
          "; (4,5,11) ->", analytic((4,5,11)),
          "; (3,5,7) ->", analytic((3,5,7)))


if __name__ == '__main__':
    check()
