#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
C=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def qbinom(n,r,q):
    if r<0 or r>n:return 0
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def gl(c,q):
    z=1
    for i in range(c):z*=q**c-q**i
    return z

def formula(q,k1,k2,r):
    a=max(0,k1-r);b=max(0,k2-r);c=k1+k2-r-a-b
    d=q**(k1+k2)-q**(k1+k2-r)-q**k1-q**k2+q**a+q**b
    m=qbinom(k1,a,q)*qbinom(k2,b,q)*qbinom(k1-a,c,q)*qbinom(k2-b,c,q)*gl(c,q)
    return d,m

def inv(a,q):return pow(a,-1,q)

def canon(v,q):
    for x in v:
        if x%q:
            u=inv(x%q,q)
            return tuple(u*y%q for y in v)

def points(q,k1,k2):
    P=set()
    for v in itertools.product(range(q),repeat=k1+k2):
        if not any(v) or not any(v[:k1]) or not any(v[k1:]):continue
        P.add(canon(v,q))
    return sorted(P)

def subspaces(n,d,q):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv) for c in range(p+1,n) if c not in P]
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*n for _ in range(d)]
            for i,p in enumerate(piv):B[i][p]=1
            for (i,c),v in zip(free,vals):B[i][c]=v
            yield B

def support(B,P,q):
    return (q-1)*sum(any(sum(row[i]*p[i] for i in range(len(p)))%q for row in B) for p in P)

for q in (2,3):
    k1,k2=2,3
    P=points(q,k1,k2)
    assert (q-1)*len(P)==(q**k1-1)*(q**k2-1)
    got_d=[];got_m=[]
    for r in range(1,k1+k2+1):
        ctr=collections.Counter(support(B,P,q) for B in subspaces(k1+k2,r,q))
        d=min(ctr);m=ctr[d]
        df,mf=formula(q,k1,k2,r)
        assert (d,m)==(df,mf)
        got_d.append(d);got_m.append(m)
    E=C["verified_examples"][str(q)]
    assert got_d==E["hierarchy"]
    assert got_m==E["minimizer_counts"]
    assert (q-1)*got_m[0]==(q**k1-1)*(q**k2-1)

print("VERIFY_OK")
