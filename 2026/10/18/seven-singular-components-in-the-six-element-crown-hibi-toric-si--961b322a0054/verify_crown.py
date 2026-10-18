#!/usr/bin/env python3
"""Exact independent finite-poset normal-fan certificate (stdlib only)."""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import gcd

N=6
# Coordinates (a0,a1,a2,b0,b1,b2); inequalities c*x >= h.
I=[]
def add(c,h,name): I.append((tuple(c),h,name))
for i in range(3):
 c=[0]*N;c[i]=1;add(c,0,f'A{i}')
for j in range(3):
 c=[0]*N;c[3+j]=-1;add(c,-1,f'B{j}')
for i in range(3):
 for j in range(3):
  if i!=j:
   c=[0]*N;c[i]=-1;c[3+j]=1;add(c,0,f'C{i}{j}')
assert len(I)==12

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rank(mat):
 if not mat:return 0
 m=[[Fraction(y) for y in x] for x in mat]
 r=0;n=len(m[0]); k=len(m)
 for c in range(n):
  p=next((i for i in range(r,k) if m[i][c]),None)
  if p is None:continue
  m[r],m[p]=m[p],m[r]
  z=m[r][c];m[r]=[v/z for v in m[r]]
  for i in range(r+1,k):
   if m[i][c]:
    z=m[i][c];m[i]=[a-z*b for a,b in zip(m[i],m[r])]
  r+=1
  if r==k:break
 return r

def det(mat):
 n=len(mat)
 if n==0:return 1
 a=[list(map(int,row)) for row in mat];sign=1;prev=1
 for k in range(n-1):
  if a[k][k]==0:
   j=next((j for j in range(k+1,n) if a[j][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    assert num%prev==0
    a[i][j]=num//prev
  for i in range(k+1,n):a[i][k]=0
  prev=pivot
 return sign*a[n-1][n-1]

# Independent all-minor total-unimodularity certificate.
rows=[x[0] for x in I]
minors=0
for k in range(1,N+1):
 for rr in combinations(range(len(I)),k):
  for cc in combinations(range(N),k):
   z=det([[rows[i][j] for j in cc] for i in rr])
   assert z in (-1,0,1),(k,rr,cc,z)
   minors+=1
assert minors==18563,minors

# The displayed complete inequality system has all and only 0/1 vertices:
# 0<=a_i<=b_j<=1 follows from the six comparisons, each a_i has
# at least one upper b_j. Every vertex is integral by total unimodularity.
V=[p for p in product((0,1),repeat=N) if all(dot(c,p)>=h for c,h,_ in I)]
assert len(V)==18,len(V)
assert len(set(V))==18

# Enumerate each nonempty face by the intersection of a subset of facets;
# a face is represented by its set of vertices.
faces=set()
for mask in range(1<<len(I)):
 vset=frozenset(t for t,p in enumerate(V) if all(dot(I[j][0],p)==I[j][1] for j in range(len(I)) if mask>>j&1))
 if vset:faces.add(vset)
assert len(faces)==403,len(faces)
info={}
fvec=Counter();singular=Counter()
for F in faces:
 active=tuple(j for j,(c,h,_) in enumerate(I) if all(dot(c,V[t])==h for t in F))
 r=rank([rows[j] for j in active]);d=N-r
 nonsimple=len(active)>r
 info[F]=(d,active,nonsimple)
 fvec[d]+=1
 if nonsimple:singular[d]+=1
assert [fvec[i] for i in range(7)]==[18,73,129,116,54,12,1],fvec
assert [singular[i] for i in range(6)]==[17,43,30,6,0,0],singular
S=[f for f in faces if info[f][2]]
components=[f for f in S if not any(f<g for g in S)]
assert len(components)==7
assert Counter((info[f][0],len(info[f][1])) for f in components)==Counter({(3,4):6,(1,6):1})

# All six codimension-three cones are four-circuits (two plus, two minus).
# The fifth-codimension cone is the alternating six-circuit (three and three).
def circuit_signs(rays):
 for choices in product((-1,1),repeat=len(rays)):
  if choices[0]!=1:continue
  if all(sum(s*rows[j][k] for s,j in zip(choices,rays))==0 for k in range(N)):
   return (choices.count(1),choices.count(-1))
 raise AssertionError('no unit circuit')
for F in components:
 d,active,_=info[F]
 assert circuit_signs(active)==((2,2) if d==3 else (3,3))

# Identify each face's polar-inequality orbit closure geometry.
# The six 3-faces have 5 lattice vertices and are unimodular square pyramids.
for F in components:
 d,active,_=info[F]
 if d==3:assert len(F)==5
 else:assert len(F)==2

# Incidence among the six quadric-cone components, and their meeting the line.
three=[F for F in components if info[F][0]==3]
one=next(F for F in components if info[F][0]==1)
assert frozenset(V[i] for i in one)==frozenset({(0,)*6,(1,)*6})
pair=Counter()
for F,G in combinations(three,2):
 H=F&G
 pair['empty' if not H else ('line' if len(H)==2 else 'point')]+=1
assert pair==Counter({'line':6,'point':3,'empty':6}),pair
assert sum(len(F&one)==1 for F in three)==6
print('VERIFY_OK')
print('all total-unimodularity minors:',minors)
print('vertices/faces:',len(V),len(faces))
print('f_vector:',[fvec[i] for i in range(7)])
print('singular_orbits:',[singular[i] for i in range(6)])
print('minimal_singular_cones: 6 circuits (2,2), 1 circuit (3,3)')
print('component_intersections:',dict(pair))
