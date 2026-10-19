#!/usr/bin/env python3
"""Reproducible corroboration of a fixed-stepsize scalar noise-control theorem."""
import math
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import minimize_scalar

def variance(h, beta):
    assert -1 < beta < 1 and 0 < h < 2*(1+beta)
    return (1+beta)/((1-beta)*h*(2*(1+beta)-h))

def beta_opt(a,b):
    return sorted([math.sqrt(a)-1, (a+b)/2-1, math.sqrt(b)-1])[1]

checks=0
for a in np.geomspace(.008,3.2,19):
    for b in np.linspace(a,3.95,17):
        if b<a:continue
        beta=beta_opt(a,b)
        lo=b/2-1
        assert lo<beta<1
        obj=lambda x:max(variance(a,x),variance(b,x))
        u=minimize_scalar(obj,bounds=(lo+1e-10,.99999999),method='bounded',options={'xatol':1e-12})
        # Numerical optimizers are less accurate at a nondifferentiable cusp.
        assert obj(beta)<=u.fun*(1+3e-8)+1e-8,(a,b,beta,u.x)
        checks+=1
        for h in np.linspace(a,b,7):
            assert variance(h,beta)<=obj(beta)*(1+5e-13)
            checks+=1
        for h in [a,b]:
            ar=np.array([[1+beta-h,-beta],[1.,0.]])
            q=np.array([[1.,0.],[0.,0.]])
            cov=solve_discrete_lyapunov(ar,q)
            assert abs(cov[0,0]/variance(h,beta)-1)<3e-9
            checks+=1
for c in [1.05,2,9,20]:
    for a in [1e-4,1e-6,1e-8]:
        b=c*a
        beta=beta_opt(a,b)
        assert beta<0
        assert abs(variance(a,0)/variance(a,beta)-(2-math.sqrt(a))**2/(2-a))<1e-8
        checks+=1
print('PASS',checks,'assertion families: closed-form robust optimizer, endpoint reduction, Lyapunov covariance, low-curvature ratio')
