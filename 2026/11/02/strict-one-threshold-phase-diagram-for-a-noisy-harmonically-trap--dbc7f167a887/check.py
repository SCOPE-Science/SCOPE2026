#!/usr/bin/env python3
"""Independent numerical diagnostics for the Gaussian-smoothed symmetric beta profile."""
import numpy as np
from scipy.integrate import quad
from scipy.special import hyp1f1, roots_jacobi
from scipy.optimize import brentq

def curvature(h,z):
    return hyp1f1(.5,h+.5,-z)-z/(h+.5)*hyp1f1(1.5,h+1.5,-z)

def root(h):
    lo=.01; hi=2.
    while curvature(h,hi)>0: hi*=2
    return brentq(lambda z:curvature(h,z),lo,hi,xtol=1e-12)

def derivative(h,z,x):
    # Gauss-Jacobi integral, weight (1-u^2)^(h-1).
    uu,ww=roots_jacobi(200,h-1,h-1)
    vv=-(x-uu)*np.exp(-z*(x-uu)**2)
    return float(np.dot(ww,vv))

hs=[.1,.25,.5,.75,.9]
zs=[root(h) for h in hs]
assert all(a<b for a,b in zip(zs,zs[1:]))
for h,z0 in zip(hs,zs):
    assert curvature(h,z0*.8)>0 and curvature(h,z0*1.2)<0
    for z in [z0*.5,z0*1.5]:
        xs=np.linspace(.002,2.5,700)
        ds=np.array([derivative(h,z,x) for x in xs])
        changes=np.sum(ds[:-1]*ds[1:]<0)
        assert changes==(1 if z>z0 else 0), (h,z,changes)
    print('h=%g, critical_z=%.12g, critical_noise_variance=%.12g'%(h,z0,1/(2*z0)))
print('PASS: 5 thresholds, 10 global derivative sign-change scans, strict monotonicity')
