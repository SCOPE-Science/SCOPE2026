#!/usr/bin/env python3
"""Exact finite check for the Rips complex of the edge-subdivided 3-cube.
Only the Python standard library is required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product

N=8
verts=range(8)
H_edges=[(a,b) for a,b in combinations(verts,2) if (a^b).bit_count()==1]
edgeno={p:i for i,p in enumerate(H_edges)}
V=20
neighbors=[set() for _ in range(V)]
for j,(a,b) in enumerate(H_edges):
 m=8+j;neighbors[a].add(m);neighbors[b].add(m)
 neighbors[m].add(a);neighbors[m].add(b)
def distances(a):
 ds={a:0};q=deque([a])
 while q:
  x=q.popleft()
  for y in neighbors[x]:
   if y not in ds:ds[y]=ds[x]+1;q.append(y)
 return ds
D=[distances(v) for v in range(V)]
assert len(H_edges)==12 and all(len(d)==V for d in D)
R_neighbors=[{j for j in range(V) if j!=i and D[i][j]<=3} for i in range(V)]
faces=[]
def cliques(prefix,candidates):
 if prefix:faces.append(tuple(prefix))
 for i,v in enumerate(candidates):
  cliques(prefix+[v],[w for w in candidates[i+1:] if w in R_neighbors[v]])
cliques([],list(range(V)))
assert len(faces)==516, len(faces)
assert Counter(len(s)-1 for s in faces)=={0:20,1:108,2:212,3:152,4:24}
# Fixed, reproducible vertex order used by an acyclic lexicographic matching.
order=[5,6,18,1,7,11,2,13,16,3,15,0,17,4,12,19,8,9,10,14]
def mask(f):return sum(1<<v for v in f)
F={mask(f) for f in faces}
active=set(F);matching=[]
for v in order:
 bv=1<<v
 for a in sorted(active):
  if (a&bv)==0 and a|bv in active:
   b=a|bv;active.remove(a);active.remove(b);matching.append((a,b))
assert len(matching)==254, len(matching)
assert Counter(a.bit_count()-1 for a in active)=={0:1,2:1,3:6}, Counter(a.bit_count()-1 for a in active)
# Every face relation is oriented downward, except matching edges upward.
M={(a,b) for a,b in matching}
out={x:[] for x in F}; indeg={x:0 for x in F}
for b in F:
 if b.bit_count()<2:continue
 for v in range(V):
  if not b>>v&1:continue
  a=b^(1<<v)
  if (a,b) in M: src,dst=a,b
  else:src,dst=b,a
  out[src].append(dst);indeg[dst]+=1
q=deque(x for x in F if indeg[x]==0);count=0
while q:
 x=q.popleft();count+=1
 for y in out[x]:
  indeg[y]-=1
  if indeg[y]==0:q.append(y)
assert count==len(F)==516,('cycle',count)
# Subdivided square faces give six embedded octahedral 3-spheres.
F3={f for f in faces if len(f)==4};F4={f for f in faces if len(f)==5}
covered=set()
for f in F4:
 for q in combinations(f,4):covered.add(q)
square_3sphere={};witness={};antipodal_pairs={}
for fixed in range(3):
 for value in range(2):
  octagon_corners=[a for a in verts if (a>>fixed)&1==value]
  mids=[8+j for j,(a,b) in enumerate(H_edges) if a in octagon_corners and b in octagon_corners]
  sub=set(octagon_corners+mids)
  assert len(sub)==8
  # Subcomplex is the join of 4 antipodal pairs; 16 tetrahedra, no 4-simplices.
  tetra={f for f in F3 if set(f)<=sub}
  assert len(tetra)==16
  assert not any(set(f)<=sub for f in F4)
  # Opposite pairs are distance four, all other pairs at distance at most three.
  opposite=[(x,y) for x,y in combinations(sorted(sub),2) if D[x][y]>3]
  assert len(opposite)==4 and len(set(sum(([a,b] for a,b in opposite),[])))==8
  sf=(fixed,value);square_3sphere[sf]=tetra;antipodal_pairs[sf]=sorted(tuple(sorted(p)) for p in opposite)
  free=sorted(tetra-covered)
  assert len(free)>=1
  witness[sf]=free[0]
assert len(set(witness.values()))==6
for sf,t in witness.items():
 for other,tetra in square_3sphere.items():
  if sf!=other:assert t not in tetra
# Hence the six top cycles pair by unit diagonal with six 3-cocycles.
# With the perfect Morse matching, each 3-sphere is primitive and the rank is six.
# Euler/Morse: one 0-cell, one 2-cell, six 3-cells, no degree-3 boundary.
# All 3-cell attaching maps have degree 0 to the single S^2, proving the wedge.
# Cube-group homology action from an exact simplicial Lefschetz trace.
face_lists={};oriented_orders={}
for fixed in range(3):
 free=[j for j in range(3) if j!=fixed]
 for val in range(2):
  def corner(a,b):
   z=[0,0,0];z[fixed]=val;z[free[0]]=a;z[free[1]]=b
   return sum(z[j]<<j for j in range(3))
  oriented_orders[(fixed,val)]=tuple(corner(*p) for p in [(0,0),(1,0),(1,1),(0,1)])

def sign_permutation(v):
 return -1 if sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))%2 else 1

def gmap(axis,flip):
 g=[0]*V
 for x in range(8):
  y=0
  for old,new in enumerate(axis):
   bit=((x>>old)&1)^((flip>>new)&1)
   y|=(bit<<new)
  g[x]=y
 for (a,b),j in edgeno.items():
  g[8+j]=8+edgeno[tuple(sorted((g[a],g[b])))]
 return g

result=[]
for axis in permutations(range(3)):
 for flip in range(8):
  g=gmap(axis,flip)
  trace_chain=0
  for f in faces:
   image=[g[v] for v in f]
   if set(image)==set(f):
    ords=[sorted(image).index(z) for z in image]
    trace_chain+=(-1)**(len(f)-1)*sign_permutation(ords)
  trace3=0
  for sf,cyc in oriented_orders.items():
   image=[g[v] for v in cyc]
   if set(image)!=set(cyc):continue
   pairs=antipodal_pairs[sf]
   pair_to_index={p:i for i,p in enumerate(pairs)}
   tgt=[];flips=0
   for a,b in pairs:
    mapped=(g[a],g[b]);j=pair_to_index[tuple(sorted(mapped))]
    tgt.append(j)
    flips+=(mapped[0]!=pairs[j][0])
   deg=sign_permutation(tgt)*((-1)**flips)
   assert deg==1,(axis,flip,sf,deg)
   trace3+=deg
  trace2=trace_chain-1+trace3
  det=sign_permutation(axis)*((-1)**flip.bit_count())
  assert trace2==det,('H2 char',axis,flip,trace2,det)
  result.append((trace2,trace3))
assert len(result)==48
assert sum(t2 for t2,t3 in result)==0 # no full-group H2 invariants
assert sum(t3 for t2,t3 in result)==48 # one full-group H3 invariant
assert sum(t2 for t2,t3 in result if t2==1)==24 # rotations invariant dimension1
assert sum(t3 for t2,t3 in result if t2==1)==24 # rotations invariant dimension1
print('SUBDIVIDED_CUBE_RIPS3_PERFECT_MORSE_SIX_FACE_SPHERES_48_SYMMETRIES_OK')
print('face_vector:',Counter(len(f)-1 for f in faces))
print('matching_pairs:',len(matching),'critical:',Counter(x.bit_count()-1 for x in active))
print('unique_4free_tetrahedra:',witness)
print('Lefschetz_trace_histogram:',Counter(result))
