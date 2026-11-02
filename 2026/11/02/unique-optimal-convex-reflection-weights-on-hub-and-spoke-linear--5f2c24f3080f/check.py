"""Supplemental arithmetic checks for weighted reflection averages on hub-spoke normals.

Run with Python 3 and SymPy, NumPy. The exact mathematics is supplied in RESULT.md;
finite tests here are supplemental, not a proof of the quantified theorem.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

checks = 0

# Exact matrix checks on rational-angle data (no floating-point eigenvalue solver).
for n in range(2, 9):
    for c, s in [(sp.Rational(3, 5), sp.Rational(4, 5)),
                 (sp.Rational(5, 13), sp.Rational(12, 13)),
                 (sp.Rational(8, 17), sp.Rational(15, 17))]:
        D = n + (n - 2)*c
        U = sp.zeros(n)
        U[0, 0] = 1
        for j in range(1, n):
            U[j, 0] = c
            U[j, j] = s
        p = [sp.cancel((1 + (n - 2)*c)/D)] + [1/D]*(n-1)
        assert sum(p) == 1
        B = 2*U.T*sp.diag(*p)*U
        lam_min = 2*(1-c)/D
        lam_mid = 2*(1-c*c)/D
        lam_max = 2*(1+c)*(1+(n-2)*c)/D
        q = sp.Matrix([1] + [-(1+c)/s]*(n-1))
        assert B*q == lam_min*q
        checks += 1
        assert sp.simplify(B.trace() - 2) == 0
        checks += 1
        assert sp.simplify(lam_min+(n-2)*lam_mid+lam_max-2) == 0
        checks += 1
        assert lam_min > 0 and lam_min < lam_max and lam_max < 2
        checks += 1
        for j in range(2, n):
            z = sp.zeros(n, 1)
            z[1] = 1
            z[j] = -1
            assert B*z == lam_mid*z
            checks += 1
        # Matrix polynomial identity independently checks the claimed spectrum.
        product = (B-lam_min*sp.eye(n))*(B-lam_mid*sp.eye(n))*(B-lam_max*sp.eye(n))
        assert product == sp.zeros(n)
        checks += 1
        # The dual direction has equal absolute inner products with every normal.
        a = U*q
        assert list(a) == [1] + [-1]*(n-1)
        checks += 1
        assert sp.simplify(2/(q.dot(q))-lam_min) == 0
        checks += 1

# Full weighted reflection symbols, unweighted Gram eigenvalue formula and numerical minimax tests.
rng = np.random.default_rng(20261031)
for n in [2, 3, 4, 5, 8, 12, 24]:
    for c in [0.07, 0.25, 0.55, 0.8, 0.98]:
        D = n + (n-2)*c
        U = np.zeros((n,n))
        U[0, 0] = 1
        for j in range(1,n):
            U[j,0] = c
            U[j,j] = math.sqrt(1-c*c)
        p = np.array([1+(n-2)*c]+[1]*(n-1), dtype=float)/D
        B = 2*U.T@np.diag(p)@U
        evals = np.linalg.eigvalsh(B)
        rate = np.linalg.norm(np.eye(n)-B, ord=2)
        predicted = ((n-2)+n*c)/D
        assert abs(rate-predicted) < 2e-12
        checks += 1
        assert abs(evals[0]-2*(1-c)/D) < 2e-12
        checks += 1
        UGram = U@U.T
        trace2 = 2+(n-2)*c*c
        discriminant = math.sqrt((n-2)**2*c**4+4*(n-1)*c*c)
        small = (trace2-discriminant)/2
        uniform_rate = 1-2*small/n
        B_unif = 2/n*(U.T@U)
        assert abs(np.linalg.norm(np.eye(n)-B_unif,2)-uniform_rate) < 2e-12
        checks += 1
        assert uniform_rate >= predicted-1e-12
        checks += 1
        for _ in range(80):
            pr = rng.dirichlet(np.ones(n))
            Br = 2*U.T@np.diag(pr)@U
            observed = np.linalg.norm(np.eye(n)-Br,2)
            assert observed >= predicted-1e-11, (n,c,pr,observed,predicted)
            checks += 1

# Large-dimension asymptotics for fixed correlations, without a large matrix eigensolve.
for c in [0.25, 0.5, 0.75]:
    for n in [1000,10000,100000]:
        D=n+(n-2)*c
        optgap=2*(1-c)/D
        trace2=2+(n-2)*c*c
        # Compute lambda_min by a stable determinant / large-eigenvalue formula.
        lmax=(trace2+math.sqrt((n-2)**2*c**4+4*(n-1)*c*c))/2
        ungap=2*(1-c*c)/(n*lmax)
        ratio=optgap/ungap
        expectation=n*c*c/(1+c)**2
        assert abs(ratio/expectation-1) < 0.04
        checks += 1
print('VERIFY_OK', checks)
