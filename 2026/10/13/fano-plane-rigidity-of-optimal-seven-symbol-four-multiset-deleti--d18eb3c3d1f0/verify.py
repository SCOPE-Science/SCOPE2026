#!/usr/bin/env python3
"""Finite checks for the seven-symbol extremal construction."""
from itertools import combinations, permutations

P = tuple(range(7))
ALL_PAIRS = tuple(combinations(P,2))
TRIPLES = tuple(combinations(P,3))

# Enumerate labeled Steiner triple systems S(2,3,7) by exact pair partitions.
pair_pos = {p:i for i,p in enumerate(ALL_PAIRS)}
trip_masks=[]
for t in TRIPLES:
    mask=sum(1<<pair_pos[p] for p in combinations(t,2))
    trip_masks.append(mask)
full=(1<<len(ALL_PAIRS))-1
systems=[]
def rec(used,chosen):
    if used == full:
        assert len(chosen)==7
        systems.append(tuple(chosen));return
    # Smallest uncovered pair, choose a containing triple.
    rem=full^used
    k=(rem & -rem).bit_length()-1
    for j,mask in enumerate(trip_masks):
        if (mask & (1<<k)) and not (mask&used):
            rec(used|mask,chosen+[j])
rec(0,[])
assert len(systems)==30, len(systems)

# Enumerate 210 weak compositions of weight 4 in seven coordinates.
profiles=[]
def comps(length,left,seq):
    if length==1:
        profiles.append(tuple(seq+[left]));return
    for v in range(left+1):comps(length-1,left-v,seq+[v])
comps(7,4,[])
assert len(profiles)==210

# Every Fano plane yields the claimed size-35 independent set.
seen=set();universal_even=set()
for i in P:
    e=[0]*7;e[i]=4;universal_even.add(tuple(e))
for i,j in ALL_PAIRS:
    e=[0]*7;e[i]=e[j]=2;universal_even.add(tuple(e))
assert len(universal_even)==28
for sys in systems:
    lines=[set(TRIPLES[j]) for j in sys]
    code=universal_even | {tuple(0 if i in line else 1 for i in P) for line in lines}
    assert len(code)==35
    for a,b in combinations(code,2):
        assert sum(abs(x-y) for x,y in zip(a,b))>=4
    seen.add(frozenset(code))
assert len(seen)==30

# All 30 are one orbit; the Fano automorphism order is 7!/30=168.
base=next(iter(seen))
orbit=set()
for p in permutations(P):
    orbit.add(frozenset(tuple(x[p[i]] for i in P) for x in base))
assert orbit == seen and len(orbit)==30

# Check directed-arc count identities for all 210 vectors.
for w in profiles:
    arc=sum(w[i]>=2 and w[j]>=1 for i in P for j in P if i!=j)
    t=tuple(sorted((v for v in w if v),reverse=True))
    assert arc=={(4,):0,(3,1):1,(2,2):2,(2,1,1):2,(1,1,1,1):0}[t]
print('VERIFY_OK: 210 profiles, 30 labeled Fano planes, 30 optimal code constructions, unique orbit, 168 stabilizer')
