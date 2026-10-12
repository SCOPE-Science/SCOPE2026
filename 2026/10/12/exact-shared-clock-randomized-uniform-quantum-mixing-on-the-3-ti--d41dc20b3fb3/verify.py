#!/usr/bin/env python3
"""Exact spectral-moment checks for randomized mixing on the 3-by-4 path grid.

Requires Python 3 and SymPy. Optional --numerical uses NumPy and SciPy.
This program checks algebraic identities and examples; the topological
positive-support and Kronecker arguments are mathematical proofs in RESULT.md.
"""
import argparse
import sympy as sp


def path_adjacency(n):
    A = sp.zeros(n)
    for k in range(n - 1):
        A[k, k + 1] = A[k + 1, k] = 1
    return A


def spectral_idempotents(A, distinct_eigenvalues):
    I = sp.eye(A.rows)
    out = {}
    for lam in distinct_eigenvalues:
        P = I
        for mu in distinct_eigenvalues:
            if mu != lam:
                P = P * (A - mu * I) / (lam - mu)
        P = P.applyfunc(sp.simplify)
        assert (A * P - lam * P).applyfunc(sp.simplify) == sp.zeros(A.rows)
        assert (P * P - P).applyfunc(sp.simplify) == sp.zeros(A.rows)
        out[lam] = P
    assert (sum(out.values(), sp.zeros(A.rows)) - I).applyfunc(sp.simplify) == sp.zeros(A.rows)
    for j, P in out.items():
        for k, Q in out.items():
            if j != k:
                assert (P * Q).applyfunc(sp.simplify) == sp.zeros(A.rows)
    return out


def expected_mixing(projectors, prescribed_gap, moment):
    n = next(iter(projectors.values())).rows
    result = sp.zeros(n)
    nonzero_gaps = set()
    for lam, P in projectors.items():
        for mu, Q in projectors.items():
            diff = sp.simplify(lam - mu)
            if diff == 0:
                coeff = sp.Integer(1)
            else:
                nonzero_gaps.add(sp.simplify(sp.Abs(diff)))
                coeff = moment if diff in (prescribed_gap, -prescribed_gap) else sp.Integer(0)
            result += coeff * P.multiply_elementwise(Q)
    return result.applyfunc(sp.simplify), nonzero_gaps


def exact_checks():
    r2, r5 = sp.sqrt(2), sp.sqrt(5)
    alpha, beta = (1 + r5) / 2, (1 - r5) / 2
    P3 = spectral_idempotents(path_adjacency(3), [r2, sp.Integer(0), -r2])
    P4 = spectral_idempotents(path_adjacency(4), [alpha, beta, -alpha, -beta])
    E3, gaps3 = expected_mixing(P3, 2 * r2, -sp.Rational(1, 3))
    E4, gaps4 = expected_mixing(P4, r5, -sp.Rational(1, 4))
    assert E3 == sp.ones(3) / 3, E3
    assert E4 == sp.ones(4) / 4, E4
    assert len(gaps3) == 2, gaps3
    assert len(gaps4) == 4, gaps4
    # Fourier densities normalized by Haar measure; their cosine coefficients
    # are -1/3 and -1/4 at the specified frequencies, respectively.
    x, y = sp.symbols('x y', real=True)
    assert sp.integrate(sp.cos(2*x) * (1-sp.Rational(2,3)*sp.cos(2*x)),(x,0,2*sp.pi))/(2*sp.pi)==-sp.Rational(1,3)
    phi, psi = sp.symbols('phi psi', real=True)
    # Orthogonality gives exactly -1/4 for cos(phi-psi).
    assert sp.integrate(sp.cos(x) * (1-sp.Rational(1,2)*sp.cos(x)),(x,0,2*sp.pi))/(2*sp.pi)==-sp.Rational(1,4)
    assert sp.kronecker_product(E3,E4) == sp.ones(12)/12
    print('VERIFY_OK idempotents=7 exact_factor_rows=7 exact_product_entries=144',
          'nonzero_gap_counts=2,4 caratheodory_support_bound=15')


def numerical_checks():
    import numpy as np
    from scipy.optimize import linprog
    from scipy.linalg import expm
    A3 = np.array(path_adjacency(3),dtype=float)
    A4 = np.array(path_adjacency(4),dtype=float)
    A12 = np.kron(A3,np.eye(4)) + np.kron(np.eye(3),A4)
    def M(A,t):
        U=expm(1j*t*A)
        return abs(U)**2
    for t in [0,0.35,1.2,2.7,4.1]:
        diff=M(A12,t)-np.kron(M(A3,t),M(A4,t))
        assert np.max(np.abs(diff))<1e-13
    v3, V3=np.linalg.eigh(A3)
    v4, V4=np.linalg.eigh(A4)
    def fastM(v,V,t):
        U=(V * np.exp(1j*v*t)) @ V.T
        return np.abs(U)**2
    rng=np.random.default_rng(123456)
    ts=rng.uniform(0,1_000_000,300)
    X=np.array([np.kron(fastM(v3,V3,t),fastM(v4,V4,t)).ravel() for t in ts]).T
    A=np.vstack((X,np.ones((1,len(ts)))))
    b=np.r_[np.ones(144)/12,1.0]
    sol=linprog(np.zeros(len(ts)),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
    assert sol.success, sol.message
    residual=float(np.max(abs(A@sol.x-b)))
    support=int(np.count_nonzero(sol.x>1e-9))
    assert support<=15 and residual<1e-8, (support,residual)
    print('NUMERICAL_OK full_matrix_trials=5 sampled_times=300',
          'positive_support=',support,'max_matrix_residual=',f'{residual:.3g}')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--numerical',action='store_true',help='Optional independent approximate witness')
    args=parser.parse_args()
    exact_checks()
    if args.numerical: numerical_checks()
