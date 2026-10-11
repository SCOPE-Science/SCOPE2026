#!/usr/bin/env python3
"""Exact algebraic identities for a resonant Holling--Tanner extinction law.

Requires Python 3 and SymPy. This checks finite algebraic steps; the
asymptotic argument is proved analytically in RESULT.md.
"""
import sympy as s

u, eta, A, M, L, theta, H = s.symbols(
    'u eta A M L theta H', positive=True, finite=True)
Q = A*(1+M)/2
S = M
v = u*(2+eta)
f = (1-u)*(u-M)-Q*v/(u+A)
F = u**2*(1+M-A-u)/(u+A)
h = Q*u/(u+A)
delta = (1+M-A)/A
assert s.simplify(f-(-M+F-h*eta)) == 0

r_prime = (2+eta)*(S*(1-(2+eta))-f)
assert s.simplify(r_prime-(2+eta)*(-M*eta-F+h*eta)) == 0
u_prime = u*f
eta_prime = r_prime
assert s.simplify(s.limit(F/u**2,u,0)-delta) == 0
J = s.Matrix([u_prime,eta_prime]).jacobian([u,eta]).subs({u:0,eta:0})
assert J == s.diag(-M,-2*M)
assert s.simplify(s.diff(eta_prime,u,2).subs({u:0,eta:0})/2 + 2*delta) == 0
assert s.simplify(s.diff(u_prime,u,2).subs({u:0,eta:0})/2) == 0
assert s.simplify(s.diff(u_prime,u,3).subs({u:0,eta:0})/6-delta)==0

# The two known coefficients follow from direct resonant coefficient balance.
d3 = -delta/(2*M)
assert s.simplify((-3*M*d3)-(-M*d3+delta)) == 0
q=s.symbols('q', positive=True)
eta_ans=q**2*(-2*delta*L**2*theta+H)
u_ans=L*q+d3*L**3*q**3
# d/dtheta(q)=-M*q, d/dtheta(theta)=1.
def dtheta(expr):
    return s.diff(expr,theta)-M*q*s.diff(expr,q)
assert s.expand(dtheta(eta_ans)-(-2*M*eta_ans-2*delta*L**2*q**2))==0
assert s.expand(dtheta(u_ans)-(-M*u_ans+delta*(L*q)**3))==0

# Sharp parameter examples on opposite sides of A=1+M.
assert delta.subs({A:s.Rational(1,2),M:s.Rational(1,4)}) == s.Rational(3,2)
assert delta.subs({A:2,M:s.Rational(1,4)}) == -s.Rational(3,8)
assert Q.subs({A:s.Rational(1,2),M:s.Rational(1,4)}) == s.Rational(5,16)
assert Q.subs({A:2,M:s.Rational(1,4)}) == s.Rational(5,4)
print('CHECK_OK: exact vector field, Jacobian, resonant forcing, and asymptotic coefficient balances')
