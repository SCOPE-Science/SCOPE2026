#!/usr/bin/env python3
"""Exact small-field rank test and squarefree-polynomial checks for pencil counts."""
from itertools import combinations, product
from math import prod, factorial

def det3(a,q):
    return (a[0]*(a[4]*a[8]-a[5]*a[7])-a[1]*(a[3]*a[8]-a[5]*a[6])+a[2]*(a[3]*a[7]-a[4]*a[6]))%q

def nonsingular(v,q):
    h=pow(2,-1,q)
    a,b,c,d,e,f=v
    M=(a,d*h%q,e*h%q,d*h%q,b,f*h%q,e*h%q,f*h%q,c)
    return det3(M,q)!=0

def count_all_smooth_conic_pencils(q):
    m=6
    result=0
    total=0
    for i,j in combinations(range(m),2):
        positions0=[k for k in range(i+1,m) if k!=j]
        positions1=[k for k in range(j+1,m)]
        n0=len(positions0)
        for par in product(range(q),repeat=n0+len(positions1)):
            row0=[0]*m; row1=[0]*m
            row0[i]=1;row1[j]=1
            for k,v in zip(positions0,par[:n0]):row0[k]=v
            for k,v in zip(positions1,par[n0:]):row1[k]=v
            total+=1
            if not nonsingular(row1,q):continue
            if all(nonsingular([(a+t*b)%q for a,b in zip(row0,row1)],q) for t in range(q)):
                result+=1
    assert total == ((q**6-1)*(q**6-q))//((q*q-1)*(q*q-q))
    return total,result

def trim(P):
    while len(P)>1 and P[-1]==0:P.pop()
    return P

def rem(A,B,q):
    A=trim(A[:]);B=trim(B[:])
    while len(A)>=len(B) and any(A):
        d=len(A)-len(B)
        c=A[-1]*pow(B[-1],-1,q)%q
        for j,b in enumerate(B): A[j+d]=(A[j+d]-c*b)%q
        trim(A)
    return A

def squarefree_rootless_monic(q,n):
    count=0
    for tup in product(range(q),repeat=n):
        f=list(tup)+[1]
        if any(sum(a*pow(t,k,q) for k,a in enumerate(f))%q==0 for t in range(q)):
            continue
        df=[k*a%q for k,a in enumerate(f)][1:]
        aa=f[:];bb=trim(df)
        while any(bb):aa,bb=bb,rem(aa,bb,q)
        if len(aa)==1:count+=1
    return count

def gl(q,n):return prod(q**n-q**i for i in range(n))

def run():
    for q in (3,5):
        t,yes=count_all_smooth_conic_pencils(q)
        s=squarefree_rootless_monic(q,3)
        formula=gl(q,3)*s//gl(q,2)
        assert yes==formula,(q,yes,formula)
        print(f'q={q} n=3: total_pencils={t} good={yes} rootfree_separable_monic={s} formula={formula} PASS')
    for q in (3,5,7):
        s=squarefree_rootless_monic(q,4)
        n2=(q*q-q)//2;n4=(q**4-q*q)//4
        assert s==n4+n2*(n2-1)//2
        ans=gl(q,4)*s//gl(q,2)
        print(f'q={q} n=4: rootfree_separable_quartics={s} predicted_good_pencils={ans} PASS')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':run()
