#!/usr/bin/env python3
"""Exact rational certificate for the sharp four-site Thue-Morse correlation bound."""
from fractions import Fraction as F
from collections import deque

STATES=((0,0,0),(0,0,1),(0,1,1),(0,1,2),(1,1,1),(1,1,2),(1,2,2),(1,2,3))
INDEX={s:i for i,s in enumerate(STATES)}
V0=tuple(map(F, ('1','-1/3','1','-1/3','-1/3','-1/3','-1/3','1/3')))
V1_EXPECT=tuple(map(F,('1/3','1/3','-1/3','0','1/3','0','0','1/3')))

def transition(r):
    rows=[]
    for a,b,c in STATES:
        L=(r+a,2*r+b,3*r+c)
        q=tuple(x//2 for x in L)
        e=tuple(x%2 for x in L)
        rows.append(((-1)**sum(e),INDEX[q],INDEX[tuple(x+y for x,y in zip(q,e))]))
    return tuple(rows)

M0,M1=transition(0),transition(1)
assert M0==((1,0,0),(-1,0,1),(1,0,2),(-1,1,2),(-1,0,4),(1,1,4),(-1,2,4),(1,2,5))
assert M1==((1,2,5),(-1,3,5),(1,3,6),(-1,3,7),(-1,5,6),(1,5,7),(-1,6,7),(1,7,7))

def apply(M,v):
    return tuple(sign*(v[i]+v[j])/2 for sign,i,j in M)
assert apply(M1,V0)==V1_EXPECT
assert apply(M0,V0)==V0 # V0 as h=0 fixed

def pattern(v):
    return tuple(1 if x==F(1,3) else -1 if x==-F(1,3) else 0 for x in v)

def pat_apply(M, p):
    return tuple(sign*p[i] if p[i]!=0 and p[i]==p[j] else 0 for sign,i,j in M)

seed=pattern(V1_EXPECT)
q=deque([seed]); seen={seed}; transitions={}
while q:
    p=q.popleft()
    nexts=(pat_apply(M0,p),pat_apply(M1,p))
    transitions[p]=nexts
    for z in nexts:
        if z not in seen:
            seen.add(z);q.append(z)
expected_strings={'++-.+..+','+-..-+..','.......+','+....-..','........','+.......'}
enc=lambda p:''.join('+' if c>0 else '-' if c<0 else '.' for c in p)
assert {enc(p) for p in seen}==expected_strings
expected_table={
    '++-.+..+':('+-..-+..','.......+'),
    '+-..-+..':('+....-..','........'),
    '.......+':('........','.......+'),
    '+....-..':('+.......','........'),
    '........':('........','........'),
    '+.......':('+.......','........'),
}
assert {enc(p):tuple(enc(z) for z in transitions[p]) for p in seen}==expected_table

from functools import lru_cache
@lru_cache(None)
def V(h):
    if h==1:return V1_EXPECT
    assert h>=2
    return apply(M0 if h%2==0 else M1,V(h//2))
for h in range(1,10001):
    p=pattern(V(h))
    assert p[0] == (1 if h&(h-1)==0 else 0), (h,V(h)[0])
    assert abs(V(h)[0])<=F(1,3)
    # Each coordinate remains in the bound.
    assert max(map(abs,V(h)))<=F(1,3)

# Independent finite-prefix cross-check of literal binary signs.
L=17
T=[(-1 if (n.bit_count()%2) else 1) for n in range(2**L+3*35)]
for h in range(1,36):
    Q=sum(T[n]*T[n+h]*T[n+2*h]*T[n+3*h] for n in range(2**L))
    assert abs(F(Q,2**L)-V(h)[0])<=F(20*h,2**L),(h,Q,V(h)[0])
print('VERIFY_OK: eight exact renormalization rows, six exhaustive saturation types, 10000 exact lag evaluations, 35 independent block comparisons')
print('CERTIFICATE_TABLE:')
for key in sorted(expected_table): print(key, '->', expected_table[key])
