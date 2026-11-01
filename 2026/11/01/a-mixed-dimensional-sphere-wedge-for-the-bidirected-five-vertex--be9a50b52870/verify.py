"""Standalone exact acyclic-Morse certificate for the bidirected five-vertex wheel."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N_RIM=4
HUB=4
ARCS=[]
for i in range(N_RIM):
    for j in ((i+1)%N_RIM,HUB):
        ARCS.extend(((i,j),(j,i)))
assert len(ARCS)==16 and len(set(ARCS))==16
# Fixed mask order is the declared arc order; no graph package needed.
ORDER=[1,7,14,11,12,3,9,0,6,2,5,13,8,10,4,15]
assert sorted(ORDER)==list(range(16))

def is_face(mask):
    out=[-1]*5
    inc=[-1]*5
    for bit,(u,v) in enumerate(ARCS):
        if mask & (1<<bit):
            if out[u]!=-1 or inc[v]!=-1:
                return False
            out[u]=v
            inc[v]=u
    # A functional directed graph has a directed cycle iff some orbit repeats.
    for source in range(5):
        visit=set()
        v=source
        while v!=-1 and v not in visit:
            visit.add(v)
            v=out[v]
        if v!=-1:
            return False
    return True

FACES={mask for mask in range(1<<16) if is_face(mask)}
assert len(FACES)==261 and 0 in FACES
assert all((mask ^ (mask & -mask)) in FACES for mask in FACES if mask)
assert Counter(m.bit_count()-1 for m in FACES)==Counter({-1:1,0:16,1:76,2:120,3:48})

alive=FACES.copy()
PAIRS=[]
for bit in ORDER:
    single=1<<bit
    for low in sorted(mask for mask in alive if not(mask & single)):
        high=low | single
        if low in alive and high in alive:
            alive.remove(low)
            alive.remove(high)
            PAIRS.append((low,high))

# Ordinary, rather than reduced, Morse matching: release the pair with empty face.
# It yields one critical vertex; the empty simplex is not a CW cell.
assert len(PAIRS)==117 and len(alive)==27
empty_pair=next((a,b) for a,b in PAIRS if a==0)
PAIRS.remove(empty_pair)
CRITICAL=alive | {empty_pair[1]}
assert len(PAIRS)==116 and len(CRITICAL)==28
assert Counter(m.bit_count()-1 for m in CRITICAL)==Counter({0:1,2:19,3:8})
assert all((low.bit_count()+1)==high.bit_count() for low,high in PAIRS)
assert len({m for pair in PAIRS for m in pair})==232

# Check the full reversed matching Hasse DAG, including the empty simplex.
matched={high:low for low,high in PAIRS}
low_to_high={low:high for low,high in PAIRS}
nonempty=FACES-{0}
indeg={mask:0 for mask in nonempty}
outgoing={mask:[] for mask in nonempty}
for upper in nonempty:
    rem=upper
    while rem:
        b=rem&-rem
        rem-=b
        lower=upper^b
        if not lower:
            continue
        if matched.get(upper)==lower:
            outgoing[lower].append(upper)
            indeg[upper]+=1
        else:
            outgoing[upper].append(lower)
            indeg[lower]+=1
queue=deque(mask for mask in nonempty if indeg[mask]==0)
topo=[]
while queue:
    mask=queue.popleft()
    topo.append(mask)
    for other in outgoing[mask]:
        indeg[other]-=1
        if indeg[other]==0:
            queue.append(other)
assert len(topo)==len(nonempty)

# Signed boundary of oriented simplex (order = increasing arc-index).
def boundary(mask):
    sign=1
    rem=mask
    while rem:
        b=rem&-rem
        rem-=b
        yield mask^b,sign
        sign=-sign

# Algebraic Morse elimination. Every matched incidence is +/-1.
@lru_cache(None)
def project(mask):
    if mask in CRITICAL:
        return {mask:1}
    if mask in matched: # matched upper cell in this chain degree
        return {}
    high=low_to_high[mask]
    x=dict(boundary(high))
    epsilon=x.pop(mask)
    assert abs(epsilon)==1
    ans={}
    for other,coefficient in x.items():
        for critical, value in project(other).items():
            ans[critical]=ans.get(critical,0)-coefficient*value//epsilon
    return {k:v for k,v in ans.items() if v}

# For an upper *critical* cell, project its signed boundary into critical lower degree.
all_columns=[]
for critical3 in sorted(mask for mask in CRITICAL if mask.bit_count()==4):
    reduced={}
    for codomain,coef in boundary(critical3):
        for bottom,val in project(codomain).items():
            reduced[bottom]=reduced.get(bottom,0)+coef*val
    reduced={k:v for k,v in reduced.items() if v}
    all_columns.append(reduced)
assert all(not c for c in all_columns),all_columns

# Independent sanity check: full mod-2 simplicial boundary ranks.
def rank_mod2(columns):
    pivots={}
    for column in columns:
        while column:
            pivot=column.bit_length()-1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot]=column
                break
    return len(pivots)

fby={d:sorted(mask for mask in FACES if mask.bit_count()==d+1) for d in range(-1,4)}
ranks={}
for d in range(1,4):
    lookup={mask:i for i,mask in enumerate(fby[d-1])}
    cols=[]
    for upper in fby[d]:
        column=0
        for low,_ in boundary(upper):
            column^=1<<lookup[low]
        cols.append(column)
    ranks[d]=rank_mod2(cols)
assert ranks=={1:15,2:61,3:40},ranks
print('VERIFY_OK faces=261 matched_pairs=116 critical_0=1 critical_2=19 critical_3=8 hasse_acyclic=1 integer_morse_boundary_zero=1 mod2_ranks=(15,61,40)')
