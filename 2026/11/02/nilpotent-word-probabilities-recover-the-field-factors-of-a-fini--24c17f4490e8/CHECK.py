#!/usr/bin/env python3
"""Exact independent finite-ring product enumeration for a nilpotent-word profile."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement

def gf8_mul(x,y):
    v=0
    for i in range(3):
        if (y>>i)&1: v^=x<<i
    for j in range(4,2,-1):
        if (v>>j)&1:v ^= 0b1011 << (j-3)
    return v

def products(name,elts,mult,is_nil,fs,max_k=6):
    N=len(elts)
    freq={x:1 for x in elts}
    for k in range(1,max_k+1):
        cnt=sum(v for x,v in freq.items() if is_nil(x))
        direct=Q(cnt,N**k)
        predicted=Q(1,1)
        for q in fs:predicted *= 1-(Q(q-1,q)**k)
        assert direct==predicted,(name,k,direct,predicted)
        if k==max_k: print(f'{name}: size={N} quotient={fs} k=1..{max_k} verified, P_{max_k}={direct}')
        new=defaultdict(int)
        for x,c in freq.items():
            for y in elts:new[mult(x,y)]+=c
        freq=new

# A square-zero unital radical extension Z/4Z.
products('Z4',list(range(4)),lambda x,y:(x*y)%4,lambda x:x%2==0,[2])
# Commutative semisimple quotient F2 x F2.
E=list(product(range(2),repeat=2))
products('F2xF2',E,lambda x,y:(x[0]*y[0],x[1]*y[1]),lambda x:x==(0,0),[2,2])
# Noncommutative upper triangular 2x2 matrices over F2.
T=list(product(range(2),repeat=3))
products('T2F2',T,lambda x,y:(x[0]*y[0],(x[0]*y[1]+x[1]*y[2])%2,x[2]*y[2]),lambda x:x[0]==x[2]==0,[2,2])
# Field F8, explicit irreducible polynomial X^3+X+1.
products('F8',list(range(8)),gf8_mul,lambda x:x==0,[8])
# Semisimple R=F2^3 x F3; a published P2 collision with F8.
R=list(product(range(2),repeat=3))
R=[t+(u,) for t in R for u in range(3)]
products('F2cubexF3',R,lambda x,y:tuple((x[i]*y[i])%([2,2,2,3][i]) for i in range(4)),lambda x:all(c==0 for c in x),[2,2,2,3])
assert Q(1,1)-(Q(7,8)**2)==Q(15,64)
assert ((1-Q(1,2)**2)**3)*(1-Q(2,3)**2)==Q(15,64)
assert 1-(Q(7,8)**3)==Q(169,512)
assert ((1-Q(1,2)**3)**3)*(1-Q(2,3)**3)==Q(6517,13824)
print('P2 collision: F8 vs F2^3xF3 = 15/64; P3: 169/512 != 6517/13824')
# A diagnostic, not a universal proof: all multisets of up to 3 selected finite-field sizes.
Qs=(2,3,4,5,7,8,9,11)
seen={}
for r in range(1,4):
    for fields in combinations_with_replacement(Qs,r):
        profile=tuple(__import__('functools').reduce(lambda x,q:x*(1-Q(q-1,q)**k),fields,Q(1,1)) for k in range(1,15))
        assert profile not in seen,(fields,seen.get(profile))
        seen[profile]=fields
print(f'{len(seen)} distinct field-factor multisets: length-14 profile separation diagnostic')
print('VERIFY_OK')
