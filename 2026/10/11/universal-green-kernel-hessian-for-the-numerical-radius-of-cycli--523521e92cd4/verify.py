#!/usr/bin/env python3
"""Reproduce checks for the weighted cyclic-shift Green-kernel expansion.
Dependencies: Python 3, NumPy, SciPy. Finite checks illustrate, do not prove, the theorem.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize


def green_energy(h):
    h = np.asarray(h, dtype=float)
    n = len(h)
    c = h - h.mean()
    L = 2*np.eye(n) - np.roll(np.eye(n), 1, axis=0) - np.roll(np.eye(n), -1, axis=0)
    z = np.linalg.solve(L + np.ones((n,n))/n, c)
    assert np.linalg.norm(L@z-c) < 1e-9
    return float(c @ z)


def predicted_coeff(p,h):
    h = np.asarray(h, dtype=float)
    c = h-h.mean()
    return (p*p/(p-1)*green_energy(h)-float(c@c))/(2*len(h))


def radius(p,h,eps):
    h = np.asarray(h, dtype=float)
    n = len(h)
    alpha, beta = (p-1)/p, 1/p
    w = 1 + eps*h
    assert np.min(w)>0
    def obj(u):
        if np.min(u)<=0: return 1000
        return -float(np.dot(w, np.power(u,alpha)*np.power(np.roll(u,-1),beta)))
    def jac(u):
        up = np.power(u,alpha)*np.power(np.roll(u,-1),beta)
        # term i depends on u_i to alpha and u_(i+1) to beta
        gr = alpha*w*up/u + beta*np.roll(w*up,1)/u
        return -gr
    result = minimize(obj,np.ones(n)/n,jac=jac,method='SLSQP',
                      constraints=[{'type':'eq','fun':lambda u:np.sum(u)-1,
                                    'jac':lambda u:np.ones(n)}],
                      bounds=[(1e-10,1) for _ in range(n)],
                      options={'ftol':1e-14,'maxiter':1000})
    assert result.success, result.message
    return -float(result.fun)


def exact_cycle_four_checks():
    a = np.array([1.,1.,0.,0.])
    b = np.array([1.,0.,1.,0.])
    assert abs(green_energy(a)-0.5)<1e-13
    assert abs(green_energy(b)-0.25)<1e-13
    nchecks=0
    for p in [1.3,1.5,2.,2.7,3.,4.,7.]:
        Ka=predicted_coeff(p,a); Kb=predicted_coeff(p,b)
        assert abs((Ka-Kb) - p*p/(32*(p-1)))<1e-12
        nchecks+=1
        for eps in [.02,.015,-.02]:
            va=radius(p,a,eps); vb=radius(p,b,eps)
            target= p*p/(32*(p-1))*eps*eps
            assert abs((va-vb)-target)< 3*abs(eps)**3 + 4e-9, (p,eps,va,vb,target)
            nchecks+=1
    return nchecks


def hilbert_spectral_checks():
    nchecks=0
    for h in [[1,2,3,4],[1,0,-1,0],[2,-1,1],[.3,0,-.2,.5,-.1]]:
        h=np.asarray(h,dtype=float)
        n=len(h)
        for eps in [.03,-.03,.01]:
            w=1+eps*h
            A=np.zeros((n,n))
            for j in range(n): A[j,(j+1)%n]+=w[j]
            Q=(A+A.T)/2
            exact=float(np.linalg.eigvalsh(Q)[-1])
            got=radius(2,h,eps)
            assert abs(exact-got)<1e-8,(h,eps,exact,got)
            approx=1+eps*h.mean()+eps*eps*predicted_coeff(2,h)
            assert abs(got-approx)<5*abs(eps)**3+1e-8
            nchecks+=1
    return nchecks


def general_checks():
    nchecks=0
    for n in [2,3,4,5,7]:
        h=np.array([math.sin(2.1*i)+.33*math.cos(i+.5) for i in range(n)])
        for p in [1.3,1.7,2.,3.,5.]:
            K=predicted_coeff(p,h)
            assert K >= -1e-10
            for eps in [-.02,.02]:
                got=radius(p,h,eps)
                approx=1+eps*h.mean()+eps*eps*K
                assert abs(got-approx) < 7*abs(eps)**3+1e-8, (n,p,eps,got,approx)
                nchecks+=1
    return nchecks


if __name__ == '__main__':
    counts=(exact_cycle_four_checks(),hilbert_spectral_checks(),general_checks())
    print('VERIFICATION_OK', 'cycle='+str(counts[0]),
          'hilbert='+str(counts[1]),'general='+str(counts[2]),
          'total='+str(sum(counts)))
