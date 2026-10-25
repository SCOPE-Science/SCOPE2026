#!/usr/bin/env python3
"""Self-contained exact certificate for a finite graph-complex homotopy computation."""
from collections import Counter, deque
from itertools import combinations

N=8
V=2*N
ORDER=(13,10,1,12,4,11,2,7,9,6,3,15,0,14,8,5)
EDGES=set()
for i in range(N):
    for a,b in ((i,(i+1)%N),(i,8+i),(8+i,8+(i+3)%N)):
        EDGES.add(tuple(sorted((a,b))))
assert len(EDGES)==24
ADJ=[set() for _ in range(V)]
for a,b in EDGES:
    ADJ[a].add(b);ADJ[b].add(a)
assert all(len(x)==3 for x in ADJ)
assert all(not ((ADJ[i]&ADJ[j]) and j in ADJ[i]) for i in range(V) for j in ADJ[i])

# Any component of order >=3 contains a length-two path, so the forbidden
# triples are precisely vertex triples inducing at least two graph edges.
forbidden=[]
for trip in combinations(range(V),3):
    if sum(tuple(sorted(e)) in EDGES for e in combinations(trip,2))>=2:
        forbidden.append(sum(1<<j for j in trip))
assert len(forbidden)==48
F=set()
for mask in range(1,1<<V):
    if not any((mask&t)==t for t in forbidden):
        F.add(mask)
assert len(F)==6812
bydim=Counter(f.bit_count()-1 for f in F)
assert dict(sorted(bydim.items()))=={0:16,1:120,2:512,3:1324,4:2064,5:1840,6:816,7:120}

# Second, logically independent, connected-component test on all 2^16 masks.
for mask in range(1,1<<V):
    remaining={v for v in range(V) if mask>>v &1}
    good=True
    while remaining:
        component={remaining.pop()}
        stack=list(component)
        while stack:
            v=stack.pop()
            for w in (ADJ[v]&remaining):
                remaining.remove(w);component.add(w);stack.append(w)
        if len(component)>2:good=False;break
    assert good==(mask in F)

# Element matchings in the stated global pivot order, each on the
# as-yet-unpaired face poset.
unpaired=set(F)
match={}
for v in ORDER:
    bit=1<<v
    for lo in sorted(tuple(unpaired)):
        if lo not in unpaired or (lo&bit):continue
        hi=lo|bit
        if hi in unpaired:
            match[lo]=hi
            unpaired.remove(lo);unpaired.remove(hi)
assert len(match)==3404
assert len(unpaired)==4
assert Counter(x.bit_count()-1 for x in unpaired)=={0:1,6:3}
assert sorted(unpaired)==[8192,33637,33644,49964]

# All codimension-one Hasse edges: reverse precisely matching edges,
# then check acyclicity by Kahn's exact directed-graph algorithm.
succ={f:[] for f in F}
indeg={f:0 for f in F}
edgecount=0
for big in F:
    for v in range(V):
        if big>>v & 1:
            small=big^(1<<v)
            if not small:continue
            if match.get(small)==big:src,dst=small,big
            else:src,dst=big,small
            succ[src].append(dst)
            indeg[dst]+=1
            edgecount+=1
assert edgecount==35104
queue=deque(f for f in F if indeg[f]==0)
seen=0
while queue:
    f=queue.popleft();seen+=1
    for g in succ[f]:
        indeg[g]-=1
        if indeg[g]==0:queue.append(g)
assert seen==len(F), 'alternating-cycle detected'

# Exact independent F_2 boundary reductions. H_d = ker(d_d)/im(d_{d+1}).
bydimfaces={d:sorted(f for f in F if f.bit_count()-1==d) for d in sorted(bydim)}
rank={}
for d in range(1,8):
    target={f:i for i,f in enumerate(bydimfaces[d-1])}
    piv={}
    for f in bydimfaces[d]:
        bits=0
        for v in range(V):
            if f>>v &1:bits^=1<<target[f^(1<<v)]
        while bits:
            k=bits.bit_length()-1
            if k in piv:bits^=piv[k]
            else:piv[k]=bits;break
    rank[d]=len(piv)
betti={d:len(bydimfaces[d])-rank.get(d,0)-rank.get(d+1,0) for d in bydimfaces}
assert betti=={0:1,1:0,2:0,3:0,4:0,5:0,6:3,7:0}
print('VERIFY_OK')
print('vertices=16 edges=24 forbidden_triples=48 nonempty_faces=6812')
print('f_vector='+str([bydim[i] for i in range(8)]))
print('matching_pairs=3404 critical_masks='+str(sorted(unpaired)))
print('directed_hasse_edges=35104 acyclic_toposort_vertices=6812')
print('mod2_boundary_ranks='+str([rank[i] for i in range(1,8)]))
print('mod2_betti='+str([betti[i] for i in range(8)]))
