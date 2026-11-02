#!/usr/bin/env python3
"""Reproduce the algebraic endpoint inequalities and sampled full spectra for a pentagonal leaf corona.
Requires Python 3 and NumPy for supplementary finite-spectrum calculations.
The interval certificates use exact integers and fractions, independent of NumPy.
"""
import math
from fractions import Fraction as Q

SCALE=10**9

def nth_root_floor(N,n):
    lo,hi=0,1
    while hi**n<=N: hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**n<=N: lo=mid
        else: hi=mid
    return lo

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo);self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,other):
        other=other if isinstance(other,I) else I(other)
        return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-asI(other)
    def __rsub__(self,other):return asI(other)+-self
    def __mul__(self,other):
        other=asI(other); t=[x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return I(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=asI(other); assert other.lo>0 or other.hi<0
        return self*I(1/other.hi,1/other.lo)
    def gtzero(self):return self.lo>0
    def ltzero(self):return self.hi<0
    def limits(self):return float(self.lo),float(self.hi)

def asI(x):return x if isinstance(x,I) else I(x)

def rootpow_interval(base, exponent_num, exponent_den):
    N=base**exponent_num*SCALE**exponent_den
    a=nth_root_floor(N,exponent_den)
    assert a**exponent_den<=N<(a+1)**exponent_den
    return I(Q(a,SCALE),Q(a+1,SCALE))

def root_interval(base):
    a=math.isqrt(base*SCALE*SCALE)
    assert a*a<=base*SCALE*SCALE<(a+1)**2
    return I(Q(a,SCALE),Q(a+1,SCALE))

def critical_functions(p):
    u=2**p;v=3**p;w=4**p
    phi=(1+5**.5)/2
    z=[(5**.5-1)/2,-phi]
    H=2*w-u-2*v
    D=[]
    for c in z:
        d=-1-c;A=c+u*d;B=1+u*c+v*d;C=u+v*c+w*d
        D.append(A*C-B*B-A*H)
    return H, D

def exact_endpoint_inequalities():
    sqrt5=root_interval(5)
    z2=-(1+sqrt5)/2
    z1=(sqrt5-1)/2
    p=Q(9,7)
    u=rootpow_interval(2,9,7);v=rootpow_interval(3,9,7);w=rootpow_interval(4,9,7)
    H=2*w-u-2*v
    assert (2*H-u).gtzero(), ('global bracket', (2*H-u).limits())
    assert ((3+sqrt5)/2-u).gtzero(), ('negative A2',( (3+sqrt5)/2-u).limits())
    D=[]
    for z in (z1,z2):
        d=-1-z;A=z+u*d;B=1+u*z+v*d;C=u+v*z+w*d
        val=A*C-B*B-A*H
        D.append(val)
    assert D[1].gtzero(), ('D2',D[1].limits())
    base8=rootpow_interval(8,9,7)
    base6=rootpow_interval(6,9,7)
    base9=rootpow_interval(9,9,7)
    hz=3*base8-3*w-2*base6-base9+3*v
    assert hz.gtzero(), ('H_z',hz.limits())
    assert 11-9*math.sqrt(5)<0
    assert 3*8**10-3*4**10-2*6**10-9**10+3*3**10<0
    print('EXACT_RATIONAL_CERTIFICATE_OK')
    print('2H-u', (2*H-u).limits())
    print('D_z2',D[1].limits())
    print('H_z',hz.limits())
    print('phi_squared-u',((3+sqrt5)/2-u).limits())


def graph_distances(r):
    from collections import deque
    N=5*(r+1)
    adj=[set() for _ in range(N)]
    for i in range(5):
        j=(i+1)%5
        a,b=i*(r+1),j*(r+1)
        adj[a].add(b);adj[b].add(a)
        for k in range(1,r+1):
            z=i*(r+1)+k
            adj[a].add(z);adj[z].add(a)
    D=[]
    for i in range(N):
        row=[-1]*N; row[i]=0
        todo=deque([i])
        while todo:
            a=todo.popleft()
            for b in adj[a]:
                if row[b]<0:
                    row[b]=row[a]+1;todo.append(b)
        assert all(d>=0 for d in row)
        D.append(row)
    # Independent metric-formula comparison.
    for i in range(N):
        for j in range(N):
            if i==j: continue
            ii,jj=i//(r+1),j//(r+1)
            ci,cj=(i%(r+1)==0),(j%(r+1)==0)
            pred=min((ii-jj)%5,(jj-ii)%5)+(not ci)+(not cj)
            assert D[i][j]==pred
    return D

def numerical_spectra():
    import numpy as np
    from scipy.optimize import brentq
    checks=0
    for r in [2,3,4,5,8,10,30]:
        g=lambda p:2*2**p-1-2*(1.5)**p
        p=brentq(lambda p:r*g(p)-1,1,1.5,xtol=1e-14)
        d=np.array(graph_distances(r),dtype=float)
        N=len(d);Q=d**p; np.fill_diagonal(Q,0)
        U=np.eye(N)[:,:-1]-np.eye(N)[:,-1,None]
        # compressed zero-sum form on N-1 independent columns
        S=U.T@Q@U
        evals=np.linalg.eigvalsh(S)
        assert abs(evals[-1])<4e-7, (r,p,evals[-1])
        assert evals[-2]<-0.005, (r,p,evals[-2])
        for q in [0.1, 0.5, 1,p-0.005]:
            T=d**q; np.fill_diagonal(T,0)
            e=np.linalg.eigvalsh(U.T@T@U)
            assert e[-1]<-1e-6, (r,q,e[-1])
            checks+=1
        for q in [p+0.001,p+0.01]:
            T=d**q;np.fill_diagonal(T,0)
            e=np.linalg.eigvalsh(U.T@T@U)
            assert e[-1]>1e-6, (r,q,e[-1]);checks+=1
        assert p>1 and p<9/7
        print('r',r,'p',format(p,'.12f'),'nullity',int(np.sum(abs(evals)<1e-6)))
        checks+=10
    print('FINITE_SPECTRA_OK', checks)

if __name__=='__main__':
    exact_endpoint_inequalities()
    numerical_spectra()
    print('CHECK_OK')
