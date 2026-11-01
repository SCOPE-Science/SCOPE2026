#!/usr/bin/env python3
"""Exact finite verification for the 2-matching complex of the three-cube.

Only the Python standard library is required. All face and incidence tests
are exhaustive. The signed Morse differential is computed with integer
arithmetic; mod-2 ranks are a separate simplicial-complex check.
"""
from collections import Counter, defaultdict, deque

NV=8
EDGES=tuple(sorted((u, u^(1<<k)) for u in range(NV)
                   for k in range(3) if u<(u^(1<<k))))
NE=len(EDGES)
assert NE==12
STARS=tuple(sum(1<<i for i, e in enumerate(EDGES) if v in e)
            for v in range(NV))

# Two equivalent and independently implemented face predicates.
def degree_predicate(mask):
    d=[0]*NV
    for i,(u,v) in enumerate(EDGES):
        if mask & (1<<i):
            d[u]+=1
            d[v]+=1
    return all(x<=2 for x in d)

def forbidden_stars_predicate(mask):
    return all((mask & star)!=star for star in STARS)

assert all(degree_predicate(mask)==forbidden_stars_predicate(mask)
           for mask in range(1<<NE))
FACES={mask for mask in range(1,1<<NE) if degree_predicate(mask)}
assert len(FACES)==1698
fvector=tuple(Counter(mask.bit_count()-1 for mask in FACES)[i]
              for i in range(8))
assert fvector==(12,66,212,423,516,352,108,9), fvector

# Greedy repeated element toggles; face pairs are never reused.
remaining=set(FACES)
matched={}
stage_counts=[]
for i in range(NE):
    bit=1<<i
    lows=sorted(face for face in remaining if not(face&bit) and
                (face|bit) in remaining)
    for face in lows:
        high=face|bit
        assert face in remaining and high in remaining
        remaining.remove(face)
        remaining.remove(high)
        matched[face]=high
    stage_counts.append(len(lows))
assert stage_counts==[665,94,8,51,8,10,7,0,2,1,0,0],stage_counts
assert len(matched)==846
assert len(remaining)==6
critical=tuple(sorted(remaining))
assert critical==(1,598,888,1446,2710,3158), critical
assert Counter(x.bit_count()-1 for x in critical)=={0:1,4:1,5:4}

# Acyclicity of every closed V-path: among low matched faces, the directed
# edge low -> other codimension-one face of its paired upper cell.
# A topological sort of the entire transition graph is exhaustive.
next_low={}
indeg=dict.fromkeys(matched,0)
for low,high in matched.items():
    nxt=tuple(high^(1<<j) for j in range(NE) if high&(1<<j)
              if (high^(1<<j)) !=low and (high^(1<<j)) in matched)
    next_low[low]=nxt
    for other in nxt: indeg[other]+=1
queue=deque(sorted(x for x in indeg if indeg[x]==0))
visited=[]
while queue:
    low=queue.popleft()
    visited.append(low)
    for other in next_low[low]:
        indeg[other]-=1
        if indeg[other]==0:queue.append(other)
assert len(visited)==len(matched),(len(visited),len(matched))

# Full Hasse face incidence count; all codimension-one faces including
# the empty face are in the ambient simplicial complex.
hasse=sum(mask.bit_count() for mask in FACES if mask.bit_count()>=2)
assert hasse==sum((i+1)*fvector[i] for i in range(1,8))

def boundary(mask):
    return {mask^(1<<j):(-1 if p%2 else 1)
            for p,j in enumerate(j for j in range(NE) if mask&(1<<j))}

# Morse boundary in dimensions 5 -> 4. Cancel paired 4- and 5-cells
# in topological V-path order, with exact integer coefficients.
paired4={low:high for low,high in matched.items() if low.bit_count()==5}
indeg4={low:0 for low in paired4}
next4={}
for low,high in paired4.items():
    successors=tuple((high^(1<<j)) for j in range(NE)
                     if high&(1<<j) and (high^(1<<j))!=low
                     and (high^(1<<j)) in paired4)
    next4[low]=successors
    for nxt in successors:indeg4[nxt]+=1
q=deque(sorted(x for x in indeg4 if indeg4[x]==0))
order=[]
while q:
    low=q.popleft()
    order.append(low)
    for other in next4[low]:
        indeg4[other]-=1
        if indeg4[other]==0:q.append(other)
assert len(order)==len(paired4)
critical4=[mask for mask in critical if mask.bit_count()==5]
critical5=[mask for mask in critical if mask.bit_count()==6]
assert critical4==[598] and critical5==[888,1446,2710,3158]
differential=[]
for high in critical5:
    coef=defaultdict(int,boundary(high))
    for low in order:
        a=coef[low]
        if a==0:continue
        paired_high=paired4[low]
        db=boundary(paired_high)
        assert db[low] in (-1,1)
        for t,c in db.items():
            coef[t]-=a*db[low]*c
    assert all(coef[low]==0 for low in paired4)
    differential.append(coef[critical4[0]])
assert differential==[-1,1,-1,-1],differential
assert any(abs(a)==1 for a in differential)

# Independent simplicial mod-2 boundary ranks computed by sparse bit-vectors.
bydim={k:sorted(x for x in FACES if x.bit_count()==k+1) for k in range(8)}
ranks={}
for k in range(1,8):
    rowindex={x:j for j,x in enumerate(bydim[k-1])}
    pivots={}
    for face in bydim[k]:
        col=0
        for j in range(NE):
            if face&(1<<j):
                col ^= 1<<rowindex[face^(1<<j)]
        while col:
            bit=col.bit_length()-1
            if bit not in pivots:
                pivots[bit]=col
                break
            col^=pivots[bit]
    ranks[k]=len(pivots)
assert ranks=={1:11,2:55,3:157,4:266,5:250,6:99,7:9},ranks
bettis={k:len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)
        -(1 if k==0 else 0) for k in range(8)}
assert bettis=={0:0,1:0,2:0,3:0,4:0,5:3,6:0,7:0}

print('CUBE_Q3_TWO_MATCHING_EXACT_VERIFIED')
print('vertices=8, edges=12')
print('edge_order='+str(EDGES))
print('tested_subsets=4096, valid_nonempty_faces=1698')
print('fvector='+str(fvector))
print('toggle_matching_stage_pairs='+str(tuple(stage_counts)))
print('total_pairs=846, V_path_vertices_verified=846, acyclic=True')
print('Hasse_cover_incidences='+str(hasse))
print('critical_masks='+str(critical))
print('critical_cell_dimensions=(0,4,5,5,5,5)')
print('integer_Morse_d5_row='+str(tuple(differential)))
print('primitive_degree=True')
print('mod2_boundary_ranks='+str(ranks))
print('reduced_mod2_Betti='+str(bettis))
print('homotopy_type=wedge_of_three_5_spheres')
