#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks for the reset-rate dimension law.

Requires scipy and sympy. This checks identities and finite sample values only;
proof of monotonicity and the asymptotic is analytical in RESULT.md.
"""
import scipy.optimize as opt
from scipy.special import kve
import sympy as sp
z,e,u = sp.symbols('z e u', positive=True)

# For F_nu(2 sqrt(nu*z)), the exact Bessel Riccati ODE gives these terms.
f = [2*z]
for k in range(1, 3):
    f.append(sp.expand(z*sp.diff(f[k-1], z) -
             sp.Rational(1, 2)*sum(f[j]*f[k-1-j] for j in range(k))))
expected = [2*z, 2*z-2*z**2, 2*z-8*z**2+4*z**3]
assert all(sp.simplify(f[j]-expected[j]) == 0 for j in range(3))
print('Exact Riccati expansion:', [str(g) for g in f])

# Independently obtain same terms from the gamma integral central moments.
mu = {0: 1, 1: 0, 2: e, 3: 2*e**2, 4: 3*e**2}
def E(phi):
    return sum(sp.diff(phi,u,j).subs(u,1)*mu[j]/sp.factorial(j) for j in mu)
h = sp.exp(-z/u)
Fg = sp.series(2*z*E(h/u)/E(h),e,0,3).removeO()
assert all(sp.simplify(sp.expand(Fg).coeff(e,j)-expected[j])==0 for j in range(3))
print('Gamma-integral second-order expansion verified')

def F(nu,x):
    return x*kve(nu-1,x)/kve(nu,x)

prev=None
for d in [2,3,4,5,6,8,12,20,50,100]:
    nu=d/2-1
    lo=1e-6 if nu == 0 else 2*nu**0.5
    hi=2*(nu+1)**0.5
    x=opt.brentq(lambda y:F(nu,y)-2,lo,hi,xtol=1e-13)
    assert 4*nu < x*x < 4*(nu+1)
    if prev is not None: assert x>prev
    prev=x
    approx=x*x-(4*nu+4/nu) if nu else float('nan')
    print('d=%3d root=%.12f detachment=%.9f second-order residual=%g'
          %(d,x,x*x-4*nu,approx))
print('All ten roots satisfy strict dimensional bracket and increasing order')
