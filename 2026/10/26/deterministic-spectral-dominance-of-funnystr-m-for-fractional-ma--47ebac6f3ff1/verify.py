"""Finite checks of deterministic power-Nystrom spectral comparisons.

Only finite tests: the proof's universal quantifiers do not rest on this program.
"""
import math
import numpy as np
import sympy as sp


def matrix_power(A, power):
    eigs, vecs = np.linalg.eigh(A)
    assert np.min(eigs) > 0
    return (vecs * eigs**power) @ vecs.T


def nystrom(A, W, q):
    A_q = matrix_power(A, q)
    A_2q_1 = matrix_power(A, 2*q - 1)
    Y = A_q @ W
    M = W.T @ A_2q_1 @ W
    return Y @ np.linalg.solve(M, Y.T)


def validate_exact():
    u = sp.symbols('u', positive=True)
    assert sp.cancel((u**5 + 1)/(u+1)) == u**4-u**3+u**2-u+1
    assert sp.simplify((u+1)/(1+1/u) - u) == 0
    assert sp.limit((u*u+1-sp.sqrt((u**5+1)/(u+1)))/u, u, sp.oo) == sp.Rational(1,2)
    assert sp.limit((u*u+1-u)/(u*u+1-sp.sqrt((u**5+1)/(u+1)))/u, u, sp.oo) == 2
    for L in [16., 256., 65536., 1e8]:
        A = np.diag([L, 1.])
        W = np.array([[L**(-3/8)], [1.]])
        alpha = np.trace(nystrom(A, W, 1))
        beta = np.trace(nystrom(matrix_power(A, .5), W, 1))
        assert np.isclose(alpha, (L**1.25+1)/(L**.25+1), rtol=2e-10)
        assert np.isclose(beta, L**.25, rtol=2e-10)
        assert math.sqrt(alpha) > beta


def validate_random():
    rg = np.random.default_rng(35102026)
    cases = 0
    for n in (2, 3, 5, 7):
        for k in (1, min(2,n), n):
            for q in (1, 2, 3):
                for rep in range(8):
                    U, _ = np.linalg.qr(rg.standard_normal((n,n)))
                    spectrum = np.exp(rg.uniform(-1,1,size=n))
                    A = (U*spectrum)@U.T
                    W = rg.standard_normal((n,k))
                    eigA = np.linalg.eigvalsh(nystrom(A, W, q))[-k:][::-1]
                    assert eigA[-1] > 0
                    for p in (.33, .5, .8, 1., 1.3, 1.8):
                        Ap = matrix_power(A,p)
                        B = nystrom(Ap,W,q)
                        eigB = np.linalg.eigvalsh(B)[-k:][::-1]
                        if p < 1:
                            assert np.all(eigB <= eigA**p + 1e-8)
                            # Both differences must be positive semidefinite.
                            # Low-rank fractional power uses clipped zero eigenvalues:
                            d,V = np.linalg.eigh(nystrom(A,W,q))
                            FA = (V*np.maximum(d,0)**p)@V.T
                            assert np.linalg.eigvalsh(Ap-FA)[0] > -2e-8
                            assert np.linalg.eigvalsh(Ap-B)[0] > -2e-8
                            assert np.trace(Ap-FA) <= np.trace(Ap-B) + 2e-8
                        elif p>1:
                            assert np.all(eigB + 1e-8 >= eigA**p)
                        else:
                            assert np.allclose(eigB,eigA,atol=1e-9)
                        cases += 1
    return cases


if __name__ == '__main__':
    validate_exact()
    n=validate_random()
    print(f'VERIFY_OK symbolic identities, sharp gap, and {n} random matrix comparisons')
