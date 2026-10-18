#!/usr/bin/env python3
"""Direct finite-field checks of the subquandle size-enumerator formula."""
from collections import Counter
from math import comb
from itertools import product

def gaussian(n,k,p):
    if k<0 or k>n:return 0
    num=1; den=1
    for i in range(k):
        num*=p**(n-i)-1
        den*=p**(k-i)-1
    assert num%den==0
    return num//den

def span_count(p,t,j):
    return sum(((-1)**(t-u))*p**(t-u+(t-u)*(t-u-1)//2)
       *gaussian(t,u,p)*comb(p**u,j) for u in range(t+1) if j<=p**u)

def theorem_counts(p,f):
    result=Counter()
    for t in range(f+1):
        affine_planes=p**(f-t)*gaussian(f,t,p)
        for j in range(1,p**t+1):
            a=span_count(p,t,j)
            assert a>=0
            if not a:continue
            # Each supported base coordinate has a nonempty union of W-cosets.
            # If W has p**t elements, a set of ell cosets contributes ell*p**t points.
            per=Counter({ell*p**t:comb(p**(f-t),ell) for ell in range(1,p**(f-t)+1)})
            d={0:1}
            for _ in range(j):
                nxt=Counter()
                for v,c in d.items():
                    for r,b in per.items():nxt[v+r]+=c*b
                d=nxt
            for size,c in d.items():result[size]+=a*affine_planes*c
    return result

def add_p(a,b,p,f):
    value=0; power=1
    for _ in range(f):
        value+=((a%p+b%p)%p)*power
        a//=p;b//=p;power*=p
    return value

def neg_p(a,p,f):
    value=0; power=1
    for _ in range(f):
        value+=(-a%p)*power
        a//=p;power*=p
    return value

def direct_counts(p,f):
    q=p**f; N=q*q
    assert N<=16
    op=[[0]*N for _ in range(N)]
    for x in range(N):
        a,b=divmod(x,q)
        for y in range(N):
            c,d=divmod(y,q)
            v=add_p(b,neg_p(d,p,f),p,f)
            op[x][y]=add_p(a,v,p,f)*q+b
    result=Counter()
    for mask in range(1,1<<N):
        S=[i for i in range(N) if mask>>i&1]
        closed=True
        for i in S:
            for j in S:
                if not(mask>>op[i][j]&1):
                    closed=False;break
            if not closed:break
        if closed:result[len(S)]+=1
    return result

def main():
    cases=[(2,1),(3,1),(2,2)]
    for p,f in cases:
        got=direct_counts(p,f)
        predicted=theorem_counts(p,f)
        assert got==predicted,(p,f,got,predicted)
        print('EXHAUSTIVE',p,f,'total',sum(got.values()),'size_counts',sorted(got.items()))
    for p,f in [(5,1),(3,2),(2,3),(3,3)]:
        got=theorem_counts(p,f)
        q=p**f
        assert sum(got.values())>0 and got[q*q]==1
        for t in range(f+1):
            for j in range(1,q+1):
                if j<=p**t:assert span_count(p,t,j)>=0
        for j in range(1,q+1):
            z=sum(p**(f-t)*gaussian(f,t,p)*span_count(p,t,j) for t in range(f+1) if j<=p**t)
            assert z==comb(q,j),(p,f,j,z,comb(q,j))
        print('COEFFICIENT_CONSISTENCY',p,f,'total',sum(got.values()))
    print('ALL_UNIPOTENT_SUBQUANDLE_CHECKS_PASSED')

if __name__=='__main__': main()
