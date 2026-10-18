#!/usr/bin/env python3
"""Self-contained exact finite certificate for homology and S4 character of a matching complex."""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from math import factorial

LABELS = tuple(range(4))
VERTICES = tuple((a,b) for a in LABELS for b in LABELS if a != b)
EDGE_SET = set()
for a in LABELS:
    bs = [b for b in LABELS if b != a]
    for b,c in combinations(bs, 2):
        EDGE_SET.add(tuple(sorted(((a,b),(a,c)))))
for a,b in combinations(LABELS,2):
    EDGE_SET.add(tuple(sorted(((a,b),(b,a)))))
EDGES = tuple(sorted(EDGE_SET))
assert len(VERTICES)==12 and len(EDGES)==18
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
TRIANGLE_EDGE_INDICES = [i for i,e in enumerate(EDGES) if e[0][0] == e[1][0]]
REVERSAL_EDGE_INDICES = [i for i in range(18) if i not in TRIANGLE_EDGE_INDICES]
assert len(TRIANGLE_EDGE_INDICES) == 12 and len(REVERSAL_EDGE_INDICES)==6
assert len([s for s in combinations(VERTICES,3) if all(tuple(sorted(pair)) in EDGE_SET for pair in combinations(s,2))])==4

# Exhaustively enumerate the faces; mask bits refer to graph edges in sorted order.
FACES = {0}
for i,e in enumerate(EDGES):
    new = set()
    for mask in FACES:
        endpoints=set()
        for j in range(18):
            if mask >> j & 1:
                endpoints.update(EDGES[j])
        if all(v not in endpoints for v in e):
            new.add(mask|(1<<i))
    FACES |= new
FACES.discard(0)
assert len(FACES)==1009
counts=Counter(f.bit_count()-1 for f in FACES)
assert [counts[k] for k in range(6)] == [18,117,332,390,144,8]

# Nonaugmented discrete Morse matching. The chosen greedy bit order processes
# all reversal edges before the twelve triangle edges.
order=tuple(REVERSAL_EDGE_INDICES+TRIANGLE_EDGE_INDICES)
remaining=set(FACES)
pairs=[]
for i in order:
    bit=1<<i
    for face in sorted(remaining):
        if not face&bit and face|bit in remaining and face in remaining:
            remaining.remove(face)
            remaining.remove(face|bit)
            pairs.append((face,face|bit))
critical=Counter(f.bit_count()-1 for f in remaining)
print('face_counts', [counts[k] for k in range(6)])
print('pairs',len(pairs),'critical',sorted(critical.items()))
assert len(pairs)==493 and critical == Counter({0:1,3:22}), (len(pairs), critical)

# Every covering relation of the nonempty face poset occurs exactly once.
paired=set(pairs)
indeg={f:0 for f in FACES}
succ=defaultdict(list)
incidences=0
for hi in FACES:
    for i in range(18):
        if hi>>i&1:
            lo=hi ^ (1<<i)
            if not lo:
                continue
            assert lo in FACES
            incidences+=1
            if (lo,hi) in paired:
                u,v=lo,hi # matched cover is reversed upward
            else:
                u,v=hi,lo # ordinary cover directed downward
            succ[u].append(v)
            indeg[v]+=1
queue=deque(f for f,n in indeg.items() if n==0)
seen=0
while queue:
    u=queue.popleft(); seen+=1
    for v in succ[u]:
        indeg[v]-=1
        if indeg[v]==0:
            queue.append(v)
print('hasse_incidences',incidences,'acyclic_vertices',seen)
assert incidences==3558 and seen==1009

# Signed fixed-simplex Lefschetz character for the full 24-element group.
face_by_dim=[sorted(f for f in FACES if f.bit_count()==r+1) for r in range(6)]
cls=defaultdict(list)
for p in permutations(LABELS):
    edge_action=[EDGE_INDEX[tuple(sorted(((p[a],p[b]),(p[c],p[d]))))]
                 for ((a,b),(c,d)) in EDGES]
    assert sorted(edge_action)==list(range(18))
    # Independent orbit-union signed fixed-simplex count. Each invariant
    # face must be the union of some cycles of the action on 18 edge labels.
    cycles=[];used=set()
    for start in range(18):
        if start in used:continue
        cycle=[];z=start
        while z not in used:
            used.add(z);cycle.append(z);z=edge_action[z]
        assert z==start
        cycles.append(cycle)
    orbit_lefschetz=0
    for sub in range(1,1<<len(cycles)):
        chosen=[c for j,c in enumerate(cycles) if sub>>j&1]
        inds=[i for c in chosen for i in c]
        mask=sum(1<<i for i in inds)
        if mask not in FACES:continue
        k=len(inds)
        orbit_sign=(-1)**sum(len(c)-1 for c in chosen)
        orbit_lefschetz+=(-1)**(k-1)*orbit_sign
    chain_traces=[]
    for row in face_by_dim:
        tr=0
        for f in row:
            inds=[i for i in range(18) if (f>>i)&1]
            target=[edge_action[i] for i in inds]
            if set(target)==set(inds):
                parity=sum(target[i]>target[j] for i in range(len(target)) for j in range(i+1,len(target)))%2
                tr+=(-1)**parity
        chain_traces.append(tr)
    # Reduced Lefschetz trace is sum (-1)^r trace C_r - 1.
    # Only reduced H_3 is nonzero, so its trace is minus the reduced trace.
    chi=1-sum((-1)**i * tr for i,tr in enumerate(chain_traces))
    assert chi==1-orbit_lefschetz,(p,chi,orbit_lefschetz)
    seen_set=set();typ=[]
    for i in LABELS:
        if i not in seen_set:
            j=i;k=0
            while j not in seen_set:
                seen_set.add(j);k+=1;j=p[j]
            typ.append(k)
    cls[tuple(sorted(typ,reverse=True))].append(chi)
classes=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
expected=(22,0,2,-2,-2)
class_sizes=(1,6,3,8,6)
assert tuple(len(cls[k]) for k in classes)==class_sizes
assert tuple(next(iter(set(cls[k]))) for k in classes)==expected
assert all(len(set(cls[k]))==1 for k in classes)
print('class_sizes',class_sizes,'H3_character',expected)
chars={
    'trivial': (1,1,1,1,1),
    'sign': (1,-1,1,1,-1),
    'standard':(3,1,-1,0,-1),
    'sign_standard':(3,-1,-1,0,1),
    'two_dimensional':(2,0,2,-1,0),
}
mult={}
for name,vec in chars.items():
    num=sum(s*x*y for s,x,y in zip(class_sizes,expected,vec))
    assert num%24==0
    mult[name]=num//24
assert mult=={'trivial':0,'sign':1,'standard':3,'sign_standard':2,'two_dimensional':3}
assert sum(mult[n]*chars[n][0] for n in chars)==22
print('S4_multiplicities',mult)
print('VERIFIED: finite acyclic Morse matching and two independent signed Lefschetz methods on 24 elements')
