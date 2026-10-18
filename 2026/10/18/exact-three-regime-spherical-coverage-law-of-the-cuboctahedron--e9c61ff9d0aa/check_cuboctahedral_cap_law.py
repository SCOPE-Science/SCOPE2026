#!/usr/bin/env python3
"""Reproducibility checks for a cuboctahedral spherical-cap union law.

Requires numpy, scipy, mpmath. Finite sampling confirms, but does not prove,
the analytic spherical inclusion-exclusion identity.
"""
from itertools import combinations
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc
import mpmath as mp

P = []
for zero in range(3):
    others = [j for j in range(3) if j != zero]
    for s in (-1, 1):
        for t in (-1, 1):
            v = [0, 0, 0]
            v[others[0]], v[others[1]] = s, t
            P.append(tuple(v))
assert len(P) == 12 and len(set(P)) == 12
E = {frozenset((i, j)) for i, j in combinations(range(12), 2)
     if sum(P[i][k]*P[j][k] for k in range(3)) == 1}
TRI = [ids for ids in combinations(range(12), 3)
       if all(frozenset(pair) in E for pair in combinations(ids, 2))]
assert len(E) == 24 and len(TRI) == 8
assert not any(all(frozenset(pair) in E for pair in combinations(ids, 2))
               for ids in combinations(range(12), 4))
assert all(sum(P[i][k]*P[j][k] for k in range(3)) <= 0
           for i, j in combinations(range(12), 2)
           if frozenset((i,j)) not in E)
V = np.asarray(P, dtype=float)/math.sqrt(2)
a, b, c = math.pi/6, math.acos(math.sqrt(2/3)), math.pi/4
eta = math.acos(1/3)

def beta(t):
    return math.acos(max(-1.0, min(1.0, 1/(math.sqrt(3)*math.tan(t)))))

def gamma(t):
    q = (0.5-math.cos(t)**2)/(math.sin(t)**2)
    return math.acos(max(-1.0,min(1.0,q)))

def lens(t):
    return 0.0 if t<=a else 2*math.pi-2*gamma(t)-4*beta(t)*math.cos(t)

def triple(t):
    return 0.0 if t<=b else 2*math.pi-3*gamma(t)-3*(2*beta(t)-eta)*math.cos(t)

def cdf(t):
    if t <= 0: return 0.0
    if t >= c: return 1.0
    return 6*(1-math.cos(t))-6*lens(t)/math.pi+2*triple(t)/math.pi

# Check the lens independently by polar spherical-area integration.
alpha = math.pi/3
for radius in (a+.035, b-.018, b+.035, c-.025):
    def phi_width(theta):
        if theta<=0: return 0
        q=(math.cos(radius)-math.cos(alpha)*math.cos(theta))/(math.sin(alpha)*math.sin(theta))
        if q>=1: return 0
        if q<=-1: return 2*math.pi
        return 2*math.acos(q)
    val,err=quad(lambda theta: phi_width(theta)*math.sin(theta),0,radius,
                 epsabs=3e-11,limit=400,points=[abs(alpha-radius)])
    assert abs(val-lens(radius))<2e-8, (radius, val, lens(radius),err)

# A digital-net quadrature independent of the inclusion-exclusion formula.
M=2**18
sample=qmc.Sobol(d=2,scramble=True,seed=674231).random_base2(m=18)
z=2*sample[:,0]-1
ang=2*math.pi*sample[:,1]
rho=np.sqrt(1-z*z)
U=np.column_stack((rho*np.cos(ang),rho*np.sin(ang),z))
nearest=np.max(U@V.T,axis=1)
for t in (0.24,0.43,a,b-.03,b,b+.03,0.67,0.72,0.765,c):
    approx=np.mean(nearest>=math.cos(t))
    assert abs(approx-cdf(t))<0.0015,(t,approx,cdf(t))

# High-precision singularity coefficients; note severe cancellation of
# spherical areas requires higher precision than machine floats.
mp.mp.dps=80
pi=mp.pi
am=pi/6
bm=mp.acos(mp.sqrt(mp.mpf(2)/3))
cm=pi/4
eta_m=mp.acos(mp.mpf(1)/3)

def terms(t):
    be=mp.acos(1/(mp.sqrt(3)*mp.tan(t)))
    ga=mp.acos((mp.mpf('.5')-mp.cos(t)**2)/mp.sin(t)**2)
    L=2*pi-2*ga-4*be*mp.cos(t)
    T=2*pi-3*ga-3*(2*be-eta_m)*mp.cos(t)
    return L,T
for eps in (mp.mpf('1e-4'),mp.mpf('1e-5')):
    T=terms(bm+eps)[1]
    assert abs(T/eps**2-3*mp.sqrt(3))<mp.mpf('.01')
    t=cm-eps
    L,T=terms(t)
    tail=1-6*(1-mp.cos(t))+6*L/pi-2*T/pi
    assert abs(tail/eps**2-6/pi-(2/pi)*eps)<mp.mpf('1e-6')
print('CUBOCTAHEDRAL_SPHERICAL_CDF_OK vertices=12 edges=24 triangles=8 sample=262144')
print('thresholds =',a,b,c)
print('cdf(a),cdf(b),cdf(c) =',cdf(a),cdf(b),cdf(c))
