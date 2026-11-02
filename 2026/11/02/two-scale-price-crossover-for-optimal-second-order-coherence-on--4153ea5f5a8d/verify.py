"""Reproducibility checks for priced-star second-order coherence optimization.

Requires Python 3, NumPy, SciPy, SymPy. Finite checks complement, not replace,
the analytic uniqueness, ratio, and asymptotic proofs.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.optimize import brentq, minimize
import sympy as sp

count = 0

def check(condition, context):
    global count
    if not condition:
        raise AssertionError(context)
    count += 1

def coefficients(m):
    return (m - 1)/(m + 1), 1/(m + 1)**2

def energy(w):
    m = len(w)
    a, d = coefficients(m)
    inv = 1/np.asarray(w, dtype=float)
    return a * np.dot(inv,inv) + d * inv.sum()**2

def gradient(w):
    m = len(w)
    a, d = coefficients(m)
    inv = 1/np.asarray(w, dtype=float)
    return -2*a*inv**3 - 2*d*inv.sum()*inv**2

def ratio(m,Q):
    A=(m-1)*(m+2)
    f=lambda t: Q*(A*t**3+t**2)-(m-1)*t-m*m
    lo=0.0
    hi=max(1.0, Q**(-1/3.)*3)
    while f(hi) <= 0:hi*=2
    return brentq(f,lo,hi,xtol=1e-15,rtol=1e-14)

def exact_identity():
    # Check the centered-cut identity using exact rationals and exact matrix inverse.
    for m in range(3,8):
        n=m+1
        J=sp.ones(n,n)/n
        for k in range(3):
            w=[sp.Rational((i+2)*(k+2)+1, (i+1)*(k+1)+2) for i in range(m)]
            L=sp.zeros(n,n)
            for j,weight in enumerate(w):
                L[0,0]+=weight
                L[j+1,j+1]+=weight
                L[0,j+1]-=weight
                L[j+1,0]-=weight
            pinv=(L+J).inv()-J
            f=sum(v*v for v in pinv)
            expected=sp.Rational(m-1,m+1)*sum(1/x**2 for x in w)+sp.Rational(1,(m+1)**2)*sum(1/x for x in w)**2
            check(sp.factor(f-expected)==0,('rational identity',m,k))

def numerical_checks():
    rng=np.random.default_rng(104821)
    for m in (3,4,5,8,12):
        for _ in range(20):
            w=np.exp(rng.uniform(-1.1,1.1,m))
            L=np.zeros((m+1,m+1))
            for i,wi in enumerate(w):
                L[0,0]+=wi
                L[i+1,i+1]+=wi
                L[0,i+1]-=wi
                L[i+1,0]-=wi
            lam=np.linalg.eigvalsh(L)[1:]
            check(abs(energy(w)-sum(lam**-2)) < 2e-9*energy(w),('spectrum',m))
    for m in (3,4,7,11):
        for Q in (0.08,0.2,0.7,1.,1.5,4.,14.,90.,500.):
            t=ratio(m,Q);B=3.7
            w0=B/(m-1+Q*t)
            w=np.array([t*w0]+[w0]*(m-1))
            prices=np.array([Q]+[1.]*(m-1))
            check(abs(prices@w-B)<1e-11,('budget',m,Q))
            check(np.max(abs(gradient(w)/prices-(gradient(w)/prices)[0]))<2e-9*(abs(gradient(w)[0]/prices[0])+1),('KKT',m,Q))
            check((t<1 if Q>1 else t>1 if Q<1 else abs(t-1)<1e-12),('monotonic',m,Q))
            for j in range(40):
                # Feasible asymmetric allocations sampled from a Dirichlet distribution.
                cost=rng.dirichlet(np.ones(m)*1.5)*B
                alt=cost/prices
                check(energy(alt)>energy(w)*(1.-1e-11),('asymmetric',m,Q,j))
    for m in (3,5,9,15):
        for _ in range(10):
            p=np.exp(rng.uniform(-2,2,m))
            B=2.0
            w_init=(B/np.sum(np.sqrt(p)))/np.sqrt(p)
            constraints={'type':'eq','fun':lambda x: float(np.dot(p,x)-B), 'jac':lambda x:p}
            result=minimize(energy,w_init,jac=gradient,method='SLSQP',bounds=[(1e-8,None)]*m,
                            constraints=constraints,options={'ftol':1e-12,'maxiter':2500})
            check(result.success,('solver',m,p,result.message))
            w=result.x
            for i in range(m):
                for j in range(m):
                    if p[i]>p[j]:
                        t=w[i]/w[j]
                        check((p[j]/p[i])**.5-1e-7<t<(p[j]/p[i])**(1/3)+1e-7,
                              ('price ratio',m,p[i],p[j],t))
            # All stationary weighted gradients agree.
            z=gradient(w)/p
            check(max(abs(z-z.mean()))<3e-5*abs(z.mean()),('general KKT',m))

def asymptotic_checks():
    for Q in (0.2,1.0,5.,50.):
        val=Q**(-1/3.)
        for m in (100,1000,10000):
            t=ratio(m,Q)
            check(abs(t/val-1)<15/m,('m asymptotics',m,Q,t))
    for m in (3,5,11,50):
        for Q in (1e8,1e10,1e12):
            t=ratio(m,Q)
            # Asymptotic error is O(m^3 / sqrt Q) in this finite range.
            check(abs(math.sqrt(Q)*t/m-1)<max(.025,20*m**3/math.sqrt(Q)),('Q asymptotics',m,Q,t))
    for kappa in (.05,.3,1,2,10):
        target=kappa**(2/3)/(1+kappa**(2/3))
        for m in (80,160,320,640):
            Q=kappa*m**1.5
            t=ratio(m,Q)
            share=Q*t/(m-1+Q*t)
            check(abs(share-target)<12/m, ('budget transition',m,kappa,t,share,target))
    for tau in (.02,.3,1,3,50):
        s=brentq(lambda x: tau*x*x*(x+1)-1,1e-8,100)
        for m in (80,160,320):
            t=ratio(m,tau*m**6)
            check(abs(m*m*t/s-1)<15/m,('joint crossover',m,tau,t))

if __name__=='__main__':
    exact_identity()
    numerical_checks()
    asymptotic_checks()
    print('PASS:',count,'checks; exact spectral identity, KKT, asymmetric feasible comparisons, price bounds and four asymptotic regimes.')
