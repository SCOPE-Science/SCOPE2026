#!/usr/bin/env python3
"""Checks for exact planar random-descent convergence laws.

Requires Python 3 and SymPy. Analytical arguments are in RESULT.md; this
program checks symbolic identities, exact witnesses, and independent quadrature.
"""
import math
from fractions import Fraction
import sympy as sp

q,z,u = sp.symbols('q z u', positive=True, real=True)
R2 = 4*q*q*u*u / ((1-q*q)**2 + 4*q*q*u*u)
GQ = ((1+q*q)/2)**2
GA = (3+q*q+sp.sqrt(1+14*q*q+q**4))/8

# Exact trace / discriminant of the Gaussian moment transfer on {1,cos(2t)}.
K = sp.Matrix([[sp.Rational(1,2),q/2],[q/2,(1+q*q)/4]])
assert sp.factor(K.charpoly().as_expr()) == sp.factor(sp.symbols('lambda')**2 - (3+q*q)*sp.symbols('lambda')/4 + (1-q*q)/8)
assert sp.simplify(((3+q*q + sp.sqrt(1+14*q*q+q**4))/8)**2 - sp.trace(K)*GA + K.det()) == 0

# Positivity proving sign annealed rate exceeds Gaussian rate at aligned axes.
N = 1+17*z-z*z-z**3
assert sp.expand(N*N-(1+14*z+z*z)*(1+z)**4 - 16*z*(1-z)*(z**3+7*z**2+15*z+1)) == 0

# The all-angle quenched threshold has one interior algebraic zero.
P = q**5+q**4+4*q**3+4*q*q+7*q-1
assert sp.expand((q-1)*P-((1+q*q)**3-8*q)) == 0
assert sp.diff(P,q).subs(q,0)>0
assert P.subs(q,0)==-1 and P.subs(q,1)>0

# Exact conflict example with H=diag(121,81) and independent fair signs.
qx = sp.Rational(1,10)
rx = sp.Rational(20,101)
sgn_typical = rx
gau_typical = GQ.subs(q,qx)
sgn_mean = (1+rx*rx)/2
gau_mean = GA.subs(q,qx)
assert sgn_typical < gau_typical
assert sgn_mean > sp.Rational(51,100)
assert gau_mean < sp.Rational(51,100)

# Verify Gaussian angular Poisson-kernel Fourier moments numerically.
# f(t)=(1-q^2)/(2pi*(1-2q*cos(2t)+q^2)) on [0,2pi).
for qv in (0.02,0.1,0.45,0.8):
    n=8192
    vals=[]
    for j in range(n):
        t=2*math.pi*(j+0.5)/n
        wt=(1-qv*qv)/(1-2*qv*math.cos(2*t)+qv*qv)
        vals.append((t,wt))
    for k in (0,1,2,3):
        est=sum(w*math.cos(2*k*t) for t,w in vals)/n
        assert abs(est-qv**k)<2e-11,(qv,k,est)
    # Fourier representation of the double-angle log integral.  The
    # independent expectation of cos(2k(t-s)) equals q^(2k).
    trunc=-2*math.log(2)+2*sum((-1)**(k+1)*qv**(2*k)/k for k in range(1,150))
    target=2*math.log((1+qv*qv)/2)
    assert abs(trunc-target)<1e-11,(qv,trunc,target)

# Direct transfer operator Gram moment comparison at finite time.
for qv in (0.1,0.35,0.7):
    # Discretized angular transfer T_{ij} = p_j*cos^2(t_i-t_j).
    # Power iteration from 1 approximates top eigenvalue.
    m=512
    t=[math.pi*(j+.5)/m for j in range(m)]
    p=[(1-qv*qv)/(1-2*qv*math.cos(2*s)+qv*qv)/m for s in t]
    v=[1.0]*m
    ratios=[]
    for _ in range(38):
        s0=sum(p[j]*v[j] for j in range(m))
        sc=sum(p[j]*v[j]*math.cos(2*t[j]) for j in range(m))
        ss=sum(p[j]*v[j]*math.sin(2*t[j]) for j in range(m))
        nv=[.5*(s0+math.cos(2*t[i])*sc+math.sin(2*t[i])*ss) for i in range(m)]
        ratio=sum(p[i]*nv[i] for i in range(m))/sum(p[i]*v[i] for i in range(m))
        ratios.append(ratio)
        v=[x/max(nv) for x in nv]
    target=(3+qv*qv+math.sqrt(1+14*qv*qv+qv**4))/8
    assert abs(ratios[-1]-target)<2e-8,(qv,ratios[-1],target)

print('VERIFY_OK: symbolic identities, exact conflict, Fourier moments, transfer eigenvalues')
