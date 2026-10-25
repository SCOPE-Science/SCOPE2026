"""Standalone exact-moment and simulation checks for Gaussian directional finite differences."""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def gaussian_expectation(expr, u):
    poly = sp.Poly(sp.expand(expr), *u)
    out = sp.Integer(0)
    for powers, coeff in poly.terms():
        if any(v % 2 for v in powers):
            continue
        prod = sp.Integer(1)
        for v in powers:
            prod *= sp.factorial2(v - 1) if v else 1
        out += coeff * prod
    return sp.simplify(out)


def exact_single_step(d, k, alpha, tau, x):
    q=d-k
    u=sp.symbols('u0:'+str(d),real=True)
    v=sp.Matrix(u)
    x=sp.Matrix(x)
    m=sp.Matrix([x[i] if i<k else 0 for i in range(d)])
    vgrad = x-m
    fwd_direction = vgrad.dot(v) + tau * v.dot(v) / 2
    xfull=x-alpha*(m+fwd_direction*v)
    vR=sp.Matrix([0]*k + list(u[k:]))
    xrestricted=x-alpha*(m+(vgrad.dot(vR)+tau*vR.dot(vR)/2)*vR)
    C_d=tau**2*(d+2)*(d+4)/4
    C_q=tau**2*(q+2)*(q+4)/4
    s=(1-alpha)**2
    r=1-2*alpha+(q+2)*alpha**2
    A0=sum(x[i]**2 for i in range(k))
    B0=sum(x[i]**2 for i in range(k,d))
    lhsAF=gaussian_expectation(sum(z*z for z in xfull[:k]),u)
    lhsBF=gaussian_expectation(sum(z*z for z in xfull[k:]),u)
    lhsAR=gaussian_expectation(sum(z*z for z in xrestricted[:k]),u)
    lhsBR=gaussian_expectation(sum(z*z for z in xrestricted[k:]),u)
    assert sp.simplify(lhsAF-(s*A0+alpha**2*k*(B0+C_d)))==0
    assert sp.simplify(lhsBF-(r*B0+alpha**2*q*C_d))==0
    assert sp.simplify(lhsAR-s*A0)==0
    assert sp.simplify(lhsBR-(r*B0+alpha**2*q*C_q))==0
    print('Exact Gaussian polynomial moments: d=',d,'k=',k,'passed')


def fixed_point_formulas(d,k,alpha,tau):
    q=d-k
    C_d=tau**2*(d+2)*(d+4)/4
    C_q=tau**2*(q+2)*(q+4)/4
    BF=alpha*q*C_d/(2-alpha*(q+2))
    AF=alpha*k*(BF+C_d)/(2-alpha)
    BR=alpha*q*C_q/(2-alpha*(q+2))
    claimedF=alpha*C_d*(2*d-alpha*(d+k))/((2-alpha)*(2-alpha*(q+2)))
    assert abs((AF+BF)-claimedF)<1e-11*(1+claimedF)
    return AF+BF,BR


def simulate(d,k,alpha,tau,seed=1827,npaths=20000,nsteps=180):
    q=d-k
    rng=np.random.default_rng(seed)
    xf=np.zeros((npaths,d))
    xr=np.zeros_like(xf)
    for _ in range(nsteps):
        uf=rng.standard_normal((npaths,d))
        ur=rng.standard_normal((npaths,q))
        bf=xf[:,k:]
        br=xr[:,k:]
        sf=(bf*uf[:,k:]).sum(axis=1)+tau*(uf*uf).sum(axis=1)/2
        sr=(br*ur).sum(axis=1)+tau*(ur*ur).sum(axis=1)/2
        xf[:,:k]*=1-alpha
        xf-=alpha*sf[:,None]*uf
        # The previous subtraction is the exact single-step update because
        # the reference component was scaled before the residual subtraction.
        xr[:,:k]*=1-alpha
        xr[:,k:]-=alpha*sr[:,None]*ur
    exactF, exactR=fixed_point_formulas(d,k,alpha,tau)
    sampleF=float(np.mean(np.sum(xf*xf,axis=1)))
    sampleR=float(np.mean(np.sum(xr*xr,axis=1)))
    print('Stationary second moments: theory',exactF,exactR,'Monte Carlo',sampleF,sampleR)
    assert abs(sampleF-exactF)<0.12*exactF
    assert abs(sampleR-exactR)<0.12*exactR


if __name__=='__main__':
    a=sp.Rational(1,4)
    t=sp.Rational(1,5)
    exact_single_step(2,1,a,t,[sp.Integer(2),sp.Integer(-3)])
    exact_single_step(3,2,a,t,[sp.Integer(1),sp.Integer(-2),sp.Integer(3)])
    exact_single_step(3,1,sp.Rational(1,7),sp.Rational(1,3),[sp.Integer(2),sp.Integer(1),sp.Integer(3)])
    for d in range(2,18):
        for k in range(1,d):
            q=d-k
            alpha=1/(q+3)
            full,restricted=fixed_point_formulas(d,k,alpha,0.1)
            assert full>restricted>0
    simulate(5,3,0.19,0.13)
    print('All scientific regression checks passed.')
