"""Compute and verify the full elementary expansion of X_{C_{8,2}} (stdlib only)."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb

V=tuple(range(8))
arcs={(u,(u+d)%8) for u in V for d in (1,2)}
stable={ij for ij in combinations(V,2) if not (ij in arcs or ij[::-1] in arcs)}
assert len(arcs)==16
assert not any(all(ij in stable for ij in combinations(S,2)) for S in combinations(V,3))

def matchings_with_singletons(left):
    if not left:
        yield ()
        return
    i,*rest=left
    for tail in matchings_with_singletons(rest):
        yield ((i,),)+tail
    for j in rest:
        if (i,j) in stable:
            for tail in matchings_with_singletons([v for v in rest if v!=j]):
                yield ((i,j),)+tail

def add_multiple(target, source, multiplier):
    for k,v in source.items():
        target[k]+=multiplier*v

observed=defaultdict(Counter)
nblocks=0
for blocks in matchings_with_singletons(V):
    nblocks+=1
    for order in permutations(blocks):
        color=[0]*8
        for i,B in enumerate(order):
            for v in B: color[v]=i
        asc=sum(color[u]<color[v] for u,v in arcs)
        observed[tuple(map(len,order))][asc]+=1

def coefficient(d,b):
    s=8-2*d
    return comb(s,b-d) if 0<=b-d<=s else 0

elements={}
for d in range(4,-1,-1):
    value=observed[(2,)*d+(1,)*(8-2*d)].copy()
    for b,poly in elements.items(): add_multiple(value,poly,-coefficient(d,b))
    elements[d]={k:v for k,v in value.items() if v}

for d in range(5):
    s=8-2*d
    prediction=Counter()
    for b,poly in elements.items():
        if coefficient(d,b): add_multiple(prediction,poly,coefficient(d,b))
    for pos in combinations(range(s+d),d):
        exp=tuple(2 if i in pos else 1 for i in range(s+d))
        assert prediction==observed.get(exp,Counter()),exp

assert nblocks==106 and sum(sum(P.values()) for P in observed.values())==136488
assert elements=={
  0:dict(enumerate((8,64,224,456,616,672,616,456,224,64,8),3)),
  1:dict(enumerate((32,136,208,208,208,136,32),5)),
  2:dict(enumerate((24,64,64,64,24),6)),
  3:dict(enumerate((8,48,80,48,8),6)),
  4:dict(enumerate((4,40,80,40,4),6)),
}
for b,poly in sorted(elements.items()):
    values=[poly.get(k,0) for k in range(17)]
    assert values==values[::-1] and all(0<=values[k]<=values[k+1] for k in range(8))
    print((8-b,b) if b else (8,), sorted(poly.items()))
print('PASS: 34 exponent patterns, 106 partitions, 136488 color orders')
