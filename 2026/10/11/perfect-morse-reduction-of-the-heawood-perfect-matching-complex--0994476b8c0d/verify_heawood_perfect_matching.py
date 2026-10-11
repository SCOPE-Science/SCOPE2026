#!/usr/bin/env python3
"""Exhaustive finite certificate for the perfect-matching complex of the Fano incidence graph.

Python 3 standard library only. Every claimed combinatorial number is reconstructed.
"""
from collections import Counter, deque
from itertools import combinations

N = 7
LINES = [frozenset((i, (i+1)%N, (i+3)%N)) for i in range(N)]
EDGES = [(p,i) for i,L in enumerate(LINES) for p in sorted(L)]
assert len(EDGES) == 21 and len(set(EDGES)) == 21
assert all(sum(p in L for L in LINES) == 3 for p in range(N))
assert all(sum({p,q} <= L for L in LINES) == 1 for p,q in combinations(range(N),2))
assert all(len(L) == 3 for L in LINES)

# Independent permanent count via subsets of used lines.
dp = {0:1}
for p in range(N):
    new = {}
    for mask,count in dp.items():
        for i,L in enumerate(LINES):
            if p in L and not(mask & (1<<i)):
                k = mask | 1<<i
                new[k] = new.get(k,0)+count
    dp=new
assert dp == {(1<<N)-1:24}, dp

# Exhaustively construct all bijective incidence assignments.
BY_POINT = [[j for j,(q,i) in enumerate(EDGES) if q==p] for p in range(N)]
facets=[]
def visit(point,used_lines,mask):
    if point == N:
        assert used_lines == (1<<N)-1 and mask.bit_count()==N
        facets.append(mask)
        return
    for e in BY_POINT[point]:
        line=EDGES[e][1]
        if not (used_lines>>line)&1:
            visit(point+1,used_lines | (1<<line), mask | (1<<e))
visit(0,0,0)
assert len(facets)==24 and len(set(facets))==24

# Exact downward closure, including all 21 possible one-edge faces.
faces=set()
for facet in facets:
    bits=[1<<j for j in range(len(EDGES)) if facet>>j&1]
    for k in range(1,N+1):
        for sub in combinations(bits,k):
            m=0
            for b in sub:m |= b
            faces.add(m)
assert len(faces)==2201
fv=tuple(sum(f.bit_count()==d+1 for f in faces) for d in range(N))
assert fv==(21,168,560,756,504,168,24),fv

# The stage-wise edge-toggle pairing (empty face excluded).
remaining=set(faces)
pairs=[]
for j in range(len(EDGES)):
    bit=1<<j
    for lower in sorted(f for f in remaining if not f & bit):
        upper=lower | bit
        if lower in remaining and upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            pairs.append((lower,upper))
assert len(pairs)==1092 and len(remaining)==17
critical_by_dim=Counter(f.bit_count()-1 for f in remaining)
assert critical_by_dim=={0:1,2:16},critical_by_dim
critical0=[x for x in remaining if x.bit_count()==1]
assert len(critical0)==1

# Confirm match edges are covers and no vertex repeats.
matched=set()
matched_up=set()
for lo,up in pairs:
    assert lo in faces and up in faces and lo.bit_count()+1==up.bit_count()
    assert lo & up == lo and lo not in matched and up not in matched
    matched.add(lo); matched.add(up); matched_up.add((lo,up))
assert matched.isdisjoint(remaining) and matched | remaining == faces

# Complete directed Hasse graph: unmatched covers high->low, matched covers low->high.
adj={f:[] for f in faces}
indeg=dict.fromkeys(faces,0)
incidences=0
for upper in faces:
    bitset=upper
    while bitset:
        bit=bitset & -bitset
        bitset -= bit
        lower=upper ^ bit
        if not lower:
            continue
        assert lower in faces
        incidences+=1
        if (lower,upper) in matched_up:
            src,dst=lower,upper
        else:
            src,dst=upper,lower
        adj[src].append(dst)
        indeg[dst]+=1
assert incidences == sum((d+1)*fv[d] for d in range(N)) - fv[0]
queue=deque(f for f,v in indeg.items() if v==0)
processed=0
while queue:
    x=queue.popleft()
    processed+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:queue.append(y)
assert processed==len(faces),('cyclic directed face poset',processed)

# Independently compute every simplicial boundary rank over F_2.
by_dim=[sorted(f for f in faces if f.bit_count()==d+1) for d in range(N)]
rank={0:0}
for d in range(1,N):
    row_of={m:i for i,m in enumerate(by_dim[d-1])}
    piv={}
    for upper in by_dim[d]:
        col=0
        q=upper
        while q:
            bit=q & -q;q-=bit
            col ^= 1<<row_of[upper^bit]
        while col:
            p=col.bit_length()-1
            if p in piv:col ^= piv[p]
            else:piv[p]=col;break
    rank[d]=len(piv)
rank[N]=0
bettis=tuple(fv[d]-rank[d]-rank[d+1] for d in range(N))
assert bettis==(1,0,16,0,0,0,0),(rank,bettis)

print('VERIFY_OK', 'facets='+str(len(facets)), 'faces='+str(len(faces)),
    'fvector='+str(fv), 'pairs='+str(len(pairs)),
    'critical='+str(dict(critical_by_dim)), 'directed_incidences='+str(incidences),
    'acyclic_visited='+str(processed), 'mod2_ranks='+str(tuple(rank[i] for i in range(1,N))),
    'mod2_betti='+str(bettis), 'homotopy=16xS2')
