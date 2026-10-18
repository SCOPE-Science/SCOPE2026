#!/usr/bin/env python3
"""Exact cyclotomic verifier for 3x3 Fourier-minor rank census.
Run: python census_verify.py. No dependencies beyond Python's standard library.
"""
from itertools import combinations, permutations
from math import comb, gcd


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    p=2; ct=0
    while p*p<=n:
        if n%p==0:
            n//=p;ct+=1
            if n%p==0:return 0
        p+=1
    if n>1:ct+=1
    return -1 if ct%2 else 1

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def poly_div(a,b):
    a=a[:]; q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b)
        assert a[-1]%b[-1]==0
        c=a[-1]//b[-1]
        q[k]=c
        for j in range(len(b)):a[k+j]-=c*b[j]
        trim(a)
    assert a==[0],a
    return trim(q)

def cyclotomic(n):
    polys={}
    for d in divisors(n):
        p=[-1]+[0]*(d-1)+[1]
        for e in divisors(d):
            if e<d:p=poly_div(p,polys[e])
        assert p[-1]==1
        polys[d]=p
    return polys[n]

def basis(n):
    phi=cyclotomic(n); k=len(phi)-1
    vec=[]
    for exp in range(n):
        q=[0]*(exp+1);q[exp]=1
        while len(q)>k:
            c=q[-1]; pos=len(q)-1-k
            for j in range(k+1):q[pos+j]-=c*phi[j]
            trim(q)
        vec.append(tuple(q+[0]*(k-len(q))))
    return vec

def count_rule(n):
    ds=divisors(n)
    def AA(e,d):
        s=d//gcd(e,d);m=n//(e*d//gcd(e,d))
        return e*comb(s,3)*m**3 if s>=3 else 0
    def T(g,d):
        return sum(mobius(e//g)*AA(e,d) for e in ds if e%g==0)
    c={g:T(g,n) for g in ds}
    r1=sum(c[g]*c[h] for g in ds for h in ds if (g*h)%n==0)
    r3=sum(T(g,n//h)*T(h,n//g) for g in ds for h in ds)
    return (r1,comb(n,3)**2-r1-r3,r3)

def count_exact(n):
    B=basis(n); k=len(B[0]); subs=list(combinations(range(n),3))
    perms=list(permutations((0,1,2)))
    signs=[-1 if sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2 else 1 for perm in perms]
    gs=[gcd(n,R[1]-R[0],R[2]-R[0]) for R in subs]
    cnt=[0,0,0,0]
    for i,R in enumerate(subs):
        for j,C in enumerate(subs):
            arr=[0]*k
            for perm,sign in zip(perms,signs):
                e=sum(R[t]*C[perm[t]] for t in range(3))%n
                for d,v in enumerate(B[e]):arr[d]+=sign*v
            if any(arr):rank=3
            else:
                rank=1 if all((R[a]-R[b])*(C[c]-C[d])%n==0 for a in range(3) for b in range(a+1,3) for c in range(3) for d in range(c+1,3)) else 2
            cnt[rank]+=1
    return tuple(cnt[1:])

if __name__=='__main__':
    for n in (3,4,5,6,7,8,9,10,12,15,16,18):
        predicted=count_rule(n); observed=count_exact(n)
        assert predicted==observed,(n,predicted,observed)
        print('N=%d phi=%s ranks=%s EXACT_CYCLOTOMIC_PASS'%(n,cyclotomic(n),observed))
    for n in (20,21,24,25,27,30,36,40,45,60):
        print('N=%d divisor_census=%s'%(n,count_rule(n)))
