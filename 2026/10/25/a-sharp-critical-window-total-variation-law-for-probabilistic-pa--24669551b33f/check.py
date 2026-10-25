#!/usr/bin/env python3
"""Exact finite checks and asymptotic diagnostics for probabilistic parking preference laws.
Run with Python 3 and scipy (optional for the large-n diagnostics): python check.py
"""
from fractions import Fraction
from math import comb, factorial, sqrt, exp, pi
from itertools import product
from functools import lru_cache

checks=0

def verify(cond, msg):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(msg)

def treepow(m):
    return 1 if m == 1 else m**(m-2)

def weights(n):
    return [Fraction(comb(n-1,j-1)*treepow(j)*treepow(n+1-j), (n+1)**(n-1)) for j in range(1,n+1)]

def formula(n,p):
    t=weights(n)
    total=sum(t)
    return [Fraction(1-p)*sum(t[:j])+t[j]+Fraction(p)*sum(t[j+1:]) for j in range(n)]

def exact_success(n, prefs,p):
    @lru_cache(None)
    def rec(i,mask):
        if i==n:
            return Fraction(1)
        v=prefs[i]-1
        if not (mask>>v)&1:
            return rec(i+1,mask | (1<<v))
        left=next((a for a in range(v-1,-1,-1) if not(mask>>a)&1),None)
        right=next((a for a in range(v+1,n) if not(mask>>a)&1),None)
        return ((Fraction(1)-p)*rec(i+1,mask | (1<<left)) if left is not None else Fraction(0)) + (p*rec(i+1,mask | (1<<right)) if right is not None else Fraction(0))
    return rec(0,0)

def test_exact():
    for n in range(1,11):
        t=weights(n)
        verify(sum(t)==Fraction(2,n+1),('total weights',n))
        verify(all(t[i]==t[n-1-i] for i in range(n)),('reflection',n))
        A=[Fraction(0)]
        for w in t: A.append(A[-1]+w)
        delta=[Fraction(2,n+1)-A[j]-A[j+1] for j in range(n)]
        verify(all(delta[i]==-delta[n-1-i] for i in range(n)),('antisym',n))
        verify(all(delta[j]==sum(t[j:n-j-1]) for j in range(n//2)),('delta sum',n))
        for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            qs=formula(n,p)
            verify(sum(qs)==1,('normalization',n,p))
            verify(all(q>=0 for q in qs),('nonnegative',n,p))
            for j,q in enumerate(qs):
                verify(q==Fraction(1,n+1)+t[j]/2+(p-Fraction(1,2))*delta[j],('decomposition',n,p,j))
                verify(q==formula(n,1-p)[n-1-j],('reflection p',n,p,j))
    for n in range(1,6):
        for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            joint=[Fraction(0) for _ in range(n)]
            for prefs in product(range(1,n+1),repeat=n):
                joint[prefs[-1]-1]+=exact_success(n,prefs,p)
            den=sum(joint)
            verify(den==(n+1)**(n-1),('total parking',n,p,den))
            for j in range(n):
                verify(joint[j]/den ==formula(n,p)[j],('independent parking enumeration',n,p,j))
    return checks

def asymptotic_diagnostics():
    try:
        import numpy as np
        from scipy.special import gammaln
    except ImportError:
        print('Optional scipy/numpy asymptotic diagnostics skipped')
        return
    C=1/sqrt(2*pi)
    for n in (100,1000,10000,100000):
        j=np.arange(1,n+1,dtype=float)
        ell=n+1-j
        logt=gammaln(n)-gammaln(j)-gammaln(ell)+(j-2)*np.log(j)+(ell-2)*np.log(ell)-(n-1)*np.log(n+1)
        t=np.exp(logt)
        aa=np.r_[0,np.cumsum(t)]
        delta=2/(n+1)-(aa[:-1]+aa[1:])
        half=1/(n+1)+t/2
        target=1/n
        tv0=0.5*np.sum(abs(half-target))
        tv1=0.5*np.sum(abs(half+delta/2-target))
        c=1
        tvc=0.5*np.sum(abs(half+c/sqrt(n)*delta-target))
        print('n',n,'n*TVcritical',round(n*tv0,8),'sqrt(n)*TV_p1',round(sqrt(n)*tv1,8),
              'n*TV_window_c1',round(n*tvc,8))
    print('theoretical limits',1, sqrt(2/pi), (1+sqrt(1+32/pi))/2)

if __name__=='__main__':
    print('exact assertions passed:',test_exact())
    asymptotic_diagnostics()
