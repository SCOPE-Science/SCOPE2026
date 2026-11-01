#!/usr/bin/env python3
"""Exact integral chain and symmetry verification for two particles on a truncated tetrahedral graph.

Requires Python 3 and SymPy. Computes all cells, boundaries, Smith invariants,
explicit geometric top cycles, and full tetrahedral character data.
"""
from itertools import combinations, permutations
from collections import Counter
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# A vertex is a directed edge (i,j) of K4, the truncation of corner i
# in direction j. Each source-i triple is a triangular face.
V = list((i,j) for i in range(4) for j in range(4) if i != j)
vi = {v:k for k,v in enumerate(V)}
E = sorted(set(tuple(sorted((vi[(i,j)], vi[(i,k)])))
               for i in range(4) for j,k in combinations([x for x in range(4) if x != i], 2))
           | set(tuple(sorted((vi[(i,j)],vi[(j,i)]))) for i,j in combinations(range(4),2)))
ei={e:k for k,e in enumerate(E)}
assert (len(V),len(E)) == (12,18)

# Unordered open-cell pairs, ordered canonical product orientations.
C0=list(combinations(range(12),2)); c0i={a:k for k,a in enumerate(C0)}
C1=[(e,v) for e,(a,b) in enumerate(E) for v in range(12) if v not in (a,b)]
c1i={x:k for k,x in enumerate(C1)}
C2=[(e,f) for e,f in combinations(range(18),2) if not set(E[e])&set(E[f])]
c2i={x:k for k,x in enumerate(C2)}
assert (len(C0),len(C1),len(C2)) == (66,180,117)

# Signed cellular chain boundary ∂(e×f)=∂e×f-e×∂f.
D1=zeros(len(C0),len(C1));D2=zeros(len(C1),len(C2))
for k,(e,v) in enumerate(C1):
 a,b=E[e]
 D1[c0i[tuple(sorted((b,v)))],k]+=1
 D1[c0i[tuple(sorted((a,v)))],k]-=1
for k,(e,f) in enumerate(C2):
 a,b=E[e];c,d=E[f]
 for row,s in ((c1i[(f,b)],1),(c1i[(f,a)],-1),
               (c1i[(e,d)],-1),(c1i[(e,c)],1)):
  D2[row,k]+=s
assert D1*D2 == zeros(len(C0),len(C2))

# Four triangles and four hexagons, all oriented cyclically.
TF=[tuple(vi[(i,j)] for j in range(4) if j != i) for i in range(4)]
HF=[]
for excluded in range(4):
 a,b,c=[j for j in range(4) if j != excluded]
 HF.append(tuple(vi[x] for x in ((a,b),(b,a),(b,c),(c,b),(c,a),(a,c))))
F=TF+HF
assert sorted(len(x) for x in F)==[3]*4+[6]*4
P=[(i,j) for i,j in combinations(range(8),2) if not set(F[i])&set(F[j])]
assert len(P)==10 and len([p for p in P if p[0]<4 and p[1]<4])==6

def oriented_face_edges(face):
 out={}
 for a,b in zip(face,face[1:]+face[:1]):
  e=ei[tuple(sorted((a,b)))];out[e]=1 if a<b else -1
 assert len(out)==len(face)
 return out
FE=[oriented_face_edges(f) for f in F]

# Each disjoint-face pair defines a genuine embedded product torus.
Z=[]
for a,b in P:
 z={}
 for e,se in FE[a].items():
  for f,sf in FE[b].items():
   k=c2i[tuple(sorted((e,f)))];z[k]=se*sf*(1 if e<f else -1)
 Z.append(z)
 assert all(sum(D2[r,k]*v for k,v in z.items())==0 for r in range(len(C1)))
T=zeros(len(C2),len(P))
for j,z in enumerate(Z):
 for k,v in z.items():T[k,j]=v
sT=smith_normal_form(T,domain=ZZ)
assert [abs(int(sT[j,j])) for j in range(10)] == [1]*10

# Lower rank bound from exact mod-2 elimination; top-cycle kernel
# supplies the matching rational upper bound, without field extrapolation.
def mod2rank(matrix):
 piv={};rank=0
 for j in range(matrix.cols):
  v=sum(1<<i for i in range(matrix.rows) if int(matrix[i,j])&1)
  while v:
   i=v.bit_length()-1
   if i not in piv:
    piv[i]=v;rank+=1;break
   v ^= piv[i]
 return rank
r2=mod2rank(D2)
assert r2==107 and 117-10==107

# A spanning tree of the configuration 1-skeleton gives integral
# coordinates for its rank-115 cycle lattice.
parent=list(range(66));size=[1]*66
def root(x):
 while parent[x]!=x:
  parent[x]=parent[parent[x]];x=parent[x]
 return x
def union(a,b):
 a=root(a);b=root(b)
 if a==b:return False
 if size[a]<size[b]:a,b=b,a
 parent[b]=a;size[a]+=size[b]
 return True
nontree=[]
for j,(e,v) in enumerate(C1):
 a,b=E[e]
 x=c0i[tuple(sorted((a,v)))];y=c0i[tuple(sorted((b,v)))]
 if not union(x,y):nontree.append(j)
assert len({root(i) for i in range(66)})==1 and len(nontree)==115
R=D2[nontree,:]
sR=smith_normal_form(R,domain=ZZ)
assert [abs(int(sR[i,i])) for i in range(107)]==[1]*107
assert all(sR[i,i]==0 for i in range(107,min(sR.rows,sR.cols)))
# Thus H0=Z, H1=Z^8, H2=Z^10, with no higher homology.

