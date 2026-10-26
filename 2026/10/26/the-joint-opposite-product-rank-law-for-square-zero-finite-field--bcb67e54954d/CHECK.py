#!/usr/bin/env python3
"""Direct finite-field enumeration and independent Gaussian flag-law check."""
from itertools import product
from fractions import Fraction
from collections import Counter
from functools import lru_cache, reduce
from math import prod

@lru_cache(None)
def gauss(n,k,q):
    if k<0 or k>n or n<0:return 0
    if k==0 or k==n:return 1
    return gauss(n-1,k,q)+q**(n-k)*gauss(n-1,k-1,q)

def hyper(n,r,s,q):
    assert 2*r<=n and 2*s<=n
    den=gauss(n,s,q)
    joint=Counter()
    for j in range(max(0,r+s-n),min(r,s)+1):
        w=Fraction(gauss(r,j,q)*gauss(n-r,s-j,q)*q**((r-j)*(s-j)),den)
        def kerprob(rank, other):
            # K/rank-image has dimension n-2*rank in V/image.
            d=n-2*rank
            a=other-j
            b=n-r-s+j
            den2=gauss(n-rank,d,q)
            return {x:Fraction(gauss(a,x,q)*gauss(b,d-x,q)*q**((a-x)*(d-x)),den2)
                    for x in range(0,min(a,d)+1) if gauss(a,x,q)*gauss(b,d-x,q)>0}
        xe=kerprob(r,s)
        yf=kerprob(s,r)
        assert sum(xe.values())==sum(yf.values())==1,(n,r,s,q,j,xe,yf)
        for x,px in xe.items():
            for y,py in yf.items():
                joint[(s-j-x,r-j-y)]+=w*px*py
    assert sum(joint.values())==1
    return joint

def field(q):
    assert q in (2,3,4)
    if q==4:
        def add(x,y):return x^y
        def mul(x,y):
            a0,a1=x&1,x>>1;b0,b1=y&1,y>>1
            return ((a0*b0+a1*b1)%2) + 2*((a0*b1+a1*b0+a1*b1)%2)
        return add,mul
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q

def rank(A,n,q,add,mul):
    B=[list(A[i*n:(i+1)*n]) for i in range(n)]
    t=0
    for c in range(n):
        pivot=next((i for i in range(t,n) if B[i][c]),None)
        if pivot is None:continue
        B[t],B[pivot]=B[pivot],B[t]
        inv=next(v for v in range(1,q) if mul(B[t][c],v)==1)
        B[t]=[mul(v,inv) for v in B[t]]
        for i in range(t+1,n):
            if B[i][c]:
                co=B[i][c]
                B[i]=[add(B[i][h],-mul(co,B[t][h])%q) if q!=4 else add(B[i][h],mul(co,B[t][h])) for h in range(n)]
        t+=1
        if t==n:break
    return t

def matmul(A,B,n,q,add,mul):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q if q!=4 else
                 reduce(add,(mul(A[i*n+k],B[k*n+j]) for k in range(n)),0)
                 for i in range(n) for j in range(n))

def test(n,q):
    add,mul=field(q)
    zero=(0,)*(n*n)
    shells={}
    for A in product(range(q),repeat=n*n):
        if matmul(A,A,n,q,add,mul)!=zero:continue
        r=rank(A,n,q,add,mul)
        shells.setdefault(r,[]).append(A)
    for r,v in shells.items():
        expected=gauss(n,r,q)*gauss(n-r,r,q)*prod(q**r-q**i for i in range(r))
        assert len(v)==expected,(n,q,r,len(v),expected)
    checks=0
    for r,Rs in shells.items():
        for s,Ss in shells.items():
            expected=hyper(n,r,s,q)
            actual=Counter()
            for E in Rs:
                for F in Ss:
                    t=rank(matmul(E,F,n,q,add,mul),n,q,add,mul)
                    u=rank(matmul(F,E,n,q,add,mul),n,q,add,mul)
                    actual[t,u]+=1
            assert {k:Fraction(v,len(Rs)*len(Ss)) for k,v in actual.items()}=={k:v for k,v in expected.items() if v>0},(n,q,r,s,actual,expected)
            checks+=len(Rs)*len(Ss)
    return len(shells),sum(len(v) for v in shells.values()),checks

if __name__=='__main__':
    total=0
    for n,q in [(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)]:
        shells,matrices,pairs=test(n,q)
        print('PASS n=%d q=%d rank_shells=%d square_zero_matrices=%d ordered_pairs=%d'%(n,q,shells,matrices,pairs))
        total+=pairs
    print('ALL_SQUARE_ZERO_JOINT_RANK_CHECKS_PASSED pairs=%d'%total)
