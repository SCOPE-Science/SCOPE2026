"""Finite direct checks for a dephased Johnson-graph quantum walk.

These computations test small instances only; the proof covers arbitrary n,k.
Run: python verify_johnson.py
"""
from itertools import combinations
from math import comb

import numpy as np
from scipy.linalg import expm


def test_case(n, k):
    verts = [frozenset(s) for s in combinations(range(n), k)]
    N = len(verts)
    H = np.zeros((N, N), dtype=float)
    for i, s in enumerate(verts):
        for j, t in enumerate(verts):
            H[i, j] = float(i != j and len(s & t) == k - 1)
    monitored = [i for i, s in enumerate(verts) if n - 1 in s]
    free = [i for i, s in enumerate(verts) if n - 1 not in s]
    B = H[np.ix_(monitored, free)]
    A = H[np.ix_(free, free)]
    d = max(0, comb(n - 1, k) - comb(n - 1, k - 1))
    assert np.linalg.matrix_rank(B) == min(*B.shape), (n, k, "rank")
    assert np.allclose(B.T @ B, k * np.eye(len(free)) + A)
    D = np.zeros((N, N), dtype=float)
    if d:
        _, _, vh = np.linalg.svd(B, full_matrices=True)
        basis = vh[-d:].T
        D[np.ix_(free, free)] = basis @ basis.T
        assert np.allclose(B @ basis, 0, atol=1e-9)
        assert np.allclose(A @ basis, -k * basis, atol=1e-9)
    assert np.allclose(D @ D, D, atol=1e-9)
    assert abs(np.trace(D) - d) < 1e-8
    assert np.allclose(H @ D, -k * D, atol=1e-9)
    assert np.allclose(D @ H, -k * D, atol=1e-9)
    U = len(free)
    w = d / U
    bright = N - d
    for j in free:
        assert abs(D[j, j] - w) < 1e-9
        initial = np.zeros((N, N)); initial[j, j] = 1
        limiting = D @ initial @ D + (1 - w) * (np.eye(N) - D) / bright
        assert abs(limiting[j, j] - w**2 - (1 - w)**2 / bright) < 1e-9
    for j in monitored:
        assert abs(D[j, j]) < 1e-9

    if N <= 15:
        identity = np.eye(N)
        # Column-major vec convention: vec(HX)=(I kron H)vec(X).
        L = -1j * (np.kron(identity, H) - np.kron(H.T, identity))
        for gamma, i in zip(np.linspace(.8, 1.3, len(monitored)), monitored):
            P = np.zeros((N, N)); P[i, i] = 1
            L += gamma * (np.kron(P, P) - .5 * np.kron(identity, P) - .5 * np.kron(P.T, identity))
        ev = np.linalg.eigvals(L)
        assert np.count_nonzero(abs(ev) < 1e-7) == d*d + 1, (n, k, "fixed algebra")
        assert np.max(ev.real) < 1e-7
        assert np.all(abs(ev.imag[ev.real > -1e-8]) < 1e-7)
        if N <= 10:
            evolution = expm(2500 * L)
            for j in (free[0], monitored[0]):
                initial = np.zeros((N, N)); initial[j, j] = 1
                predicted = D @ initial @ D + (1 - np.trace(D @ initial)) * (identity - D) / bright
                observed = (evolution @ initial.flatten(order="F")).reshape((N, N), order="F")
                assert np.linalg.norm(observed - predicted) < 2e-6, (n, k, "finite-time convergence")
    print("PASS", "n", n, "k", k, "vertices", N, "protected", d, "stationary_dimension", 1+d*d)


def main():
    count = 0
    for n in range(3, 8):
        for k in range(1, n):
            if comb(n, k) <= 16:
                test_case(n, k)
                count += 1
    for k in range(2, 16):
        n = 2*k+1
        catalan = comb(2*k, k) // (k+1)
        assert (comb(n-1, k) - comb(n-1, k-1)) == catalan
        assert comb(n, k) - catalan == 2*k*catalan
    print("ALL CHECKS PASSED:", count, "matrix/superoperator instances and 14 central-rank Catalan identities")


if __name__ == "__main__":
    main()
