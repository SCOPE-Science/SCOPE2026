#!/usr/bin/env python3
"""Exhaustive prime-field tests for the joint center/annihilator law of square-cube-zero algebras."""
from itertools import product
from collections import Counter
from functools import lru_cache
from math import prod

@lru_cache(None)
def gb(n,k,q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    return gb(n-1,k,q)+q**(n-k)*gb(n-1,k-1,q)

def onto(D,s,q):
    if D<s:return 0
    return prod(q**D-q**i for i in range(s))

def D(r,a,b):
    assert 0<=a<=b<=r
    return (r-a)**2-(b-a)*(r-b)-(b-a)*(b-a-1)//2

def predicted(q,r,s):
    den=onto(r*r,s,q)
    assert den>0
    ans={}
    for a in range(r+1):
        for b in range(a,r+1):
            accum=0
            for i in range(b-a+1):
                u=(-1)**i*q**(i*(i-1)//2)*gb(b-a,i,q)
                for j in range(r-b+1):
                    v=(-1)**j*q**(j*(j-1)//2)*gb(r-b,j,q)
                    accum+=u*v*onto(D(r,a+i,b+j),s,q)
            ct=gb(r,b,q)*gb(b,a,q)*accum
            assert ct>=0,(q,r,s,a,b,ct)
            ans[(a,b)]=ct
    assert sum(ans.values())==den,(q,r,s,sum(ans.values()),den)
    return ans

def rank(rows,q):
    if not rows:return 0
    rows=[list(x) for x in rows]
    nr=len(rows);nc=len(rows[0]);piv=0
    for col in range(nc):
        row=next((h for h in range(piv,nr) if rows[h][col]%q),None)
        if row is None:continue
        rows[row],rows[piv]=rows[piv],rows[row]
        a=pow(rows[piv][col]%q,-1,q)
        rows[piv]=[a*x%q for x in rows[piv]]
        for j in range(nr):
            if j!=piv and rows[j][col]%q:
                v=rows[j][col]
                rows[j]=[(x-v*y)%q for x,y in zip(rows[j],rows[piv])]
        piv+=1
        if piv==nr:break
    return piv

def brute(q,r,s):
    counts=Counter();total=0
    for flat in product(range(q),repeat=s*r*r):
        B=[[[flat[k*r*r+i*r+j] for j in range(r)] for i in range(r)] for k in range(s)]
        if rank([[B[k][i][j] for i in range(r) for j in range(r)] for k in range(s)],q)!=s:continue
        C=[[ (B[k][i][j]-B[k][j][i])%q for i in range(r)] for k in range(s) for j in range(r)]
        Z=[[B[k][i][j] for i in range(r)] for k in range(s) for j in range(r)] + [[B[k][j][i] for i in range(r)] for k in range(s) for j in range(r)]
        extra_center=r-rank(C,q)
        extra_ann=r-rank(Z,q)
        assert extra_ann<=extra_center
        counts[(extra_ann,extra_center)]+=1
        total+=1
    return counts,total

def main():
    for q,r,s in [(2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),(3,2,1),(3,2,2)]:
        expected=predicted(q,r,s)
        counts,total=brute(q,r,s)
        assert sum(expected.values())==total
        for pair,v in expected.items():
            assert counts[pair]==v,(q,r,s,pair,counts[pair],v)
        nonzero={str(k):v for k,v in sorted(counts.items()) if v}
        print('PASS',q,r,s,'onto',total,'joint',nonzero)
    print('ALL TESTS PASSED')

if __name__=='__main__':main()
