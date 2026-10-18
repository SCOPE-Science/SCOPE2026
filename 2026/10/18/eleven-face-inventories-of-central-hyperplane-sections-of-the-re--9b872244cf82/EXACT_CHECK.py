#!/usr/bin/env python3
"""Exact central-hyperplane section inventory of the regular 600-cell.
All computations are in Z[phi] with phi^2=phi+1; no floating point operations.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
from functools import lru_cache

z=(0,0); one=(1,0); phi=(0,1); inverse_phi=(-1,1)
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c+b*d, a*d+b*c+b*d)
def sig(x):
 # sign (2*a+b)+b*sqrt(5), exact integer comparison
 a,b=x; u=2*a+b
 if b==0:return (u>0)-(u<0)
 if u==0:return (b>0)-(b<0)
 if (u>0)==(b>0):return (u>0)-(u<0)
 return ((u>0)-(u<0)) if u*u>5*b*b else ((b>0)-(b<0))
def dot(x,y):
 acc=z
 for a,b in zip(x,y):acc=add(acc,mul(a,b))
 return acc

def det(x):
 n=len(x);total=z
 for perm in permutations(range(n)):
  inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  t=one
  for j,k in enumerate(perm):t=mul(t,x[j][k])
  total=add(total,neg(t) if inversions%2 else t)
 return total

def adjugate(x):
 n=len(x)
 return [[ (lambda minor,i,j: neg(det(minor)) if (i+j)%2 else det(minor))
             ([[x[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j],i,j) for j in range(n)] for i in range(n)]

# Radius-two root system of H4, vertices of the 600-cell.
verts=[]
for i in range(4):
 for s in (-1,1):
  v=[z]*4; v[i]=(2*s,0);verts.append(tuple(v))
for s in product((-1,1),repeat=4):verts.append(tuple((t,0) for t in s))
template=[z,one,phi,inverse_phi]
for q in permutations(range(4)):
 if sum(q[i]>q[j] for i in range(4) for j in range(i+1,4))%2:continue
 base=[template[i] for i in q]
 ids=[i for i in range(4) if base[i]!=z]
 for ss in product((-1,1),repeat=3):
  v=base[:]
  for i,s in zip(ids,ss):
   if s<0:v[i]=neg(v[i])
  verts.append(tuple(v))
assert len(verts)==len(set(verts))==120
assert all(dot(v,v)==(4,0) for v in verts)

def edge_exists(i,j):return dot(verts[i],verts[j])==(0,2)
neighbors=[set() for _ in verts]
for i,j in combinations(range(120),2):
 if edge_exists(i,j):
  neighbors[i].add(j);neighbors[j].add(i)
edges=sorted((i,j) for i in range(120) for j in neighbors[i] if i<j)
assert len(edges)==720 and all(len(adj)==12 for adj in neighbors)
# 4-cliques are all tetrahedral facets: the root 600-cell has 600 tetrahedral facets.
triangles=[]
for i,j in edges:
 for k in neighbors[i]&neighbors[j]:
  if k>j:triangles.append((i,j,k))
assert len(triangles)==1200
facets=[]
for i,j,k in triangles:
 for l in neighbors[i]&neighbors[j]&neighbors[k]:
  if l>k:facets.append((i,j,k,l))
assert len(facets)==600

# Simple H4 root system: diagram 5--3--3, so a chamber is alpha_i.dot(u) >= 0.
alpha=[verts[i] for i in (0,76,5,41)]
G=[[dot(x,y) for y in alpha] for x in alpha]
assert G==[[(4,0), (0,-2),z,z],[(0,-2),(4,0),(-2,0),z],[z,(-2,0),(4,0),(-2,0)],[z,z,(-2,0),(4,0)]]
# The simple reflections preserve the complete vertex set, and the root orbit is transitive.
def reflect(v,a):
 d=dot(v,a)
 assert d[0]%2==d[1]%2==0
 c=(d[0]//2,d[1]//2)
 return tuple(sub(x,mul(c,y)) for x,y in zip(v,a))
for a in alpha:
 assert {reflect(v,a) for v in verts}==set(verts)
orbit={alpha[0]}; frontier=[alpha[0]]
while frontier:
 v=frontier.pop()
 for a in alpha:
  w=reflect(v,a)
  if w not in orbit:orbit.add(w);frontier.append(w)
assert len(orbit)==120
D=det(alpha); Ad=adjugate(alpha)
assert sig(D)!=0
for i in range(4):
 for j in range(4):
  t=dot(alpha[i],[Ad[k][j] for k in range(4)])
  assert t==(D if i==j else z), (i,j,t)

def section(mask):
 weights=[int(bool(mask&(1<<i))) for i in range(4)]
 normal=[z]*4
 for j,w in enumerate(weights):
  if w:
   for k in range(4):normal[k]=add(normal[k],Ad[k][j])
 if sig(D)<0:normal=list(map(neg,normal))
 s=[sig(dot(v,normal)) for v in verts]
 zero=[('v',i) for i in range(120) if s[i]==0]
 crosses=[('e',i,j) for i,j in edges if s[i]*s[j]<0]
 vset=set(zero+crosses)
 faces=set()
 for f in facets:
  hits={('v',i) for i in f if s[i]==0}
  for i,j in combinations(f,2):
   if s[i]*s[j]<0: hits.add(('e',min(i,j),max(i,j)))
  if len(hits)>=3:
   assert len(hits)<=4
   faces.add(frozenset(hits))
 section_edges=set()
 inc=Counter()
 # Every section edge lies in an original triangular ridge or is a side of one.
 for tri in triangles:
  hits={('v',i) for i in tri if s[i]==0}
  for i,j in combinations(tri,2):
   if s[i]*s[j]<0:hits.add(('e',i,j))
  if len(hits)==2:
   edge=frozenset(hits)
   section_edges.add(edge)
   inc[edge]=sum(edge<=fac for fac in faces)
  elif len(hits)==3:
   # whole triangular face lies on the plane; its three sides are section edges
   for a,b in combinations(hits,2):
    edge=frozenset((a,b))
    section_edges.add(edge)
    inc[edge]=sum(edge<=fac for fac in faces)
 if set(inc.values())!={2}:raise AssertionError(('edge incidence',mask,Counter(inc.values())))
 V,E,F=len(vset),len(section_edges),len(faces)
 assert V-E+F==2,(mask,V,E,F)
 polygon_count=Counter(len(f) for f in faces)
 assert sum(k*n for k,n in polygon_count.items())==2*E
 assert sum(polygon_count.values())==F
 return {'mask':format(mask,'04b'),'zeros':len(zero),'crossings':len(crosses),'f_vector':[V,E,F],'face_sizes':dict(sorted(polygon_count.items()))}

if __name__=='__main__':
 import json
 data=[section(m) for m in range(1,16)]
 for d in data:print(json.dumps(d,separators=(',',':')))
 distinct=sorted(set((tuple(d['f_vector']),tuple(d['face_sizes'].items())) for d in data))
 print('EXACT_H4_SECTION_OK roots=120 edges=720 triangles=1200 tetrahedra=600 strata=15 inventories='+str(len(distinct)))
 assert len(distinct)==11
