#!/usr/bin/env python3
"""Exact checks for a partial-permutohedron covering-ellipsoid threshold.
Standard library only. All arithmetic in the checks is rational.
"""
from fractions import Fraction as F
from itertools import permutations

def invariants(n,m,k):
    S = n*(n+1)//2
    Q = n*(n+1)*(2*n+1)//6
    a = k*(2*n-k+1)//2
    b = Q-(n-k)*(n-k+1)*(2*(n-k)+1)//6
    return S,Q,a,b

def deficit(n,m,k):
    S,Q,a,b = invariants(n,m,k)
    ap=F(m*(m*Q-S*S),(m+1)*(m-1))
    bp=F(m*S*S,(m+1)**2)
    t=F(S,m+1)
    L=(F(b)-F(a*a,m))/ap + (F(a)-m*t)**2/(m*bp)
    return 1-L

def certificate(n,m):
    S,Q,*_=invariants(n,m,0)
    w=F(m,m+1); z=1-w
    t=F(S,m+1)
    ap=F(m*(m*Q-S*S),(m+1)*(m-1))
    bp=F(m*S*S,(m+1)**2)
    assert ap>0 and bp>0
    # Moment construction: probability w on a uniform full-support orbit,
    # probability z on the origin.
    assert w*S/m == t
    assert w*F(m*Q-S*S,m*(m-1)) == ap/m
    assert F(S*S,m)*w*z == bp/m
    assert deficit(n,m,0)==0
    assert deficit(n,m,n)==0
    return ap,bp,t

def factor_verification(n,m,k):
    S,Q,a,b = invariants(n,m,k)
    r=n-k
    A=F(k*n*(n+1)*r*(r+1)*(2*n*r+r+n+1),24)
    N0=F(k*n*n*(n-1)*(n+1)**2*r*(r+1)*(r-1),12)
    N=A*(m-(n*(n+1)-1))+N0
    assert deficit(n,m,k)==F((m+1)*N, S*S*m*(m*Q-S*S))

runs=0
for n in range(3,23):
    T=n*(n+1)-1
    for m in sorted({n,n+1,T-2,T-1,T,T+1,T+2,2*T,T+100}):
        if m<n:continue
        certificate(n,m)
        for k in range(1,n):
            factor_verification(n,m,k)
            v=deficit(n,m,k)
            if m>=T:
                assert v>=0
                assert (v==0)==(m==T and k==n-1)
            if m<T and k==n-1: assert v<0
            runs+=1

# Independent coordinate realization for moderately sized cases.
for n,m in [(3,11),(3,12),(4,19)]:
    ap,bp,t=certificate(n,m)
    S=n*(n+1)//2
    for k in range(n+1):
        x=tuple(range(n,n-k,-1))+tuple([0]*(m-k))
        # Direct orthogonal decomposition in coordinate Euclidean space.
        sumx=sum(x); norm2=sum(i*i for i in x)
        norm_parallel=F((sumx-m*t)**2,m)
        norm_trans=F(norm2)-F(sumx*sumx,m)
        D=1-norm_parallel/bp-norm_trans/ap
        assert D==deficit(n,m,k)
        assert D>=0
print('CHECKS_PASSED',runs,'exact rational layer/factor checks and 3 coordinate decompositions')
