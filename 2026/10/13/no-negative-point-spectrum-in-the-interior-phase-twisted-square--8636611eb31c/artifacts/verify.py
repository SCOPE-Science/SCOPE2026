#!/usr/bin/env python3
import sympy as sp

kappa, ell, mu, Q = sp.symbols('kappa ell mu Q', positive=True, real=True)
s = sp.sinh(kappa*ell)
c = sp.cosh(kappa*ell)

c0 = sp.sin(2*mu)*s**2
c4 = c0
c2 = -sp.sin(2*mu)*(1 + 3*sp.cosh(2*kappa*ell))
c1 = -2*(2*sp.cos(2*mu)*c - Q)*s
c3 = 2*(2*sp.cos(2*mu)*c + Q)*s
F = sp.expand(c0 + c1*kappa + c2*kappa**2 + c3*kappa**3 + c4*kappa**4)
expected = 2*kappa*(1+kappa**2)*s
assert sp.simplify(sp.diff(F,Q) - expected) == 0
remainder = sp.expand(F - expected*Q)
assert Q not in remainder.free_symbols
assert sp.simplify(sp.diff(remainder,Q)) == 0
print('VERIFY_OK q_coefficient=' + str(sp.factor(expected)))
