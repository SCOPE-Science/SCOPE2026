#!/usr/bin/env python3
"""Reproduce finite-dimensional calculations for the selective-reset two-Brownian model.
The analytical tail theorem requires the proof in RESULT.md, not this finite test.
Dependencies: Python 3, NumPy, SciPy. No network access required.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

checks = 0

def close(a,b,tol=2e-10):
    global checks
    assert np.allclose(a,b,atol=tol,rtol=tol), (a,b)
    checks += 1

def A_matrix(g):
    return np.array([[-1.,1.],[1./g,-1./g]])

def propagator(g,t):
    lam=1+1/g
    e=math.exp(-lam*t)
    return np.array([[(1+g*e)/(1+g),g*(1-e)/(1+g)],
                     [(1-e)/(1+g),(g+e)/(1+g)]])

def vx(g,t):
    lam=1+1/g
    return (g*g*(-math.expm1(-2*lam*t))+2*(g+1)*t)/(g+1)**2

def vq(g,t):
    lam=1+1/g
    return (-math.expm1(-2*lam*t)+2*(g+1)*t)/(g+1)**2

def a(g,t):
    return (g+math.exp(-(1+1/g)*t))/(g+1)

def h(g,t):
    return g*(1-math.exp(-(1+1/g)*t))/(g+1)

for g in [0.25, 0.5, 1., 2., 8.]:
    A=A_matrix(g)
    sig=np.diag([2.,2./g])
    for t in [0.03,0.3,1.,2.2,10.]:
        close(propagator(g,t),expm(A*t))
        close(propagator(g,t)[0,1],h(g,t))
        close(propagator(g,t)[1,1],a(g,t))
        def cov(z):
            E=expm(A*z)
            return E@sig@E.T
        nu_x=quad(lambda z:cov(z)[0,0],0,t,epsabs=1e-10)[0]
        nu_q=quad(lambda z:cov(z)[1,1],0,t,epsabs=1e-10)[0]
        close(vx(g,t),nu_x,5e-9)
        close(vq(g,t),nu_q,5e-9)

# Exact stationary covariance via the linear Ito/Poisson-moment equations.
for g in [0.25,0.5,1.,2.,8.]:
  for r in [0.25, 1., 2., 5.]:
    M=np.array([[2+r,-2,0],[-1/g,1+1/g+r,-1],[0,-2/g,2/g]])
    b=np.array([2.,0.,2./g])
    xx,xq,qq=np.linalg.solve(M,b)
    paper=4*(g*(r+1)+1)/(g*(2*r+4)*r+2*r)
    close(xx,paper)
    # The stationary bath state Q is an affine random recursion with an
    # independent Exp(r) duration. Its variance is E[U(T)]/(1-E[a(T)^2]).
    Ea2 = (g*g+2*g*r/(r+1+1/g)+r/(r+2*(1+1/g)))/(g+1)**2
    EU = ((1-r/(r+2*(1+1/g)))+2*(g+1)/r)/(g+1)**2
    close(qq,EU/(1-Ea2))
    # At an independent observation time, the age T is also Exp(r).
    Eh2 = (g/(g+1))**2*(1-2*r/(r+1+1/g)+r/(r+2*(1+1/g)))
    EVx = (g*g*(1-r/(r+2*(1+1/g)))+2*(g+1)/r)/(g+1)**2
    close(xx,Eh2*qq+EVx)
    kc=math.sqrt(r*(g+1))
    for factor in [0.75,1.,1.25]:
        k=kc*factor
        # The exponent in the last-reset Gaussian integral is asymptotic
        # to (k^2/(1+g)-r)*T, and changes sign precisely at k=kc.
        slope=k*k/(g+1)-r
        close(slope,r*(factor*factor-1),5e-12)
        # Compare exact and asymptotic slope between two long ages.
        for vv in [vx,vq]:
            logw=lambda t:-r*t+0.5*k*k*vv(g,t)
            close((logw(800)-logw(400))/400,slope,5e-8)

# One exact rational witness: g=1, r=2.
close(vx(1,1),1.25-math.exp(-4)/4)
close(vq(1,1),vx(1,1))
close(math.sqrt(2*(1+1)),2.)
M=np.array([[4.,-2.,0.],[-1.,4.,-1.],[0.,-2.,2.]])
close(np.linalg.solve(M,np.array([2.,0.,2.])),[0.8,0.6,1.6])

# Lower-tail variational cost of an unreset Gaussian excursion:
# minimize r*t + x^2/(2V(t)). Its ratio to x tends to sqrt(r(g+1)).
for g,r in [(0.5,2.),(1.,2.),(5.,0.5)]:
  kc=math.sqrt(r*(1+g))
  for x in [100.,300.,1000.]:
    for v in [vx,vq]:
      opt=minimize_scalar(lambda t:r*t+x*x/(2*v(g,t)),bounds=(x*0.05,x*30),method='bounded',options={'xatol':1e-8})
      assert opt.success
      assert abs(opt.fun/x-kc)<0.045, (g,r,x,opt.fun/x,kc)
      checks+=1

print(f'PASS: {checks} deterministic checks; exact stationary g=1,r=2 variances (X,Q)=(4/5,8/5), mgf cutoff 2.')
