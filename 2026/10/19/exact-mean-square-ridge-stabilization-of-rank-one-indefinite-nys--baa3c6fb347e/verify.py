"""Reproducible exact algebra and deterministic integration checks for a two-mode indefinite Nyström risk formula.

Requires Python 3.10+ and SymPy 1.12+; no external data.
"""
from fractions import Fraction
from math import asin, cos, isclose, pi, sin, sqrt
import sympy as sp

x = sp.symbols('x', positive=True)
c = sp.symbols('c', positive=True)
w, z = sp.symbols('w z', real=True)
J = 1 / (x * sp.sqrt(1 + x*x))
term = sp.simplify(J + x * sp.diff(J, x)/2)
F = 2*x / sp.sqrt(1+x*x) + 1/(2*x*(1+x*x)**sp.Rational(3,2))
H = 4*sp.asin(c)/sp.pi + 2*sp.sqrt(1-c*c)/(sp.pi*c)
assert sp.simplify(term - 1/(2*x*(1+x*x)**sp.Rational(3,2))) == 0
assert sp.simplify((2 - 2*(1-x*x*J) + term) - F) == 0
assert sp.simplify(sp.diff(F,x) - (2*x*x-1)*(2*x*x+1)/(2*x*x*(1+x*x)**sp.Rational(5,2))) == 0
assert sp.simplify(F.subs(x,1/sp.sqrt(2))-8*sp.sqrt(3)/9)==0
assert sp.simplify(sp.diff(H,c) - 2*(2*c*c-1)/(sp.pi*c*c*sp.sqrt(1-c*c)))==0
assert sp.simplify(H.subs(c,1/sp.sqrt(2))-(1+2/sp.pi))==0
assert sp.expand(2-2*w*z+w*w - (2-z*z+(w-z)**2))==0
assert 8*sqrt(3)/9 < 1+2/pi
assert 1.5 < 8*sqrt(3)/9

# Exact rational matrix calculation. A = 2 diag(1,-1), u = (3/5, 4/5).
lam = Fraction(2)
u = [Fraction(3,5), Fraction(4,5)]
v = [lam*u[0], -lam*u[1]]
d = lam*(u[0]*u[0]-u[1]*u[1])
for tau in [Fraction(1,3), Fraction(1), Fraction(3)]:
    coeff = d/(d*d+tau*tau)
    residual = [[(lam if i==j==0 else -lam if i==j==1 else Fraction(0))
                 -coeff*v[i]*v[j] for j in range(2)] for i in range(2)]
    direct = sum(a*a for row in residual for a in row)
    formula = 2*lam*lam-2*coeff*lam*lam*d+coeff*coeff*lam**4
    assert direct==formula

# Independent deterministic angular quadrature of the actual squared matrix error.
N = 40_000
for lam_float in (0.5, 1., 2.5):
    for ratio in (0.2, 1/sqrt(2), 1.0, 2.0):
        tau_float = lam_float*ratio
        empirical = 0.
        for j in range(N):
            theta = 2*pi*(j+0.5)/N
            u1,u2=cos(theta),sin(theta)
            v1,v2=lam_float*u1, -lam_float*u2
            d=lam_float*(u1*u1-u2*u2)
            coeff=d/(d*d+tau_float*tau_float)
            e11=lam_float-coeff*v1*v1
            e22=-lam_float-coeff*v2*v2
            e12=-coeff*v1*v2
            empirical+=e11*e11+e22*e22+2*e12*e12
        empirical/=N
        analytic=lam_float**2*(2*ratio/sqrt(1+ratio**2)+1/(2*ratio*(1+ratio**2)**1.5))
        assert isclose(empirical,analytic,abs_tol=2e-8,rel_tol=2e-8),(lam_float,ratio,empirical,analytic)

# The hard cutoff is optimal at exactly 1/sqrt(2), and the exact tail law is a CDF.
for cutoff in (0.1, 0.3, 1/sqrt(2), 0.9):
    empirical=0.
    for j in range(N):
        theta=2*pi*(j+0.5)/N
        zval=cos(2*theta)
        empirical += 1/(zval*zval) if abs(zval)>=cutoff else 2
    empirical/=N
    expected=4/pi*asin(cutoff)+2/pi*sqrt(1-cutoff*cutoff)/cutoff
    assert isclose(empirical,expected,rel_tol=1e-3,abs_tol=1e-3), (cutoff,empirical,expected)
for r in (1.0,1.5,2.0,5.0,100.):
    prob = 2/pi*asin(1/r)
    assert 0<prob<=1

print('PASS: 7 symbolic identities, 2 strict constant inequalities, 3 rational matrix identities, 12 angular ridge quadratures, 4 hard-cutoff quadratures, 5 tail-formula domain checks')
