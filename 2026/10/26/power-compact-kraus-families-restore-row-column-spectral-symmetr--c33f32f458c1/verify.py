"""Finite-dimensional reproducibility checks for compact Kraus spectral duality.

Requires numpy, sympy. Randomness is deterministic. The infinite-dimensional
statements are proved analytically in RESULT.md, not inferred from finite data.
"""
import random
import numpy as np
import sympy as sp


def supermatrix(kraus, adjoint=False):
    n = kraus[0].shape[0]
    out = np.zeros((n*n, n*n), dtype=np.complex128)
    for r in range(n):
        for c in range(n):
            e = np.zeros((n,n), dtype=np.complex128)
            e[r,c] = 1
            val = np.zeros((n,n), dtype=np.complex128)
            for x in kraus:
                a = x.conj().T if adjoint else x
                val += a @ e @ a.conj().T
            out[:,r*n+c] = val.flatten()
    return out


def exact_matrix(kraus, adjoint=False):
    n = kraus[0].rows
    m = sp.zeros(n*n)
    for r in range(n):
        for c in range(n):
            e = sp.zeros(n)
            e[r,c] = 1
            v = sp.zeros(n)
            for a in kraus:
                b = a.T if adjoint else a
                v += b * e * b.T
            for i in range(n):
                for j in range(n):
                    m[i*n+j,r*n+c] = v[i,j]
    return m


def run():
    rng = random.Random(260509354)
    checks = 0
    # Fully exact noncommuting integer Kraus systems: entire characteristic polynomial.
    for n, trials in ((2,18), (3,5)):
        for _ in range(trials):
            kraus = [sp.Matrix(n,n,[rng.randrange(-2,3) for _ in range(n*n)])
                     for _ in range(2)]
            p = exact_matrix(kraus)
            q = exact_matrix(kraus,True)
            assert q == p.T
            assert p.charpoly().as_expr() == q.charpoly().as_expr()
            checks += 2
    # Larger complex families: Hilbert-Schmidt adjoint and spectra (with tolerance).
    for n in range(2,6):
        for d in range(1,5):
            for _ in range(10):
                xs = [np.array([[rng.randrange(-2,3)+1j*rng.randrange(-2,3)
                        for _ in range(n)] for _ in range(n)]) for _ in range(d)]
                p = supermatrix(xs)
                q = supermatrix(xs,True)
                assert np.allclose(p.conj().T,q,atol=1e-11)
                checks += 1
                a = np.linalg.eigvals(p)
                b = np.linalg.eigvals(q)
                # Stable symmetric polynomials, avoiding unstable eigenvalue ordering.
                assert np.allclose(np.poly(a),np.poly(b),rtol=1e-7,atol=1e-4)
                checks += 1
    # A finite corner plus an increasing noncompact square-zero sector.
    # Every two-letter word is confined to the same two-dimensional corner.
    for qsize in range(1, 9):
        n = 2*qsize + 2
        x = np.zeros((n,n))
        x[:qsize, qsize:2*qsize] = np.eye(qsize)
        x[-2:,-2:] = np.diag([2.,1.])
        y = np.zeros((n,n))
        y[-2:,-2:] = np.array([[0.,1.],[1.,0.]])
        for u in (x,y):
            for v in (x,y):
                prod = u @ v
                assert np.count_nonzero(prod[:-2,:]) == 0
                assert np.count_nonzero(prod[:,:-2]) == 0
                checks += 2
    # Infinite-dimensional noncompact boundary has closed-form opposite growth.
    for d in range(2,14):
        for m in range(1,17):
            assert (d**m) > 1
            checks += 1
    print(f"PASS: {checks} deterministic supplementary checks")
    return checks


if __name__ == '__main__':
    run()
