#!/usr/bin/env python3
"""Symbolic identities and finite high-precision diagnostics for a rational interval map.

Run: python checks/verify.py
Requires SymPy and mpmath. Analytical infinite-parameter claims are proved in RESULT.md.
"""
from sympy import symbols, sqrt, factor, simplify, diff, together, fraction, Poly, discriminant, Rational
from mpmath import mp

mu, x = symbols('mu x')
f = lambda z: mu*z*(1-z)/(1+z)
fx = f(x)
fp = diff(fx, x)
Q = mu*(mu-1)*x*x-(mu*mu-1)*x+mu+1
L = 1-(mu*mu-1)*(mu*mu-4*mu-1)/(2*mu*mu)
mu_b = 2+sqrt(5)
mu_f = 1+sqrt(2)+sqrt(4+2*sqrt(2))
mu_max = 3+2*sqrt(2)
a_formula = (mu*mu+1)*(mu*mu-2*mu-1)/mu**3

# Complete factorization of fixed points of the second iterate.
Gx = together(f(fx))
factorization = x*(mu*x-mu+x+1)*Q/((x+1)*(mu*x*x-mu*x-x-1))
assert simplify(together(Gx-x-factorization)) == 0
assert factor(discriminant(Q,x)) == (mu-1)*(mu+1)*(mu*mu-4*mu-1)

# Full two-cycle multiplier, derived using the two-cycle polynomial Q.
multiplier = together(fp*fp.subs(x,fx))
num, den = fraction(together(multiplier-L))
assert Poly(num, x).rem(Poly(Q,x)).is_zero
assert simplify(-diff(L,mu)-a_formula) == 0

# Exact threshold and the negative Schwarzian.
quartic = mu**4-4*mu**3-6*mu**2+4*mu+1
assert simplify(quartic.subs(mu,mu_f)) == 0
assert simplify((L+1)*2*mu**2+quartic) == 0
assert simplify(mu_max*(3-2*sqrt(2))-1) == 0
S = together(diff(fx,x,3)/fp-Rational(3,2)*(diff(fx,x,2)/fp)**2)
assert simplify(S+12/(x*x+2*x-1)**2) == 0

# Inexact finite checks are supplementary only, not proofs of local existence.
mp.dps=65
mcrit=1+mp.sqrt(2)+mp.sqrt(4+2*mp.sqrt(2))
mb=2+mp.sqrt(5)
upper=3+2*mp.sqrt(2)
assert mb<mcrit<upper
aval=(mcrit*mcrit+1)*(mcrit*mcrit-2*mcrit-1)/mcrit**3
assert aval>0
fnum=lambda m,z:m*z*(1-z)/(1+z)
dnum=lambda m,z:m*(1-2*z-z*z)/(1+z)**2

def roots2(m):
    rad=mp.sqrt((m+1)*(m*m-4*m-1)/(m-1))
    return ((m+1-rad)/(2*m),(m+1+rad)/(2*m))

pminus,pplus=roots2(mcrit)
assert mp.almosteq(fnum(mcrit,pminus),pplus)
assert mp.almosteq(fnum(mcrit,pplus),pminus)
assert abs(dnum(mcrit,pminus)*dnum(mcrit,pplus)+1)<mp.mpf('1e-55')

def scaling(p,q):
    Sf=-12/(p*p+2*p-1)**2
    Sg=Sf-12*dnum(mcrit,p)**2/(q*q+2*q-1)**2
    return mp.sqrt(-6*aval/Sg)

Cminus=scaling(pminus,pplus)
Cplus=scaling(pplus,pminus)
assert abs(Cminus-mp.mpf('0.211072666779666474'))<mp.mpf('1e-17')
assert abs(Cplus-mp.mpf('0.101360669114122318'))<mp.mpf('1e-17')

eta=mp.mpf('1e-8')
m=mcrit+eta
low,high=roots2(m)
F=lambda z:fnum(m,z)
H=lambda z:F(F(F(F(z))))-z

for p,C in [(low,Cminus),(high,Cplus)]:
    r1=mp.findroot(H,(p-mp.sqrt(eta)*C*mp.mpf('1.01'),p-mp.sqrt(eta)*C*mp.mpf('0.99')))
    r2=mp.findroot(H,(p+mp.sqrt(eta)*C*mp.mpf('0.99'),p+mp.sqrt(eta)*C*mp.mpf('1.01')))
    assert r1<p<r2 and abs((r2-p)/mp.sqrt(eta)-C)<mp.mpf('3e-5')
    assert abs(F(F(r1))-r2)<mp.mpf('1e-40')
    points=[r1]
    for _ in range(3):points.append(F(points[-1]))
    assert len(set([str(mp.nstr(w,40)) for w in points]))==4
    assert abs(F(points[-1])-r1)<mp.mpf('1e-40')
    mult=mp.fprod([dnum(m,z) for z in points])
    assert 0<mult<1
    assert abs(mult-(1-4*aval*eta))<mp.mpf('1e-10')

print('PASS: symbolic factorization, discriminant, two-cycle multiplier, flip radical, Schwarzian, derivative, invariant-range edge.')
print('PASS: finite high-precision local four-cycle roots, distinctness, multipliers and square-root scaling in both neighborhoods.')
print('Critical parameter:',mp.nstr(mcrit,20))
print('Amplitudes:',mp.nstr(Cminus,20),mp.nstr(Cplus,20))
print('Scope: these computations supplement, and do not replace, the analytic proof.')
