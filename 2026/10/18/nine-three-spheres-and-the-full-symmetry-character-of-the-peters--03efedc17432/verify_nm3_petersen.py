#!/usr/bin/env python3
"""Finite exact certificate for NM_3 of the Petersen graph and its S_5 character.
No third-party dependencies; run: python -S verify_nm3_petersen.py
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import lru_cache

VERTS = tuple(combinations(range(5), 2))
VERT_INDEX = {v: i for i, v in enumerate(VERTS)}
EDGES = tuple([tuple(sorted((i,(i+1)%5))) for i in range(5)]
              + [(i,i+5) for i in range(5)]
              + [tuple(sorted((i+5,((i+2)%5)+5))) for i in range(5)])
assert len(EDGES) == 15
EDGE_INDEX = {e: i for i,e in enumerate(EDGES)}
BAD = tuple(sum(1 << i for i in triple)
            for triple in combinations(range(15), 3)
            if len({z for k in triple for z in EDGES[k]}) == 6)
assert len(BAD) == 145
FACES = {mask for mask in range(1 << 15)
         if all(mask & forbidden != forbidden for forbidden in BAD)}
F_VEC = Counter(mask.bit_count()-1 for mask in FACES)
assert len(FACES) == 1073
assert [F_VEC[i] for i in range(-1,6)] == [1,15,105,310,405,207,30]

# Explicit repeated toggling, leaving the singleton {edge 0} as the base cell.
remaining = FACES - {0}
MATCH = {}
for i in range(15):
    pairs = [(x, x | (1 << i)) for x in sorted(remaining)
             if x != 1 and not (x >> i & 1) and (x | (1 << i)) in remaining]
    for lo,hi in pairs:
        assert lo in remaining and hi in remaining and lo not in MATCH
        remaining.remove(lo)
        remaining.remove(hi)
        MATCH[lo] = hi
assert len(MATCH) == 530
CRIT = tuple(sorted(remaining))
assert Counter(mask.bit_count()-1 for mask in CRIT) == {0:1, 3:10, 4:1}
assert 1 in CRIT

# Exhaustive Hasse orientation, upward on pairs, downward otherwise.
INDEG = {x: 0 for x in FACES if x}
ADJ = {x: [] for x in FACES if x}
for hi in ADJ:
    for i in range(15):
        if hi >> i & 1:
            lo = hi ^ (1 << i)
            if lo == 0: continue
            if MATCH.get(lo) == hi:
                src,dst = lo,hi
            else:
                src,dst = hi,lo
            ADJ[src].append(dst)
            INDEG[dst] += 1
ready = deque(x for x in ADJ if INDEG[x] == 0)
visited=0
while ready:
    x=ready.popleft();visited+=1
    for y in ADJ[x]:
        INDEG[y]-=1
        if INDEG[y] == 0:ready.append(y)
assert visited==1072, (visited, len(ADJ))

# Signed boundaries, with simplex vertices ordered by edge index.
def boundary(mask):
    parity=0
    for i in range(15):
        if mask >> i & 1:
            yield mask ^ (1 << i), 1 if parity == 0 else -1
            parity ^= 1
CRIT3 = tuple(c for c in CRIT if c.bit_count()==4)
CRIT4 = tuple(c for c in CRIT if c.bit_count()==5)
assert len(CRIT3)==10 and len(CRIT4)==1
crit_set = set(CRIT3)
@lru_cache(None)
def reduce_three(face):
    """Project a 3-simplex through 3-to-4 gradient paths onto critical 3-cells."""
    if face in crit_set:return {face:1}
    if face not in MATCH:return {} # upper partner of a 2-face
    coface=MATCH[face]
    assert coface.bit_count()==5
    b=dict(boundary(coface))
    factor=-b[face]
    out=defaultdict(int)
    for sub,coeff in b.items():
        if sub==face:continue
        for target,z in reduce_three(sub).items():
            out[target]+=factor*coeff*z
    return {x:z for x,z in out.items() if z}

morse=defaultdict(int)
for face,sgn in boundary(CRIT4[0]):
    for target,coeff in reduce_three(face).items():
        morse[target]+=sgn*coeff
VECTOR = tuple(morse[c] for c in CRIT3)
assert sorted(abs(v) for v in VECTOR)==[0,0,0,1,1,1,1,1,1,1], VECTOR
assert sum(1 for x in VECTOR if x) == 7
# A unit coefficient makes the attaching vector primitive, so the 4-cell
# cancels one 3-cell up to homotopy. The result is a wedge of nine 3-spheres.

# Character of S5 on H_3 via signed Lefschetz fixed-simplex count.
def cycletype(p):
    seen=set();out=[]
    for i in range(5):
        if i in seen:continue
        j=i;k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        out.append(k)
    return tuple(sorted(out,reverse=True))

def parity(seq):
    return -1 if sum(x>y for i,x in enumerate(seq) for y in seq[i+1:])%2 else 1

# A concrete graph isomorphism: original outer/spoke/star labeling -> KG(5,2).
KG_EDGE_SET = {tuple(sorted((i,j))) for i in range(10) for j in range(i+1,10)
               if set(VERTS[i]).isdisjoint(VERTS[j])}
ISO = None
for outer in permutations(range(10),5):
    if not all(tuple(sorted((outer[i],outer[(i+1)%5]))) in KG_EDGE_SET for i in range(5)):
        continue
    rest = set(range(10))-set(outer)
    inner=[]
    for v in outer:
        choices = [w for w in rest if tuple(sorted((v,w))) in KG_EDGE_SET]
        if len(choices)!=1:break
        inner.append(choices[0])
    if len(inner)!=5 or len(set(inner))!=5:continue
    mapping=tuple(outer)+tuple(inner)
    if {tuple(sorted((mapping[a],mapping[b]))) for a,b in EDGES}==KG_EDGE_SET:
        ISO=mapping;break
assert ISO is not None
INVERSE_ISO = {v:i for i,v in enumerate(ISO)}

def induced_edge_perm(p):
    kg_perm=[VERT_INDEX[tuple(sorted(p[z] for z in pair))] for pair in VERTS]
    vp=[INVERSE_ISO[kg_perm[ISO[v]]] for v in range(10)]
    return tuple(EDGE_INDEX[tuple(sorted((vp[a],vp[b])))] for a,b in EDGES)

def lef_trace(p):
    ep=induced_edge_perm(p)
    alternating=-1  # augmented empty face contributes -1 to reduced Lefschetz
    for face in FACES:
        if not face:continue
        ids=[i for i in range(15) if face>>i&1]
        img=[ep[i] for i in ids]
        if set(img)==set(ids):
            alternating+=parity(img)*((-1)**(len(ids)-1))
    return -alternating  # only reduced degree three survives

results=defaultdict(set)
for p in permutations(range(5)):
    typ=cycletype(p);value=lef_trace(p)
    # The ten vertices of Petersen are the two-subsets of five points.
    fixed_vertices=sum(tuple(sorted(p[z] for z in pair))==pair for pair in VERTS)
    assert value==fixed_vertices-1, (typ,value,fixed_vertices-1)
    results[typ].add(value)
assert all(len(v)==1 for v in results.values())
assert {t:next(iter(v)) for t,v in results.items()}=={
 (1,1,1,1,1):9, (2,1,1,1):3, (2,2,1):1, (3,1,1):0,
 (3,2):0, (4,1):-1, (5,):-1}

print('PASS: 15 graph edges; 145 forbidden triple matchings; 1073 augmented faces')
print('PASS: 530 pairs; 1 critical vertex, 10 critical 3-cells, 1 critical 4-cell')
print('PASS: acyclic Hasse orientation on 1072 nonempty faces')
print('PASS: integral Morse differential',VECTOR,'(primitive), hence wedge of 9 S^3')
print('PASS: all 120 S5 actions; H3 character is the 10-vertex permutation minus trivial')
print('S5 trace by cycle type:', {str(k):next(iter(v)) for k,v in sorted(results.items(),reverse=True)})
