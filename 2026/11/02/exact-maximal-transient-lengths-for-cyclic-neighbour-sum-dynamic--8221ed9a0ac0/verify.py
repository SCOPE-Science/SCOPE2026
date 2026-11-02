#!/usr/bin/env python3
"""Exact finite checks for cyclic neighbour-sum transient lengths.
Finite checks supplement, rather than replace, the uniform proof.
"""
from itertools import product
from math import gcd

def vp(n,p):
    v=0
    while n%p==0:
        n//=p; v+=1
    return v

def factors(n):
    a=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d;e+=1
            a.append((d,e))
        d+=1
    if n>1:a.append((n,1))
    return a

def tau(m,n):
    if m==1:return 0
    z=[]
    for p,a in factors(m):
        d=vp(n,p)
        if p==2:
            z.append(a if d==0 else (1<<(d-1))*(a+1))
        elif n%2:
            z.append(0)
        elif d==0:
            z.append(1)
        else:
            z.append(p**d+(a-1)*(p-1)*p**(d-1))
    return max(z)

def nil_index(p,a,d):
    q=p**d;mod=p**a
    w=[1]+[0]*(q-1)
    for j in range(1,q*a+q+1):
        w=[(w[i]+((-1) if p!=2 else 1)*w[(i-1)%q])%mod for i in range(q)]
        if not any(w):return j
    raise AssertionError((p,a,d))

cases=0
for p in [2,3,5,7,11]:
    for d in range(1,4):
        if p**d>135:continue
        for a in range(1,6):
            expect=p**d+(a-1)*(p-1)*p**(d-1)
            got=nil_index(p,a,d)
            assert got==expect,(p,a,d,got,expect)
            cases+=1

# Independent functional-graph enumeration of all states in manageable finite modules.
# An orbit's transient is the number of iterates preceding its first cycle entry.

def exhaustive(m,n):
    limit=m**n
    nxt=[0]*limit
    for state in range(limit):
        x=state
        t=[]
        for _ in range(n):
            t.append(x%m);x//=m
        u=[(t[i]+t[(i+1)%n])%m for i in range(n)]
        idx=0
        for j in range(n-1,-1,-1):idx=idx*m+u[j]
        nxt[state]=idx
    dist=[-1]*limit
    for s in range(limit):
        if dist[s]>=0:continue
        route=[];vis={};u=s
        while dist[u]<0 and u not in vis:
            vis[u]=len(route);route.append(u);u=nxt[u]
        if dist[u]>=0:
            d=dist[u]
            for v in reversed(route):d+=1;dist[v]=d
        else:
            st=vis[u]
            for v in route[st:]:dist[v]=0
            d=0
            for v in reversed(route[:st]):d+=1;dist[v]=d
    return max(dist)

nchecks=0
for m in range(1,16):
    for n in range(1,12):
        if m**n>50000:continue
        got=exhaustive(m,n)
        expect=tau(m,n)
        assert got==expect,(m,n,got,expect)
        nchecks+=1

print('VERIFY_OK', 'prime_power_cases='+str(cases), 'whole_state_cases='+str(nchecks),
      'examples='+','.join(f'{m}:{n}:{tau(m,n)}' for m,n in [(8,12),(9,6),(12,5),(25,10),(16,8)]))
