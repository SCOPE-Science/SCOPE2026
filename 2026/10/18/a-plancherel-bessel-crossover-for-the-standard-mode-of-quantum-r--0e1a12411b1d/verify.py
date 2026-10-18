#!/usr/bin/env python3
"""Reproduce finite-rank branching profile and small exact-group quantum dynamics."""
import math, cmath
from functools import lru_cache
from itertools import permutations

@lru_cache(None)
def partitions(n, maxpart=None):
    if maxpart is None: maxpart=n
    if n==0:return ((),)
    return tuple((k,)+r for k in range(min(n,maxpart),0,-1) for r in partitions(n-k,k))

@lru_cache(None)
def dim(shape):
    n=sum(shape)
    h=1
    for i,row in enumerate(shape):
        for j in range(row):
            h *= row-j + sum(1 for lower in shape[i+1:] if lower>j)
    return math.factorial(n)//h

def addable(shape):
    n=len(shape)
    ans=[]
    for i in range(n+1):
        if i==n:
            a=shape+(1,)
            c=-n
        elif i==0 or shape[i-1]>shape[i]:
            a=shape[:i]+(shape[i]+1,)+shape[i+1:]
            c=shape[i]-i
        else:continue
        ans.append((a,c))
    return ans

def kappa_branch(n,theta):
    if n<2:raise ValueError
    norm=math.factorial(n-1)
    den=n*(n-1)/2
    ans=0.
    for nu in partitions(n-1):
        d=dim(nu)
        phi=sum(dim(lam)/(n*d)*cmath.exp(1j*theta*c/den) for lam,c in addable(nu))
        assert sum(dim(lam) for lam,c in addable(nu))==n*d
        ans+=(d*d/norm)*abs(phi)**2
    return n/(n-1)*ans - 1/(n-1)

def direct_kappa(n,theta):
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import expm_multiply
    group=list(permutations(range(n)))
    ids={g:i for i,g in enumerate(group)}
    N=len(group)
    rows=[]; cols=[]; data=[]
    for i,g in enumerate(group):
        for a in range(n):
            for b in range(a+1,n):
                g2=tuple((b if x==a else a if x==b else x) for x in g)
                rows.append(ids[g2]);cols.append(i);data.append(1/math.comb(n,2))
    H=csr_matrix((data,(rows,cols)),shape=(N,N),dtype=complex)
    e=np.zeros(N,dtype=complex);e[ids[tuple(range(n))]]=1
    amp=expm_multiply((-1j*theta)*H,e)
    return float(sum(abs(amp[i])**2*(sum(x==j for j,x in enumerate(g))-1) for i,g in enumerate(group))/(n-1))

def main():
    checks=0
    for n in range(2,7):
        for theta in (0,.125,.5,1.,2.25,3.8):
            x=kappa_branch(n,theta); y=direct_kappa(n,theta)
            assert abs(x-y)<1.e-10,(n,theta,x,y)
            assert -1/(n-1)-1e-10 <=x<=1+1e-10
            checks+=1
    # Check moment identity from the original model: kappa(theta)=1- m theta^2/((n-1) C(n,m)) + O(theta^4), m=2.
    for n in range(2,16):
        t=0.0001
        expected=2/((n-1)*math.comb(n,2))
        ratio=(1-kappa_branch(n,t))/(t*t)
        assert abs(ratio-expected)<1e-5,(n,ratio,expected)
        checks+=1
    try:
        import scipy.special
        def asymp(s):return (scipy.special.j1(4*s)/(2*s))**2 if s else 1.
        for n in (10,20,30):
            for s in (.1,.25,.5,.75,1.):
                y=kappa_branch(n,s*n**1.5)
                z=asymp(s)
                assert abs(y-z)<.30,(n,s,y,z)
                checks+=1
                print('PROFILE',n,s,round(y,8),round(z,8))
    except ImportError:pass
    print('VERIFY_OK',checks,'finite independent group, branching, moment and profile checks')
if __name__=='__main__':main()
