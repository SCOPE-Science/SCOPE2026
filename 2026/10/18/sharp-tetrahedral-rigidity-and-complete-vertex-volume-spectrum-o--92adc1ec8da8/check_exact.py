#!/usr/bin/env python3
"""Exact finite verification of the rhombic-triacontahedron tetrahedron theorem.

Arithmetic takes place in Z[phi], phi^2=phi+1. All comparisons use
integer arithmetic; no floating-point, optimization library, or external
file is needed. Run: python3 check_exact.py
"""
from itertools import product, combinations
from collections import Counter
from functools import cmp_to_key
import json

ZERO=(0,0); ONE=(1,0); PHI=(0,1); INVPHI=(-1,1)

def add(x,y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[0], -x[1]
def sub(x,y): return add(x,neg(y))
def scale(z,k): return z[0]*k,z[1]*k
def mul(x,y):
 a,b=x; c,d=y
 return a*c+b*d, a*d+b*c+b*d

def sign(z):
 # 2*(a+b*phi) = (2a+b)+b*sqrt(5): exact comparison.
 a,b=z; p=2*a+b; q=b
 if p==0 and q==0: return 0
 if p>=0 and q>=0: return 1
 if p<=0 and q<=0: return -1
 if p>0 and q<0: return 1 if p*p>5*q*q else -1
 if p<0 and q>0: return 1 if 5*q*q>p*p else -1
 raise AssertionError((p,q))
def absolute(z): return z if sign(z)>=0 else neg(z)
def dot(v,w):
 t=ZERO
 for x,y in zip(v,w): t=add(t,mul(x,y))
 return t
def vadd(v,w): return tuple(add(x,y) for x,y in zip(v,w))
def vneg(v): return tuple(neg(x) for x in v)
def vsub(v,w): return vadd(v,vneg(w))
def vscale(v,s): return tuple(mul(x,s) for x in v)
def cross(v,w):
 return (sub(mul(v[1],w[2]),mul(v[2],w[1])),
         sub(mul(v[2],w[0]),mul(v[0],w[2])),
         sub(mul(v[0],w[1]),mul(v[1],w[0])))
def det(v,w,z): return dot(v,cross(w,z))
def cyc(v): return (v,(v[1],v[2],v[0]),(v[2],v[0],v[1]))

# Coordinate normalization: the outer icosahedron has edge length 2.
# The 20 inner vertices form its inscribed dual dodecahedron.
outer=set()
inner=set()
for s,t in product((-1,1),repeat=2):
 outer.update(cyc((ZERO,scale(ONE,s),scale(PHI,t))))
 inner.update(cyc((ZERO,scale(PHI,s),scale(INVPHI,t))))
for s,t,u in product((-1,1),repeat=3):
 inner.add((scale(ONE,s),scale(ONE,t),scale(ONE,u)))
assert len(outer)==12 and len(inner)==20 and not (outer&inner)
vertices=sorted(outer|inner)
assert len(vertices)==32

# Independent zonotope realization. The Minkowski sum of six symmetric
# segments has the same thirty rhombic facets as the convex hull above.
gens=((ZERO,ONE,PHI),(ZERO,neg(ONE),PHI),
      (ONE,PHI,ZERO),(neg(ONE),PHI,ZERO),
      (PHI,ZERO,ONE),(PHI,ZERO,neg(ONE)))
sgn_sums=set()
for signs in product((-1,1),repeat=6):
 x=(ZERO,ZERO,ZERO)
 for s,g in zip(signs,gens): x=vadd(x,tuple(scale(q,s) for q in g))
 sgn_sums.add(x)
assert len(sgn_sums)==64
stretch=scale(PHI,2) # 2 phi
scaled_vertices={vscale(v,stretch) for v in vertices}
assert scaled_vertices<=sgn_sums
normals=[]
for i,j in combinations(range(6),2):
 n=cross(gens[i],gens[j])
 assert n!=(ZERO,ZERO,ZERO)
 assert sum(dot(n,g)==ZERO for g in gens)==2
 normals.append(n)
assert len(normals)==15
for a,b in combinations(normals,2):
 assert cross(a,b)!=(ZERO,ZERO,ZERO) # distinct normal directions
supports=[]
for n in normals:
 h=ZERO
 for g in gens:h=add(h,absolute(dot(n,g)))
 supports.append(h)
 for x in sgn_sums: assert sign(sub(h,absolute(dot(n,x))))>=0
 # A supporting rhombus has exactly four vertices in each direction.
 assert sum(dot(n,x)==h for x in scaled_vertices)==4
 assert sum(dot(n,x)==neg(h) for x in scaled_vertices)==4

def active_normals(x):
 return [n for n,h in zip(normals,supports) if absolute(dot(n,x))==h]
def has_independent_triple(arr):
 return any(det(*t)!=ZERO for t in combinations(arr,3))
valences=Counter()
for x in sgn_sums:
 aa=active_normals(x)
 if x in scaled_vertices:
  assert has_independent_triple(aa)
  valences[len(aa)]+=1
 else: assert not has_independent_triple(aa)
assert valences=={3:20,5:12},valences
# All facets of a 3-zonotope have normals perpendicular to at least
# two generators. The fifteen displayed pairs hence exhaust facets.
# This certifies the exact 32-vertex and 30-rhombus realization.

# Exact zonotope volume (multilinearity of Minkowski volume for segments):
zvolume=ZERO
for i,j,k in combinations(range(6),3):
 zvolume=add(zvolume,absolute(det(gens[i],gens[j],gens[k])))
zvolume=scale(zvolume,8)
# P = Z/(2 phi); P has volume 20 by direct ring identity.
assert zvolume == mul((20,0),mul(stretch,mul(stretch,stretch)))

# Exhaustion of all unordered vertex quadruples. Volume = determinant/6.
frequency=Counter();max_det=ZERO;maximizers=[]
for idx in combinations(range(32),4):
 a,b,c,d=(vertices[i] for i in idx)
 v=absolute(det(vsub(b,a),vsub(c,a),vsub(d,a)))
 frequency[v]+=1
 if sign(sub(v,max_det))>0:
  max_det=v;maximizers=[idx]
 elif v==max_det:
  maximizers.append(idx)
assert sum(frequency.values())==35960
assert len(frequency)==39
assert frequency[ZERO]==2340
assert max_det==(6,8),max_det  # 6 + 8 phi = 10 + 4 sqrt(5)
assert len(maximizers)==20
assert frequency[max_det]==20

# Equality geometry: three outer vertices form an equilateral long
# triangle with squared side 4 phi^2; fourth is -phi times their sum.
long_squared=(4,4)
outer_triples=set()
for idx in maximizers:
 obj=[vertices[i] for i in idx]
 o=[v for v in obj if v in outer]
 d=[v for v in obj if v in inner]
 assert len(o)==3 and len(d)==1
 assert all(dot(vsub(a,b),vsub(a,b))==long_squared for a,b in combinations(o,2))
 assert d[0]==vneg(vscale(vadd(vadd(o[0],o[1]),o[2]),PHI))
 outer_triples.add(frozenset(o))
assert len(outer_triples)==20
# The twenty triangles, rather than the triangular faces of the
# icosahedron, use its larger edge-diagonal length 2 phi.
all_long={frozenset(t) for t in combinations(outer,3)
          if all(dot(vsub(a,b),vsub(a,b))==long_squared for a,b in combinations(t,2))}
assert all_long==outer_triples
# No two maximizing vertex quadruples agree in three vertices.
# The affine determinant is multi-affine in its four point arguments;
# any nonvertex maximizer would force two maximizers sharing three.
assert all(len(set(a)&set(b))<=2 for a,b in combinations(maximizers,2))

# Canonical data table: (6*volume) = a+b*phi, sorted exactly.
levels=sorted(frequency, key=cmp_to_key(lambda x,y: sign(sub(x,y))))
# Both sorting and its verification use exact integer comparisons.
assert all(sign(sub(y,x))>0 for x,y in zip(levels,levels[1:]))
data={
 'coordinate_normalization':'outer icosahedron edge=2',
 'vertex_count':32,'facets':30,'edges':60,
 'total_vertex_quadruples':35960,'affinely_dependent_quadruples':frequency[ZERO],
 'determinant_levels':len(levels),
 'largest_determinant_a_plus_b_phi':list(max_det),
 'maximizer_count':len(maximizers),
 'polytope_volume':20,
 'levels':[{'a':a,'b':b,'count':frequency[a,b]} for (a,b) in levels]
}
print(json.dumps(data,separators=(',',':')))
print('VERIFY_OK 32 vertices, 30 rhombic facets, 39 exact levels, 20 isolated maximizers')
