"""Reproduce the identities and sample checks for the Alexander SDIRK2 star positivity theorem.

Requires Python 3, sympy, numpy. The proof in RESULT.md is independent of the finite checks.
"""
from math import sqrt, isclose
import random
import numpy as np
import sympy as sp

checks = 0

def check(ok, msg):
    global checks
    checks += 1
    if not bool(ok):
        raise AssertionError(msg)

q = sp.sqrt(2)
gamma = 1 - q/2
c = 1 - 2*gamma
t = (q-1)/2
w0 = 4 + 3*q
z0 = 3 + 2*q
x = sp.symbols('x', positive=True)
R = (1-c*x)/(1+gamma*x)**2
F = (1+gamma**2*x)/(1+gamma*x)**2

# Derive R from the exact Butcher tableau, not by assumption.
zsym = sp.symbols('zsym')
Am = sp.Matrix([[gamma, 0], [1-gamma, gamma]])
bm = sp.Matrix([[1-gamma, gamma]])
R_butcher = sp.factor(1 + zsym*(bm*(sp.eye(2)-zsym*Am).inv()*sp.ones(2,1))[0])
check(sp.simplify(R_butcher - (1+(1-2*gamma)*zsym)/(1-gamma*zsym)**2)==0,
      "Butcher stability function")
check(sp.simplify((1-R)/x-F)==0, "loss identity")
check(sp.simplify(sp.diff(F,x) - gamma*(gamma-2-gamma**2*x)/(1+gamma*x)**3)==0, "F derivative")
check(sp.simplify(sp.diff(R,x) - (-1+gamma*c*x)/(1+gamma*x)**3)==0, "R derivative")
check(sp.simplify(w0 - 1/(gamma*c))==0, "unique minimizer")
check(sp.simplify(R.subs(x,w0)+t)==0, "minimum")
check(sp.simplify(z0-1-1/t)==0, "critical ratio")

delta = sp.simplify(1-4*t +(R.subs(x,z0*w0)-1)/z0)
check(sp.simplify(delta-(297-211*q)/98)==0, "negative leaf certificate")
check(2*211**2 > 297**2, "negative exact sign")
for m in (2,3,4):
    check(sp.simplify(1-m*t)>0, "balanced lower bound sign")
    check(sp.simplify(m*(1-m*t)/(m+1) -(1+(m-1)*(-t)+(-t-1)/(m+1)))==0,
          "balanced leaf lower bound")
for m in range(5,101):
    check(sp.simplify(delta-(m-5)*t)<0, "unavoidable leaf negativity")

rng = random.Random(1827)
num_cases=0
for m in range(2,16):
    for k in range(30):
        u=10**rng.uniform(-1.7,1.7)
        v=10**rng.uniform(-1.7,1.7)
        h=10**rng.uniform(-4,4)
        z=1+m*v/u
        w=u*h
        Q=np.zeros((m+1,m+1))
        Q[0,0]=-m*v
        for j in range(1,m+1):
            Q[0,j]=v
            Q[j,0]=u
            Q[j,j]=-u
        B=np.linalg.solve(np.eye(m+1)-float(gamma)*h*Q,np.eye(m+1))
        P=(np.eye(m+1)+float(c)*h*Q)@(B@B)
        # Stage-by-stage application to every canonical initial state.
        stage1=B
        stage2=B@(np.eye(m+1)+(1-float(gamma))*h*Q@stage1)
        check(np.max(np.abs(P-stage2))<5e-9,"direct Butcher stages")
        def rr(s):
            return (1-float(c)*s)/(1+float(gamma)*s)**2
        rlow=rr(w); rhigh=rr(z*w)
        pi_h=1/z
        pi_l=(z-1)/(m*z)
        S=np.zeros_like(P)
        S[0,0]=pi_h+(1-pi_h)*rhigh
        S[0,1:]=pi_l*(1-rhigh)
        S[1:,0]=pi_h*(1-rhigh)
        for i in range(m):
            for j in range(m):
                S[i+1,j+1]=pi_l + (float(i==j)-1/m)*rlow + (1/m-pi_l)*rhigh
        check(np.max(np.abs(P-S))<5e-9,"exact spectral projector vs direct matrix RK")
        check(np.max(np.abs(P.sum(axis=1)-1))<5e-9,"row stochastic")
        check(np.min(P[np.logical_not(np.eye(m+1,dtype=bool))])>-5e-9,"off diagonal positivity")
        num_cases +=1

# Numerically replay the all-ratio witness choice, with strict gaps away from threshold.
for m in range(5,22):
    for v_over_u in (0.01,0.1,0.5,0.9,1.0,1.2,2.0,10.0):
        z=1+m*v_over_u
        if z<=float(z0):
            w=float(w0)
            leaf=(1+(m-1)*((1-float(c)*w)/(1+float(gamma)*w)**2)
                     +(((1-float(c)*z*w)/(1+float(gamma)*z*w)**2)-1)/z)/m
            check(leaf<-1e-6,"leaf witness")
        else:
            high=float(w0)
            hub=(1+(z-1)*((1-float(c)*high)/(1+float(gamma)*high)**2))/z
            check(hub<-1e-6,"hub witness")

# For the symmetric cases, every h>=0 is safe by proof; sample the full range.
for m in range(2,5):
    z=m+1
    for h in np.geomspace(1e-7,1e7,300):
        lo=(1-float(c)*h)/(1+float(gamma)*h)**2
        hi=(1-float(c)*z*h)/(1+float(gamma)*z*h)**2
        hub=(1+m*hi)/z
        leaf=(1+(m-1)*lo+(hi-1)/z)/m
        off=h/m * ((1+float(gamma)**2*h)/(1+float(gamma)*h)**2 - (1+float(gamma)**2*z*h)/(1+float(gamma)*z*h)**2)
        check(hub>0 and leaf>0 and off>0,"balanced positivity")

print(f"VERIFY_OK assertions={checks} direct_RK_cases={num_cases}")
