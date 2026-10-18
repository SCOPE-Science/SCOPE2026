"""Small affine-orbit certificate for the four-point classification lemma.

The 108 maps (x,y)->(a*x+c,d*y+e*x+f) preserve vertical classes
and permute the three nonvertical slopes. The four listed orbit
representatives cover every four-point subset of the affine 3x3 plane.
"""
from itertools import combinations, permutations, product

F = range(3)
points = tuple(product(F, F))
lines = tuple(product(F, F))
reps = (
    ((0,0),(0,1),(0,2),(1,0)),
    ((0,0),(0,1),(1,0),(1,1)),
    ((0,0),(0,1),(1,0),(2,0)),
    ((0,0),(0,1),(1,0),(2,1)),
)

def incident(p, l):
    x,y=p; m,b=l
    return (y-m*x-b)%3 == 0

def good(P,L):
    pset=set(P); lset=set(L)
    if any(not any(incident(p,l) for p in pset) for l in lines if l not in lset):
        return False
    if any(not any(incident(p,l) for l in lset) for p in points if p not in pset):
        return False
    return any(all(incident(p,l) for p,l in zip(P, Q)) for Q in permutations(L))

maps=[]
for a,d in product((1,2),repeat=2):
    for c,e,f in product(F,repeat=3):
        tr=lambda p,a=a,d=d,c=c,e=e,f=f: ((a*p[0]+c)%3,(d*p[1]+e*p[0]+f)%3)
        maps.append(tr)
assert len(maps)==108
orbits=[]
for r in reps:
    o={tuple(sorted(t(p) for p in r)) for t in maps}
    orbits.append(o)
all4=set(combinations(points,4))
assert not any(orbits[i]&orbits[j] for i in range(4) for j in range(i+1,4))
assert set.union(*orbits)==all4
assert sorted(map(len,orbits))==[18,27,27,54]
for r,o in zip(reps,orbits):
    num=sum(good(r,L) for L in combinations(lines,4))
    print(f'point_orbit_size={len(o)} representative={r} compatible_line_sets={num}')
    assert num == (12 if len(o)==18 else 0)
assert sum(len(o)*sum(good(r,L) for L in combinations(lines,4)) for r,o in zip(reps,orbits))==216
print('orbit_classification=complete')
print('VERIFY_OK')
