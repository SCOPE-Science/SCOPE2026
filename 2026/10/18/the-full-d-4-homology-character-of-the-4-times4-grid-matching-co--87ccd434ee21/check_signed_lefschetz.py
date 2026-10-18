#!/usr/bin/env python3
"""Independent signed fixed-face enumeration for square-grid matching complexes."""
from collections import Counter

n = 4
# Deliberately use a different graph-edge order: horizontal edges first.
links = []
for r in range(n):
    for c in range(n-1):
        links.append((n*r+c, n*r+c+1))
for r in range(n-1):
    for c in range(n):
        links.append((n*r+c, n*(r+1)+c))
assert len(links)==24
index = {tuple(sorted(e)):j for j,e in enumerate(links)}
matchings = [(0,0)]  # (edge bitmask, occupied-graph-vertices bitmask)
for j,(u,v) in enumerate(links):
    occupied = (1<<u)|(1<<v)
    additions = [(mask|(1<<j), used|occupied)
                 for mask,used in matchings if not (used & occupied)]
    matchings.extend(additions)
assert len(matchings)==10012
counts=Counter(mask.bit_count()-1 for mask,_ in matchings)
assert [counts[d] for d in range(-1,8)]==[1,24,224,1044,2593,3388,2150,552,36]

def point(x,op):
    r,c=divmod(x,4)
    return {
        'i':(r,c),'r':(c,3-r),'r2':(3-r,3-c),'r3':(3-c,r),
        'h':(r,3-c),'v':(3-r,c),'d':(c,r),'a':(3-c,3-r)
    }[op]

EXPECTED={'i':4,'r':2,'r2':4,'r3':2,'h':0,'v':0,'d':-2,'a':-2}
for op in EXPECTED:
    transform=[]
    for u,v in links:
        ru,cu=point(u,op)
        rv,cv=point(v,op)
        transform.append(index[tuple(sorted((4*ru+cu,4*rv+cv)))])
    signed=Counter()
    for mask,occupied in matchings:
        edge_ids=[j for j in range(24) if mask&(1<<j)]
        perm=[transform[j] for j in edge_ids]
        if set(perm)!=set(edge_ids):continue
        inversions=sum(perm[i]>perm[j] for i in range(len(perm))
                       for j in range(i+1,len(perm)))
        signed[len(edge_ids)-1]+= -1 if inversions&1 else 1
    reduced=sum((-1 if d%2 else 1)*trace for d,trace in signed.items())
    assert reduced==EXPECTED[op]
    print('symmetry',op,'reduced_integral_Lefschetz',reduced,
          'signed_face_traces',[(d,signed[d]) for d in range(-1,8)])
print('INDEPENDENT_LEFSCHETZ_VERIFIED')
