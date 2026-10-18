#!/usr/bin/env python3
"""Exact finite verification for noncover complexes of the Cremona--Richmond configuration.

Requires Python 3.9+ standard library only. No floating-point arithmetic.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from math import factorial

V = tuple(combinations(range(6), 2))
idx = {e:i for i,e in enumerate(V)}
lines = sorted(set(tuple(sorted(idx[e] for e in matching))
                   for matching in combinations(V,3)
                   if len(set().union(*(set(e) for e in matching))) == 6))
assert len(V)==15 and len(lines)==15
assert all(len(e)==3 for e in lines)
FULL=(1<<15)-1
facets = [FULL ^ sum(1<<i for i in line) for line in lines]

def downward_closure(fcs):
    out={0}
    for f in fcs:
        s=f
        while s:
            out.add(s)
            s=(s-1)&f
    return out

K=downward_closure(facets)
Kminus=downward_closure(facets[1:])
J={s for s in Kminus if s&facets[0]==s}

def matching_and_acyclic(faces):
    remaining=set(faces)
    matched={}
    by_pass=[]
    for v in range(15):
        u=1<<v
        pairs=[(s,s|u) for s in sorted(remaining)
               if not (s&u) and s|u in remaining]
        for s,t in pairs:
            assert s in remaining and t in remaining
            remaining.remove(s)
            remaining.remove(t)
            matched[t]=s
        by_pass.append(len(pairs))
    assert 0 not in remaining
    # Ignore the reduced pair (empty set, one vertex) to obtain an ordinary
    # acyclic matching with exactly one critical zero-dimensional simplex.
    singleton = next(t for t,s in matched.items() if s==0)
    del matched[singleton]
    remaining.update([0,singleton])
    cells=sorted(x for x in faces if x)
    pos={x:i for i,x in enumerate(cells)}
    adj=[[] for _ in cells]
    indeg=[0]*len(cells)
    incidences=0
    for t in cells:
        s=t
        while s:
            bit=s&-s
            low=t^bit
            s-=bit
            if not low:continue
            # Reverse matched incidences, direct other incidences down.
            if matched.get(t)==low:src,dst=low,t
            else:src,dst=t,low
            adj[pos[src]].append(pos[dst]);indeg[pos[dst]]+=1
            incidences+=1
    q=deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while q:
        x=q.popleft();visited+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert visited==len(cells), 'cyclic discrete gradient'
    critical=Counter(x.bit_count()-1 for x in remaining if x)
    assert critical[0]==1
    return len(matched),dict(sorted(critical.items())),incidences,by_pass

for name,complex_,expected in [
    ('full',K,{0:1,7:9}),
    ('line-deleted',Kminus,{0:1,7:4}),
    ('intersection',J,{0:1,6:5}),
]:
    pairs,critical,incidences,passes=matching_and_acyclic(complex_)
    assert critical==expected
    assert 2*pairs+sum(critical.values())==len(complex_)-1
    print(name,'faces_including_empty',len(complex_),
          'pairs',pairs,'critical',critical,'incidences',incidences)

assert len(K)==24823 and len(Kminus)==24274 and len(J)==3547

def action(p):
    return [idx[tuple(sorted((p[x],p[y])))] for x,y in V]

def cycle_data(a):
    seen=set();cy=[]
    for i in range(15):
        if i in seen:continue
        s=0;j=i
        while j not in seen:
            seen.add(j);s|=1<<j;j=a[j]
        cy.append(s)
    return cy

def character(faces_flags,cycles):
    # Equivariant reduced Euler characteristic, with exact simplex signs.
    # A g-invariant simplex is a union of vertex cycles. Its contribution to
    # (-1)^(dimension+1) times signed Lefschetz is (-1)^number_of_cycles.
    masks={0:1}
    for orbit in cycles:
        masks.update({m|orbit:-sign for m,sign in tuple(masks.items())})
    return sum(sign for m,sign in masks.items() if faces_flags[m])

def permutation_type(p):
    seen=set();lengths=[]
    for i in range(6):
        if i in seen:continue
        j=i;length=0
        while j not in seen:
            seen.add(j);j=p[j];length+=1
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))

kflag=bytearray(1<<15)
pflag=bytearray(1<<15)
for m in K:kflag[m]=1
for m in Kminus:pflag[m]=1
whole=[];stab=[];classes=defaultdict(Counter)
for p in permutations(range(6)):
    a=action(p);cycles=cycle_data(a)
    c=character(kflag,cycles)
    typ=permutation_type(p)
    classes[typ][c]+=1
    whole.append(c)
    if set(a[i] for i in lines[0]) == set(lines[0]):
        d=character(pflag,cycles)
        stab.append((p,a,c,d))
assert len(whole)==720 and len(stab)==48
assert sum(whole)==0 and sum(c*c for c in whole)==720
expected_types={
 (1,1,1,1,1,1):(1,9),
 (2,1,1,1,1):(15,-3),
 (2,2,1,1):(45,1),
 (2,2,2):(15,-3),
 (3,1,1,1):(40,0),
 (3,2,1):(120,0),
 (3,3):(40,0),
 (4,1,1):(90,1),
 (4,2):(90,1),
 (5,1):(144,-1),
 (6,):(120,0),
}
for typ,(size,value) in expected_types.items():
    assert classes[typ]==Counter({value:size}), (typ,classes[typ])
print('full_action S6_size',len(whole),'class_character',
      [(str(k),v[1]) for k,v in expected_types.items()],
      'character_square_sum',sum(c*c for c in whole))
assert sum(c for p,a,c,d in stab)==0
assert sum(d for p,a,c,d in stab)==0
assert sum(d*d for p,a,c,d in stab)==96
assert sum((c-d)**2 for p,a,c,d in stab)==96
print('line_stabilizer_size',len(stab),'H7_dim',4,'H7_invariants',0,
      'H7_character_square_sum',96,'relative_dim',5,
      'relative_character_square_sum',96)

# The distinguished one-dimensional H-character measures the parity of the
# three internal pair flips in the deleted syntheme.
inner=0
for p,a,c,d in stab:
    flips=0
    for j in range(3):
        assert p[2*j]//2 == p[2*j+1]//2
        flips+=p[2*j]%2
    inner+=d*((-1)**flips)
assert inner==48
print('internal_flip_sign_character_multiplicity',inner//48,
      'orthogonal_three_dimensional_complement_irreducible',True)

# Independent signed-trace formula for all 48 stabilizer elements.
# This deliberately does not use the vertex-cycle subsets formula.
flags=sorted(x for x in Kminus if x)
for p,a,c,d in stab:
    alternating=-1  # reduced empty face, in degree -1
    for m in flags:
        bits=[i for i in range(15) if m>>i&1]
        img=[a[i] for i in bits]
        if sum(1<<i for i in img)!=m:continue
        inversions=sum(img[i]>img[j]
                       for i in range(len(img)) for j in range(i+1,len(img)))
        alternating+=(-1)**(len(bits)-1+inversions)
    assert -alternating==d
print('independent_signed_Lefschetz_checks',len(stab),'passed')
print('ALL_CHECKS_PASSED')
