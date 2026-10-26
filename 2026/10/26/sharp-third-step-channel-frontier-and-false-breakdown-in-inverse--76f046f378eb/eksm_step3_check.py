"""Reproducibility checks for the third-vector extended Krylov comparison.

Requires Python 3, SymPy, and NumPy. Run: python eksm_step3_check.py
Checks exact rational identities and independently constructed Euclidean projections.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

A = sp.diag(-sp.Rational(6, 5), 2, 3)
ones = sp.ones(3, 1)
w = A.inv() * ones
assert (ones.T * w)[0] == 0
assert sp.det(sp.Matrix.hstack(ones, w, A * ones)) == sp.Rational(28, 15)
v = ones / sp.sqrt(3)
beta_squared = sp.simplify((v.T * A.inv()**2 * v)[0] - (v.T * A.inv() * v)[0]**2)
assert beta_squared == sp.Rational(19, 54)
m1 = sp.simplify((v.T * A * v)[0])
m2 = sp.simplify((v.T * A**2 * v)[0])
rS_squared = sp.simplify(m2 - m1**2 - 1/beta_squared)
assert rS_squared == sp.Rational(1568, 4275)
assert sp.simplify(rS_squared/m2) == sp.Rational(1568, 20577)

for b, expected in [(sp.Matrix([1, 1, 2]), sp.Rational(16, 45)),
                    (sp.Matrix([1, 2, 2]), sp.Rational(47, 81))]:
    alpha = (b.T * A.inv() * b)[0] / (b.T * b)[0]
    rq = (b.T * A * b)[0] / (b.T * b)[0]
    assert alpha * rq == expected
    assert sp.det(sp.Matrix.hstack(b, A.inv()*b, A*b)) != 0

t = sp.symbols('t', real=True)
At = sp.diag(-sp.Rational(6, 5)+t, 2, 3)
alpha_t = (ones.T * At.inv() * ones)[0] / 3
assert sp.simplify(alpha_t + 25*t/(18*(6-5*t))) == 0
lim_const = sp.limit(sp.Abs(alpha_t/t), t, 0, dir='+') * sp.sqrt(m2)
assert sp.simplify(lim_const - 95/(108*sp.sqrt(3))) == 0

rng = np.random.default_rng(20261018)
checks = 0
for n in (3, 4, 6):
    for trial in range(1200):
        # A deliberately spans symmetric indefinite, definite, and nonsymmetric cases.
        d = rng.choice([-1., 1.], n) * rng.uniform(0.4, 5.0, n)
        if trial % 3 == 0:
            mat = np.diag(d)
        elif trial % 3 == 1:
            Q, _ = np.linalg.qr(rng.normal(size=(n,n)))
            mat = Q @ np.diag(d) @ Q.T
        else:
            mat = np.diag(d) + np.triu(rng.normal(size=(n,n))*0.18, 1)
        vin = rng.normal(size=n)
        vin /= np.linalg.norm(vin)
        invv = np.linalg.solve(mat, vin)
        alpha = float(vin @ invv)
        beta = float(np.linalg.norm(invv-alpha*vin))
        if beta < 1e-10: continue
        v2 = (invv-alpha*vin)/beta
        wS = mat @ vin
        wM = mat @ v2
        projS = wS - (wS @ vin)*vin - (wS @ v2)*v2
        projM = wM - (wM @ vin)*vin - (wM @ v2)*v2
        if np.linalg.norm(projS)<1e-9 or np.linalg.norm(projM)<1e-11: continue
        rhoS = np.linalg.norm(projS)/np.linalg.norm(wS)
        rhoM = np.linalg.norm(projM)/np.linalg.norm(wM)
        m1 = float(vin @ (mat @ vin))
        m2 = float(np.linalg.norm(mat @ vin)**2)
        denominator = 1-2*alpha*m1+alpha**2*m2
        assert denominator>0
        pred = abs(alpha)*math.sqrt(m2/denominator)
        assert np.isclose(rhoM/rhoS, pred, rtol=1e-8, atol=5e-9)
        assert (rhoM>rhoS) == (2*alpha*m1>1), (n, trial, alpha*m1)
        checks += 1

print('PASS: rational full-rank premature breakdown, exact residual, two sign reversals')
print('PASS: symbolic one-parameter singular asymptotic coefficient')
print(f'PASS: {checks} independent random 3/4/6-dimensional projection comparisons')
