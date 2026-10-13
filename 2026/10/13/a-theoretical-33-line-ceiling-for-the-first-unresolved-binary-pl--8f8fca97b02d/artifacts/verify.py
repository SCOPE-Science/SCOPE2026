#!/usr/bin/env python3
import itertools, json, math
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def rank_bits(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y^=piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

def span_nonzero(vs):
    S={0}
    for x in vs:
        S |= {y^x for y in list(S)}
    S.discard(0)
    return frozenset(S)

pts=list(range(1,32))

lines=set()
for a,b in itertools.combinations(pts,2):
    lines.add(span_nonzero((a,b)))

planes=set()
for T in itertools.combinations(pts,3):
    if rank_bits(T)==3:
        planes.add(span_nonzero(T))

assert len(pts)==CERT["pg42"]["points"]==31
assert len(lines)==CERT["pg42"]["lines"]==155
assert len(planes)==CERT["pg42"]["planes"]==155
assert all(len(L)==3 for L in lines)
assert all(sum(L<=P for P in planes)==7 for L in lines)

# Convexity minima used in the proof.
def convex_min(total,slots):
    q,r=divmod(total,slots)
    return (slots-r)*math.comb(q,2)+r*math.comb(q+1,2)

assert convex_min(102,31)==120
assert 3*math.comb(2,2)+convex_min(93,28)==114
assert 238//2==119
assert 231//2==115

triples=[]
for S in range(111,116):
    x2=S
    x1=231-2*S
    x0=155-x1-x2
    triples.append([x0,x1,x2])
assert triples==CERT["hypothetical_33"]["plane_occupancy_triples"]

# Explicit 32-line lower-bound witness.
W=[frozenset(x) for x in CERT["witness_32"]]
assert len(W)==32
assert len(set(W))==32
assert all(L in lines for L in W)

occ=Counter(sum(L<=P for L in W) for P in planes)
assert max(occ)<=2
assert dict(occ)=={0:43,2:112}

# Independent incidence cross-checks for the witness.
point_deg=Counter()
for L in W:
    for p in L:
        point_deg[p]+=1
assert sum(point_deg.values())==96
assert sum(math.comb(d,2) for d in point_deg.values())==112

print("VERIFY_OK")
