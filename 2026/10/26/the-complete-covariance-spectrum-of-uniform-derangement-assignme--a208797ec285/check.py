#!/usr/bin/env python3
"""Exact enumeration for local covariance and operator eigen identities."""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial,comb

def D(n):
    if n<0:return 0
    return sum((-1)**j*comb(n,j)*factorial(n-j) for j in range(n+1))

def theory(n):
    d=D(n);p=Fraction(1,n-1);r=Fraction(D(n-3),(n-1)*d)
    g2=-(n-2)*r;g3=r;g4=n*r+Fraction(D(n-4),d)
    va=p*(1-p)
    return p,va,g2,g3,g4,p+p*p+n*r,p+p*p+n*r+2*Fraction(D(n-4),d)

def typ(e,f):
    i,j=e;k,l=f
    if e==f:return 'diag'
    if i==k or j==l:return 'same_row_or_col'
    return 's'+str(len({i,j,k,l}))

def main():
    asserts=0
    for n in range(3,9):
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        ec={e:p for p,e in enumerate(edges)}
        ct=[0]*len(edges); co=Counter();num=0
        for pi in permutations(range(n)):
            if any(i==x for i,x in enumerate(pi)):continue
            num+=1
            active=[ec[(i,x)] for i,x in enumerate(pi)]
            for a in active:ct[a]+=1
            for x,a in enumerate(active):
                for b in active[x+1:]:co[(min(a,b),max(a,b))]+=1
        assert num==D(n);asserts+=1
        p,va,g2,g3,g4,la,ls=theory(n)
        for a,e in enumerate(edges):
            assert Fraction(ct[a],num)==p;asserts+=1
            for b,f in enumerate(edges[a:],start=a):
                pr=Fraction(ct[a],num) if a==b else Fraction(co[(a,b)],num)
                cv=pr-Fraction(ct[a]*ct[b],num*num)
                t=typ(e,f)
                v={'diag':va,'same_row_or_col':-p*p,'s2':g2,'s3':g3,'s4':g4}[t]
                assert cv==v,(n,e,f,t,cv,v)
                asserts+=1
        if n>=4:
            # Two symmetric zero-degree and antisymmetric zero-divergence test matrices.
            sy={(0,1):1,(1,0):1,(2,3):1,(3,2):1,(0,2):-1,(2,0):-1,(1,3):-1,(3,1):-1}
            assert all(sum(sy.get((i,j),0) for j in range(n))==0 for i in range(n))
        else:sy={}
        ak={(0,1):1,(1,2):1,(2,0):1,(1,0):-1,(2,1):-1,(0,2):-1}
        for A,lam in [(ak,la)]+([(sy,ls)] if n>=4 else []):
            for e in edges:
                action=Fraction(0)
                for f in edges:
                    t=typ(e,f)
                    v={'diag':va,'same_row_or_col':-p*p,'s2':g2,'s3':g3,'s4':g4}[t]
                    action+=v*A.get(f,0)
                assert action==lam*A.get(e,0),(n,e,action,lam,A.get(e,0))
                asserts+=1
        g4_label=str(g4) if n>=4 else 'not_applicable'
        ls_label=str(ls) if n>=4 else 'not_applicable'
        print(f'n={n} derangements={num}, edges={len(edges)}, pair classes {g2},{g3},{g4_label}, eigen {la},{ls_label}')
    print('ALL',asserts,'EXACT ASSERTIONS PASSED')
if __name__=='__main__':main()
