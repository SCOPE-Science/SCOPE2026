#!/usr/bin/env python3
"""Exact finite verification of Bidiakis matching-complex theorem.

Python standard library only. No files, network, or state external to this source.
The interpretation of exact computations is established in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd
from functools import reduce

N=12
S=(-6,4,-4)
EDGES=tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
                   {tuple(sorted((i,(i+S[i%3])%N))) for i in range(N)}))
assert len(EDGES)==18
ADJ=[set() for _ in range(N)]
for x,y in EDGES:ADJ[x].add(y);ADJ[y].add(x)
assert all(len(a)==3 for a in ADJ)

# Form the entire face poset of the ordinary matching complex.
F=defaultdict(list)
for k in range(1,7):
 for ix in combinations(range(18),k):
  ends=[v for j in ix for v in EDGES[j]]
  if len(set(ends))==len(ends):
   F[k-1].append(sum(1<<j for j in ix))
assert tuple(map(len,(F[i] for i in range(6))))==(18,117,336,418,184,12)
ALL=set(sum((F[i] for i in range(6)),[]))
assert len(ALL)==1085

# A complete acyclic discrete-Morse matching, generated deterministically.
REM=set(ALL);PAIRS=[]
for vertex in reversed(range(18)):
 for lower in sorted(ALL):
  upper=lower|(1<<vertex)
  if not lower>>vertex&1 and lower in REM and upper in REM:
   REM.remove(lower);REM.remove(upper);PAIRS.append((lower,upper))
CRIT=Counter(c.bit_count()-1 for c in REM)
assert CRIT=={0:1,3:10},CRIT
assert len(PAIRS)==537
PM=set(PAIRS)
OUT=defaultdict(list);INDEG=defaultdict(int)
for upper in ALL:
 for j in range(18):
  if not upper>>j&1:continue
  lower=upper^(1<<j)
  if lower not in ALL:continue
  source,target=((lower,upper) if (lower,upper) in PM else (upper,lower))
  OUT[source].append(target);INDEG[target]+=1
q=deque(x for x in ALL if INDEG[x]==0)
visited=0
while q:
 x=q.popleft();visited+=1
 for y in OUT[x]:
  INDEG[y]-=1
  if INDEG[y]==0:q.append(y)
assert visited==len(ALL),('Morse matching has cycle',visited)

# Determine the integral Morse coordinates of 3-cycles by cancelling matched 4/3 pairs.
PAIR43={lo:hi for lo,hi in PAIRS if lo.bit_count()==4}
assert len(PAIR43)==172

def boundary(mask):
 vs=[j for j in range(18) if mask>>j&1]
 return {mask^(1<<j):(-1)**p for p,j in enumerate(vs)}
BDRY={lo:boundary(hi) for lo,hi in PAIR43.items()}
SUCC={lo:(set(BDRY[lo])&set(PAIR43))-{lo} for lo in PAIR43}
IN43=Counter(x for vs in SUCC.values() for x in vs)
Q=[x for x in sorted(PAIR43) if IN43[x]==0];TOP=[]
while Q:
 x=Q.pop();TOP.append(x)
 for y in SUCC[x]:
  IN43[y]-=1
  if IN43[y]==0:Q.append(y)
assert len(TOP)==172
CRIT3=tuple(sorted(m for m in REM if m.bit_count()==4))
UPPER3=tuple(sorted(hi for lo,hi in PAIRS if hi.bit_count()==4))
assert len(UPPER3)==236
# The boundary restricted to the 236 upper paired three-faces is injective:
# a full mod-two column rank certificate, independent of the Morse theorem.
ROW2={m:i for i,m in enumerate(F[2])}
BASIS2={}
for hi in UPPER3:
 col=0
 for face in boundary(hi):col ^= 1<<ROW2[face]
 while col:
  k=col.bit_length()-1
  if k not in BASIS2:
   BASIS2[k]=col;break
  col ^= BASIS2[k]
assert len(BASIS2)==236

def morse_coords(z):
 z=dict(z)
 for lo in TOP:
  coeff=z.get(lo,0)
  if not coeff:continue
  factor=coeff*BDRY[lo][lo]
  for m,a in BDRY[lo].items():
   value=z.get(m,0)-factor*a
   if value:z[m]=value
   else:z.pop(m,None)
 assert all(m not in z for m in PAIR43)
 # Other surviving 3-cells are paired as uppers with 2-cells. For cycles,
 # their coefficients are uniquely determined by the ten critical ones.
 return tuple(z.get(m,0) for m in CRIT3)

# Four vertex-disjoint length-two paths are precisely the eight-vertex
# induced octahedral 3-spheres of this flag matching complex.
PATHS=[]
for center in range(N):
 for a,b in combinations(sorted(ADJ[center]),2):
  pair=tuple(sorted((EDGES.index(tuple(sorted((a,center)))),
                     EDGES.index(tuple(sorted((b,center)))))))
  PATHS.append((frozenset((a,center,b)),pair))
assert len(PATHS)==36
CARRIERS=[]
for path_ids in combinations(range(36),4):
 if len(set().union(*(PATHS[i][0] for i in path_ids)))==12:
  CARRIERS.append(tuple(sorted(PATHS[i][1] for i in path_ids)))
assert len(CARRIERS)==len(set(CARRIERS))==39

def octahedron_cycle(pairs):
 z={}
 for bits in product(range(2),repeat=4):
  indices=[pairs[i][bits[i]] for i in range(4)]
  inversions=sum(a>b for i,a in enumerate(indices) for b in indices[i+1:])
  z[sum(1<<j for j in indices)]=(-1)**(sum(bits)+inversions)
 bd={}
 for m,c in z.items():
  for face,s in boundary(m).items():bd[face]=bd.get(face,0)+c*s
 assert all(not v for v in bd.values())
 return z

COORDS=tuple(morse_coords(octahedron_cycle(p)) for p in CARRIERS)
assert all(any(c) for c in COORDS)
assert all(reduce(gcd,c,0)==1 for c in COORDS)

# Fraction-free exact determinant, no floating-point arithmetic.
def det(M):
 a=[list(map(int,row)) for row in M]
 n=len(a)
 assert all(len(r)==n for r in a)
 prev=1;sgn=1
 if n==1:return a[0][0]
 for k in range(n-1):
  if a[k][k]==0:
   r=next((i for i in range(k+1,n) if a[i][k]),None)
   if r is None:return 0
   a[k],a[r]=a[r],a[k];sgn=-sgn
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    assert num%prev==0
    a[i][j]=num//prev
  for i in range(k+1,n):a[i][k]=0
  prev=pivot
 return sgn*a[n-1][n-1]

BASIS=(0,6,10,14,19,22,23,25,28,30)
assert det([[COORDS[j][i] for j in BASIS] for i in range(10)])==-1

# Enumerate every automorphism via constrained backtracking (no libraries).
def graph_automorphisms():
 mapping={};used=set();answers=[]
 def rec():
  if len(mapping)==N:
   answers.append(tuple(mapping[i] for i in range(N)));return
  # Most mapped neighbors first; reduces the state space.
  x=min((i for i in range(N) if i not in mapping),key=lambda v:(-len(ADJ[v]&mapping.keys()),v))
  for y in range(N):
   if y in used:continue
   if all((w in ADJ[x])==(mapping[w] in ADJ[y]) for w in mapping):
    mapping[x]=y;used.add(y);rec();used.remove(y);del mapping[x]
 rec()
 return answers
AUTOS=graph_automorphisms()
assert len(AUTOS)==8
idx={p:i for i,p in enumerate(CARRIERS)}
def image(p,g):
 return tuple(sorted(tuple(sorted(
  EDGES.index(tuple(sorted((g[EDGES[j][0]],g[EDGES[j][1]])))) for j in pair
 )) for pair in p))
ORBS=[];seen=set()
for i,p in enumerate(CARRIERS):
 if i in seen:continue
 orbit=tuple(sorted({idx[image(p,g)] for g in AUTOS}))
 ORBS.append(orbit);seen.update(orbit)
assert len(seen)==39
assert tuple(map(len,ORBS))==(4,8,8,8,4,1,2,2,2)

# Exact rational rank and integral saturation index of each orbit lattice.
def rank(A):
 M=[[Fraction(x) for x in row] for row in A]
 rows=len(M);cols=len(M[0]);r=0
 for c in range(cols):
  piv=next((i for i in range(r,rows) if M[i][c]),None)
  if piv is None:continue
  M[r],M[piv]=M[piv],M[r]
  v=M[r][c];M[r]=[x/v for x in M[r]]
  for i in range(r+1,rows):
   f=M[i][c]
   if f:M[i]=[a-f*b for a,b in zip(M[i],M[r])]
  r+=1
  if r==rows:break
 return r

def saturation_index(orbit,k):
 # gcd of all maximal minors. Equals index in rational saturation.
 cols=len(orbit);g=0
 for rows in combinations(range(10),k):
  for cc in combinations(range(cols),k):
   v=abs(det([[COORDS[orbit[c]][r] for c in cc] for r in rows]))
   g=gcd(g,v)
   if g==1:return 1
 return g
RANKS=[];INDICES=[]
for orbit in ORBS:
 k=rank([[COORDS[j][i] for j in orbit] for i in range(10)])
 RANKS.append(k);INDICES.append(saturation_index(orbit,k))
assert tuple(RANKS)==(4,8,8,5,3,1,2,2,2),RANKS
assert tuple(INDICES)==(1,3,1,1,1,1,1,1,1),INDICES
print('VERIFY_OK_BIDIAKIS_MATCHING_SHORTEST_SPHERES')
print('FACE_VECTOR',tuple(len(F[d]) for d in range(6)),'MORSE_PAIRS',len(PAIRS),'CRITICAL',dict(CRIT),'MORSE_DAG',visited)
print('UPPER_THREE_BOUNDARY_MOD_TWO_FULL_RANK',len(BASIS2))
print('INDUCED_OCTAHEDRAL_CARRIERS',len(CARRIERS),'ALL_NONZERO_PRIMITIVE','UNIT_BASIS_DET',-1)
print('GRAPH_AUTOMORPHISMS',len(AUTOS),'ORBITS',tuple(map(len,ORBS)))
print('ORBIT_RANKS',tuple(RANKS),'SATURATION_INDICES',tuple(INDICES))
print('HOMOTOPY_WEDGE_TEN_THREE_SPHERES_AND_INTEGRAL_CARRIER_GENERATION_VERIFIED')
