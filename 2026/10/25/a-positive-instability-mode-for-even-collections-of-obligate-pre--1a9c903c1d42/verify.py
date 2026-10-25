#!/usr/bin/env python3
"""Independent algebraic and numerical checks for obligate predation cycles.

Requires numpy, scipy, sympy. The proof for all parameter choices is in RESULT.md.
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def exact_two_cycles():
    successor = (1, 2, 0, 4, 5, 3)
    n = len(successor)
    P = sp.zeros(n)
    for i, j in enumerate(successor):
        P[i, j] = 1
    U = sp.ones(n, n)
    B = U - (n + 3) * P
    one = sp.ones(n, 1)
    assert B * one == -3 * one
    for i in range(n):
        assert B[i, i] > 0 and B[i, successor[i]] < 0
        for j in range(n):
            if j not in (i, successor[i]):
                assert B[i, j] > 0
    J = -B
    assert J * one == 3 * one
    eigen = J.eigenvals()
    assert eigen == {
        sp.Integer(3): 1,
        sp.Integer(9): 1,
        sp.Rational(-9, 2) + sp.Rational(9, 2)*sp.sqrt(3)*sp.I: 2,
        sp.Rational(-9, 2) - sp.Rational(9, 2)*sp.sqrt(3)*sp.I: 2,
    }, eigen
    return eigen


def sample_decomposition(successor, rng, trials=40):
    n = len(successor)
    for _ in range(trials):
        V = rng.uniform(0.08, 3.1, (n, n))
        d = rng.uniform(0.2, 4.0, n)
        F = np.zeros((n, n))
        for i, j in enumerate(successor):
            V[i, j] = 0.0
            F[i, j] = V[i].sum() + d[i]
        M = F - V
        assert np.allclose(M @ np.ones(n), d)
        Finv = np.linalg.inv(F)
        def radius(z):
            return max(abs(np.linalg.eigvals(Finv @ (V + z*np.eye(n)))))
        lo, hi = min(d), max(d)
        lam = brentq(lambda z: radius(z)-1.0, lo-1e-8, hi+1e-8, xtol=1e-12)
        assert lo-1e-7 <= lam <= hi+1e-7
        assert min(abs(w-lam) for w in np.linalg.eigvals(M)) < 1e-7
        vals, vecs = np.linalg.eig(Finv @ (V + lam*np.eye(n)))
        v = np.real(vecs[:, np.argmin(abs(vals-1.0))])
        if v.mean() < 0:
            v = -v
        assert v.min() > 0
        assert np.linalg.norm(M@v-lam*v) < 1e-7


if __name__ == "__main__":
    exact_two_cycles()
    rng = np.random.default_rng(20261021)
    partitions = [
        (1,2,0,4,5,3),
        (1,2,0,4,5,6,3),
        (1,2,3,0,5,6,7,4),
        (1,2,0,4,5,3,7,8,6,10,11,9),
    ]
    for sigma in partitions:
        sample_decomposition(sigma, rng, trials=40)
    print("CHECK_OK; exact six-species case and 160 numerical positive-equilibrium trials")
