#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def qbinom(n,r,q):
    if r<0 or r>n:return 0
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def formulas(p,n,m,t,r):
    N=p**n-p**m-t
    a=max(0,m-r)
    d=N-p**(n-r)+p**a
    if r<=m:
        aa=m-r
        nin=qbinom(m-1,aa-1,p)
        nout=qbinom(m,aa,p)-nin
        c=n-m
        M=p**(r*(c-1))*(nin*(p**r-1)+nout*(p**r-t))
    elif r<n:
        h=n-r
        c=n-m
        M=p**(m*h)*qbinom(c,h,p)-t*p**(m*(h-1))*qbinom(c-1,h-1,p)
    else:
        M=1
    return d,M

def rref_subspaces(n,d,p):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,q in enumerate(piv) for c in range(q+1,n) if c not in P]
        for vals in itertools.product(range(p),repeat=len(free)):
            B=[[0]*n for _ in range(d)]
            for i,q in enumerate(piv):B[i][q]=1
            for (i,c),v in zip(free,vals):B[i][c]=v
            yield B

def defining_set(p,n,m,t):
    A={tuple(a)+(0,)*(n-m) for a in itertools.product(range(p),repeat=m)}
    extra={tuple([p-1]*m+[j]+[0]*(n-m-1)) for j in range(1,t+1)}
    I=A|extra
    return [x for x in itertools.product(range(p),repeat=n) if x not in I]

def support(B,D,p):
    return sum(any(sum(row[i]*x[i] for i in range(len(x)))%p for row in B) for x in D)

tests=[(3,4,2,1),(3,4,2,2),(3,5,3,2),(5,4,2,1),(5,4,2,4)]
for p,n,m,t in tests:
    D=defining_set(p,n,m,t)
    key=f"p{p}_n{n}_m{m}_t{t}"
    got_d=[]
    got_m=[]
    for r in range(1,n+1):
        ctr=collections.Counter(support(B,D,p) for B in rref_subspaces(n,r,p))
        d=min(ctr)
        M=ctr[d]
        assert (d,M)==formulas(p,n,m,t,r)
        got_d.append(d)
        got_m.append(M)
    assert got_d==CERT["verified_examples"][key]["hierarchy"]
    assert got_m==CERT["verified_examples"][key]["minimizer_counts"]

print("VERIFY_OK")
