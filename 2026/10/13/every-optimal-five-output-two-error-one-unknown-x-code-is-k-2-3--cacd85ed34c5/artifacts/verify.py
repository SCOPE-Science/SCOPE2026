#!/usr/bin/env python3
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import json

M=5
V=tuple(range(1,1<<M))

def is_xcode_direct(code):
    code=tuple(code)
    # Standard (m,n,2,1) condition: one unknown codeword may not cover
    # the XOR of either one or two disjoint error codewords.
    for u in code:
        for a in code:
            if a==u:
                continue
            if a & ~u == 0:
                return False
        rem=[a for a in code if a!=u]
        for a,b in combinations(rem,2):
            if (a^b) & ~u == 0:
                return False
    return True

def is_xcode_setform(code):
    # Independent support-set formulation: antichain plus the
    # three-support symmetric-difference obstruction.
    C=tuple(frozenset(i for i in range(M) if (v>>i)&1) for v in code)
    for A,B in combinations(C,2):
        if A <= B or B <= A:
            return False
    for A,B,D in combinations(C,3):
        if (A^B) <= D or (A^D) <= B or (B^D) <= A:
            return False
    return True

def ok_add(S,v):
    for a in S:
        if (a & ~v)==0 or (v & ~a)==0:
            return False
    for a,b in combinations(S,2):
        if (a^b) & ~v == 0:
            return False
    for a in S:
        x=a^v
        for c in S:
            if c!=a and x & ~c == 0:
                return False
    return True

# A zero column cannot occur in any code of size at least two: choosing it
# as a one-error word gives zero XOR, which every unknown word covers.
# Since a six-word construction is checked below, it is exhaustive to search
# the 31 nonzero columns for the optimum.

# Method A: complete include/exclude search over the 31 nonzero columns.
best=0; maxima=set(); nodes=0
def search(S,cands):
    global best,nodes,maxima
    nodes+=1
    if len(S)+len(cands)<best:
        return
    if not cands:
        t=tuple(sorted(S))
        if len(S)>best:
            best=len(S); maxima={t}
        elif len(S)==best:
            maxima.add(t)
        return
    v=cands[0]
    rest=cands[1:]
    if ok_add(S,v):
        new=[w for w in rest if ok_add(S+[v],w)]
        search(S+[v],new)
    search(S,rest)
search([],list(V))
assert best==6, best
assert len(maxima)==10, len(maxima)

# Method B: exhaustive fixed-size census. Both independently coded predicates
# are evaluated on every one of the C(31,6) and C(31,7) candidate families.
valid6=[]
for C in combinations(V,6):
    a=is_xcode_direct(C); b=is_xcode_setform(C)
    assert a==b
    if a:
        valid6.append(C)
assert len(valid6)==10
assert set(valid6)==maxima
valid7=0
for C in combinations(V,7):
    a=is_xcode_direct(C); b=is_xcode_setform(C)
    assert a==b
    if a:
        valid7 += 1
assert valid7==0

# Structural classification.
def edge(v):
    pts=[i for i in range(M) if (v>>i)&1]
    assert len(pts)==2
    return tuple(pts)

def is_K23(C):
    if any(v.bit_count()!=2 for v in C):
        return False
    deg=[0]*M
    E={edge(v) for v in C}
    for a,b in E:
        deg[a]+=1; deg[b]+=1
    if sorted(deg)!=[2,2,2,3,3]:
        return False
    side2={i for i,d in enumerate(deg) if d==3}
    side3=set(range(M))-side2
    return E=={tuple(sorted((a,b))) for a in side2 for b in side3}
assert all(is_K23(C) for C in valid6)

k23=[]
for side2 in combinations(range(M),2):
    side2=set(side2); side3=set(range(M))-side2
    C=tuple(sorted((1<<a)|(1<<b) for a in side2 for b in side3))
    k23.append(C)
assert set(k23)==set(valid6)

# Verify the packaged census itself.
census_path=Path(__file__).with_name('census.json')
obj=json.loads(census_path.read_text(encoding='utf-8'))
from_file={tuple(x['column_masks']) for x in obj['maxima']}
assert obj['maximum_n']==6 and obj['labeled_maxima']==10
assert from_file==set(valid6)

# Coordinate-permutation orbit and stabilizer.
def perm_word(v,p):
    out=0
    for i in range(M):
        if (v>>i)&1:
            out |= 1<<p[i]
    return out
rep=valid6[0]
orb=set(); stab=0
for p in permutations(range(M)):
    T=tuple(sorted(perm_word(v,p) for v in rep))
    orb.add(T)
    if T==rep:
        stab+=1
assert orb==set(valid6)
assert len(orb)==10 and stab==12

# Context check: m=5 is the first dimension in this parameter family with
# strict compaction n>m.
def maximum_for_m(m):
    verts=list(range(1,1<<m))
    def okadd(S,v):
        for a in S:
            if (a & ~v)==0 or (v & ~a)==0:
                return False
        for a,b in combinations(S,2):
            if (a^b) & ~v == 0:
                return False
        for a in S:
            x=a^v
            for c in S:
                if c!=a and x & ~c == 0:
                    return False
        return True
    b=0
    def rec(S,cands):
        nonlocal b
        if len(S)+len(cands)<=b:
            return
        if len(S)>b:
            b=len(S)
        for j,v in enumerate(cands):
            if okadd(S,v):
                new=[w for w in cands[j+1:] if okadd(S+[v],w)]
                rec(S+[v],new)
    rec([],verts)
    return b
small=[maximum_for_m(m) for m in range(1,5)]
assert small==[1,2,3,4]

print(f'COMBINATIONS_CHECKED_6={comb(31,6)}')
print(f'COMBINATIONS_CHECKED_7={comb(31,7)}')
print(f'SEARCH_NODES={nodes}')
print('SMALL_MAXIMA=' + ','.join(map(str,small)))
print('VERIFY_OK M(5,2,1)=6 labeled_maxima=10 all_K23=true S5_orbits=1 orbit_size=10 stabilizer=12')
