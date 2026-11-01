#!/usr/bin/env python3
"""Exact-arithmetic checks of equatorial edge belts in three convex solids.
Coordinates are integer pairs representing a+b*sqrt(5). Pure Python 3.
The general equivalence theorem is proved analytically, not by this program.
"""
from itertools import combinations, product
from collections import Counter, defaultdict

ZERO=(0,0);ONE=(1,0);PHI2=(1,1) # equals 2*golden_ratio

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,k):return (k*x[0],k*x[1])
def vecadd(x,y):return tuple(map(add,x,y))
def vecsub(x,y):return tuple(map(sub,x,y))
def dot(x,y):
 out=ZERO
 for a,b in zip(x,y):out=add(out,mul(a,b))
 return out
def cross(x,y):
 return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def sign(x):
 a,b=x
 if not b:return (a>0)-(a<0)
 if not a:return (b>0)-(b<0)
 if a*b>0:return (a>0)-(a<0)
 q=a*a-5*b*b
 assert q!=0 # since 5 is nonsquare and a,b integers
 return ((a>0)-(a<0)) if q>0 else ((b>0)-(b<0))
def is_zero(v):return all(x==ZERO for x in v)
def iv(v):return tuple((int(x),0) for x in v)

def check_belts(vertices,edges,expected_sizes):
 groups=[];rep=[]
 for i,j in edges:
  n=cross(vertices[i],vertices[j])
  assert not is_zero(n)
  for k,r in enumerate(rep):
   if is_zero(cross(n,r)):
    groups[k].append((i,j));break
  else:rep.append(n);groups.append([(i,j)])
 sizes=sorted(map(len,groups))
 assert sizes==sorted(expected_sizes),(sizes,expected_sizes)
 for group in groups:
  degrees=Counter(k for e in group for k in e)
  assert all(d==2 for d in degrees.values())
  assert len(degrees)==len(group)
  # A degree-2, connected graph is precisely a polygonal cycle.
  unseen=set(degrees); stack=[next(iter(unseen))];unseen.remove(stack[0])
  while stack:
   v=stack.pop()
   for i,j in group:
    if v==i and j in unseen:unseen.remove(j);stack.append(j)
    if v==j and i in unseen:unseen.remove(i);stack.append(i)
  assert not unseen
 return sizes

def icosahedron():
 v=[]
 for i in range(3):
  for a,b in product([-1,1],repeat=2):
   w=[ZERO,ZERO,ZERO]
   w[i]=(2*a,0);w[(i+1)%3]=scale(PHI2,b)
   v.append(tuple(w))
 # coordinate set uses cyclic forms (2,phi,0),(0,2,phi),(phi,0,2)
 assert len(set(v))==12
 faces=[]
 for c in combinations(range(12),3):
  i,j,k=c
  normal=cross(vecsub(v[j],v[i]),vecsub(v[k],v[i]))
  if is_zero(normal):continue
  sg={sign(dot(normal,vecsub(v[m],v[i]))) for m in range(12) if m not in c}
  if sg=={1} or sg=={-1}:faces.append(c)
 assert len(faces)==20,len(faces)
 es=sorted(set(tuple(sorted(x)) for f in faces for x in combinations(f,2)))
 assert len(es)==30
 return v,faces,es

def rectify(v,faces,es):
 w=[vecadd(v[i],v[j]) for i,j in es]
 lookup={e:i for i,e in enumerate(es)}
 ed=set()
 for f in faces:
  ids=[lookup[tuple(sorted(p))] for p in combinations(f,2)]
  ed.update(tuple(sorted(p)) for p in combinations(ids,2))
 return w,sorted(ed)

def test_cut(vertices,edges,u):
 ss=[sign(dot(p,u)) for p in vertices]
 assert all(s!=0 for s in ss)
 return sum(ss[i]!=ss[j] for i,j in edges)

def main():
 vi,fi,ei=icosahedron()
 w,ed=rectify(vi,fi,ei)
 assert len(w)==30 and len(ed)==60
 assert check_belts(w,ed,[10]*6)==[10]*6
 # octahedron and cuboctahedron: exact integer vertices
 vo=[iv(p) for j in range(3) for q in [-1,1] for p in [tuple(q if k==j else 0 for k in range(3))]]
 fo=[]
 for triple in combinations(range(6),3):
  t=[vo[i] for i in triple]
  if all(is_zero(vecadd(t[i],t[j])) is False for i,j in combinations(range(3),2)):
   fo.append(triple)
 assert len(fo)==8
 eo=sorted(set(tuple(sorted(z)) for f in fo for z in combinations(f,2)))
 assert len(eo)==12
 assert check_belts(vo,eo,[4,4,4])==[4,4,4]
 wc,ec=rectify(vo,fo,eo)
 assert len(wc)==12 and len(ec)==24
 assert check_belts(wc,ec,[6,6,6,6])==[6,6,6,6]
 for v,e,num in [(vo,eo,6),(wc,ec,8),(w,ed,12)]:
  tests=0
  for coords in product(range(-5,6),repeat=3):
   if coords==(0,0,0):continue
   u=iv(coords)
   if any(sign(dot(p,u))==0 for p in v):continue
   assert test_cut(v,e,u)==num
   tests+=1
  print('constant_sections',len(v),len(e),'sides',num,'normals',tests)
 # cube is equiprojective but its generic central sections have different sizes.
 vc=[iv(x) for x in product((-1,1),repeat=3)]
 pts=list(product((-1,1),repeat=3))
 ecube=[(i,j) for i in range(8) for j in range(i+1,8) if sum(x!=y for x,y in zip(pts[i],pts[j]))==1]
 assert len(ecube)==12
 assert test_cut(vc,ecube,iv((3,1,1)))==4
 assert test_cut(vc,ecube,iv((10,11,12)))==6
 print('cube_witness',4,6)
 print('VERIFICATION_OK')
if __name__=='__main__':main()
