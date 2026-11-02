#!/usr/bin/env python3
"""Exact rational verification of a periodically switched PAT recurrence.
Requires Python 3 and sympy. Run: python verify.py
"""
import sympy as sp

t = sp.symbols('t', real=True)
z = sp.symbols('z')
lam = sp.Rational(1, 2)
mu = de = sp.Rational(1, 4)
al = t
ga = sp.Integer(1)
A = sp.Matrix([
    [1-lam, 0, 0, 0],
    [ga*(1-lam), mu, 0, -ga],
    [al*ga*(1-lam), al*mu, de, -al*ga],
    [al*ga*(1-lam), al*mu, de, 1-al*ga],
])
B = sp.Matrix([lam, ga*lam, al*ga*lam, al*ga*lam])
e = sp.Matrix([[0, 0, 0, 1]])
U = B*e
O = sp.zeros(4)
S = A.row_join(O).col_join(U.row_join(A))
T = A.row_join(U).col_join(O.row_join(A))
P = T*S
J = O.row_join(sp.eye(4)).col_join(sp.eye(4).row_join(O))
K = J*S
checks = {
    'single_filter_characteristic': sp.simplify(A.charpoly(z).as_expr()
        - (z-sp.Rational(1,2))*(z**3+(t-sp.Rational(3,2))*z**2+sp.Rational(9,16)*z-sp.Rational(1,16)))==0,
    'switch_swap': T == J*S*J,
    'monodromy_square': P == K*K,
    'det_positive_mode': sp.simplify((sp.eye(8)-K).det() - t*(75-32*t)/64)==0,
    'det_negative_mode': sp.simplify((sp.eye(8)+K).det() - t*(225-64*t)/64)==0,
    'det_monodromy': sp.simplify((sp.eye(8)-P).det() - t**2*(32*t-75)*(64*t-225)/4096)==0,
    'schur_quadratic_reduction': sp.simplify((z**3+(t-sp.Rational(3,2))*z**2+sp.Rational(9,16)*z-sp.Rational(1,16)) - (-sp.Rational(1,16))*(1+(t-sp.Rational(3,2))*z+sp.Rational(9,16)*z**2-sp.Rational(1,16)*z**3)-z*(255*z**2+(256*t-375)*z+(16*t+120))/256)==0,
    'rational_instance_negative': sp.simplify((sp.eye(8)-P).det().subs(t,3)+sp.Rational(6237,4096))==0,
    'threshold_unity_eigenvalue': (sp.eye(8)-P).det().subs(t,sp.Rational(75,32))==0,
}
for title, passed in checks.items():
    if not passed:
        raise AssertionError(title)
    print('PASS',title)
print('All',len(checks),'exact symbolic checks passed.')
