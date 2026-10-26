#!/usr/bin/env python3
"""Analytic identities and finite-dimensional cross-checks for hemispherical affine projection."""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, ndtr

mu = math.sqrt(2/math.pi)
v = 1-mu*mu
m4 = 3-2*mu**2-3*mu**4
C = v-m4/6
u0 = Fraction(7, 11)
P_lower = -Fraction(3,2)+Fraction(10,3)*u0-Fraction(3,2)*u0*u0
assert P_lower == Fraction(5,363)
assert C > 2*v*v, (C, 2*v*v)

def moments(d):
    m=math.exp(gammaln(d/2)-gammaln((d+1)/2)-0.5*math.log(math.pi))
    return m, 1-d*m*m

def fprofile(t):
    s=math.sqrt(max(0,1-t*t)); q=t/v
    def conditional(r):
        h=q*(r-mu)
        if s < 1e-14:
            return abs(h)
        x=h/s
        return s*mu*math.exp(-0.5*x*x)+h*(2*ndtr(x)-1)
    return quad(lambda r: mu*math.exp(-r*r/2)*conditional(r),0,11,epsabs=1e-11)[0]

fgrid=np.array([fprofile(float(t)) for t in np.linspace(0,1,81)])
assert np.all(np.diff(fgrid)>0)

# Check leading constant independently against half-normal tail formula.
phi=math.exp(-mu*mu/2)/math.sqrt(2*math.pi)
tail=1-ndtr(mu)
mad=4*(phi-mu*tail)
assert abs(mad/v-fgrid[-1])<2e-10

# Verify the exactly normalized spherical-coordinate law and pole rows via 1D integration.
# r = sqrt(d)*Y_d, with density 2 Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2)*sqrt(d))
# times (1-r^2/d)^((d-3)/2).
def pole_row(d):
    m,vd=moments(d)
    md=math.sqrt(d)*m
    pref=math.exp(math.log(2)+gammaln(d/2)-gammaln((d-1)/2)-0.5*math.log(math.pi)-0.5*math.log(d))
    def integrand(r):
        dens=pref*math.exp(0.5*(d-3)*math.log1p(-r*r/d)) if r*r<d else 0.0
        kernel=1/math.sqrt(d)+(1-m)*(r-md)/vd
        return abs(kernel)*dens
    return quad(integrand,0, min(11,math.sqrt(d)),epsabs=3e-9,limit=300)[0]

for d in (4,12,64,256,1024,4096):
    p = pole_row(d)
    assert math.isfinite(p)
    assert abs(p-mad/v)< 1.3, (d,p)
    print('d',d,'pole norm/sqrt(d)',format(p,'.9f'))
assert abs(pole_row(4096)-mad/v)<0.025

# Verify exact affine kernel reproduces constants and coordinates under a random spherical draw.
# This finite check is diagnostic; infinite claims rely on the analytic proof.
rng=np.random.default_rng(240917)
for d in (4,8,25):
    m,vd=moments(d)
    X=rng.standard_normal((180000,d))
    X /= np.linalg.norm(X,axis=1,keepdims=True)
    X[:,-1]=abs(X[:,-1])
    t=0.4
    a=np.zeros(d); a[0]=math.sqrt(1-t*t); a[-1]=t
    K=1+d*(X[:,:-1]@a[:-1])+(t-m)*(X[:,-1]-m)*d/vd
    assert abs(np.mean(K)-1)<0.055,(d,np.mean(K))
    for idx in (0,d-1):
        assert abs(np.mean(K*X[:,idx])-a[idx])<0.045,(d,idx,np.mean(K*X[:,idx]),a[idx])
print('analytic gap C-2v^2:',format(C-2*v*v,'.12f'))
print('limit constant:',format(mad/v,'.12f'))
print('all checks passed')
