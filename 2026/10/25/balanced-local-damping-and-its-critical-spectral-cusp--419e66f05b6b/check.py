#!/usr/bin/env python3
"""Finite diagnostics for a two-oscillator damping-allocation theorem.
Run: python3 check.py. Requires numpy and sympy."""
import math
import numpy as np
import sympy as sp

s,a,b,G,d,z=sp.symbols('s a b G d z', real=True)
F1=s*s+G*s/2+a
F2=F1+2*b
P=sp.expand(F1*F2-d*d*s*s)
p2=sp.expand((s*s+G*s/2+a+b)**2-b*b-d*d*s*s)
assert sp.simplify(P-p2)==0
assert sp.simplify(P.subs(d,0)-F1*F2)==0
poly=sp.Poly(P,s)
assert [sp.simplify(v) for v in poly.all_coeffs()]==[1,G,2*(a+b)+G*G/4-d*d,G*(a+b),a*(a+2*b)]
shift=sp.Poly(sp.expand(P.subs(s,z-G/4)),z)
assert sp.simplify(shift.coeff_monomial(z)-G*d*d/2)==0
assert sp.simplify(P.subs(s,0)-a*(a+2*b))==0
assert sp.simplify(P.subs(s,-sp.sqrt(a)).subs(G,4*sp.sqrt(a))+a*d*d)==0
print('6 exact symbolic checks passed')

def roots(a,b,G,d):
    coeff=[1,G,2*(a+b)+G*G/4-d*d,G*(a+b),a*(a+2*b)]
    return np.roots(coeff)

def alpha(a,b,G,d):return float(max(t.real for t in roots(a,b,G,d)))

def opt(a,G):
    return -G/4+math.sqrt(max(0,G*G/16-a))

rng=np.random.default_rng(4127)
count=0
for _ in range(1200):
    aa=float(np.exp(rng.uniform(-1.8,2.0)))
    bb=float(np.exp(rng.uniform(-1.8,2.0)))
    GG=4*math.sqrt(aa)*float(np.exp(rng.uniform(-1.4,1.4)))
    dd=float(rng.uniform(-.5,.5)*GG)
    z0=alpha(aa,bb,GG,0)
    z1=alpha(aa,bb,GG,dd)
    assert abs(z0-opt(aa,GG))<1e-6*max(1,GG)
    assert z1 > z0 - 1e-7*max(1,GG)
    assert z1 < 1e-7
    count+=1
print(count,'random-allocation spectral comparisons passed')

for aa,bb,fac in [(1.,.6,.7), (1.,.6,1.),(1.,.6,1.45), (2.,1.2,.7),(2.,1.2,1.),(2.,1.2,1.45),(.7,3.,.8),(.7,3.,1.5)]:
    GG=4*math.sqrt(aa)*fac
    eps=.002*min(1.,bb,math.sqrt(aa))
    delta=alpha(aa,bb,GG,eps)-alpha(aa,bb,GG,0)
    if fac<1:
        predicted=GG*eps**2/(8*bb)
    elif fac==1:
        predicted=math.sqrt(aa/(2*bb))*eps
    else:
        r=GG/4-math.sqrt(GG**2/16-aa)
        S=math.sqrt(GG**2/4-4*aa)
        predicted=r*r*eps*eps/(2*bb*S)
    assert predicted>0 and abs(delta/predicted-1)<0.04,(aa,bb,fac,delta,predicted)
print('8 small-imbalance asymptotic comparisons passed')
print('All checks passed')
