#!/usr/bin/env python3
"""A dependency-free check of the clique complex of the 27 skew lines on a cubic surface.

The labels E_i, L_{ij}, Q_i are divisor classes on the blow-up of P^2 at six points.
Their intersection numbers determine which pairs are disjoint.
"""
from collections import Counter,deque
from itertools import combinations

E=[('E',i) for i in range(6)]
L=[('L',i,j) for i,j in combinations(range(6),2)]
Q=[('Q',i) for i in range(6)]
VERTICES=E+L+Q

def meets(x,y):
    if x[0]=='E' and y[0]=='E':return False
    if x[0]=='Q' and y[0]=='Q':return False
    if x[0]=='E' and y[0]=='L':return x[1] in y[1:]
    if x[0]=='L' and y[0]=='E':return y[1] in x[1:]
    if x[0]=='E' and y[0]=='Q':return x[1]!=y[1]
    if x[0]=='Q' and y[0]=='E':return x[1]!=y[1]
    if x[0]=='L' and y[0]=='L':return not set(x[1:]) & set(y[1:])
    if x[0]=='L' and y[0]=='Q':return y[1] in x[1:]
    if x[0]=='Q' and y[0]=='L':return x[1] in y[1:]
    raise AssertionError((x,y))

ADJ={i:set() for i in range(27)}
for i,j in combinations(range(27),2):
    assert meets(VERTICES[i],VERTICES[j])==meets(VERTICES[j],VERTICES[i])
    if not meets(VERTICES[i],VERTICES[j]):
        ADJ[i].add(j)
        ADJ[j].add(i)
assert all(len(ADJ[i])==16 for i in ADJ)
for i,j in combinations(range(27),2):
    common=len(ADJ[i]&ADJ[j]);assert common==(10 if j in ADJ[i] else 8), (i,j,common)

BY_SIZE={1:[(i,) for i in range(27)]}
for k in range(2,7):
    BY_SIZE[k]=[]
    for sigma in BY_SIZE[k-1]:
        for v in range(sigma[-1]+1,27):
            if all(v in ADJ[w] for w in sigma):
                BY_SIZE[k].append(sigma+(v,))
assert [len(BY_SIZE[k]) for k in range(1,7)]==[27,216,720,1080,648,72]
CELLS={face for k in range(1,7) for face in BY_SIZE[k]}
assert len(CELLS)==2763
# Exactly 216 of the 648 five-vertex cliques cannot be extended to six vertices.
MAXIMAL_FIVES=sum(1 for face in BY_SIZE[5] if not any(set(face).issubset(six) for six in BY_SIZE[6]))
assert MAXIMAL_FIVES==216

# Repeated lowest-available-vertex matching: in each stage, pair a remaining
# face not containing v with the remaining face obtained by adjoining v.
UNPAIRED=set(CELLS)
PAIR=set()
for v in range(27):
    for sigma in sorted([s for s in UNPAIRED if v not in s],key=lambda s:(len(s),s)):
        if sigma not in UNPAIRED:continue
        coface=tuple(sorted(sigma+(v,)))
        if coface in UNPAIRED:
            UNPAIRED.remove(sigma);UNPAIRED.remove(coface)
            assert (sigma,coface) not in PAIR
            PAIR.add((sigma,coface))
assert len(PAIR)==1368
assert Counter(len(s)-1 for s in UNPAIRED)=={0:1,4:26}
assert sum((-1)**(k-1)*len(BY_SIZE[k]) for k in BY_SIZE)==27

# The usual acyclicity orientation sends every unmatched incidence from a
# coface to its codimension-one face, reversing each matched incidence.
indeg={s:0 for s in CELLS}
out={s:[] for s in CELLS}
for size in range(2,7):
    for high in BY_SIZE[size]:
        for cut in range(size):
            low=high[:cut]+high[cut+1:]
            tail,head=(low,high) if (low,high) in PAIR else (high,low)
            out[tail].append(head);indeg[head]+=1
q=deque(s for s,d in indeg.items() if d==0)
count=0
while q:
    s=q.popleft();count+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
assert count==len(CELLS),(count,len(CELLS))

# An independent simplicial-boundary check over the field of two elements.
# This corroborates homology ranks but does not replace the integral Morse proof.
def boundary_rank_mod2(k):
    lower_index={face:i for i,face in enumerate(BY_SIZE[k-1])}
    pivots={}
    for face in BY_SIZE[k]:
        col=0
        for j in range(k):
            col^=1<<lower_index[face[:j]+face[j+1:]]
        while col:
            bit=col.bit_length()-1
            if bit in pivots:
                col^=pivots[bit]
            else:
                pivots[bit]=col
                break
    return len(pivots)
MOD2_BOUNDARY_RANKS=[boundary_rank_mod2(k) for k in range(2,7)]
assert MOD2_BOUNDARY_RANKS==[26,190,530,550,72]
print('VERIFY_OK')
print('vertices=27 edges=216 degrees=16 lambda=10 mu=8')
print('f-vector=',*[len(BY_SIZE[k]) for k in range(1,7)])
print('nonempty_faces=',len(CELLS),'incidences=',sum(len(y) for y in out.values()))
print('maximal_five_vertex_cliques=',MAXIMAL_FIVES)
print('matched_pairs=',len(PAIR),'critical=',Counter(len(s)-1 for s in UNPAIRED))
print('acyclic_topological_sort=',count)
print('mod2_boundary_ranks=',MOD2_BOUNDARY_RANKS)
print('critical_labels=',[VERTICES[i] for i in min(UNPAIRED,key=lambda x:(len(x),x))])
print('critical_4_cells=', sorted([list(s) for s in UNPAIRED if len(s)==5]))
