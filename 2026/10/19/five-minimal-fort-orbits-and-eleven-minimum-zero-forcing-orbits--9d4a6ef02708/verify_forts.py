#!/usr/bin/env python3
"""Independent exact verifier via forts, downward-subset DP and transversals."""
from collections import Counter
from itertools import permutations
import json

SIZE=16
FULL=(1<<SIZE)-1
# Hamming distance exactly one; built without the neighbor bitmask method.
mat=tuple(tuple(int((u^v).bit_count()==1) for v in range(SIZE)) for u in range(SIZE))

def is_fort(mask):
    if mask==0:return False
    members=[u for u in range(SIZE) if mask>>u&1]
    for u in range(SIZE):
        if not (mask>>u&1) and sum(mat[u][v] for v in members)==1:
            return False
    return True

fort=[is_fort(mask) for mask in range(1<<SIZE)]
# contains_fort(M) iff some (possibly non-minimal) fort is a subset of M.
# Unlike zero forcing, the fort property is NOT inclusion-monotone.
# Therefore checking single-vertex deletions for fort minimality is invalid;
# the downward-subset recurrence searches all proper subsets.
contains=[False]*(1<<SIZE)
minimal_forts=[]
for m in range(1,1<<SIZE):
    smaller=any(contains[m^(1<<v)] for v in range(SIZE) if m>>v&1)
    contains[m]=fort[m] or smaller
    if fort[m] and not smaller:minimal_forts.append(m)
assert sum(fort)==17487
assert len(minimal_forts)==348
assert Counter(f.bit_count() for f in minimal_forts)=={4:28,6:32,8:288}

counts=Counter()
forcing=[]
for black in range(1<<SIZE):
    if not contains[FULL^black]:
        counts[black.bit_count()]+=1
        forcing.append(black)
expected={8:2360,9:6016,10:6240,11:4032,12:1792,13:560,14:120,15:16,16:1}
assert dict(counts)==expected

# Entire minimal-fort symmetry classification.
perms=[]
for p in permutations((1,2,4,8)):
    for a in range(16):
        perms.append([a^sum(p[b] for b in range(4) if (u>>b)&1) for u in range(16)])
assert len({tuple(p) for p in perms})==384

def move(m,p):
    return sum(1<<p[v] for v in range(SIZE) if m>>v&1)
rem=set(minimal_forts);orbits=[]
while rem:
    x=min(rem)
    y={move(x,p) for p in perms}
    assert len(y)==len(y&rem)
    rem-=y
    orbits.append({'representative':x,'cardinality':x.bit_count(),'orbit_size':len(y)})
assert len(orbits)==5
assert Counter((o['cardinality'],o['orbit_size']) for o in orbits)=={(4,12):1,(4,16):1,(6,32):1,(8,96):1,(8,192):1}

# As a further check, minimum transversals of the minimal-fort family are
# exactly the inclusion-minimal zero forcing sets, all of cardinality 8.
trans=set(forcing)
minimum=[s for s in forcing if all(s^(1<<v) not in trans for v in range(SIZE) if s>>v&1)]
assert len(minimum)==2360 and all(s.bit_count()==8 for s in minimum)
if __name__=='__main__':
    print('FORTS_OK subset_masks=65536 forts=17487 minimal_forts=348 spectrum='+str(sorted(Counter(x.bit_count() for x in minimal_forts).items())))
    print('FORTS_OK transversal_zero_forcing=21137 min_transversals=2360 size=8 polynomial='+str(sorted(counts.items())))
    print('FORTS_ORBITS_OK automorphisms=384 orbits=5 sizes='+str(sorted(Counter((o['cardinality'],o['orbit_size']) for o in orbits).items())))
    print('FORT_REPRESENTATIVES='+json.dumps(orbits,separators=(',',':')))
