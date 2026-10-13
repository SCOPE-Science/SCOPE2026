"""Standalone numerical cross-checks for the finite-dimensional coherence bound.

Run: python verify.py (requires NumPy). The universal theorem uses an analytic
spectral argument; finite checks here are corroborative, not a proof.
"""
from itertools import product
import math
import numpy as np


def coherence(x):
    off = x - np.diag(np.diag(x))
    return float(np.linalg.norm(off, 'fro'))


def channel_data(d):
    m = d // 2
    ks = []
    for j in range(m):
        k = np.zeros((2, d), dtype=complex)
        k[0, 2*j] = 1
        k[1, 2*j + 1] = 1
        ks.append(k)
    if d % 2:
        k = np.zeros((2, d), dtype=complex)
        k[0, d - 1] = 1
        ks.append(k)
    return ks


def apply_channel(ks, rho):
    return sum((k @ rho @ k.conj().T for k in ks),
               np.zeros((2, 2), dtype=complex))


def exact_vertex_bound(d):
    # Vertices of the traceless Hermitian-contraction eigenvalue polytope:
    # at least d-1 eigenvalues are ±1, the last is their negative sum.
    vals = []
    for signs in product((-1, 1), repeat=d - 1):
        last = -sum(signs)
        if abs(last) <= 1:
            vals.append(sum(s*s for s in signs) + last*last)
    assert vals
    return max(vals)


def main():
    ncases = 0
    for d in range(2, 13):
        m = d // 2
        assert exact_vertex_bound(d) == 2*m
        ks = channel_data(d)
        ident = sum((k.conj().T @ k for k in ks),
                    np.zeros((d, d), dtype=complex))
        assert np.array_equal(ident, np.eye(d))
        h = np.zeros((d, d), dtype=complex)
        for j in range(m):
            h[2*j, 2*j+1] = h[2*j+1, 2*j] = 1
        epsilon = 1.0 / (2*d)
        rho = np.eye(d)/d + epsilon*h
        assert np.linalg.eigvalsh(rho).min() > 0
        out = apply_channel(ks, rho)
        assert np.allclose(np.trace(out), 1)
        left = coherence(out)
        right = math.sqrt(m) * coherence(rho)
        assert math.isclose(left, right, rel_tol=1e-12, abs_tol=1e-13)
        # Verify diagonal states always have diagonal outputs, and Kraus
        # actions have at most one nonzero per row and per column.
        for k in ks:
            assert (np.abs(k)>0).sum(axis=0).max() <= 1
            assert (np.abs(k)>0).sum(axis=1).max() <= 1
        for i in range(d):
            e = np.zeros((d,d), dtype=complex)
            e[i,i] = 1
            assert coherence(apply_channel(ks,e)) == 0
        ncases += 1
    print(f'VERIFY_OK dimensions={ncases} exact_spectral_vertices=passed '
          'Kraus_completeness=passed full_rank_saturation=passed '
          'incoherent_marginals=passed')

if __name__ == '__main__':
    main()
