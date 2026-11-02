"""Symbolic/algebraic and numerical checks for a two-power Wien mixture.

Run: python verify.py
Only finite diagnostic assertions are made; the analytical proof supplies universality.
"""
import math
import sympy as sp
import numpy as np
from scipy.optimize import brentq

x,r = sp.symbols('x r', positive=True)
A,B=sp.symbols('A B', positive=True)
S = A*x**3*sp.exp(-x)+B*x**4*sp.exp(-x/r)
R = r*sp.exp(-(r-1)*x/r)*(x-3)/(x*(4*r-x))
H=1/(x-3)-1/x+1/(4*r-x)-(r-1)/r
H_x=sp.diff(H,x)
H_xx=sp.diff(H_x,x)
N=sp.together(H).as_numer_denom()[0]
P=28*r**4-120*r**3+168*r**2-92*r+15
assert sp.simplify(sp.diff(S,x)-x**3*sp.exp(-x/r)*(4-x/r)*(B-A*R))==0
assert sp.simplify(sp.diff(sp.log(R),x)-H)==0
assert sp.simplify(H_xx-(2/(x-3)**3-2/x**3+2/(4*r-x)**3))==0
res=sp.factor(sp.resultant(N,sp.diff(N,x),x))
assert res==sp.factor(-12*r**2*(r-1)*(4*r-3)**2*P)
t=sp.symbols('t')
assert sp.expand(P.subs(r,t+1))==28*t**4-8*t**3-24*t**2-4*t-1

rf=lambda xx,rr:rr*math.exp(-(rr-1)*xx/rr)*(xx-3)/(xx*(4*rr-xx))
hf=lambda xx,rr:1/(xx-3)-1/xx+1/(4*rr-xx)-(rr-1)/rr
hxf=lambda xx,rr:-1/(xx-3)**2+1/xx**2+1/(4*rr-xx)**2
rcrit=brentq(sp.lambdify(r,P,'math'),2.15,2.16,xtol=1e-14)
xcrit=brentq(lambda z:hxf(z,rcrit),3.001,4*rcrit-0.001,xtol=1e-14)
assert abs(hf(xcrit,rcrit))<1e-12
assert 2.15664080873<rcrit<2.15664080874
assert 5.63959482745<xcrit<5.63959482747
assert 0.0164160<rf(xcrit,rcrit)<0.0164161
kappa=1/rcrit**2+4/(4*rcrit-xcrit)**2
curvature=2/(xcrit-3)**3-2/xcrit**3+2/(4*rcrit-xcrit)**3
K=4*kappa/3*math.sqrt(2*kappa/curvature)
assert abs(K-2.4517450659)<1e-8

def turning_points(rr):
    if rr<=rcrit: return []
    mid=brentq(lambda z:hxf(z,rr),3+1e-10,4*rr-1e-10)
    assert hf(mid,rr)<0
    return [brentq(lambda z:hf(z,rr),3+1e-10,mid),
            brentq(lambda z:hf(z,rr),mid,4*rr-1e-10)]

def modes(rr,lam):
    # Solve the actual derivative after removing the strictly positive x**2.
    # Using finite endpoint values also handles extremely unbalanced mixtures.
    def reduced_gradient(z):
        return math.exp(-z)*(3-z)+lam*z*math.exp(-z/rr)*(4-z/rr)
    xs=[3.0,*turning_points(rr),4*rr]
    roots=[]
    for lo,hi in zip(xs[:-1],xs[1:]):
        if reduced_gradient(lo)*reduced_gradient(hi)<0:
            roots.append(brentq(reduced_gradient,lo,hi,xtol=2e-14))
    return roots

checks=5
for rr in [1.05,1.4,2.0,2.15,2.16,2.2,2.5,3.,4.,7.]:
    for lam in [1e-5,0.001,0.01,0.1,1.,3.]:
        rrts=modes(rr,lam)
        assert len(rrts) in (1,3)
        for v in rrts:
            grad = float(sp.diff(S,x).subs({A:1,B:lam,x:v,r:rr}).evalf())
            assert abs(grad)<1e-7*max(1,lam)
            eps=min(1e-5,0.1*(v-3),0.1*(4*rr-v))
            # Simple root changes sign; three-root case alternates maximum/minimum.
            gradient_left=math.exp(-(v-eps))*(3-(v-eps))+lam*(v-eps)*math.exp(-(v-eps)/rr)*(4-(v-eps)/rr)
            gradient_right=math.exp(-(v+eps))*(3-(v+eps))+lam*(v+eps)*math.exp(-(v+eps)/rr)*(4-(v+eps)/rr)
            assert gradient_left*gradient_right<0
        if rr<rcrit: assert len(rrts)==1
        checks+=1
    if rr>rcrit:
        lo,hi=turning_points(rr)
        low,high=rf(hi,rr),rf(lo,rr)
        assert low<high
        assert len(modes(rr,math.sqrt(low*high)))==3
        assert len(modes(rr,low/2))==1
        assert len(modes(rr,high*2))==1
        checks+=3

# Global cusp scaling; use two not-too-tiny perturbations to avoid cancellation.
for eps in [1e-3,1e-4]:
    rr=rcrit+eps
    roots=turning_points(rr)
    ratio=rf(roots[0],rr)/rf(roots[1],rr)
    empirical=math.log(ratio)/eps**1.5
    assert abs(empirical-K)/K < 0.005
    checks+=1

print('PASS: symbolic identities, quartic and critical root, phase-diagram sampling, cusp law')
print('checks',checks,'rcrit',format(rcrit,'.15f'),'xcrit',format(xcrit,'.15f'),'critical_weight_ratio',format(rf(xcrit,rcrit),'.12f'),'cusp_constant',format(K,'.10f'))
