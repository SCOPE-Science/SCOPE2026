#!/usr/bin/env python3
"""Deterministic, finite-threshold numerical checks; not an asymptotic proof.
Requires Python 3 and SciPy. The model and numerical tests are fully specified below.
"""
from math import exp, sqrt, pi, isfinite
from scipy.integrate import quad
from scipy.special import ndtr, log_ndtr

def joint_probability(N,m,r,D,x):
    lam=r*m/N
    c=r*m*(m-1)/(N*(N-1))
    alpha=lam-c
    delta=2*lam-c
    k=sqrt(lam/D)
    assert abs(2*alpha+c-delta)<1e-12
    assert abs(alpha+c-lam)<1e-12
    if m==1: return 0.25*exp(-2*k*x)
    def integrand(t):
        if t<=0:return 0.0
        sig=sqrt(2*D*t)
        q=ndtr(-x/sig)
        g=q+0.5*exp(-k*x+k*k*D*t+log_ndtr(x/sig-k*sig))-0.5*exp(k*x+k*k*D*t+log_ndtr(-x/sig-k*sig))
        return exp(-delta*t)*(c*q*q+2*alpha*q*g)
    return quad(integrand,0,80+2*x,epsabs=1e-90,epsrel=1e-7,limit=600)[0]

def asymptotic(N,m,r,D,x):
    lam=r*m/N
    c=r*m*(m-1)/(N*(N-1))
    alpha=lam-c
    delta=2*lam-c
    k1=sqrt(lam/D)
    if m==1:return .25*exp(-2*k1*x)
    k2=sqrt(2*delta/D)
    assert k1>k2/2
    mgf=k1*k1/(k1*k1-k2*k2/4)
    assert abs(mgf-2*lam/c)<1e-10
    return (c+2*alpha*mgf)*exp(-k2*x)/(delta*sqrt(2*pi*k2*x))

def main():
    count=0
    for N,m,r,D in [(5,2,5.0,1.0),(5,4,5.0,1.0),(5,5,5.0,1.0),(3,2,3.0,2.0)]:
        for x in [12.0,20.0,40.0]:
            p=joint_probability(N,m,r,D,x)
            a=asymptotic(N,m,r,D,x)
            assert p>0 and a>0 and isfinite(p/a)
            assert 0<p/a<2.5
            count+=1
        print(f'N={N} m={m}: finite ratios P_exact/P_asym at x=12,20,40 verified')
    for N in [3,5,8]:
        p=joint_probability(N,1,4.0,1.2,5.0)
        a=asymptotic(N,1,4.0,1.2,5.0)
        assert abs(p/a-1)<1e-14
        count+=1
    print(f'{count} finite comparisons and boundary checks passed')
if __name__=='__main__':main()
