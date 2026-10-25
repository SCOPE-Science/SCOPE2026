#!/usr/bin/env python3
"""Exact bounded-height-three Dyck arch-index checks (stdlib only)."""
from collections import defaultdict
from fractions import Fraction
from itertools import product

H=3
states=[(h,b,m) for h in range(H+1) for b in (0,1) if not ((h==0 and b!=1) or (h==H and b!=0)) for m in (0,1)]
assert len(states)==12
step={}
for h,b,m in states:
    arcs=[]
    for c in (0,1):
        hh=h+(1 if c==0 else -1)
        if 0<=hh<=H:
            mm=int(c!=b and not m)
            arcs.append(((hh,c,mm),mm))
    step[(h,b,m)]=arcs

# Polynomial arrays in u, coefficients counted exactly in Z.
def add_scaled(a,b,shift=0):
    c=a[:]
    if len(c)<len(b)+shift:c += [0]*(len(b)+shift-len(c))
    for k,v in enumerate(b):c[k+shift]+=v
    return c

# Counts for every length in transitions of this deterministic finite graph.
P=[{(1,0,0):[1]}]  # the initial 0, length 1
for j in range(1,23):
    d={}
    for s,v in P[-1].items():
        for t,k in step[s]:d[t]=add_scaled(d.get(t,[]),v,k)
    P.append(d)

def coefficient(i):
    if i==0:return [1]
    d=P[2*i-1]
    v=[]
    for s,poly in d.items():
        if s[0]==0:v=add_scaled(v,poly)
    return v

# Predicted bivariate rational function N(z,u)/D(z,u):
# N=1-4uz+(u+4u²)z²+(u-3u²)z³
# D=(1-uz)((1-2uz)²-u²z³)
#   = 1-5uz+8u²z²+(-4u³-u²)z³+u³z⁴
N=[[1],[0,-4],[0,1,4],[0,1,-3]]
D=[[1],[0,-5],[0,0,8],[0,0,-1,-4],[0,0,0,1]]

# Compare the series identity D*F=N to order z^10. Matrix inverse
# numerator and denominator have degrees <= 12 in word-length x;
# cross multiplying with proposed N,D (x-degrees 6,8) yields polynomial
# x-degree <=20, so matching all x<=20 proves exact rational equality.
for n in range(11):
    lhs=[]
    for j in range(min(n,4)+1):
        a=D[j];b=coefficient(n-j)
        cv=[0]*(len(a)+len(b)-1)
        for k,v in enumerate(a):
            for l,w in enumerate(b):cv[k+l]+=v*w
        lhs=add_scaled(lhs,cv)
    rhs=N[n] if n<len(N) else []
    for i in range(max(len(lhs),len(rhs))):
        assert (lhs[i] if i<len(lhs) else 0)==(rhs[i] if i<len(rhs) else 0),(n,i,lhs,rhs)

# Independent brute force: generate every Dyck word of height <= 3,
# compute minimal greedy arches directly and compare all coefficients.
def words(n):
    def rec(w,z,o,h):
        if z==n and o==n:
            yield w
            return
        if z<n and h<H:
            yield from rec(w+'0',z+1,o,h+1)
        if o<z:
            yield from rec(w+'1',z,o+1,h-1)
    yield from rec('',0,0,0)

def arch(w):
    j=k=0
    while j<len(w):
        a=w[j];j+=1
        while j<len(w) and w[j]==a:j+=1
        if j==len(w):break
        j+=1;k+=1
    return k

for n in range(11):
    hist=defaultdict(int)
    for w in words(n):hist[arch(w)]+=1
    p=coefficient(n)
    assert all(hist[k]==(p[k] if k<len(p) else 0) for k in set(hist)|set(range(len(p)))),(n,hist,p)
    if n<=8:
        for w in words(n):
            ki=arch(w)
            for v in product('01',repeat=ki):
                it=iter(w)
                assert all(any(ch==c for c in it) for ch in v)
            absent=False
            for v in product('01',repeat=ki+1):
                it=iter(w)
                if not all(any(ch==c for c in it) for ch in v):
                    absent=True;break
            assert absent
    print('n=',n,'Dyck=',sum(hist.values()),'hist=',sorted(hist.items()))
print('HEIGHT3_DYCK_ARCH_DISTRIBUTION_PASS')
