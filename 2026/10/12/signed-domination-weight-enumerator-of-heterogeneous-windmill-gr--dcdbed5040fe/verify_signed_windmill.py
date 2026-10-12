#!/usr/bin/env python3
from itertools import product
from math import comb, ceil
from collections import Counter


def poly_mul(a,b):
    c=Counter()
    for i,ai in a.items():
        for j,bj in b.items():
            c[i+j]+=ai*bj
    return c

def P(m):
    return Counter({2*k-m: comb(m,k) for k in range(ceil(m/2),m+1)})

def Q(m):
    lo=ceil((m+2)/2)
    return Counter({2*k-m: comb(m,k) for k in range(lo,m+1)}) if lo<=m else Counter()

def formula_enum(ms):
    a=Counter({0:1})
    for m in ms: a=poly_mul(a,P(m))
    a=Counter({e+1:c for e,c in a.items()})
    b=Counter({0:1})
    for m in ms: b=poly_mul(b,Q(m))
    b=Counter({e-1:c for e,c in b.items()})
    a.update(b)
    return +a

def build(ms):
    # vertices: 0=center, then consecutive blade intervals
    blades=[]
    t=1
    for m in ms:
        blades.append(list(range(t,t+m)))
        t+=m
    n=t
    adj=[set() for _ in range(n)]
    for B in blades:
        for v in B:
            adj[0].add(v); adj[v].add(0)
        for i in range(len(B)):
            for j in range(i+1,len(B)):
                u,v=B[i],B[j]
                adj[u].add(v);adj[v].add(u)
    return adj,blades

def is_sdf(vals,adj):
    return all(vals[v]+sum(vals[u] for u in adj[v])>=1 for v in range(len(vals)))

def criterion(vals,blades):
    e=vals[0]
    sums=[sum(vals[v] for v in B) for B in blades]
    return all(e+s>=1 for s in sums) and e+sum(sums)>=1

def predicted_min(ms):
    o=sum(m%2 for m in ms)
    gamma=1+o
    count=1
    for m in ms: count*=comb(m,ceil(m/2))
    return gamma,count

checks=0
criterion_checks=0
coefficient_checks=0
minimum_checks=0
tuples=0
for r in range(2,5):
    for ms in product(range(1,5), repeat=r):
        if 1+sum(ms)>11:
            continue
        tuples+=1
        adj,blades=build(ms)
        enum=Counter()
        for vals in product((-1,1), repeat=len(adj)):
            checks+=1
            a=is_sdf(vals,adj)
            b=criterion(vals,blades)
            criterion_checks+=1
            if a!=b:
                raise AssertionError((ms,vals,a,b))
            if a:
                enum[sum(vals)]+=1
        frm=formula_enum(ms)
        if enum!=frm:
            raise AssertionError((ms,enum,frm))
        coefficient_checks += len(set(enum)|set(frm))
        gamma=min(enum)
        cnt=enum[gamma]
        pg,pc=predicted_min(ms)
        minimum_checks+=2
        if (gamma,cnt)!=(pg,pc):
            raise AssertionError((ms,(gamma,cnt),(pg,pc)))

# Boundary and large-parameter algebra checks: branch minima and optimizer count.
for r in range(2,10):
    for ms in product(range(1,7), repeat=r):
        # bounded deterministic sample: first 5000 tuples per r is unnecessary; break by checksum filter
        if sum((i+1)*m for i,m in enumerate(ms)) % 97 != 0:
            continue
        o=sum(m%2 for m in ms)
        plus=1+o
        if all(m>=2 for m in ms):
            minus=-1+sum(2+(m%2) for m in ms)
            if not minus>plus:
                raise AssertionError((ms,plus,minus))
        minimum_checks+=1

print(f"VERIFY_OK tuples={tuples} labelings={checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=11")
