"""Independent finite-time polynomial-generator and energy-martingale consistency checks.

Requires Python 3, NumPy, SciPy. Run: python work_variance_checker.py
These finite checks supplement, but do not prove, the all-parameter theorem.
"""
from math import exp, isclose
import numpy as np
from scipy.linalg import expm

CASES = 0
ASSERTIONS = 0

def verify(q, D, r, stiffness, t):
    global CASES, ASSERTIONS
    k = r * (1-q*q)
    c = stiffness * (1-q*q) / 2
    m2 = 2 * D / k
    m4 = 24 * D**2 / (k**2 * (1+q*q))
    # For joint state (X_t,Y_t), generator on polynomials:
    # G f = D f_xx + r[f(qx,y+c*x*x)-f(x,y)].
    # z components: 1, E X², E X⁴, E Y, E YX², E Y².
    G = np.zeros((6, 6))
    G[1, 0], G[1, 1] = 2*D, -k
    G[2, 1], G[2, 2] = 12*D, -r*(1-q**4)
    G[3, 1] = r*c
    G[4, 3], G[4, 4], G[4, 2] = 2*D, -k, r*c*q*q
    G[5, 4], G[5, 2] = 2*r*c, r*c*c
    z = expm(G*t) @ np.array([1., m2, m4, 0., 0., 0.])
    mean = stiffness * D * t
    var_exact = stiffness**2 * (4*D**2*t/k
                 + 2*D**2*(1-5*q*q)*(1-exp(-k*t))/(k*k*(1+q*q)))
    # Independent quadratic-energy martingale calculation.
    var_U = stiffness**2 * (m4-m2*m2)/4
    var_mart = stiffness**2 * 2*D*m2*t
    cov_mart_U = stiffness**2 * 2*D*m2*(1-exp(-k*t))/k
    var_energy = var_mart + 2*var_U*(1-exp(-k*t)) - 2*cov_mart_U
    tests = [
        isclose(z[1], m2, rel_tol=2e-8, abs_tol=1e-8),
        isclose(z[2], m4, rel_tol=2e-8, abs_tol=1e-8),
        isclose(z[3], mean, rel_tol=2e-8, abs_tol=1e-8),
        isclose(z[5]-z[3]**2, var_exact, rel_tol=2e-8, abs_tol=1e-8),
        isclose(var_energy, var_exact, rel_tol=2e-8, abs_tol=1e-8),
        var_exact > 0
    ]
    assert all(tests), (q,D,r,stiffness,t,tests,z,var_exact,var_energy)
    CASES += 1
    ASSERTIONS += len(tests)

for q in [0., 0.1, 0.2, 0.3, np.sqrt(0.2), 0.5, 0.7, 0.85, 0.95]:
 for D in [0.2, 1., 2.]:
  for r in [0.4, 1., 3.]:
   for t in [0.01, 0.2, 1.3, 5.]:
    for stiffness in [0.7, 1.5]:
     verify(q,D,r,stiffness,t)

# Exact symbolic identity for the unique cancellation factor.
try:
 import sympy as sp
 a=sp.symbols('a', real=True)
 expr = sp.factor(2*(5-a*a)/(1+a*a)-8)
 assert sp.simplify(expr-2*(1-5*a*a)/(1+a*a))==0
 ASSERTIONS += 1
except ImportError:
 pass # SymPy is optional. Numeric assertions remain complete.

print(f'PASS: {CASES} independent-generator cases, {ASSERTIONS} checks')
