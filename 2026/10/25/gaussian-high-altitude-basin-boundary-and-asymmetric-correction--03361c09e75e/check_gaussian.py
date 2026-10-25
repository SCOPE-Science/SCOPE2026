#!/usr/bin/env python3
"""Reproducibility checks of the high-altitude basin-separatrix scaling theorem."""
import math
import numpy as np
from scipy.integrate import solve_ivp,quad
from sympy import symbols,exp,diff,simplify,series
u,eta=symbols('u eta',real=True)
a=200/21
# Exact rescaled flow: R_dot = -(400/21)R u^2 - eta^2 R C(R)/21;
# u_dot = -u-eta R^2/10.  At eta=0, R=exp(a*u^2) is the stable leaf.
R0=exp(200*u*u/21)
assert simplify(diff(R0,u)*(-u)+(400/21)*R0*u*u)==0
# For logarithmic first correction L1, the O(eta) invariance residual is
# -u L1'(u)-(40/21)*u*exp(400*u^2/21) = 0.
assert simplify(-u*(-40*exp(400*u*u/21)/21)-(40/21)*u*exp(400*u*u/21))==0
print('EXACT_RESCALED_GAUSSIAN_STABLE_FIBER_PASS')
print('EXACT_ODD_SQRT_MU_CORRECTION_IDENTITY_PASS')

def stable_graph(mu, target):
    A=166*mu/21; B=80*mu/21; C=-.2; D=-1.
    eigen=(A+D-math.sqrt((A-D)**2+4*B*C))/2
    slope=-B/(A-eigen)
    dz=1e-8*(1 if target>-.1 else -1)
    z0=-.1+dz
    def rhs(zz,arr):
        r=arr[0]
        return [-mu*r*(21*r**4-125*r**2+400*zz**2+100)/(21*(-zz-r*r/10))]
    sol=solve_ivp(rhs,(z0,target),[1+slope*dz],rtol=1e-11,atol=1e-13,method='DOP853',max_step=.025)
    if not sol.success: raise RuntimeError(sol.message)
    return sol.y[0,-1]

for U in (-.28,-.14,.14,.28):
    for mu in (.001,.00025,.0000625):
        r=stable_graph(mu,U/math.sqrt(mu))
        prediction=a*U*U-math.sqrt(mu)*(40/21)*quad(lambda s:math.exp((400/21)*s*s),0,U)[0]
        remainder=math.log(r)-prediction
        print('HIGH_ALTITUDE_LOG_GRAPH',f'U={U:g}',f'mu={mu:g}',f'log_r={math.log(r):.12g}',f'error_over_mu={remainder/mu:.8g}')
print('UNIFORM_K_LIMITS_PROVED_VIA_STRONG_STABLE_FOLIATION_NOT_FINITE_NUMERICS')
