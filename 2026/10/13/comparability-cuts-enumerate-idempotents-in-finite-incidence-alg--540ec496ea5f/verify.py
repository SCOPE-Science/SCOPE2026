#!/usr/bin/env python3
from itertools import combinations, product

def relations(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for mask in range(1<<len(pairs)):
        R={(i,i) for i in range(n)}
        for k,p in enumerate(pairs):
            if mask>>k & 1: R.add(p)
        ok=True
        for i,j in tuple(R):
            for j2,k in tuple(R):
                if j==j2 and (i,k) not in R:
                    ok=False; break
            if not ok: break
        if ok: out.append(R)
    return out

def comparable_edges(n,R):
    return [(i,j) for i in range(n) for j in range(i+1,n) if (i,j) in R]

def formula_count(n,R,q):
    E=comparable_edges(n,R)
    ans=0
    for mask in range(1<<n):
        cut=sum(((mask>>i)&1)!=((mask>>j)&1) for i,j in E)
        ans += q**cut
    return ans

def convolution(a,b,basis,R,q):
    idx={xy:k for k,xy in enumerate(basis)}
    c=[0]*len(basis)
    for k,(x,y) in enumerate(basis):
        s=0
        for z in range(x,y+1):
            if (x,z) in R and (z,y) in R:
                s += a[idx[(x,z)]]*b[idx[(z,y)]]
        c[k]=s%q
    return tuple(c)

def brute_count(n,R,q):
    basis=sorted(R)
    total=0
    for a in product(range(q), repeat=len(basis)):
        if convolution(a,a,basis,R,q)==a:
            total += 1
    return total

def cut_poly(n,R):
    E=comparable_edges(n,R)
    coeff={}
    for mask in range(1<<n):
        c=sum(((mask>>i)&1)!=((mask>>j)&1) for i,j in E)
        coeff[c]=coeff.get(c,0)+1
    return coeff

cases=0
for n in range(1,5):
    for R in relations(n):
        q=2
        assert brute_count(n,R,q)==formula_count(n,R,q)
        p=cut_poly(n,R)
        assert max(p)==max(sum(((m>>i)&1)!=((m>>j)&1) for i,j in comparable_edges(n,R)) for m in range(1<<n))
        cases += 1
for n in range(1,4):
    for R in relations(n):
        q=3
        assert brute_count(n,R,q)==formula_count(n,R,q)
        cases += 1
# Chain specialization.
from math import comb
for n in range(1,9):
    R={(i,j) for i in range(n) for j in range(i,n)}
    for q in (2,3,5):
        lhs=formula_count(n,R,q)
        rhs=sum(comb(n,r)*q**(r*(n-r)) for r in range(n+1))
        assert lhs==rhs
print(f"VERIFY_OK cases={cases}")
