#!/usr/bin/env python3
from itertools import product
from hashlib import sha256
import json

# X_2: three two-point levels; distinct points in the same level are incomparable.
NPTS = 6
LEVEL = (0,0,1,1,2,2)
def le_x(a,b):
    return a == b or LEVEL[a] < LEVEL[b]

maps=[]
for f in product(range(NPTS), repeat=NPTS):
    if all((not le_x(a,b)) or le_x(f[a],f[b]) for a in range(NPTS) for b in range(NPTS)):
        maps.append(f)
assert len(maps)==446

m=len(maps)
def le_m(i,j):
    f,g=maps[i],maps[j]
    return all(le_x(f[x],g[x]) for x in range(NPTS))

LE=[[le_m(i,j) for j in range(m)] for i in range(m)]
constants={i for i,f in enumerate(maps) if len(set(f))==1}
autos={i for i,f in enumerate(maps) if len(set(f))==NPTS}
assert len(constants)==6
assert len(autos)==8

# Homeomorphisms are isolated in the full map poset.
for i in autos:
    assert all(j==i or (not LE[i][j] and not LE[j][i]) for j in range(m))

# Deterministic Stong beat-point reduction. At each stage scan indices upward;
# down-beat is preferred to up-beat. Store the unique extremal witness.
def beat(active,i):
    lower=[j for j in active if j!=i and LE[j][i]]
    for w in lower:
        if all(LE[j][w] for j in lower):
            # uniqueness follows in a T0 poset; assert it directly.
            assert sum(all(LE[j][u] for j in lower) for u in lower)==1
            return ('down',w)
    upper=[j for j in active if j!=i and LE[i][j]]
    for w in upper:
        if all(LE[w][j] for j in upper):
            assert sum(all(LE[u][j] for j in upper) for u in upper)==1
            return ('up',w)
    return None

active=set(range(m))
sequence=[]
while True:
    chosen=None
    for i in sorted(active):
        b=beat(active,i)
        if b is not None:
            chosen=(i,b)
            break
    if chosen is None:
        break
    i,b=chosen
    sequence.append((i,b))
    active.remove(i)

expected=constants|autos
assert active==expected
assert len(sequence)==432
assert sum(1 for _,(kind,_) in sequence if kind=='down')==352
assert sum(1 for _,(kind,_) in sequence if kind=='up')==80
# Final subspace is beat-point-free.
assert all(beat(active,i) is None for i in active)

# Constants carry exactly the original X_2 order.
const_by_value={maps[i][0]:i for i in constants}
assert set(const_by_value)==set(range(NPTS))
for a in range(NPTS):
    for b in range(NPTS):
        assert LE[const_by_value[a]][const_by_value[b]] == le_x(a,b)

# Autos are disjoint isolated components, hence the core is X_2 plus eight points.
core_indices=sorted(active)
core_maps=[maps[i] for i in core_indices]
digest=sha256(json.dumps(sequence,separators=(',',':')).encode()).hexdigest()
print('VERIFY_OK')
print('self_maps=446')
print('constants=6')
print('homeomorphisms=8')
print('beat_deletions=432')
print('down_deletions=352')
print('up_deletions=80')
print('core_size=14')
print('core_indices='+json.dumps(core_indices,separators=(',',':')))
print('core_maps='+json.dumps(core_maps,separators=(',',':')))
print('deletion_sequence_sha256='+digest)
