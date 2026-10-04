#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, Counter
import json
from pathlib import Path
MOD=(1<<9)|(1<<4)|1; MASK=(1<<9)-1

def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1; a<<=1
        if a&(1<<9):a^=MOD
    return r&MASK

def pw(a,e):
    r=1
    while e:
        if e&1:r=mul(r,a)
        a=mul(a,a); e//=2
    return r
x=2
assert pw(x,511)==1 and pw(x,73)!=1 and pw(x,7)!=1
theta=pw(x,7); assert pw(theta,73)==1 and theta!=1
# cyclotomic cosets
C1=set(); a=1
while a not in C1:C1.add(a); a=(2*a)%73
C3=set(); a=3
while a not in C3:C3.add(a); a=(2*a)%73
assert len(C1)==len(C3)==9 and C1.isdisjoint(C3)
assert 73-len(C1|C3)==55
# Minimal-polynomial and generator-polynomial consistency.
def peval(poly, a):
    r=0
    for i in range(poly.bit_length()-1, -1, -1):
        r=mul(r,a)
        if (poly>>i)&1:r^=1
    return r
def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
    return r
f1=sum(1<<i for i in [9,7,4,3,0])
f3=sum(1<<i for i in [9,4,2,1,0])
assert peval(f1,theta)==0 and peval(f3,pw(theta,3))==0
G=pmul(f1,f3)
assert [i for i in range(19) if (G>>i)&1]==[0,1,2,3,4,6,9,10,12,16,18]
vals=[pw(theta,i) for i in range(73)]; cubes=[pw(theta,3*i) for i in range(73)]
# no weight 5 after shifting one support position to 0
by=defaultdict(list)
for a,b in combinations(range(1,73),2):by[(vals[a]^vals[b],cubes[a]^cubes[b])].append((a,b))
for (u,v),arr in by.items():
    for a,b in arr:
        for c,d in by.get((u^1,v^1),[]):
            assert len({a,b,c,d})<4
# count weight 6
B=defaultdict(list)
for T in combinations(range(73),3):
    B[(vals[T[0]]^vals[T[1]]^vals[T[2]],cubes[T[0]]^cubes[T[1]]^cubes[T[2]])].append(T)
counts=Counter()
for arr in B.values():
    for i,A in enumerate(arr):
        s=set(A)
        for B0 in arr[:i]:
            if s.isdisjoint(B0):counts[tuple(sorted(A+B0))]+=1
assert sum(counts.values())==8760
assert len(counts)==876 and set(counts.values())=={10}
for S in counts:
    u=v=0
    for i in S:u^=vals[i];v^=cubes[i]
    assert u==v==0

def canon(S):return min(tuple(sorted((i-t)%73 for i in S)) for t in range(73))
orbits=defaultdict(list)
for S in counts:orbits[canon(S)].append(S)
assert len(orbits)==12 and all(len(v)==73 for v in orbits.values())
cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text())
assert cert['minimum_weight_codewords']==876 and cert['cyclic_orbits']==12
assert cert['orbit_representatives']==[list(r) for r in sorted(orbits)]
print('VERIFY_OK')