# Automorphisms are exactly S4 on the four triangular faces.
# The four triangles are all graph triangles and a vertex in triangle i
# is uniquely determined by the other triangle j containing its sole
# external neighbor, so any automorphism is a simultaneous permutation
# of the two coordinates.
Fset={frozenset(f):k for k,f in enumerate(F)}
Pset={p:k for k,p in enumerate(P)}

def cyclesign(mapped,ref):
 for k in range(len(ref)):
  if mapped==ref[k:]+ref[:k]:return 1
  if mapped==tuple(reversed(ref[k:]+ref[:k])):return -1
 raise AssertionError('face orientation map invalid')

def ctype(p):
 seen=set();sizes=[]
 for i in range(4):
  if i not in seen:
   x=i;k=0
   while x not in seen:seen.add(x);k+=1;x=p[x]
   sizes.append(k)
 return tuple(sorted(sizes,reverse=True))

char={};counts=Counter()
for p in permutations(range(4)):
 vmap=[vi[(p[i],p[j])] for i,j in V]
 emap=[]
 for a,b in E:
  aa,bb=vmap[a],vmap[b]
  emap.append((ei[tuple(sorted((aa,bb)))], 1 if aa<bb else -1))
 c0map=[c0i[tuple(sorted((vmap[a],vmap[b])))] for a,b in C0]
 c1map=[(c1i[(emap[e][0],vmap[v])],emap[e][1]) for e,v in C1]
 c2map=[]
 for e,f in C2:
  ee,se=emap[e];ff,sf=emap[f]
  c2map.append((c2i[tuple(sorted((ee,ff)))],se*sf*(1 if ee<ff else -1)))
 # All signed face tori map to ±the corresponding face torus.
 fmap=[]
 for face in F:
  mapped=tuple(vmap[v] for v in face)
  j=Fset[frozenset(mapped)]
  fmap.append((j,cyclesign(mapped,F[j])))
 ht=0
 for k,(a,b) in enumerate(P):
  aa,sa=fmap[a];bb,sb=fmap[b]
  target=tuple(sorted((aa,bb)))
  sg=sa*sb*(1 if aa<bb else -1)
  assert target in Pset
  actual={}
  for c,val in Z[k].items():
   d,ss=c2map[c];actual[d]=actual.get(d,0)+val*ss
  expected={c:sg*val for c,val in Z[Pset[target]].items()}
  assert actual==expected
  if target==(a,b):ht+=sg
 # Check chain compatibility on all 1- and 2-cell basis vectors.
 for k,(j,s) in enumerate(c1map):
  left={c0map[r]:int(D1[r,k]) for r in range(len(C0)) if D1[r,k]}
  right={r:s*int(D1[r,j]) for r in range(len(C0)) if D1[r,j]}
  assert left==right
 for k,(j,s) in enumerate(c2map):
  left={}
  for r in range(len(C1)):
   if D2[r,k]:
    rr,ss=c1map[r];left[rr]=left.get(rr,0)+ss*int(D2[r,k])
  right={r:s*int(D2[r,j]) for r in range(len(C1)) if D2[r,j]}
  assert left==right
 tr0=sum(k==j for k,j in enumerate(c0map))
 tr1=sum(s for k,(j,s) in enumerate(c1map) if k==j)
 tr2=sum(s for k,(j,s) in enumerate(c2map) if k==j)
 h1=1+ht-(tr0-tr1+tr2)
 ty=ctype(p);counts[ty]+=1
 if ty in char:assert char[ty]==(h1,ht)
 else:char[ty]=(h1,ht)

ordered=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
assert [counts[t] for t in ordered]==[1,6,3,8,6]
assert [char[t][0] for t in ordered]==[8,-4,0,2,0]
assert [char[t][1] for t in ordered]==[10,2,-2,1,0]
# Rational irreducibles of S4: trivial, sign, two-dimensional,
# standard three-dimensional, sign-twisted standard.
irreps={
 'trivial':[1,1,1,1,1],
 'sign':[1,-1,1,1,-1],
 'two_dimensional':[2,0,2,-1,0],
 'standard':[3,1,-1,0,-1],
 'twisted_standard':[3,-1,-1,0,1]
}
mult={}
for degree in (0,1):
 mult[degree]={}
 for name,row in irreps.items():
  numerator=sum(counts[t]*char[t][degree]*c for t,c in zip(ordered,row))
  assert numerator%24==0 and numerator>=0
  mult[degree][name]=numerator//24
assert mult[0]=={'trivial':0,'sign':2,'two_dimensional':0,'standard':0,'twisted_standard':2}
assert mult[1]=={'trivial':1,'sign':0,'two_dimensional':0,'standard':2,'twisted_standard':1}
# Finite-group quotient rational homology equals invariant homology.
full=[sum(counts[t]*char[t][j] for t in ordered)//24 for j in (0,1)]
even=[sum(counts[t]*char[t][j] for t in ((1,1,1,1),(2,2),(3,1)))//12 for j in (0,1)]
assert full==[0,1] and even==[2,1]
print('VERIFY_OK cells=66,180,117 boundaries=(65,107) top_face_tori=10 HZ=(1,8,10) Aut=S4')
print('Smith_H1_nonzero=1x107 Smith_top_tori=1x10')
print('classes=',[(t,counts[t],char[t]) for t in ordered])
print('H1=',mult[0])
print('H2=',mult[1])
print('rational_invariant_dims_full=',full,'orientation_preserving=',even)
