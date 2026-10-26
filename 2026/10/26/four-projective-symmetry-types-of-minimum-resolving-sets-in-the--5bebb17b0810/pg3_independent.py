#!/usr/bin/env python3
"""Independent incidence-signature enumeration of optimum PG(2,3) landmarks."""
from itertools import combinations, product
from collections import Counter

F = range(3)
def canonical(v):
    if not any(v):
        return None
    t=next(x for x in v if x)
    return tuple(x * t % 3 for x in v)

V=sorted({canonical(v) for v in product(F,repeat=3)}-{None})
assert len(V)==13
I=tuple(tuple(sum(a*b for a,b in zip(p,l))%3==0 for l in V) for p in V)
assert all(sum(row)==4 for row in I)
assert all(sum(I[i][j] for i in range(13))==4 for j in range(13))
quadruples=list(combinations(range(13),4))
masks=[sum(1<<i for i in q) for q in quadruples]
def ambiguous_pairs(m, first):
    selected=[i for i in range(13) if m>>i&1]
    sigs=[]
    for j in range(13):
        sig=tuple(I[i][j] if first else I[j][i] for i in selected)
        sigs.append(sig)
    return [((1<<a)|(1<<b)) for a,b in combinations(range(13),2) if sigs[a]==sigs[b]]

line_conflicts={m:ambiguous_pairs(m,True) for m in masks}
point_conflicts={m:ambiguous_pairs(m,False) for m in masks}
line_allowed={m: [lm for lm in masks if all(c & lm for c in line_conflicts[m])] for m in masks}

def collinear3(sel):
    return sum(any(all(I[i][j] for i in triple) for j in range(13)) for triple in combinations(sel,3))

def concurrent3(sel):
    return sum(any(all(I[i][j] for j in triple) for i in range(13)) for triple in combinations(sel,3))

profile=Counter()
count=0
for pi,pm in enumerate(masks):
    P=quadruples[pi]
    for lm in line_allowed[pm]:
        if not all(c & pm for c in point_conflicts[lm]):
            continue
        count+=1
        L=quadruples[masks.index(lm)]
        e=sum(I[i][j] for i in P for j in L)
        t=collinear3(P)+concurrent3(L)
        profile[e,t]+=1
assert count==9828,(count,profile)
assert profile=={(1,0):936,(2,0):1404,(3,0):5616,(3,2):1872},profile

# In a split resolving set each color class must resolve the opposite class alone.
semi=[]
for k in range(1,7):
    semi=[P for P in combinations(range(13),k)
          if len({tuple(I[i][j] for i in P) for j in range(13)}) == 13]
    if semi:
        assert k==6 and len(semi)==1170
        break
else:
    raise AssertionError('semi-resolving minimum was not found')
print('Semi-resolving minimum: 6 on either side; minimum split size: 12')

print('VERIFY_OK independently: 9828 balanced (4 point + 4 line) resolving sets')
print('incidence/collinearity signatures:',sorted(profile.items()))
