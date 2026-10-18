"""Exact certificate of the persistent 3-torsion class among seven-vertex matching complexes.

Requires only Python 3 and adjacent verify_m7_sign.py and torsion_atlas_masks.json.
"""
import json
from itertools import combinations,permutations
from pathlib import Path
import verify_m7_sign as base

edges=base.labels
edge_idx=base.label_index
pairs=list(combinations(range(7),2))
idx={e:i for i,e in enumerate(pairs)}
minimal=[(0,1),(0,5),(0,6),(1,3),(1,4),(2,3),(2,4),(2,5),(2,6),(3,5),(3,6),(4,5),(4,6)]
mask=sum(1<<idx[e] for e in minimal)
missing=[i for i in range(21) if not(mask>>i&1)]
assert len(missing)==8
permuted_positions=[]
for g in permutations(range(7)):
    permuted_positions.append([idx[tuple(sorted((g[a],g[b])))] for a,b in pairs])

def canon(m):
    best=1<<22
    for moved in permuted_positions:
        q=0
        for j in range(21):
            if m>>j&1:q|=1<<moved[j]
        if q<best:best=q
    return best

catalog=json.loads(Path(__file__).with_name('torsion_atlas_masks.json').read_text())['masks']
known={canon(v) for v in catalog.values()}
assert len(known)==40
supers=set()
for flags in range(256):
    q=mask
    for j,e in enumerate(missing):
        if flags>>j&1:q|=1<<e
    supers.add(canon(q))
assert len(supers)==40 and known==supers

# An explicit integral Bockstein lifts a mod-three d2 cycle of the minimal graph.
V={e:i for i,e in enumerate(minimal)}
f1=[(i,j) for i,j in combinations(range(len(minimal)),2)
    if set(minimal[i]).isdisjoint(minimal[j])]
f2=[(i,j,k) for i,j,k in combinations(range(len(minimal)),3)
    if len(set(minimal[i]+minimal[j]+minimal[k]))==6]
lookup={f:i for i,f in enumerate(f1)}
cols=[]
for i,j,k in f2:
    col=[0]*len(f1)
    for f,s in (((j,k),1),((i,k),-1),((i,j),1)):
        col[lookup[f]]+=s
    cols.append(col)
assert (len(f1),len(f2))==(42,30)
# Row-reduce the 42-by-30 d2 matrix over F3 and extract a kernel vector.
A=[[cols[j][i]%3 for j in range(len(cols))] for i in range(len(f1))]
pivots=[]
row=0
for j in range(len(cols)):
    rr=next((r for r in range(row,len(A)) if A[r][j]),None)
    if rr is None:continue
    A[row],A[rr]=A[rr],A[row]
    inv=pow(A[row][j],-1,3)
    A[row]=[x*inv%3 for x in A[row]]
    for r in range(len(A)):
        if r!=row and A[r][j]:
            scale=A[r][j]
            A[r]=[(x-scale*y)%3 for x,y in zip(A[r],A[row])]
    pivots.append(j)
    row+=1
assert len(pivots)==29
free=next(j for j in range(len(cols)) if j not in pivots)
c=[0]*len(cols)
c[free]=1
for k,j in enumerate(pivots):c[j]=-A[k][free]%3
bd=[sum(c[j]*cols[j][e] for j in range(len(cols))) for e in range(len(f1))]
assert all(x%3==0 for x in bd)
z=[x//3 for x in bd]
# Verify the integral chain is closed in the minimal matching complex.
d1=[0]*len(minimal)
for k,x in enumerate(z):
    if x:
        i,j=f1[k]
        d1[i]-=x
        d1[j]+=x
assert all(v==0 for v in d1)
# The inclusion into M(K7) is detected by its independently computed mod-3 cocycle.
embedded=0
for k,x in enumerate(z):
    if x:
        i,j=f1[k]
        a=edge_idx[minimal[i]]
        b=edge_idx[minimal[j]]
        embedded+=x*(1 if a<b else -1)*base.phi[base.face1_index[(min(a,b),max(a,b))]]
embedded%=3
assert embedded in (1,2)
print('Exactly 40 isomorphism types arise from the 256 labelled supergraphs of G1105')
print('The 40 isomorphism types equal the independently encoded published torsion catalog')
print('Minimal torsion 2-chain has',sum(bool(v) for v in c),'nonzero mod-3 coefficients')
print('Integral Bockstein torsion cycle support',sum(bool(x) for x in z))
print('Its image in H1(M(K7);Z/3) has nonzero torsion coordinate',embedded)
print('Therefore inclusion on integral Z/3 homology is injective for every torsion graph')
print('PASS')
