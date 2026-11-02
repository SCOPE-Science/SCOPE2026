#!/usr/bin/env python3
"""Finite rational-point and Hessian checks for the cubic elementary-symmetric critical locus.
This program checks examples, not the infinite-field classification.
"""
from itertools import product, combinations
from math import comb

def e3grad(x,p):
    n=len(x)
    return [sum(x[j]*x[k] for j in range(n) if j!=i for k in range(j+1,n) if k!=i)%p for i in range(n)]

def e3(x,p):
    return sum(x[i]*x[j]*x[k] for i,j,k in combinations(range(len(x)),3))%p

def rankmod(rows,p):
    A=[list(map(lambda v:v%p,row)) for row in rows]; h=len(A); w=len(A[0]); rank=0
    for col in range(w):
        ix=next((i for i in range(rank,h) if A[i][col]),None)
        if ix is None: continue
        A[rank],A[ix]=A[ix],A[rank]
        s=pow(A[rank][col],-1,p)
        A[rank]=[(v*s)%p for v in A[rank]]
        for i in range(h):
            if i!=rank and A[i][col]:
                t=A[i][col]; A[i]=[(A[i][j]-t*A[rank][j])%p for j in range(w)]
        rank+=1
    return rank

def main():
    for p,n in ((3,3),(3,4),(3,6),(3,7),(3,9),(5,4),(5,6),(5,8),(7,4)):
        assert (n-2)%p
        # Every rational point, not just lines over the prime subfield.
        found=0
        for x in product(range(p),repeat=n):
            if not any(x): continue
            actual=not any(e3grad(x,p))
            values=set(x)
            nonzero=[a for a in values if a]
            predicted=len(nonzero)==1 and all(v in (0,nonzero[0]) for v in x) and sum(bool(v) for v in x)%p==1
            if actual!=predicted:
                raise AssertionError(('critical classification',p,n,x,actual,predicted))
            if actual:
                found+=1
                m=sum(bool(v) for v in x)
                h=[[sum(x[k] for k in range(n) if k not in (i,j))%p if i!=j else 0 for j in range(n)] for i in range(n)]
                assert rankmod(h,p)==n-1, ('hessian',p,n,m)
                predicted_singular=(p!=3 or m%9==1)
                assert (e3(x,p)==0)==predicted_singular, ('singular',p,n,m)
        count=sum(comb(n,m) for m in range(1,n+1) if m%p==1)
        assert found==(p-1)*count, (p,n,found,(p-1)*count)
        print(f'p={p}, n={n}, components={count}, nonzero rational critical points={found}: OK')
    print('VERIFY_OK')

if __name__=='__main__': main()
