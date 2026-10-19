#!/usr/bin/env python3
"""Standalone numerical/algebraic checks for the finite-state opinion equation.
All tests are finite consistency checks; the proof is analytical.
"""
from math import tanh,exp,log,sqrt
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

def exp_family(k,t):
    j=np.arange(-k,k+1,dtype=float)
    z=np.exp(t*(j-k))
    return j,z/z.sum()

def equation(k,eps,p):
    j=np.arange(-k,k+1,dtype=float)
    m=np.dot(j,p)
    up=(1+eps+m/k)/2
    down=(1+eps-m/k)/2
    flux=up*p[:-1]-down*p[1:]
    out=np.zeros_like(p)
    out[:-1]-=flux
    out[1:]+=flux
    return out

def energy(k,eps,p):
    j=np.arange(-k,k+1,dtype=float)
    m=np.dot(j,p)
    v=m/(k*(1+eps))
    phi=2*m*np.arctanh(v)+k*(1+eps)*np.log1p(-v*v)
    return sum(x*np.log(x) for x in p if x>0)-phi

def tests():
    n=0
    for k in range(1,10):
        var=k*(k+1)/3
        w=k*(k+1)*(4*k*(k+1)-3)/45
        assert w>0
        for t in [0.001,0.12,0.7,2.0,7.0]:
            j,p=exp_family(k,t)
            m=float(np.dot(j,p));second=float(np.dot(j*j,p))
            lhs=m/tanh(t/2)
            rhs=k*(k+1)-second
            assert abs(lhs-rhs)<2e-7*max(1,abs(rhs)),(k,t,lhs,rhs)
            n+=1
        ec=(2*k-1)/3
        for frac in [0.08,0.3,0.75,0.98]:
            eps=frac*ec
            def f(t):
                j,p=exp_family(k,t)
                return np.dot(j*j,p)-k*(k-eps)
            t=brentq(f,1e-12,80,xtol=1e-13)
            j,p=exp_family(k,t)
            assert abs(np.linalg.norm(equation(k,eps,p)))<2e-12
            assert abs(np.dot(j,p)-k*(1+eps)*tanh(t/2))<2e-12
            # Bifurcation branch approaches zero like sqrt(eps_c-eps)
            n+=1
        # deterministic Lyapunov check over random interior vectors
        for eps in [.03, .7*ec, 1.9*ec]:
            for seed in range(12):
                rng=np.random.default_rng(k*1000+seed)
                p=rng.random(2*k+1);p=p/p.sum()
                dt=1e-5
                deriv=(energy(k,eps,p+dt*equation(k,eps,p))-energy(k,eps,p))/dt
                assert deriv<1e-6,(k,eps,seed,deriv)
                n+=1
    # Mathematical exact boundary for k=1: cosh(t)=(1-eps)/(2eps)
    for eps in [Fraction(1,12),Fraction(1,6),Fraction(1,4)]:
        k=1;u=float(eps)
        def f(t):
            j,p=exp_family(1,t)
            return np.dot(j*j,p)-k*(k-u)
        t=brentq(f,1e-9,50)
        assert abs(np.cosh(t)-((1-u)/(2*u)))<1e-11
        n+=1
    # ODE convergence to one of the three phases, for k=1..3
    for k in [1,2,3]:
        ec=(2*k-1)/3
        for eps in [.35*ec, 1.3*ec]:
            for seed in range(6):
                rng=np.random.default_rng(7344+seed+10*k)
                p0=rng.random(2*k+1);p0/=p0.sum()
                sol=solve_ivp(lambda _,p:equation(k,eps,p),[0,280],p0,rtol=1e-9,atol=1e-11)
                p=sol.y[:,-1]
                assert max(abs(equation(k,eps,p)))<1e-7
                j=np.arange(-k,k+1)
                if eps>ec: assert abs(np.dot(j,p))<1e-6
                n+=1
    print('PASS',n,'identity, stationary-phase, dissipation, and trajectory checks')
if __name__=='__main__':
    tests()
