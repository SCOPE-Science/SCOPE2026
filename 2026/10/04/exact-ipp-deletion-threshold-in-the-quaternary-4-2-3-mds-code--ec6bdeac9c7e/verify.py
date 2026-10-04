#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

def add(a,b): return a ^ b

def mul(a,b):
    r=0
    while b:
        if b & 1: r ^= a
        b >>= 1
        a <<= 1
        if a & 4: a ^= 0b111
    return r & 3

def codeword(u,v):
    return (u,v,add(u,v),add(u,mul(2,v)))
C=[codeword(u,v) for u in range(4) for v in range(4)]
assert len(set(C))==16
assert min(sum(x!=y for x,y in zip(C[i],C[j])) for i,j in combinations(range(16),2))==3

def bad_triple(indices):
    x,y,z=(C[i] for i in indices)
    return not any(len({x[k],y[k],z[k]})==3 for k in range(4))

def bad_pairing(x,y,z,w):
    return all(({x[k],y[k]} & {z[k],w[k]}) for k in range(4))

bad=[]; bt=bq=0
for I in combinations(range(16),3):
    if bad_triple(I):
        bad.append(sum(1<<i for i in I)); bt+=1
for I in combinations(range(16),4):
    a,b,c,d=(C[i] for i in I)
    if bad_pairing(a,b,c,d) or bad_pairing(a,c,b,d) or bad_pairing(a,d,b,c):
        bad.append(sum(1<<i for i in I)); bq+=1

best=-1; maxima=[]
for mask in range(1<<16):
    size=mask.bit_count()
    if size < best: continue
    if any((mask & e)==e for e in bad): continue
    if size>best:
        best=size; maxima=[mask]
    elif size==best:
        maxima.append(mask)
assert best==8
assert len(maxima)==48

# The twenty affine lines of AG(2,4), in parameter coordinates (u,v).
lines=[]
def add_line(L):
    F=frozenset(L)
    if F not in lines: lines.append(F)
for t in range(4):
    add_line(4*u+t for u in range(4))
for s in range(4):
    for t in range(4):
        add_line(4*u+add(mul(s,u),t) for u in range(4))
for t in range(4):
    add_line(4*t+v for v in range(4))
assert len(lines)==20
profiles=Counter()
for mask in maxima:
    S={i for i in range(16) if (mask>>i)&1}
    c=Counter(len(S & L) for L in lines)
    profiles[tuple(sorted(c.items(), reverse=True))]+=1
expected={((4,2),(2,16),(0,2)):24, ((3,8),(2,4),(1,8)):24}
assert dict(profiles)==expected
print(f"VERIFY_OK maximum={best} maxima={len(maxima)} bad3={bt} bad4={bq} profiles=24+24 subsets={1<<16}")
