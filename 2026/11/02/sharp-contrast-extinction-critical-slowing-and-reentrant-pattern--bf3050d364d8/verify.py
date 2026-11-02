#!/usr/bin/env python3
"""Reproduce exact functional identities and numerical diagnostics for the logistic threshold-response network."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

def F(z): return 1/(1+np.exp(-z))

def delta(W):return max(0.5*np.sum(np.abs(W[i]-W[j])) for i in range(len(W)) for j in range(len(W)))

def right(x,W,beta,theta):return -x+F(theta+beta*(W@x))

def h(v):return (1-v*v)*np.arctanh(v)/v

def root(k):return brentq(lambda v:np.tanh(k*v)-v,0.0001,0.9999999999) if k>1 else 0.0

# Exact algebra in sympy and rational samples.
import sympy as sp
z,t,be,de=sp.symbols('z t be de',real=True)
S=lambda v:1/(1+sp.exp(-v))
assert sp.simplify(S(z)+S(-z)-1)==0
assert sp.simplify(((2*S(z)-1)-sp.tanh(z/2)).rewrite(sp.exp))==0
assert sp.limit((sp.tanh(t)-t)/t**3,t,0)==-sp.Rational(1,3)

rng=np.random.default_rng(260910)
for N in [2,3,5,8]:
    for _ in range(100):
        W=rng.uniform(0.001,1,size=(N,N));W=W/W.sum(axis=1,keepdims=True)
        x=rng.uniform(0,1,size=N)
        b=float(rng.uniform(0,12));theta=float(rng.uniform(-6,2))
        d=x.max()-x.min();D=delta(W)
        i=int(np.argmax(x));j=int(np.argmin(x))
        # For unique extrema the diameter derivative is the difference of vector-field entries.
        actual=right(x,W,b,theta)[i]-right(x,W,b,theta)[j]
        bound=-d+np.tanh(b*D*d/4)
        assert actual<=bound+1e-11,(N,actual,bound)
        assert np.ptp(W@x)<=D*d+1e-12

# Stable and saddle pair exact Jacobian spectra.
for dval in [0.1,0.25,0.5,0.9,1.0]:
    W=np.array([[(1+dval)/2,(1-dval)/2],[(1-dval)/2,(1+dval)/2]])
    for k in [1.01,1.3,2.5,5]:
        beta=4*k/dval;v=root(k)
        x=np.array([(1+v)/2,(1-v)/2])
        res=right(x,W,beta,-beta/2)
        assert np.max(abs(res))<1e-11
        q=beta*(1-v*v)/4
        J=-np.eye(2)+q*W
        lam=np.sort(np.linalg.eigvals(J).real)
        expected=np.sort(np.array([-1+q,-1+q*dval]))
        assert np.max(abs(lam-expected))<2e-12

for dval in [0.1,0.25,0.5,0.9]:
    vs=brentq(lambda v:h(v)-dval,1e-10,0.9999999999)
    beta_star=4/(1-vs*vs)
    assert beta_star>4/dval
    for frac,stable in [((1+4/dval/beta_star)/2,False),(1.02,True)]:
        beta=beta_star*frac
        assert beta*dval>4
        v=root(beta*dval/4)
        common=-1+beta*(1-v*v)/4
        assert (common<0)==stable
    print('delta',dval,'v_stability',vs,'beta_stability',beta_star)

# At beta*delta=4, the two-node symmetric invariant line realizes the t^{-1/2} envelope.
Dval=0.5;beta=4/Dval;W=np.array([[(1+Dval)/2,(1-Dval)/2],[(1-Dval)/2,(1+Dval)/2]])
def dv(t,y):return [-y[0]+math.tanh(y[0])]
sol=solve_ivp(dv,(0,500000),[0.7],rtol=1e-11,atol=1e-14,dense_output=True,max_step=1000)
for time in [1000,5000,20000,100000,500000]:
    v=float(sol.sol(time)[0]); print('critical_t',time,'t*v**2',time*v*v)
assert abs(500000*float(sol.y[0,-1])**2-1.5)<0.01
print('all symbolic and numerical diagnostics passed')
