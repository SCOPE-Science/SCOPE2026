"""Stand-alone reproducibility checks of finite algebra and sample truncations.

The all-dimensional theorem relies on the analytic proof, not on these tests.
Requires Python 3, NumPy, SciPy and SymPy.
"""
from fractions import Fraction
from math import sqrt

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import minimize_scalar


def numerical_radius_trunc(q, s, t, dimension=100):
    e = np.array([q**k * (s if k % 4 == 1 else t if k % 4 == 3 else 1.0)
                  for k in range(dimension - 1)], dtype=float)
    lam = eigh_tridiagonal(np.zeros(dimension), e, select='i',
                          select_range=(dimension - 1, dimension - 1))[0][0]
    return lam / 2


def check_exact(q):
    # Weighted four-vertex path: det(I-S)=1-a^2-b^2-d^2+a^2 d^2.
    a, d = q**2, q**4
    b2 = (1 - q**4) * (1 - q**8)
    assert 1 - a*a - b2 - d*d + a*a*d*d == 0
    # Effective two-level perturbation matrix at the large-budget crossing.
    y = -(1-q*q)/(2*(1+q*q))
    M = sp.Matrix([[q*y, q*q/2], [q*q/2, -q**3*y]])
    target = q**3/(1+q*q)
    assert sp.simplify((target*sp.eye(2)-M).det()) == 0
    assert M[0, 0] < target and M[1, 1] < target
    return float(target)


def check_numeric(q):
    cstar = sqrt((1-q**4)*(1-q**8))/q**3
    below = 0.75*cstar
    above = 1.3*cstar
    assert abs(numerical_radius_trunc(q, 0, below) - 0.5) < 2e-11
    assert numerical_radius_trunc(q, 0, above) > 0.5
    minim = minimize_scalar(lambda s: numerical_radius_trunc(q, s, above-s),
                            bounds=(0, above), method='bounded',
                            options={'xatol': 1e-10})
    assert minim.success and 0 < minim.x < above
    assert minim.fun < numerical_radius_trunc(q, 0, above) - 1e-7
    assert minim.fun < numerical_radius_trunc(q, above, 0) - 1e-7
    c = 3000*cstar
    minim = minimize_scalar(lambda s: numerical_radius_trunc(q, s, c-s),
                            bounds=(0, c), method='bounded',
                            options={'xatol': 1e-9})
    slope = q**3/(2*(1+q*q))
    s_asym = q*q/(1+q*q)*c - (1-q*q)/(2*(1+q*q))
    assert abs(minim.fun - slope*(c+1)) < 0.008
    assert abs(minim.x - s_asym) < 0.04


for qs in (sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(3, 4)):
    check_exact(qs)
for qf in (0.3, 0.6, 0.85):
    check_numeric(qf)
print('WEIGHTED_SHIFT_BUDGET_THRESHOLD_AND_ASYMPTOTIC_CHECKS_OK')
