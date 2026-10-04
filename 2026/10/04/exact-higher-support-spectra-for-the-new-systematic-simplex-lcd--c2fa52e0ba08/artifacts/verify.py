#!/usr/bin/env python3
import itertools, math, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def qbinom(n,r,q):
    if r<0 or r>n: return 0
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def full_count(s,r,q):
    return sum((-1)**j*math.comb(s,j)*qbinom(s-j,r,q) for j in range(s+1))

def formula(q,m,r):
    base=q**m-q**(m-r)
    return {base+s:math.comb(m,s)*full_count(s,r,q)
            for s in range(r,m+1) if math.comb(m,s)*full_count(s,r,q)}

def rref_subspaces(m,r,q):
    for piv in itertools.combinations(range(m),r):
        P=set(piv)
        free=[]
        for i,p in enumerate(piv):
            for c in range(p+1,m):
                if c not in P:
                    free.append((i,c))
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*m for _ in range(r)]
            for i,p in enumerate(piv): B[i][p]=1
            for (i,c),v in zip(free,vals): B[i][c]=v
            yield B

def generator(q,m):
    cols=[]
    for j in range(m):
        v=[0]*m;v[j]=1;cols.append(tuple(v))
    for v in itertools.product(range(q),repeat=m):
        if any(v): cols.append(tuple(v))
    return cols

def support_size(B,cols,q):
    return sum(any(sum(row[i]*col[i] for i in range(len(col)))%q for row in B)
               for col in cols)

for q,m in [(2,3),(2,4),(3,2),(3,3)]:
    cols=generator(q,m)
    key=f"q{q}_m{m}"
    got_h=[]
    got_s={}
    for r in range(1,m+1):
        ctr=collections.Counter(support_size(B,cols,q) for B in rref_subspaces(m,r,q))
        f=formula(q,m,r)
        assert dict(sorted(ctr.items()))==f
        assert sum(ctr.values())==qbinom(m,r,q)
        got_h.append(min(ctr))
        got_s[str(r)]={str(k):v for k,v in sorted(ctr.items())}
    assert got_h==cert["verified_examples"][key]["hierarchy"]
    assert got_s==cert["verified_examples"][key]["spectra"]

print("VERIFY_OK")
