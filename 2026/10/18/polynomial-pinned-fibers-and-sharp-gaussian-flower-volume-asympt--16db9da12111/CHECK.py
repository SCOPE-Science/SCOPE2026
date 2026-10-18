#!/usr/bin/env python3
"""Exact rational checks for pinned Boolean-quadric cycle volume identities.
Requires SymPy; run `python CHECK.py`. Finite checks supplement the paper proof.
"""
import math
import sympy as sp
u=sp.symbols('u', nonnegative=True)

def cycle(ell):
    a=1-2*u
    C=(-1)**(ell+1)*sp.Rational(2)**(4*ell-1)/sp.factorial(2*ell)*(sp.bernoulli(2*ell,a/2)-sp.Rational(1,2**(2*ell))*sp.bernoulli(2*ell,a))
    S=(-1)**(ell+1)*sp.bernoulli(2*ell)*sp.Rational(2)**(2*ell-1)*(2**(2*ell)-1)/sp.factorial(2*ell)
    Q=sp.expand(sp.Rational(1,2**ell)*(S-C))
    D=sp.expand(sp.Rational(1,2**ell*sp.factorial(ell-1)**2)*sum(sp.binomial(ell-1,j)*(-4*u*u)**j*(1-(2*u)**(2*ell-1-2*j))/sp.Rational(2*ell-1-2*j) for j in range(ell)))
    return S,Q,D,sp.expand(Q-D)

for ell in range(3,13):
    S,Q,D,P=cycle(ell)
    assert sp.expand(P.subs(u,-u)-P)==0
    assert sp.degree(P,u)<=2*ell-2
    assert sp.expand(Q-D-P)==0
    assert sp.simplify(Q.subs(u,0)-sp.Rational(1,2**(ell-1))*S)==0
    assert sp.simplify(D.subs(u,0)-sp.binomial(2*ell-2,ell-1)/sp.Rational(2**ell*sp.factorial(2*ell-1)))==0
    bQ=sp.simplify(-Q.coeff(u,2)/Q.subs(u,0))
    bD=sp.simplify(-D.coeff(u,2)/D.subs(u,0))
    bP=sp.simplify(-P.coeff(u,2)/P.subs(u,0))
    assert sp.simplify(bD-4*(ell-1)*(2*ell-1)/sp.Integer(2*ell-3))==0
    assert 0<bP<bQ<bD
    assert P.subs(u,sp.Rational(1,2))==0
    print('cycle',ell,'center ratio',sp.factor(P.subs(u,0)/Q.subs(u,0)),'bP',bP,'bQ',bQ)
S,Q,D,P=cycle(3)
assert P==sp.expand((1-4*u*u)**2/sp.Integer(96))
assert cycle(4)[3]==sp.Rational(1,320)-sp.Rational(7,240)*u*u+u**4/sp.Integer(12)-u**6/sp.Integer(15)
bP=sp.Rational(8); bQ=sp.Rational(10)
assert sp.simplify(sp.sqrt(bQ/bP)-sp.sqrt(5)/2)==0
from mpmath import mp
mp.dps=35
q=lambda t:(1-10*t*t+40*t**4-32*abs(t)**5)/60
p=lambda t:(1-4*t*t)**2/96
for k in (30,120,300):
    num=2*mp.quad(lambda t: mp.mpf(p(t))**k,[0,mp.mpf('0.10'),mp.mpf('0.25'),mp.mpf('0.5')])
    den=2*mp.quad(lambda t: mp.mpf(q(t))**k,[0,mp.mpf('0.10'),mp.mpf('0.25'),mp.mpf('0.5')])
    scaled=num/den/(mp.mpf(5)/8)**k
    assert abs(scaled-mp.sqrt(5)/2)<mp.mpf('0.04')
    print('triangle flower k',k,'scaled',mp.nstr(scaled,18))
print('All symbolic and numerical checks passed.')
