#!/usr/bin/env python3
"""Exact integral lattice symmetry and polygon-face certificate for an explicit reflexive four-polytope."""
import itertools, math
from collections import Counter
VERTICES = tuple(tuple(map(int,part.split())) for part in (
    '1 0 0 0;0 1 0 0;1 -1 0 0;0 0 1 0;0 0 0 1;0 0 1 -1;'
    '0 0 -1 1;0 0 0 -1;0 0 -1 0;-1 1 0 0;0 -1 0 0;-1 1 -1 1;'
    '0 -1 0 -1;0 -1 -1 0;-1 1 -1 0;-1 0 0 -1;-1 0 -1 1;'
    '-1 -1 0 -1;-2 1 -1 1;-2 1 -1 0;-1 -1 -1 0;-2 0 -1 0'
).split(';'))

def mul(A,x):return tuple(sum(A[i][j]*x[j] for j in range(4)) for i in range(4))
def transpose(A):return tuple(zip(*A))
def subtract(x,y):return tuple(a-b for a,b in zip(x,y))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def det3(rows):
 a,b,c=rows
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def cross4(u,v,w):return tuple((-1)**j*det3([tuple(q[k] for k in range(4) if k!=j) for q in (u,v,w)]) for j in range(4))
def det4(A):return sum(A[0][j]*(-1)**j*det3([tuple(row[k] for k in range(4) if k!=j) for row in A[1:]]) for j in range(4))
def rank(points):
 # integer elimination preserving exactness by using fractions
 from fractions import Fraction
 rows=[[Fraction(y) for y in subtract(x,points[0])] for x in points[1:]]
 nr=len(rows);r=0
 for col in range(4):
  pivot=next((i for i in range(r,nr) if rows[i][col]!=0),None)
  if pivot is None:continue
  rows[r],rows[pivot]=rows[pivot],rows[r]
  fac=rows[r][col]
  rows[r]=[v/fac for v in rows[r]]
  for k in range(r+1,nr):
   t=rows[k][col]
   if t:rows[k]=[v-t*w for v,w in zip(rows[k],rows[r])]
  r+=1
  if r==4:break
 return r

def facets(vertices):
 out={}
 for quad in itertools.combinations(range(len(vertices)),4):
  a,b,c,d=[vertices[t] for t in quad]
  n=cross4(subtract(b,a),subtract(c,a),subtract(d,a))
  g=math.gcd(*n)
  if not g:continue
  n=tuple(x//g for x in n)
  scores=[dot(n,p) for p in vertices]
  c0=dot(n,a)
  if min(scores)==c0 and max(scores)>c0:pass
  elif max(scores)==c0 and min(scores)<c0:n=tuple(-x for x in n);c0=-c0
  else:continue
  assert c0==-1,(n,c0)
  fs=frozenset(i for i,p in enumerate(vertices) if dot(n,p)==-1)
  assert len(fs)>=4
  if fs in out:assert out[fs]==n
  out[fs]=n
 return out

def faces2(vertices,facets_map):
 out=set()
 for f,g in itertools.combinations(facets_map.keys(),2):
  inter=f&g
  if len(inter)>=3 and rank([vertices[i] for i in inter])==2:out.add(frozenset(inter))
 return out

def is_square_face(F,vertices):
 if len(F)!=4:return False
 a,b,c,d=sorted(F)
 return any(add(vertices[i],vertices[j])==add(vertices[k],vertices[l]) for (i,j),(k,l) in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))])

# Enumeration of GL(4,Z) stabilizer. Four standard basis vectors are among vertices,
# so every stabilizer is determined by their four ordered images. Pre-filter pairs
# using image conditions of known vertices e1-e2,-e1+e2,e3-e4,-e3+e4,-e3,-e4.
S=set(VERTICES)
AB=[(a,b) for a,b in itertools.product(VERTICES,repeat=2) if subtract(a,b) in S and subtract(b,a) in S]
CD=[(c,d) for c,d in itertools.product(VERTICES,repeat=2) if subtract(c,d) in S and subtract(d,c) in S and tuple(-z for z in c) in S and tuple(-z for z in d) in S]
assert len(AB)==52 and len(CD)==12
G=[]
for a,b in AB:
 for c,d in CD:
  A=tuple(zip(a,b,c,d))
  if abs(det4(A)) !=1:continue
  if {mul(A,x) for x in VERTICES}==S:G.append(A)
