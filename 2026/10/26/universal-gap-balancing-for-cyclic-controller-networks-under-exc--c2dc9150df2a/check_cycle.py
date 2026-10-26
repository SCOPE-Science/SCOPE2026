#!/usr/bin/env python3
"""Recompute exact outage counts for controlled cycles; independently enumerate vertex failures."""
from math import comb
from itertools import combinations
from collections import Counter

def B(a,b): return comb(a,b) if a>=0 and 0<=b<=a else 0

def F(n,r,d):
    return sum(B(n-1,r)-B(n-1-t,r)-B(n-1-d+t,r)+B(n-1-d,r) for t in range(1,d))

def f2(n,r,d):
    return (d-1)*(B(n-1,r)+B(n-1-d,r))-2*(B(n-1,r+1)-B(n-d,r+1))

def gaps(n,controllers):
    d=sorted(controllers)
    return [((d[(i+1)%len(d)]-d[i])%n) for i in range(len(d))]

def covered(n,controllers,failed):
    controllers=set(controllers); failed=set(failed)
    seen=set(); total=0
    for v in range(n):
        if v in failed or v in seen:continue
        component={v}; frontier=[v];seen.add(v)
        while frontier:
            x=frontier.pop()
            for y in ((x-1)%n,(x+1)%n):
                if y not in failed and y not in seen:
                    seen.add(y);component.add(y);frontier.append(y)
        if component.intersection(controllers): total+=len(component)
    return total

def run():
    checks=0; positions=0; optimizers=0
    for n in range(3,10):
        for k in range(2,n+1):
            for r in range(2,n+1):
                rows=[]; bvals=[]
                for D in combinations(range(n),k):
                    analytic=sum(F(n,r,d) for d in gaps(n,D))
                    assert analytic==sum(f2(n,r,d) for d in gaps(n,D))
                    experimental=sum(n-r-covered(n,D,A) for A in combinations(range(n),r))
                    assert experimental==analytic,(n,k,r,D,analytic,experimental)
                    rows.append((analytic,D)); checks+=1
                q,s=divmod(n,k)
                optimal=(k-s)*F(n,r,q)+s*F(n,r,q+1)
                assert min(v for v,D in rows)==optimal,(n,k,r,optimal,rows)
                positions+=len(rows)
                if k>r:
                    assert all((v==optimal)==(max(gaps(n,D))-min(gaps(n,D))<=1) for v,D in rows),(n,k,r)
                    optimizers+=1
    for n in range(4,32):
        for r in range(2,n+1):
            for d in range(2,n-1):
                assert F(n,r,d+1)-2*F(n,r,d)+F(n,r,d-1)==d*B(n-2-d,r-2),(n,r,d)
    for n in range(4,32):
        for d in range(1,n): assert F(n,2,d)==comb(d+1,3),(n,d)
    print('PASS: exact pair enumeration, balanced global optimality, and uniqueness if k>r; cycles n=3..9, k=2..n, r=2..n')
    print('PASS: discrete second difference identity n=4..31 r=2..n; exact 2-failure simplification')
    print('strategy triples:',checks,'tested profiles:',positions,'unique-optimality parameter triples:',optimizers)
if __name__=='__main__':run()
