#!/usr/bin/env python3
"""Exact symbolic checks of the critical fear--refuge predator extinction identities.

Dependencies: Python 3.10+ and SymPy (requirements.txt). These are algebra
checks, not substitutes for the comparison and planar convergence proof.
"""
from sympy import symbols, simplify, diff, factor, Rational

u, v, U = symbols('u v U', positive=True)
r, a, alpha, k, b, c, eta = symbols('r a alpha k b c eta', positive=True)
D, D1 = 1 + alpha*u + k*v, 1 + alpha*U
F = r/D - a*u - b*v
Auv = a + r*alpha/(D*D1)
Buv = b + r*k/(D*D1)
# Exact difference equals the predator-free equilibrium residual.
assert simplify(F + Auv*(u-U) + Buv*v - (r/D1-a*U)) == 0
A = a + r*alpha/D1**2
B = b + r*k/D1**2
Q = eta + c*b*B/A
# Exact algebra underlying the forced linear equation for p=(u-U)/v:
w = u-U
p = w/v
udot = u*F
vdot = v*(c*b*(u-U)-eta*v)
actual_pdot = diff(p,u)*udot + diff(p,v)*vdot
expected_pdot = -(u*Auv+c*b*w-eta*v)*p-u*Buv
assert simplify(actual_pdot-expected_pdot - u*(r/D1-a*U)/v) == 0
assert simplify(diff(Q,k)-c*b*r/(A*D1**2)) == 0
assert simplify(diff(B/(A*Q),k)-A*eta*r/(D1**2*(A*eta+c*b*B)**2)) == 0
sample = {r:Rational(2),a:Rational(1),alpha:Rational(1),k:Rational(1),
          b:Rational(1),c:Rational(1),eta:Rational(1),U:Rational(1)}
assert simplify(r/D1-a*U).subs(sample) == 0
assert A.subs(sample) == Rational(3,2)
assert B.subs(sample) == Rational(3,2)
assert Q.subs(sample) == 2
assert (1/Q).subs(sample) == Rational(1,2)
assert (B/(A*Q)).subs(sample) == Rational(1,2)
print('VERIFY_OK')
