"""Exact algebraic reproduction for the hyperbolic three-space covariance criterion.

Requires Python 3 and SymPy; no network, numerical solver, or external data.
"""
import sympy as sp

a, w, u = sp.symbols("a w u", real=True)

def denom(c):
    return (c*c + u + w*w)**2 - 4*u*w*w

def numerator(c):
    return c*c + u - w*w

P = (u**2 + 2*(a*a + w*w + 1)*u + (a*a - 1)**2
     - 2*(a*a + 1)*w*w - 3*w**4)
identity = numerator(a-1)*denom(a+1) - numerator(a+1)*denom(a-1) - 4*a*P
assert sp.expand(identity) == 0

# The sharp spectral threshold is the positive root of P(0)=0 in t=w^2.
t = sp.symbols("t", nonnegative=True)
tstar = (2*sp.sqrt(a**4 - a*a + 1) - (a*a + 1))/3
assert sp.simplify(-3*tstar**2 - 2*(a*a+1)*tstar + (a*a-1)**2) == 0

# The rational transform's polynomial at sample spectral parameter u=0.
assert P.subs({a: 2, w: sp.Rational(1,2), u: 0}) > 0
assert P.subs({a: 2, w: sp.Rational(6,5), u: 0}) < 0
assert sp.simplify(sp.diff(P,u) - (2*u+2*(a*a+w*w+1))) == 0
print("PASS: exact transform numerator, threshold algebra, and sample signs")
