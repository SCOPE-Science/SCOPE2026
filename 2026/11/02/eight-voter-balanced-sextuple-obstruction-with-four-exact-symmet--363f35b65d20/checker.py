#!/usr/bin/env python3
"""Exhaustive eight-point balanced-trade certificate; Python standard library only.
Run: python checker.py. Every case, implication and orbit is constructed afresh.
"""
from collections import defaultdict
from itertools import combinations, permutations

U=range(8)
SUBSETS=list(combinations(U,4))
INDEX={a:i for i,a in enumerate(SUBSETS)}
REPS=[a for a in SUBSETS if 0 in a]
RI={a:i for i,a in enumerate(REPS)}
BITS=[sum(1<<i for i in a) for a in SUBSETS]
assert len(SUBSETS)==70 and len(REPS)==35

def lit(a):
    if 0 in a:return (RI[a],1)
    return (RI[tuple(i for i in U if i not in a)],0)

def complement_free(ids):
    vals={BITS[j] for j in ids}
    return all((v^255) not in vals for v in vals)

# Every six-distinct balanced family has a partition into two 3-subfamilies.
# Group 3-subfamilies by their eight coordinate sums, then pair complementary
# sums (each coordinate totals 3), removing duplicates and complements.
buckets=defaultdict(list)
for ids in combinations(range(70),3):
    degree=tuple(sum(i in SUBSETS[j] for j in ids) for i in U)
    buckets[degree].append(ids)
SIX=set()
for degree,ps in buckets.items():
    other=tuple(3-d for d in degree)
    if degree>other or other not in buckets:continue
    for a in ps:
        for b in buckets[other]:
            ids=tuple(sorted(a+b))
            if len(set(ids))==6 and complement_free(ids):SIX.add(ids)
assert len(SIX)==35280

# Vertex permutations act on six-families. List all four exact orbits.
pactions=[]
for p in permutations(U):
    pactions.append(tuple(INDEX[tuple(sorted(p[i] for i in a))] for a in SUBSETS))
assert len(pactions)==40320
unseen=set(SIX);CLASSES=[]
while unseen:
    seed=min(unseen)
    orbit={tuple(sorted(p[j] for j in seed)) for p in pactions}
    assert orbit<=unseen
    unseen-=orbit
    CLASSES.append((seed,len(orbit)))
assert CLASSES==[
    ((0,1,12,64,66,67),5040),
    ((0,1,28,52,64,67),20160),
    ((0,9,14,56,62,68),3360),
    ((0,9,20,50,64,66),6720),
]
assert not unseen and sum(size for _,size in CLASSES)==35280

# A balanced 4-family uses four distinct selected 4-sets and has degree 2
# at each point. Every corresponding signed set of four literals is forbidden.
pairs=defaultdict(list)
for a,b in combinations(SUBSETS,2):
    deg=tuple(int(i in a)+int(i in b) for i in U)
    pairs[deg].append((a,b))
forbidden=set()
for deg,pp in pairs.items():
    other=tuple(2-d for d in deg)
    if deg>other or other not in pairs:continue
    for aa in pp:
        for bb in pairs[other]:
            tt=set(aa+bb)
            if len(tt)!=4:continue
            pp4=tuple(sorted(lit(a) for a in tt))
            if len({i for i,_ in pp4})==4:forbidden.add(pp4)
FORBIDDEN=sorted(forbidden)
assert len(FORBIDDEN)==1260

# Deterministic unit-propagation. Given six fixed winning coalitions, every
# forbidden quartet is a four-literal clause saying not all are selected.
# Each of the four orbit representatives gives a short forced contradiction.
CONFLICT_SIZES=[]
for six,size in CLASSES:
    fixed={i:v for j in six for i,v in [lit(SUBSETS[j])]}
    assert len(fixed)==6
    assignment=dict(fixed);steps=[];conflict=None
    for _ in range(36):
        new=False
        for clause in FORBIDDEN:
            if any(i in assignment and assignment[i]!=v for i,v in clause):continue
            unknown=[(i,v) for i,v in clause if i not in assignment]
            if not unknown:
                conflict=clause;break
            if len(unknown)==1:
                i,v=unknown[0]
                assignment[i]=1-v
                steps.append((i,1-v,clause))
                new=True
        if conflict or not new:break
    assert conflict is not None
    assert len(steps)<=5
    CONFLICT_SIZES.append(len(steps))
    print('ORBIT',size,'FORCED_STEPS',len(steps),'FINAL_CONFLICT',conflict)
assert CONFLICT_SIZES==[4,5,3,3]
print('ALL_CHECKS_OK: 35280 distinct balanced sextuples, four orbits, 1260 balanced quartets, four short contradictions')
