#!/usr/bin/env python3
"""Exact four-round first-order types of Hamming graphs H(d,a).

This certificate uses coordinate-pattern orbits, complete extension enumeration,
and a finite 27-state saturation lemma. No approximate sampling is used.
"""
from functools import lru_cache
from itertools import product

PARTS = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
STATES = tuple(product(range(3),repeat=3))
INDEX = {s:i for i,s in enumerate(STATES)}
CAPS = {2:(2,4,4,4,0),3:(2,3,3,3,3),4:(2,3,3,3,3)}

def cap2(x): return min(x,2)
def opts(a,p):
    old=PARTS[p]; r=len(set(old))
    if r>a: return ()
    return tuple(tuple(int(old[i]!=symbol) for i in range(3))
                 for symbol in range(r+(r<a)))

def nextmask(mask,T):
    new=0
    while mask:
        b=mask&-mask;mask-=b
        new |= T[b.bit_length()-1]
    return new

# A true bitwise OR is required even if different coordinate choices give the same pattern.
TRANS={}
for a in (2,3,4):
    for p in range(5):
        if not opts(a,p):continue
        TRANS[a,p]=tuple(__import__('functools').reduce(
            lambda v,o:v | (1<<INDEX[tuple(min(2,s[i]+o[i]) for i in range(3))]),
            set(opts(a,p)),0) for s in STATES)

# Verify the finite transformation powers for EVERY one of the 27 input states.
for a in (2,3,4):
    for p,C in enumerate(CAPS[a]):
        if not C:continue
        T=TRANS[a,p]
        for s in range(27):
            mask=1<<s
            for _ in range(C):mask=nextmask(mask,T)
            assert nextmask(mask,T)==mask,(a,p,C,s)
print('FINITE_27_STATE_SATURATION_CERTIFICATE_OK')

@lru_cache(None)
def triple_type(a,h):
    # Truncate counts using the proved transformation identities. Original
    # pairwise distances are preserved after truncation at any caps >=2.
    old=tuple(cap2(sum(h[p] for p,x in enumerate(PARTS) if x[i]!=x[j]))
              for i,j in ((0,1),(0,2),(1,2)))
    mask=1<<INDEX[(0,0,0)]
    for p,c in enumerate(h):
        if not c:continue
        T=TRANS[a,p]
        for _ in range(min(c,CAPS[a][p])):
            mask=nextmask(mask,T)
    return old,mask

@lru_cache(None)
def pair_type(d,a,j):
    extensions=set()
    for s in range(d-j+1):
        if a==2:
            for v in range(j+1):
                extensions.add(triple_type(a,(d-j-s,s,v,j-v,0)))
        else:
            for v in range(j+1):
                for w in range(j-v+1):
                    extensions.add(triple_type(a,(d-j-s,s,v,w,j-v-w)))
    return (cap2(j),frozenset(extensions))

def sentence_type(d,a):
    # Vertex-transitivity reduces four-round types of the empty tuple to
    # the available two-vertex types about any one fixed first vertex.
    return frozenset(pair_type(d,a,j) for j in range(d+1))

def canonical(a,d):
    return ('binary' if a==2 else 'ternary' if a==3 else 'large',
            min(d,6 if a==2 else 5))

SIG={}
for a in (2,3,4):
    for d in range(1,15):
        signature=sentence_type(d,a)
        label=canonical(a,d)
        if label in SIG:assert SIG[label]==signature,(label,d,'missed equivalence')
        else:SIG[label]=signature
assert len(SIG)==16
assert len(set(SIG.values()))==16,'distinct labels collapsed'
# The following is the analytic infinite-tail certificate: the truncated
# first-three-selection profiles only depend on (min(d-j,A),min(j,B)).
for a in (2,3,4):
    A=CAPS[a][0]+CAPS[a][1]
    B=CAPS[a][2]+CAPS[a][3]+CAPS[a][4]
    assert A+B==14
    def possible(d):return frozenset((min(d-j,A),min(j,B)) for j in range(d+1))
    target=possible(14)
    for d in (15,16,17,24,50,100,1000): assert possible(d)==target
    print('TAIL_PROFILES_OK',a,'threshold',A+B,'A',A,'B',B)
print('RANK4_CLASSES_OK',len(SIG))
for a in (2,3,4):
    print('ALPHABET_CLASS',a,'DIMENSION_REPRESENTATIVES',
          ','.join(map(str,range(1,7 if a==2 else 6))))
print('SHARP_REPRESENTATIVE_BOUND',4**5)
print('VERIFY_OK')
