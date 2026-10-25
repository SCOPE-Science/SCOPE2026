#!/usr/bin/env python3
"""Reproducible exact integer verification of a Pappus incidence-graph complex.
Run with Python 3.10+; standard library only. No external files needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json
from math import lcm

NVERT = 18
OFFSETS = [5, 7, -7, 7, -7, -5] * 3
EDGES = sorted({tuple(sorted((i, (i+1) % NVERT))) for i in range(NVERT)} |
               {tuple(sorted((i, (i+OFFSETS[i]) % NVERT))) for i in range(NVERT)})
assert len(EDGES) == 27
ADJ = [0]*NVERT
for u,v in EDGES:
    ADJ[u] |= 1<<v
    ADJ[v] |= 1<<u
assert all(a.bit_count()==3 for a in ADJ)
TOTAL = 1<<NVERT


def forest_union_find(mask):
    parent = list(range(NVERT))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for u,v in EDGES:
        if (mask>>u)&1 and (mask>>v)&1:
            r,s=root(u),root(v)
            if r==s:
                return False
            parent[r] = s
    return True


def forest_component_count(mask):
    remaining = mask
    components = 0
    twice_edges = 0
    x=mask
    while x:
        b=x&-x
        twice_edges += (ADJ[b.bit_length()-1] & mask).bit_count()
        x ^= b
    while remaining:
        components += 1
        wave=remaining&-remaining
        remaining ^= wave
        while wave:
            b=wave&-wave
            wave ^= b
            fresh=ADJ[b.bit_length()-1] & remaining
            wave |= fresh
            remaining ^= fresh
    return twice_edges//2 == mask.bit_count()-components


FLAGS=bytearray(TOTAL)
FACE_DIM=Counter()
for m in range(TOTAL):
    a=forest_union_find(m)
    assert a==forest_component_count(m), ('forest algorithms disagree',m)
    FLAGS[m]=a
    if a:FACE_DIM[m.bit_count()-1]+=1
assert FACE_DIM[-1]==1

# Sequential coordinate-toggle matching in ascending coordinate order.
MATCH=[-1]*TOTAL
for v in range(NVERT):
    bit=1<<v
    for face in range(TOTAL):
        if not FLAGS[face] or face&bit or MATCH[face]>=0:
            continue
        upper=face|bit
        if FLAGS[upper] and MATCH[upper]<0:
            MATCH[face]=upper
            MATCH[upper]=face
# Keep the original vertex used in the augmented empty-face pair as a
# critical 0-cell, and discard the artificial empty simplex from the CW model.
base_vertex=MATCH[0]
assert base_vertex>0 and base_vertex.bit_count()==1
MATCH[0]=MATCH[base_vertex]=-1
CRITICAL=defaultdict(list)
for m in range(1,TOTAL):
    if FLAGS[m] and MATCH[m]<0:
        CRITICAL[m.bit_count()-1].append(m)
MATCHED_PAIRS=sum(FLAGS[m] and MATCH[m]>=0 for m in range(1,TOTAL))//2
assert MATCHED_PAIRS*2 + sum(map(len,CRITICAL.values())) == sum(FLAGS)-1


def facets(simplex):
    x=simplex
    while x:
        bit=x&-x
        yield (simplex^bit),(-1 if (simplex&(bit-1)).bit_count()%2 else 1)
        x^=bit

# Check every directed Hasse incidence, not merely abstract matching criteria.
INDEG=[0]*TOTAL
INCIDENCES=0
for hi in range(1,TOTAL):
    if not FLAGS[hi]:continue
    for lo,coeff in facets(hi):
        INCIDENCES+=1
        if MATCH[hi]==lo:
            INDEG[hi]+=1   # matched arrow lo -> hi
        else:
            INDEG[lo]+=1   # unmatched arrow hi -> lo
queue=deque(v for v in range(TOTAL) if FLAGS[v] and INDEG[v]==0)
POPPED=0
while queue:
    face=queue.popleft()
    POPPED+=1
    for lo,coeff in facets(face):
        if MATCH[face]==lo:
            continue
        INDEG[lo]-=1
        if INDEG[lo]==0:
            queue.append(lo)
    mate=MATCH[face]
    if mate>=0 and mate.bit_count()>face.bit_count():
        INDEG[mate]-=1
        if INDEG[mate]==0:
            queue.append(mate)
assert POPPED==sum(FLAGS),('non-acyclic Hasse matching',POPPED,sum(FLAGS))


def morse_boundary(k):
    lower=CRITICAL[k-1]
    upper=CRITICAL[k]
    index={s:i for i,s in enumerate(lower)}
    @lru_cache(None)
    def expand(face):
        partner=MATCH[face]
        if partner<0:
            return ((index[face],1),)
        if partner.bit_count()<face.bit_count():
            return ()
        pivot=None
        result=defaultdict(int)
        for other,sgn in facets(partner):
            if other==face:
                pivot=sgn
                continue
            for i,value in expand(other):
                result[i]-=sgn*value
        assert pivot in (-1,1)
        return tuple((i,pivot*val) for i,val in sorted(result.items()) if val)
    matrix=[[0]*len(upper) for _ in lower]
    for j,upperface in enumerate(upper):
        for lo,sgn in facets(upperface):
            for i,val in expand(lo):
                matrix[i][j] += sgn*val
    return matrix

B10=morse_boundary(10)
B11=morse_boundary(11)
assert (len(B10),len(B10[0]))==(1,62)
assert (len(B11),len(B11[0]))==(62,21)
assert sum(x!=0 for row in B10 for x in row)==5
assert all(abs(x)<=1 for row in B10+B11 for x in row)
assert all(sum(B10[0][i]*B11[i][j] for i in range(62))==0 for j in range(21))
assert any(abs(x)==1 for x in B10[0])

# Certify that B11 is a primitive rank-21 integer sublattice by
# literal unimodular integer Gaussian elimination using unit pivots.
M=[row[:] for row in B11]
PIVOTS=[]
for k in range(21):
    pick=next(((r,c) for r in range(k,62) for c in range(k,21) if abs(M[r][c])==1),None)
    assert pick is not None,('no unimodular pivot',k)
    r,c=pick
    M[k],M[r]=M[r],M[k]
    for row in M:
        row[k],row[c]=row[c],row[k]
    sgn=M[k][k]
    assert abs(sgn)==1
    PIVOTS.append(sgn)
    for rr in range(k+1,62):
        factor=M[rr][k]*sgn
        if factor:
            for cc in range(k,21):
                M[rr][cc]-=factor*M[k][cc]
assert all(M[r][c]==0 for r in range(21,62) for c in range(21))

# Independently enumerate the full automorphism group using distance matrices.
DIST=[]
for start in range(NVERT):
    row=[NVERT+1]*NVERT
    row[start]=0
    q=deque([start])
    while q:
        u=q.popleft()
        x=ADJ[u]
        while x:
            bit=x&-x;x^=bit
            v=bit.bit_length()-1
            if row[v]>NVERT:
                row[v]=row[u]+1
                q.append(v)
    DIST.append(row)
assert max(max(r) for r in DIST)==4
ORDER=[0]
while len(ORDER)<NVERT:
    avail=[v for v in range(NVERT) if v not in ORDER]
    ORDER.append(max(avail,key=lambda v:(sum(DIST[v][u]==1 for u in ORDER),-sum(DIST[v][u] for u in ORDER),-v)))
MAP=[-1]*NVERT
AUT=[]
def extend(level,used):
    if level==NVERT:
        assert all(DIST[i][j]==DIST[MAP[i]][MAP[j]] for i in range(NVERT) for j in range(NVERT))
        AUT.append(tuple(MAP))
        return
    vertex=ORDER[level]
    for w in range(NVERT):
        if used>>w&1:continue
        if all(DIST[vertex][u]==DIST[w][MAP[u]] for u in ORDER[:level]):
            MAP[vertex]=w
            extend(level+1,used|(1<<w))
            MAP[vertex]=-1
extend(0,0)
assert len(AUT)==216

CHAR=Counter()
CHAR_BY_ORDER=defaultdict(Counter)
for perm in AUT:
    seen=set();orbits=[];order=1
    for v in range(NVERT):
        if v in seen:continue
        cycle=[];u=v
        while u not in seen:
            seen.add(u)
            cycle.append(u)
            u=perm[u]
        order=lcm(order,len(cycle))
        orbits.append(sum(1<<i for i in cycle))
    num=1<<len(orbits)
    unions=[0]*num
    parity=[1]*num
    acc=0
    for subset in range(num):
        if subset:
            b=subset&-subset
            prev=subset^b
            unions[subset]=unions[prev]|orbits[b.bit_length()-1]
            parity[subset]=-parity[prev]
        if FLAGS[unions[subset]]:
            acc+=parity[subset]
    trace=-acc # reduced signed simplicial Lefschetz; H10 only
    CHAR[trace]+=1
    CHAR_BY_ORDER[order][trace]+=1
assert sum(CHAR.values())==216 and CHAR[40]==1
assert sum(t*count for t,count in CHAR.items())==216
assert sum(t*t*count for t,count in CHAR.items())==2160

answer={
    'graph_vertices':NVERT,'graph_edges':len(EDGES),
    'forest_subsets_including_empty':sum(FLAGS),
    'face_dimensions':dict(sorted(FACE_DIM.items())),
    'matching_pairs':MATCHED_PAIRS,
    'critical_dimensions':{str(k):len(v) for k,v in sorted(CRITICAL.items())},
    'hasse_incidences':INCIDENCES,'hasse_toposort_faces':POPPED,
    'morse_B10_shape':[len(B10),len(B10[0])],
    'morse_B10_nonzero':sum(x!=0 for a in B10 for x in a),
    'morse_B11_shape':[len(B11),len(B11[0])],
    'morse_B11_nonzero':sum(x!=0 for a in B11 for x in a),
    'morse_B11_unit_pivots':len(PIVOTS),
    'reduced_homology':{'10':40},
    'automorphism_group_order':len(AUT),
    'character_distribution':dict(sorted(CHAR.items())),
    'character_by_element_order':{str(k):dict(sorted(v.items())) for k,v in sorted(CHAR_BY_ORDER.items())},
    'fixed_space_dimension':sum(t*count for t,count in CHAR.items())//len(AUT),
    'character_inner_product':sum(t*t*count for t,count in CHAR.items())//len(AUT),
}
print(json.dumps(answer,sort_keys=True,ensure_ascii=False))
print('VERIFY_OK')
