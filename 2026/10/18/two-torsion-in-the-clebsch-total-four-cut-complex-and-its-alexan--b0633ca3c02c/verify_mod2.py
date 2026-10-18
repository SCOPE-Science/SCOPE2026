#!/usr/bin/env python3
"""Independent mod-two check of the Clebsch bounded-independence dual.

Uses dynamic independence-number recursion and raw simplicial boundary ranks;
does not use discrete-Morse matching or signed integer chain elimination.
"""
from collections import defaultdict
from functools import lru_cache
N=16
S={1,2,4,8,15}
NEIGH=[sum(1<<(v^d) for d in S) for v in range(N)]
@lru_cache(maxsize=None)
def alpha(mask):
    if not mask:return 0
    bit=mask&-mask
    v=bit.bit_length()-1
    return max(alpha(mask^bit),1+alpha((mask^bit)&~NEIGH[v]))

faces_by_degree=defaultdict(list)
for mask in range(1<<N):
    if alpha(mask)<=3:
        faces_by_degree[mask.bit_count()-1].append(mask)
assert sum(len(x) for x in faces_by_degree.values())==12621


def boundary_rank(k):
    below={f:i for i,f in enumerate(faces_by_degree[k-1])}
    pivots={}
    for face in faces_by_degree[k]:
        column=0
        bits=face
        while bits:
            bit=bits&-bits
            bits^=bit
            column ^= 1 << below[face^bit]
        while column:
            position=column.bit_length()-1
            if position not in pivots:
                pivots[position]=column
                break
            column^=pivots[position]
    return len(pivots)

ranks={k:boundary_rank(k) for k in range(0,8)}
assert ranks=={0:1,1:15,2:105,3:455,4:1245,5:2067,6:1800,7:599},ranks
betti={d:len(faces_by_degree[d])-ranks[d]-ranks[d+1] for d in range(0,7)}
betti[7]=len(faces_by_degree[7])-ranks[7]
assert betti=={0:0,1:0,2:0,3:0,4:0,5:45,6:1,7:1},betti
print('ALEXANDER_DUAL_MOD2_COUNTS',dict(sorted((k,len(v)) for k,v in faces_by_degree.items())))
print('ALEXANDER_DUAL_MOD2_BOUNDARY_RANKS',ranks)
print('ALEXANDER_DUAL_MOD2_REDUCED_BETTI',betti)
print('MOD2_VERIFY_OK')