assert len(G)==2
T=next(x for x in G if x!=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
assert T==((1,1,0,0),(0,-1,0,0),(0,0,1,1),(0,0,0,-1))
assert all(mul(T,mul(T,x))==x for x in VERTICES)
F0=facets(VERTICES)
assert len(F0)==26
P=tuple(sorted(F0.values()))
assert len(set(P))==26
F1=facets(P)
assert len(F1)==22
F2_0=faces2(VERTICES,F0)
F2_1=faces2(P,F1)
assert len(F2_0)==72 and len(F2_1)==68
assert Counter(map(len,F2_0))=={3:50,4:21,6:1}
assert Counter(map(len,F2_1))=={3:38,4:26,5:2,6:2}
assert sum(is_square_face(f,VERTICES) for f in F2_0)==20
assert sum(is_square_face(f,P) for f in F2_1)==26

def face_orbits(vertices,faces,matrix):
 ix={x:i for i,x in enumerate(vertices)}
 assert {mul(matrix,x) for x in vertices}==set(vertices)
 perm={i:ix[mul(matrix,x)] for i,x in enumerate(vertices)}
 seen=set();out=[]
 for f in faces:
  if f in seen:continue
  f2=frozenset(perm[i] for i in f)
  assert f2 in faces
  if f2==f:out.append((f,))
  else:out.append((f,f2))
  seen.update((f,f2))
 return out

or0=face_orbits(VERTICES,F2_0,T)
or1=face_orbits(P,F2_1,transpose(T))
for name,vertices,orbits in [('primal',VERTICES,or0),('dual',P,or1)]:
 for k in [3,4,5,6]:
  relevant=[orb for orb in orbits if len(orb[0])==k]
  if not relevant:continue
  print(name,k,'orbits',Counter(map(len,relevant)))
  if k==4:
   print(name,'squares orbit lengths',Counter(len(o) for o in relevant if is_square_face(o[0],vertices)))
   print(name,'non-square quadrilaterals orbits',Counter(len(o) for o in relevant if not is_square_face(o[0],vertices)))
# Published two coloop square faces on the dual; check direct exchange under transpose(T).
Sminus={(-1,-1,0,-1),(-1,0,0,-1),(0,1,0,-1),(0,0,0,-1)}
Splus={(-1,-1,0,1),(0,-1,0,1),(0,0,0,1),(-1,0,0,1)}
assert Sminus in [{P[i] for i in f} for f in F2_1]
assert Splus in [{P[i] for i in f} for f in F2_1]
assert {mul(transpose(T),x) for x in Sminus}==Splus


# Equivariant node-dependency module. For a square face choose the
# lexicographically first pair of opposite vertices as the + diagonal.
SQ=tuple(sorted((f for f in F2_1 if is_square_face(f,P)), key=lambda f:tuple(sorted(f))))
assert len(SQ)==26

def rho(f):
 a,b,c,d=sorted(f)
 for (i,j),(k,l) in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]:
  if add(P[i],P[j])==add(P[k],P[l]):
   z=[0]*len(P)
   for t in (i,j):z[t]=1
   for t in (k,l):z[t]=-1
   return tuple(z)
 raise AssertionError('nonparallelogram')
B=tuple(rho(f) for f in SQ)

def rational_rank(columns):
 from fractions import Fraction
 basis={}
 for column in columns:
  vec=[Fraction(x) for x in column]
  for pivot in sorted(basis):
   q=vec[pivot]
   if q:vec=[u-q*v for u,v in zip(vec,basis[pivot])]
  p=next((i for i,x in enumerate(vec) if x),None)
  if p is not None:
   val=vec[p]
   basis[p]=[x/val for x in vec]
 return len(basis)
assert rational_rank(B)==18
coloops=[i for i in range(len(B)) if rational_rank(B[:i]+B[i+1:])==17]
assert len(coloops)==2
assert {frozenset(P[i] for i in SQ[j]) for j in coloops}=={frozenset(Sminus),frozenset(Splus)}
# A lattice involution permutes ambient basis vectors and maps each
# signed square-diagonal relation to another such relation up to sign.
polar_index={x:i for i,x in enumerate(P)}
polar_permutation={i:polar_index[mul(transpose(T),x)] for i,x in enumerate(P)}
node_index={f:i for i,f in enumerate(SQ)}
node_action={}
for i,f in enumerate(SQ):
 target=frozenset(polar_permutation[k] for k in f)
 j=node_index[target]
 permuted=tuple(B[i][polar_permutation[k]] for k in range(len(P))) # involution: inverse equals itself
 if permuted==B[j]:sgn=1
 elif permuted==tuple(-x for x in B[j]):sgn=-1
 else:raise AssertionError('incompatible diagonal action')
 node_action[i]=(j,sgn)
assert all(node_action[node_action[i][0]][0]==i and node_action[node_action[i][0]][1]*node_action[i][1]==1 for i in node_action)
for parity,expected in ((1,(14,9,5)),(-1,(12,9,3))):
 eig_columns=[]
 image_columns=[]
 for i,(j,sgn) in node_action.items():
  z=[0]*len(B)
  z[i]+=1
  z[j]+=parity*sgn
  eig_columns.append(tuple(z))
  image_columns.append(tuple(sum(z[k]*B[k][row] for k in range(len(B))) for row in range(len(P))))
 result=(rational_rank(eig_columns),rational_rank(image_columns),rational_rank(eig_columns)-rational_rank(image_columns))
 assert result==expected,(parity,result)
 print('node relation parity',parity,'source/image/kernel dimensions',result)
print('VERIFY_OK polytope_aut=C2 tested_images=624 primal_nodes=10_pairs mirror_nodes=12_pairs+2_fixed mirror_coloops=exchanged node_relations=5_plus+3_minus')
