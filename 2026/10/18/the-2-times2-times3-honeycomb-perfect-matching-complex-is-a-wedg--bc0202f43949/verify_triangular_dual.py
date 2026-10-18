#!/usr/bin/env python3
"""Exhaustive independent dual-triangle perfect-matching verifier for H(2,2,3).
Only finite exact integer/set operations; prints the full matching and Morse counts.
"""
from collections import Counter
from itertools import combinations

A,B,C=2,2,3
ex=(1,0);ey=(0,1);ez=(-1,-1)
steps={'x':(ey,ez),'y':(ex,ez),'z':(ex,ey)}
def add(q,v):return(q[0]+v[0],q[1]+v[1])
def tiles(t,q):
 u,v=steps[t];uv=add(u,v)
 return tuple(sorted((tuple(sorted((q,add(q,u),add(q,uv)))),tuple(sorted((q,add(q,v),add(q,uv)))))))
# One explicit tiling with all plane-partition entries zero. This specifies
# exactly the thirty-two elementary triangular cells of the hexagonal region.
base=[]
for i in range(A):
 for j in range(B):base.append(('z',(i,j)))
for j in range(B):
 for k in range(C):base.append(('x',(-k,j-k)))
for i in range(A):
 for k in range(C):base.append(('y',(i-k,-k)))
region=set()
for t,q in base:
 ts=tiles(t,q)
 assert not any(x in region for x in ts),(t,q)
 region.update(ts)
assert len(region)==2*(A*B+B*C+A*C)==32
tri=sorted(region);loc={T:i for i,T in enumerate(tri)}
# Every pair of adjacent unit triangles makes a possible lozenge. This
# constructs the honeycomb graph without using plane partitions.
adj={}
for i,j in combinations(range(len(tri)),2):
 if len(set(tri[i])&set(tri[j]))==2:
  adj[(i,j)]=None
# Coordinate atlas of all possible rhombus edges, independent of tiling.
lookup={}
for typ in 'xyz':
 for x in range(-C-2,A+B+3):
  for y in range(-C-2,A+B+3):
   pair=tiles(typ,(x,y))
   if all(p in loc for p in pair):
    e=tuple(sorted(loc[p] for p in pair))
    assert e not in lookup or lookup[e]==(typ,x,y)
    lookup[e]=(typ,x,y)
assert set(adj)==set(lookup),(set(adj)-set(lookup),set(lookup)-set(adj))
edges=sorted(lookup.values())
index={e:i for i,e in enumerate(edges)}
assert len(edges)==41,len(edges)
edgeends={index[lookup[e]]:e for e in adj}
incident=[[] for _ in tri]
for ei,(a,b) in edgeends.items():
 incident[a].append((b,ei));incident[b].append((a,ei))
# Enumerate all perfect matchings using first uncovered triangle branching.
allbits=(1<<len(tri))-1
perfect=set()
def dfs(mask,selected):
 if mask==allbits:
  perfect.add(selected);return
 rest=allbits^mask
 pick=(rest&-rest).bit_length()-1
 for other,ei in incident[pick]:
  if not (mask>>other)&1:
   dfs(mask|(1<<pick)|(1<<other),selected|(1<<ei))
dfs(0,0)
assert len(perfect)==50,len(perfect)
assert all(f.bit_count()==16 for f in perfect)
# Independent plane-partition coordinate parametrization must give precisely
# these perfect matchings, not merely the same cardinality.
from itertools import product
plane=set()
for hflat in product(range(C+1),repeat=A*B):
 h=[hflat[i*B:(i+1)*B] for i in range(A)]
 if any(h[i][j]<h[i+1][j] for i in range(A-1) for j in range(B)):continue
 if any(h[i][j]<h[i][j+1] for i in range(A) for j in range(B-1)):continue
 f=[]
 for i in range(A):
  for j in range(B):f.append(('z',i-h[i][j],j-h[i][j]))
 for j in range(B):
  for k in range(C):
   x=sum(h[i][j]>k for i in range(A));f.append(('x',x-k,j-k))
 for i in range(A):
  for k in range(C):
   y=sum(h[i][j]>k for j in range(B));f.append(('y',i-k,y-k))
 plane.add(sum(1<<index[e] for e in f))
assert plane==perfect
# Complete face-union enumeration; no plane partition data enters this run.
faces={0}
for facet in perfect:
 s=facet
 while s:
  faces.add(s);s=(s-1)&facet
assert len(faces)==2517788,len(faces)
fvector=Counter(s.bit_count()-1 for s in faces if s)
assert [fvector[k] for k in range(16)]==[41,706,6186,31566,104477,241386,407750,517618,501141,371866,210600,89700,27900,6000,800,50]
# Stagewise elementary element pairings on the nonempty face poset.
faces.remove(0)
pivots=(24,1,17,12,40,6,7,28,34)
trace=[]
for pivot in pivots:
 bit=1<<pivot
 lows=[s for s in faces if not s&bit and s|bit in faces]
 for s in lows:
  faces.remove(s);faces.remove(s|bit)
 trace.append((pivot,len(lows),len(faces)))
assert trace==[(24,1011305,495177),(1,247522,133),(17,30,73),(12,26,21),(40,3,15),(6,3,9),(7,1,7),(28,1,5),(34,1,3)],trace
assert len(faces)==3
assert Counter(s.bit_count()-1 for s in faces)=={0:1,4:2}
assert sorted(faces)==[16777216,2155873346,137439215754],sorted(faces)
print('dual-triangle graph:',len(tri),'vertices,',len(edges),'usable edges,',len(perfect),'perfect matchings')
print('f-vector:',','.join(str(fvector[k]) for k in range(16)))
print('ordinary Morse pairing stages:',trace)
print('critical bit-mask simplices:',sorted(faces))
print('VERIFIED: one zero-cell, two dimension-four critical cells.')
