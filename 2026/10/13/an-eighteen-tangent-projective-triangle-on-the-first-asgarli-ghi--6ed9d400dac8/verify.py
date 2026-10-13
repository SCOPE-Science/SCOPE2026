"""Exhaustive arithmetic certificate for a finite projective-plane tangent cover."""
from collections import Counter

P = 11
W = (
    (0,1,3),(1,0,4),(1,1,2),(1,1,7),(1,1,8),(1,2,1),
    (1,3,0),(1,4,9),(1,5,9),(1,6,6),(1,7,3),(1,7,7),
    (1,7,10),(1,8,6),(1,9,5),(1,9,7),(1,9,9),(1,10,1)
)
DIRECTIONS = ((1,1,8),(1,7,7),(1,9,8))

def normalize(v):
    for a in v:
        if a % P:
            k = pow(a, -1, P)
            return tuple((k * b) % P for b in v)
    raise ValueError('zero projective vector')

def pair(a,b):
    return sum(x*y for x,y in zip(a,b)) % P

def tangent(v):
    x,y,z = v
    s = (x+y+z)%P
    return normalize(tuple((3*pow(s,-1,P) - pow(c,-1,P))%P for c in v))

projective = sorted({normalize((x,y,z)) for x in range(P) for y in range(P) for z in range(P) if (x,y,z) != (0,0,0)})
assert len(projective) == 133
smooth = [v for v in projective if all(v) and sum(v)%P and len(set(v))>1]
assert len(smooth) == 90
assert all((sum(pow(c,10,P) for c in v)-3*pow(sum(v)%P,10,P))%P==0 for v in smooth)
T = sorted({tangent(v) for v in smooth})
assert len(T) == 72
assert len(set(W)) == 18
assert set(W).issubset(T)
assert all(any(tangent(v) == w for v in smooth) for w in W)
full_counts=Counter(sum(pair(t,v)==0 for t in T) for v in projective)
assert full_counts=={1:3,4:6,5:30,6:25,7:24,8:42,11:3}, full_counts
assert max(full_counts)==11  # no complete 12-line pencil among all tangents
w_counts=Counter(sum(pair(w,v)==0 for w in W) for v in projective)
assert w_counts=={1:90,2:15,3:25,7:3}, w_counts
assert min(w_counts)==1  # covers all 133 points
assert sorted(sum(pair(w,d)==0 for w in W) for d in DIRECTIONS)==[7,7,7]
assert all(sum(pair(w,d)==0 for d in DIRECTIONS)>=1 for w in W)
assert len({tuple(i for i,d in enumerate(DIRECTIONS) if pair(w,d)==0) for w in W if sum(pair(w,d)==0 for d in DIRECTIONS)>1})==3
print('VERIFY_OK: 90 smooth rational points, 72 tangent lines; 18 triangle tangents cover 133 points; no complete pencil')
