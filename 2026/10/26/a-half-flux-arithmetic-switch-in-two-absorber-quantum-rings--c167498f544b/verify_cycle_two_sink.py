"""Standalone numerical checks for flux-threaded cycle with two absorbers.
Requires numpy; scipy is not needed.
"""
import math
import numpy as np


def predicted(n, separation, phase_class):
    g = math.gcd(n, separation)
    L = n // g
    values = []
    for x in range(n):
        if phase_class == 'generic':
            v = 0.0
        elif phase_class == 'zero':
            if L % 2 == 0:
                v = g / n if x % g else 0.0
            else:
                h = g // math.gcd(g, 2)
                v = g / (2 * n) if x % h else 0.0
        else:
            if L % 2 == 0:
                v = 0.0
            elif g % 2:
                v = g / (2 * n) if x % g else 0.0
            else:
                v = (0.0 if x % g == 0 else
                     (g / n if x % g == g // 2 else g / (2 * n)))
        values.append(v)
    return np.asarray(values)


def hamiltonian(n, flux):
    H = np.zeros((n, n), dtype=complex)
    z = np.exp(-1j * flux / n)
    for j in range(n):
        k = (j + 1) % n
        H[k, j] += z
        H[j, k] += z.conjugate()
    return H


def dark_projection(H, sites=(0, 1), tol=1e-8):
    vals, U = np.linalg.eigh(H)
    n = len(vals)
    P = np.zeros((n, n), dtype=complex)
    rank = 0
    begin = 0
    while begin < n:
        end = begin + 1
        while end < n and abs(vals[end] - vals[begin]) < tol:
            end += 1
        basis = U[:, begin:end]
        A = basis[list(sites), :]
        _, sing, Vh = np.linalg.svd(A, full_matrices=True)
        r = int(np.sum(sing > tol))
        Z = basis @ Vh[r:, :].conj().T
        P += Z @ Z.conj().T
        rank += Z.shape[1]
        begin = end
    return rank, P


def verify():
    checked = 0
    for n in range(3, 13):
        for s in range(1, n):
            for flux, flag in [(0.0, 'zero'), (math.pi, 'half'), (0.461, 'generic')]:
                H = hamiltonian(n, flux)
                assert np.allclose(H, H.conj().T)
                d, P = dark_projection(H, (0, s))
                expected = predicted(n, s, flag)
                assert np.max(np.abs(P.diagonal().real - expected)) < 4e-9, (n, s, flag, P.diagonal(), expected)
                assert abs(P.trace().real - d) < 4e-9
                assert abs(expected.sum() - d) < 4e-9
                assert np.linalg.norm(P @ P - P) < 4e-9
                for ga, gb in [(1.1, 2.9), (0.43, 3.7)]:
                    L = H - 0.5j * np.diag([ga if j == 0 else gb if j == s else 0 for j in range(n)])
                    ev = np.linalg.eigvals(L)
                    assert np.max(ev.imag) < 1e-8
                    d_eval = sum(abs(z.imag) < 1e-8 for z in ev)
                    assert d_eval == d, (n, s, flag, d_eval, d, ev)
                checked += 1
    print(f'PASS: {checked} spectral and projector checks, each with two distinct positive loss-rate pairs')

if __name__ == '__main__':
    verify()
