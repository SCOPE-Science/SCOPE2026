#!/usr/bin/env python3
"""Exact arithmetic verification of the rhombic-triacontahedron illumination theorem.
All algebra is in Z[phi], phi^2=phi+1. No external dependencies.
"""
from itertools import combinations
from collections import Counter

Z=(0,0); ONE=(1,0); PHI=(0,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p,q=a; r,s=b
    return (p*r+q*s,p*s+q*r+q*s)
def scale(k,a):return (k*a[0],k*a[1])
def sgn(x):
    p,q=x; a=2*p+q; b=q
    if b==0:return (a>0)-(a<0)
    if a==0:return (b>0)-(b<0)
    if a*b>0:return (a>0)-(a<0)
    delta=a*a-5*b*b
    assert delta!=0
    z=a if delta>0 else b
    return (z>0)-(z<0)
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vsub(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def vscale(k,a):return tuple(mul(k,x) for x in a)
def dot(a,b):
    z=Z
    for x,y in zip(a,b): z=add(z,mul(x,y))
    return z
def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def ints(v):return tuple((x,0) for x in v)

V=[]
for t in (-1,1):
 for s in (-1,1): V.append((Z,scale(t,ONE),scale(s,PHI)))
for t in (-1,1):
 for s in (-1,1): V.append((scale(t,ONE),scale(s,PHI),Z))
for t in (-1,1):
 for s in (-1,1): V.append((scale(s,PHI),Z,scale(t,ONE)))
assert len(V)==12 and len(set(V))==12
E=[(i,j) for i,j in combinations(range(12),2) if dot(vsub(V[i],V[j]),vsub(V[i],V[j]))==(4,0)]
assert len(E)==30
F=[t for t in combinations(range(12),3) if all(tuple(sorted(e)) in E for e in combinations(t,2))]
assert len(F)==20
N=[vadd(V[i],V[j]) for i,j in E]
assert len(set(N))==30
EV=[tuple(q for q,e in enumerate(E) if i in e) for i in range(12)]
EF=[tuple(q for q,e in enumerate(E) if e[0] in t and e[1] in t) for t in F]
assert list(map(len,EV))==[5]*12 and list(map(len,EF))==[3]*20

# Exhaust all 3-subsets of the 30 rectified vertices, obtaining every
# possible supporting facet as a maximal coplanar set; the hull has no others.
facets=set(); noncollinear=0
for a,b,c in combinations(range(30),3):
 u=cross(vsub(N[b],N[a]),vsub(N[c],N[a]))
 if u==(Z,Z,Z):continue
 noncollinear+=1
 h=dot(u,N[a]); side=[sgn(sub(dot(u,p),h)) for p in N]
 if max(side)>0 and min(side)<0:continue
 face=frozenset(i for i,s in enumerate(side) if s==0)
 assert len(face)>=3
 facets.add(face)
assert len(facets)==32, len(facets)
assert facets==set(map(frozenset,EV+EF))
assert sorted(Counter(map(len,facets)).items())==[(3,20),(5,12)]

# Reflection in the hyperplane perpendicular to each normal must permute
# all twelve original icosahedral vertices. Avoid division: for each v,
# a candidate w satisfies (n.n)(v-w)=2(v.n)n.
for n in N:
 den=dot(n,n)
 images=[]
 for v in V:
  t=scale(2,dot(v,n))
  hits=[i for i,w in enumerate(V) if vscale(den,vsub(v,w))==vscale(t,n)]
  assert len(hits)==1, (n,v,hits)
  images.extend(hits)
 assert len(set(images))==12

# Since these reflecting hyperplanes are exactly those defined by N,
# every chamber of the central arrangement is reflection-equivalent.
def illuminated(u):
 signs=[sgn(dot(n,u)) for n in N]
 assert 0 not in signs, (u,signs)
 def illuminated_face(face):return all(signs[j]<0 for j in face)
 return [i for i,face in enumerate(EV+EF) if illuminated_face(face)]

ref=illuminated(ints((-2,-2,1)))
assert (len([i for i in ref if i<12]),len([i for i in ref if i>=12]))==(3,7)

D=[(-2,-2,1),(-1,2,-1),(1,1,2),(2,-2,-1)]
cover=[0]*32
for d in D:
 for i in illuminated(ints(d)):cover[i]+=1
assert cover[:12]==[1]*12 and min(cover[12:])>=1
assert Counter(cover[12:])==Counter({1:12,2:8})

# Optional no-proof sanity checks on another 150 independent sample directions.
for i in range(1,151):
 u=ints((i+2,3*i*i+7,8*i*i*i+2*i+1))
 if all(sgn(dot(n,u)) for n in N):
  found=illuminated(u)
  assert (sum(j<12 for j in found),sum(j>=12 for j in found))==(3,7)
print('EXACT_OK original_vertices=12 roots=30 hull_facets=32 pentagons=12 triangles=20')
print('EXACT_OK reflections=30x12 generic_incidence=(3,7) witnesses=4 min_vertex_coverage=1')
print('EXACT_OK ordinary_illumination=4 fractional_illumination=4')
