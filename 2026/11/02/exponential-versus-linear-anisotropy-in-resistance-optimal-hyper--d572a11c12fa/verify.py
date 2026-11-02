#!/usr/bin/env python3
"""Independent spectral, derivative, and optimality checks for weighted hypercube design.

Requires Python 3 with NumPy, SciPy, and SymPy.
Run: python verify.py
"""
import math
from fractions import Fraction
from itertools import product
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize
from scipy.stats import binom


def edges(d):
    return [(v, v ^ (1 << j), j) for v in range(1 << d)
            for j in range(d) if not (v & (1 << j))]


def laplacian(d, weights):
    n = 1 << d
    a = np.zeros((n, n))
    for (u, v, j), w in zip(edges(d), weights):
        a[u, u] += w
        a[v, v] += w
        a[u, v] -= w
        a[v, u] -= w
    return a


def trace_inverse(d, weights):
    n = 1 << d
    m = laplacian(d, weights) + np.ones((n, n))/n
    return float(np.trace(np.linalg.inv(m)) - 1)


def tr_spectrum(d, x, y):
    n = d - 1
    return .5*(1/x + sum(math.comb(n,k)*(1/(k*y)+1/(x+k*y))
                           for k in range(1, n+1)))


def derivative(N, r, P, Q):
    k = np.arange(1,N+1, dtype=float)
    weights = binom.pmf(k,N,0.5)
    A = np.sum(weights/k)
    T = np.sum(weights/(k+r))
    U = np.sum(weights/(k+r)**2)
    return -(N*Q)*math.exp(-N*math.log(2))/(r*r) + P*(A+T-r*U)-N*Q*U


def optimum_ratio(d,P,Q):
    N = d-1
    if P == Q:
        return 1.0
    lo,hi=-100.0, math.log(N*1.e5)
    return math.exp(brentq(lambda t: derivative(N,math.exp(t),P,Q),lo,hi,
                           xtol=1.e-13))


def class_optimum(d,P,Q,B):
    N=d-1
    r=optimum_ratio(d,P,Q)
    y=B/(2**N*(P*r+N*Q))
    return r*y,y


def exact_tests():
    ct=0
    for d in (2,3,4):
        n=1<<d
        E=edges(d)
        for x,y in ((sp.Rational(2,3),sp.Rational(7,5)),
                    (sp.Rational(11,4),sp.Rational(3,2))):
            L=sp.zeros(n)
            for u,v,j in E:
                w=x if j==0 else y
                L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
            J=sp.ones(n)/n
            observed=sp.trace((L+J).inv())-1
            expected=sp.Rational(1,2)*(1/x+sum(sp.binomial(d-1,k)*
                            (1/(k*y)+1/(x+k*y)) for k in range(1,d)))
            assert sp.simplify(observed-expected)==0,('spectrum',d,x,y)
            ct+=1
    P=sp.Rational(7,5);Q=sp.Rational(9,10);r=sp.Rational(8,7)
    for N in range(1,8):
        A=sum(sp.binomial(N,k)/k for k in range(1,N+1))
        T=sum(sp.binomial(N,k)/(k+r) for k in range(1,N+1))
        U=sum(sp.binomial(N,k)/(k+r)**2 for k in range(1,N+1))
        F=(P*r+N*Q)*(1/r+A+T)
        closed=-N*Q/r**2+P*(A+T-r*U)-N*Q*U
        z=sp.Symbol('z', positive=True)
        expression=(P*z+N*Q)*(1/z+A+sum(sp.binomial(N,k)/(k+z)
                                              for k in range(1,N+1)))
        assert sp.simplify(sp.diff(expression,z).subs(z,r)-closed)==0
        ct+=1
    print('exact identities:',ct)


def numeric_tests():
    ct=0
    rng=np.random.default_rng(374119)
    for d in (2,3,4):
        E=edges(d); n=1<<d
        for P,Q in ((2.,1.),(.5,1.),(1.,1.)):
            B=2.3
            x,y=class_optimum(d,P,Q,B)
            weights=np.array([x if j==0 else y for _,_,j in E])
            prices=np.array([P if j==0 else Q for _,_,j in E])
            assert abs(np.dot(weights,prices)-B)<1e-11
            direct=trace_inverse(d,weights)
            spec=tr_spectrum(d,x,y)
            assert abs(direct-spec)<2e-8*max(1,direct),('trace',d,P)
            L=laplacian(d,weights)
            M=np.linalg.inv(L+np.ones((n,n))/n)
            grad=np.array([-np.dot(M[:,u]-M[:,v],M[:,u]-M[:,v])
                           for u,v,_ in E])
            marginal=grad/prices
            assert max(marginal)-min(marginal)<3e-6*max(1,abs(marginal.mean())),\
                ('KKT',d,P,Q, marginal.max()-marginal.min())
            for _ in range(60):
                g=rng.dirichlet(np.ones(len(E)))*B/prices
                val=trace_inverse(d,g)
                assert val>=direct-1e-7*max(1,direct),(d,P, val,direct)
                ct+=1
            if d<=3:
                def obj(z):
                    return trace_inverse(d,z/prices)
                z0=np.full(len(E),B/len(E))
                res=minimize(obj,z0,method='SLSQP',bounds=[(1.e-8,None)]*len(E),
                           constraints={'type':'eq','fun':lambda z:sum(z)-B},
                           options={'maxiter':350,'ftol':1.e-11})
                assert res.success,(d,P,Q,res.message)
                assert abs(res.fun-direct)<4e-6*max(1,direct)
                ct+=1
    for d in (32,48,64):
        N=d-1
        r=optimum_ratio(d,2.,1.)
        lim=N*2**(-N/2)*.5
        assert abs(r/lim-1)<.03,(d,r/lim)
        ct+=1
    for d in (64,96,128):
        r=optimum_ratio(d,.5,1.)
        lim=(math.sqrt(3.)-1.)/2
        assert abs(r/(d-1)-lim)<.007,(d,r/(d-1),lim)
        ct+=1
    for d in (2,3,8,40):
        assert abs(optimum_ratio(d,1.,1.)-1)<1e-15
        ct+=1
    print('numeric comparisons:',ct)
    print('P=2 Q=1 d=48, ratio:',optimum_ratio(48,2.,1.))
    print('P=1/2 Q=1 d=48, ratio:',optimum_ratio(48,.5,1.))


if __name__=='__main__':
    exact_tests()
    numeric_tests()
    print('ALL CHECKS PASSED')
