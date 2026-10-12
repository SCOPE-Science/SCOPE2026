#!/usr/bin/env python3
from itertools import product, combinations, permutations
import hashlib, json

Q = tuple(product(range(3), repeat=3))
IDX = {w:i for i,w in enumerate(Q)}

def hamming(a,b):
    return sum(x != y for x,y in zip(a,b))

# BAD[x][y] is the bit mask of words z that are within Hamming distance <2
# of at least one nontrivial length-three splice of x and y.
BAD = [[0]*27 for _ in range(27)]
for ix,x in enumerate(Q):
    for iy,y in enumerate(Q):
        overlaps = ((x[1],x[2],y[0]), (x[2],y[0],y[1]))
        mask = 0
        for iz,z in enumerate(Q):
            if any(hamming(o,z) < 2 for o in overlaps):
                mask |= 1 << iz
        BAD[ix][iy] = mask

def valid(ids):
    mask = sum(1 << i for i in ids)
    return all((BAD[i][j] & mask) == 0 for i in ids for j in ids)

max4 = [tuple(c) for c in combinations(range(27),4) if valid(c)]
size5 = [tuple(c) for c in combinations(range(27),5) if valid(c)]
assert len(size5) == 0
assert len(max4) == 9

# Complete structural classification.
def template(j,b):
    return tuple(sorted(IDX[w] for w in Q
                        if w[j] == b and all(w[k] != b for k in range(3) if k != j)))
templates = {template(j,b):(j,b) for j in range(3) for b in range(3)}
assert set(max4) == set(templates)

# Natural symmetries: one common alphabet permutation, with optional reversal.
perms = tuple(permutations(range(3)))
group = tuple((p,r) for p in perms for r in (False,True))
assert len(group) == 12

def act(code,p,rev):
    out=[]
    for i in code:
        w=tuple(p[a] for a in Q[i])
        if rev:
            w=w[::-1]
        out.append(IDX[w])
    return tuple(sorted(out))

maxset=set(max4)
seen=set(); orbits=[]
for C in max4:
    if C in seen:
        continue
    orb={act(C,p,r) for p,r in group}
    assert orb <= maxset
    seen |= orb
    orbits.append(orb)
assert seen == maxset
sizes=sorted(len(o) for o in orbits)
assert sizes == [3,6]
stabilizers=sorted(12//len(o) for o in orbits)
assert stabilizers == [2,4]

# The two orbits are exactly middle-fixed versus end-fixed templates.
for orb in orbits:
    coords={templates[C][0] for C in orb}
    if len(orb)==3:
        assert coords=={1}
    else:
        assert coords=={0,2}

census = [
    [''.join(map(str,Q[i])) for i in C]
    for C in sorted(max4)
]
blob=json.dumps(census,separators=(',',':'),ensure_ascii=False).encode('utf-8')
digest=hashlib.sha256(blob).hexdigest()
print('VERIFY_OK maximum=4 labeled_maxima=9 size5=0 natural_group=12 orbits=2 orbit_sizes=3,6 stabilizers=2,4 census_sha256='+digest)
