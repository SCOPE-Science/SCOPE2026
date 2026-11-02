"""Direct matrix/rational spot checks for weighted-prism resistance design.

Run: python VERIFY_prism.py
Needs: Python, numpy, scipy, sympy. Finite checks support the analytic
proof; none of these tests establishes the asymptotic theorem by itself.
"""
import math
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.optimize import minimize, minimize_scalar, brentq


def prism_laplacian(n, rail, rung, symbolic=False):
    if symbolic:
        L = sp.zeros(2*n)
    else:
        L = np.zeros((2*n, 2*n), dtype=float)
    for i in range(n):
        ed = [(i, (i+1)%n, rail), (n+i, n+(i+1)%n, rail), (i,n+i,rung)]
        for u,v,w in ed:
            L[u,u] += w
            L[v,v] += w
            L[u,v] -= w
            L[v,u] -= w
    return L


def trace_formula(n, x, y):
    mu = 4 * np.sin(np.pi * np.arange(n)/n)**2
    return (n*n-1)/(12*x) + sum(1/(x*z+2*y) for z in mu)


def normalized_objective(n, t, p, q, B=1.):
    x = B/(n*(2*p+q*t))
    return trace_formula(n,x,t*x)


def solve_opt(n,p,q,B=1.):
    res = minimize_scalar(lambda z: normalized_objective(n, math.exp(z),p,q,B),
                          bounds=(-28,15), method='bounded',
                          options={'xatol':1e-13})
    assert res.success
    t=math.exp(res.x)
    x=B/(n*(2*p+q*t))
    return x,t*x,t,res.fun


def all_edges(n):
    ed=[]
    for i in range(n):
        ed.extend([(i,(i+1)%n), (i+n,(i+1)%n+n), (i,i+n)])
    return ed


def dense_objective(weights, ed, n):
    # A positive regularization on the mean-zero subspace is exact for
    # connected L; for disconnected L the augmented matrix is singular.
    L=np.zeros((2*n,2*n))
    for (u,v),w in zip(ed,weights):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    L+=np.ones_like(L)/(2*n)
    try:
        eig=np.linalg.eigvalsh(L)
        if eig[0]<1e-10: return 1e100
        return np.sum(1/eig)-1
    except np.linalg.LinAlgError: return 1e100


def check():
    checks=0
    # Exact algebraic identity: trace(L^+) and the Fourier sum, with
    # the coefficients computed on the full 2n by 2n graph.
    for n in range(3,8):
        for y in (sp.Rational(1,3),sp.Rational(2,1),sp.Rational(7,2)):
            x=sp.Rational(3,2)
            L=prism_laplacian(n,x,y,True)
            N=2*n;J=sp.ones(N)/N
            T=sp.trace((L+J).inv())-1
            # use exact Laplacian of cycle and (its shift by 2y)
            C=sp.zeros(n)
            for i in range(n):
                j=(i+1)%n
                C[i,i]+=1;C[j,j]+=1;C[i,j]-=1;C[j,i]-=1
            A=(n*n-1)/(12*x)
            A=sp.Rational(n*n-1,12)/x
            F=sp.trace((x*C+2*y*sp.eye(n)).inv())
            assert sp.simplify(T-A-F)==0, (n,x,y,T-A-F)
            checks+=1

    # Direct unconstrained numerical optimization without orbit tying.
    rng=np.random.default_rng(98431)
    for n in (3,4,5):
        ed=all_edges(n)
        for p,q in ((1.,1.),(.6,1.7),(2.1,.8)):
            x,y,t,f=solve_opt(n,p,q)
            raw=np.array([x if k%3!=2 else y for k in range(3*n)])
            cost=np.array([p if k%3!=2 else q for k in range(3*n)])
            assert abs(np.dot(raw,cost)-1)<1e-12
            assert abs(dense_objective(raw,ed,n)-f)<1e-8
            for _ in range(2):
                z=rng.uniform(.2,1.8,size=3*n)
                z/=cost@z
                res=minimize(lambda w: dense_objective(w,ed,n),z,
                             method='SLSQP',bounds=[(0,None)]*(3*n),
                             constraints=[{'type':'eq','fun':lambda w:cost@w-1}],
                             options={'maxiter':900,'ftol':1e-12})
                assert res.success, (n,p,q,res.message)
                assert abs(res.fun-f)<5e-7, (n,p,q,res.fun,f)
                assert np.max(abs(res.x-raw))<8e-4,(n,p,q,np.max(abs(res.x-raw)))
                checks+=1

    # Unique stationary point for the cube with all unit prices, exact.
    t=sp.symbols('t',positive=True)
    a=sp.Rational(5,4)
    F=1/(2*t)+1/(1+t)+1/(2*(t+2))
    D=sp.factor(sp.diff((2+t)*(a+F),t))
    assert D.subs(t,1)==0 and sp.simplify(D/(t-1)).is_positive is not False
    x,y,tmin,f=solve_opt(4,1,1)
    assert abs(tmin-1)<1e-6 and abs(f-29)<1e-8
    checks+=1

    # Closed Fourier resolvent identity across several nonasymptotic cases.
    for n in (3,4,7,19,100):
        mu=4*np.sin(np.pi*np.arange(n)/n)**2
        for t in (.001,.2,1.6,8.0):
            rho=1+t-math.sqrt(t*(t+2))
            rhs=n/(2*math.sqrt(t*(t+2)))*(1+rho**n)/(1-rho**n)
            lhs=np.sum(1/(mu+2*t))
            assert abs(rhs/lhs-1)<8e-11,(n,t,lhs,rhs)
            checks+=1

    # Mesoscopic rung/rail scaling, and two-term optimum asymptotics.
    s=(18)**(1/3)
    for n in (1000,10000,100000):
        mu=4*np.sin(np.pi*np.arange(n)/n)**2
        a=(n*n-1)/12
        derivative=lambda t: a+np.sum((mu-4)/(mu+2*t)**2)
        t=brentq(derivative,1e-12,1.0)
        scaled=t*n**(2/3)
        assert abs(scaled/s-1)<(.006 if n==1000 else .002)
        obj=normalized_objective(n,t,1,1)
        base=n*(n*n-1)/6
        asym=(obj-base)/(n**(7/3))
        assert abs(asym/(s/4)-1)<(.017 if n==1000 else .005),(n,asym,s/4)
        checks+=1
    print('PASS',checks,'exact, direct-matrix, and numerical checks')

if __name__=='__main__': check()
