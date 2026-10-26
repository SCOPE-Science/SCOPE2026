#!/usr/bin/env python3
"""Finite numerical sanity checks for an analytic cubic mean-field Ising theorem.
No finite test proves the asymptotic result. Python 3 standard library only.
"""
import math

def energy(m, k, j):
    if abs(m) >= 1:
        entropy = math.log(2.0)
    else:
        entropy = 0.5 * ((1+m)*math.log1p(m)+(1-m)*math.log1p(-m))
    return k*m**3/3+j*m*m/2-entropy

def derivative(m,k,j):
    return k*m*m+j*m-math.atanh(m)

def coexistence(k):
    # Equal-energy and stationary equations reduced to a scalar root.
    # For m>0, use stationarity j=(atanh(m)-k*m*m)/m.
    def eq(m):
        j=(math.atanh(m)-k*m*m)/m
        return energy(m,k,j)
    a=k*1.2
    b=min(0.95,k*3)
    assert eq(a)*eq(b)<0
    for _ in range(75):
        mid=(a+b)/2
        if eq(a)*eq(mid)<=0: b=mid
        else: a=mid
    m=(a+b)/2
    return (math.atanh(m)-k*m*m)/m,m

def finite_weights(n,k,j,h=0):
    mvals=[(2*r-n)/n for r in range(n+1)]
    logs=[math.lgamma(n+1)-math.lgamma(r+1)-math.lgamma(n-r+1)
          +n*(k*m**3/3+j*m*m/2+h*m) for r,m in enumerate(mvals)]
    mx=max(logs)
    w=[math.exp(z-mx) for z in logs]
    tot=sum(w)
    return mvals,[x/tot for x in w]

def simpson(fn,a,b,n=20000):
    assert n%2==0
    d=(b-a)/n
    s=fn(a)+fn(b)
    for i in range(1,n): s+=(4 if i%2 else 2)*fn(a+i*d)
    return s*d/3

def test():
    # Exact reflection identity in the limiting potential, numeric moments.
    kappa=1.5
    q=lambda x: math.exp(-x*x*(x-2*kappa)**2/12)
    z=simpson(q,-12,15)
    mean=simpson(lambda x:x*q(x),-12,15)/z
    left=simpson(q,-12,kappa)/z
    assert abs(mean-kappa)<1e-7
    assert abs(left-.5)<1e-7
    print('critical symmetric mean, left well mass:',mean,left)
    # Coexistence coefficients, checked at successively smaller couplings.
    for k in [0.15,0.1,0.07]:
        j,m=coexistence(k)
        jc=1-2*k*k/3+16*k**4/15
        mc=2*k-32*k**3/5
        assert abs(j-jc)<.0001 and abs(m-mc)<.004
        print('K, gamma exact, gamma expansion, m* exact, m* expansion:',k,j,jc,m,mc)
    # Check finite-N phase weights at coexistence, distinguishing two wells.
    k=.1
    n=100000
    j,m=coexistence(k)
    ms,weights=finite_weights(n,k,j)
    pos=sum(w for x,w in zip(ms,weights) if x>m/2)
    assert abs(pos-.5)<.06
    print('finite N coexistence positive-well probability:',pos)
    # Critical scaling trend (not a rate guarantee).
    n=20000
    kappa=.8
    kk=kappa*n**(-.25)
    jj=1-2*kappa*kappa/3*n**(-.5)
    ms,w=finite_weights(n,kk,jj)
    mn=sum(x*w0 for x,w0 in zip(ms,w))*n**.25
    assert abs(mn-kappa)<.3
    print('finite N critical rescaled mean:',mn)

if __name__ == '__main__':
    test()
