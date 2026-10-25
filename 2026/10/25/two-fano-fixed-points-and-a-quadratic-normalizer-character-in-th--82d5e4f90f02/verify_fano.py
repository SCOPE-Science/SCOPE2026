"""Exact seven-point orbit and normalizer computation for the pairwise-intersecting triples complex."""
from itertools import combinations
P=7
triples=list(combinations(range(P),3))
def translate(t,b):return tuple(sorted((x+b)%P for x in t))
def multiply(t,a):return tuple(sorted((a*x)%P for x in t))
seen=set();orbits=[]
for t in triples:
    if t in seen:continue
    orbit=sorted({translate(t,b) for b in range(P)})
    assert len(orbit)==P
    seen.update(orbit);orbits.append(tuple(orbit))
assert len(orbits)==5 and len(seen)==35
can_select=[]
for O in orbits:
    good=all(set(s)&set(t) for s,t in combinations(O,2))
    if good:can_select.append(O)
assert len(can_select)==2
representatives={min(O) for O in can_select}
assert representatives=={(0,1,3),(0,1,5)}
assert not all(set(s)&set(t) for s in can_select[0] for t in can_select[1])
squares={1,2,4}
for a in range(1,7):
    images=[next(j for j,Q in enumerate(can_select) if multiply(O[0],a) in Q)
            for O in can_select]
    assert images==([0,1] if a in squares else [1,0]),(a,images)
for b in range(P):
    for O in can_select:
        assert translate(O[0],b) in O
print('PASS: 35 triples; 5 translation orbits; exactly two individually compatible orbits;')
print('no compatible union; affine normalizer action is the quadratic character on reduced H0.')
