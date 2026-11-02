#!/usr/bin/env python3
"""Exact Q(sqrt(5)) sign-chamber certificate for truncated icosahedron central sections.
The enumerated sign chambers are exhaustive by iterative spherical halfspace clipping.
No floating-point arithmetic enters incidence, classification, or counting.
"""
from collections import Counter
from itertools import combinations,product
from math import gcd
from functools import reduce
import math

Z=(0,0); ONE=(1,0); TWO=(2,0); PHI2=(1,1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sn(x):
 a,b=x
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if (a>0)==(b>0):return (a>0)-(a<0)
 v=a*a-5*b*b
 return ((v>0)-(v<0))*((a>0)-(a<0))
def vadd(u,v):return tuple(add(x,y) for x,y in zip(u,v))
def vneg(u):return tuple(neg(x) for x in u)
def dot(u,v):return reduce(add, (mul(x,y) for x,y in zip(u,v)),Z)
def cross(u,v):return (sub(mul(u[1],v[2]),mul(u[2],v[1])),sub(mul(u[2],v[0]),mul(u[0],v[2])),sub(mul(u[0],v[1]),mul(u[1],v[0])))
def simpl(u):
 vals=[v for x in u for v in x];d=reduce(gcd,(abs(x) for x in vals),0)
 return tuple((x[0]//d,x[1]//d) for x in u) if d else u
def eqray(u,v):return cross(u,v)==(Z,Z,Z) and sn(dot(u,v))>0
def axis(i,sign=1):return tuple((sign,0) if j==i else Z for j in range(3))
def scale(u,s):return tuple(mul(x,s) for x in u)
def fnum(v):return tuple(a+b*math.sqrt(5) for a,b in v)
def xarea(poly):
 W=[fnum(x) for x in poly]
 W=[tuple(t/math.sqrt(sum(z*z for z in w)) for t in w) for w in W]
 def d(u,v):return sum(x*y for x,y in zip(u,v))
 def cr(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
 area=0.0
 for i in range(1,len(W)-1):
  u,v,w=W[0],W[i],W[i+1]
  area+=2*math.atan2(abs(d(u,cr(v,w))),1+d(u,v)+d(v,w)+d(w,u))
 return area
# Twice classical icosahedron vertex coordinates
I=[(Z,(a*2,0),(b,b)) for a,b in product((-1,1),repeat=2)]+[((a*2,0),(b,b),Z) for a,b in product((-1,1),repeat=2)]+[((a,a),Z,(b*2,0)) for a,b in product((-1,1),repeat=2)]
IE=[]
for i,j in combinations(range(12),2):
 z=vadd(I[i],vneg(I[j]))
 if dot(z,z)==(16,0):IE.append((i,j))  # doubled edge length 4
assert len(IE)==30,len(IE)
V=[vadd(scale(I[i],(2,0)),I[j]) for i,j in IE]+[vadd(scale(I[j],(2,0)),I[i]) for i,j in IE]
N=[]
for v in V:
 if not any(cross(v,w)==(Z,Z,Z) for w in N):N.append(v)
assert len(N)==30,len(N)
M=[axis(i) for i in range(3)]+N
# Initial octant spherical triangles, each has known ray coordinates
polys=[[axis(0,sx),axis(1,sy),axis(2,sz)] for sx,sy,sz in product((-1,1),repeat=3)]
# Cached all exact planes through the ray
zcache={}
def zeros(u):
 if u not in zcache:zcache[u]=frozenset(j for j,m in enumerate(M) if dot(u,m)==Z)
 return zcache[u]
def normalize_path(out):
 if not out:return []
 clean=[]
 for u in out:
  if not clean or not eqray(u,clean[-1]):clean.append(u)
 if len(clean)>1 and eqray(clean[0],clean[-1]):clean.pop()
 if len(clean)<3:return []
 # Collinear vertices can stay: no effect on nonzero area, no issue for sign checks.
 return clean

def clip(poly,j,sgn):
 m=M[j] if sgn==1 else vneg(M[j]);out=[]
 for i,u in enumerate(poly):
  v=poly[(i+1)%len(poly)];s=sn(dot(u,m));t=sn(dot(v,m))
  if s>=0:out.append(u)
  if s*t<0:
   candidates=zeros(u)&zeros(v)
   # Distinct great-circle vertices determine a unique edge-support plane.
   assert len(candidates)==1,(i,j,len(candidates),candidates)
   z=simpl(cross(M[next(iter(candidates))],M[j]))
   assert z!=(Z,Z,Z)
   if sn(dot(z,vadd(u,v)))<0:z=vneg(z)
   assert sn(dot(z,vadd(u,v)))>0
   assert dot(z,m)==Z
   out.append(z)
 return normalize_path(out)
for k in range(3,len(M)):
 new=[]
 for poly in polys:
  for s in (-1,1):
   pp=clip(poly,k,s)
   if pp:
    # If all rays collinear (degenerate), discard.
    if not all(cross(pp[0],v)==(Z,Z,Z) for v in pp[1:]):new.append(pp)
 polys=new
 print('clip',k-2,'cells',len(polys),flush=True)

# Edges: precisely the 90 shortest edges; avoid floating: raw W has lengths3 * normal solid edges
E=[]
for i,j in combinations(range(60),2):
 w=vadd(V[i],vneg(V[j]))
 if dot(w,w)==(16,0):E.append((i,j)) # length is (2/3) in undoubled coords; W length 4
assert len(E)==90,len(E)
# The 12 pentagon and 20 hexagon faces are those inherited by truncating an icosahedron.
F5=[]
for i in range(12):F5.append([k for k,(a,b) in enumerate(IE) if (a if k<30 else b)==i] + [k+30 for k,(a,b) in enumerate(IE) if b==i])
# correct F5 by indexing oriented W
F5=[[q for q in range(60) if (IE[q%30][0] if q<30 else IE[q%30][1])==i] for i in range(12)]
assert all(len(f)==5 for f in F5)
FI=[]
for a,b,c in combinations(range(12),3):
 if all(frozenset(z) in set(map(frozenset,IE)) for z in ((a,b),(b,c),(c,a))):FI.append((a,b,c))
assert len(FI)==20,len(FI)
idx={frozenset(x):i for i,x in enumerate(IE)}
F6=[[val for x,y in combinations(t,2) for q in [idx[frozenset((x,y))]] for val in (q,q+30)] for t in FI]
assert all(len(f)==6 for f in F6)
D=Counter();area=Counter();eighteen=[]
for poly in polys:
 u=reduce(vadd,poly,(Z,Z,Z))
 signs=[sn(dot(u,v)) for v in V]
 assert all(signs), 'interior landed exactly on a vertex-circle boundary'
 a5=sum(any(signs[j]!=signs[f[0]] for j in f[1:]) for f in F5)
 a6=sum(any(signs[j]!=signs[f[0]] for j in f[1:]) for f in F6)
 assert a5+a6==sum(signs[i]!=signs[j] for i,j in E)
 D[(a5,a6)]+=1
 area[(a5,a6)]+=xarea(poly)
 if a5+a6==18:eighteen.append(poly)
print('EXACT COUNT',len(polys),'distribution',sorted(D.items()))
print('NUMERICAL AREAS',sorted((k,area[k]/(4*math.pi)) for k in area))
print('18 count',len(eighteen),'area',sum(xarea(p) for p in eighteen),'expected',4*math.pi*.030024640796753762)
# Exhaustively certify that the 18-gon cells are precisely the 20 vertex-circle
# chambers containing the 20 original icosahedron face-center directions.
base={}
for t in FI:
 q=reduce(vadd,(I[i] for i in t),(Z,Z,Z))
 signseq=tuple(sn(dot(q,n)) for n in N)
 assert all(signseq)
 assert signseq not in base, 'distinct ico faces have distinct sign vectors'
 base[signseq]=t
from collections import Counter
belongs=Counter()
for poly in eighteen:
 u=reduce(vadd,poly,(Z,Z,Z)); signseq=tuple(sn(dot(u,n)) for n in N)
 assert signseq in base, '18-cell not contained in the listed 20 spherical chambers'
 belongs[base[signseq]]+=1
print('20 face-normal chamber certificates: number',len(base), 'refined cells per chamber',Counter(belongs.values()))
# Find the chamber corresponding to original I face with normal proportional (1,1,1)
c=(ONE,ONE,ONE)
key=tuple(sn(dot(c,n)) for n in N)
print('body diagonal face',base.get(key))
central=[p for p in eighteen if tuple(sn(dot(reduce(vadd,p,(Z,Z,Z)),n)) for n in N)==key]
print('body diagonal chamber pieces',len(central),'polygon count',list(map(len,central)), 'areas',list(map(xarea,central)))
# Boundary planes for this spherical hexagon, edge support intersection zero sets.
poly=central[0]; assert len(poly)==6
active=[]
for i,u in enumerate(poly):
 v=poly[(i+1)%len(poly)]
 j=next(iter((zeros(u)&zeros(v)) - {0,1,2}))
 active.append(j)
print('active GLOBAL',active)
vals=[]
for i,j in enumerate(active):
 k=active[(i+1)%6]
 a=M[j] if sn(dot(c,M[j]))>0 else vneg(M[j])
 b=M[k] if sn(dot(c,M[k]))>0 else vneg(M[k])
 numer=dot(a,b);den=dot(a,a)
 assert den==dot(b,b)
 vals.append((numer,den))
print('alternate exact normal-angle cos components',vals)
# Exact inequalities: the 6 candidate halfspaces really delimit the entire
# sphere cell containing (1,1,1); no remaining plane cuts it.
cert_verts=[]
for i,j in enumerate(active):
 k=active[(i+1)%6]
 u=simpl(cross(M[j],M[k]))
 if sn(dot(u,c))<0:u=vneg(u)
 cert_verts.append(u)
for u in cert_verts:
 for j,m in enumerate(N):
  orient=sn(dot(c,m))
  val=sn(dot(u,m))*orient
  assert val>=0,(j,u)
  if j+3 not in active:assert val>0,(j,u)
for i,j in enumerate(active):
 p,q=cert_verts[i-1],cert_verts[i]
 assert dot(p,M[j])==Z and dot(q,M[j])==Z
# Exact common normal dot products alternate between two algebraic constants.
for i,(nu,de) in enumerate(vals):
 target=(88,-1) if i%2==0 else (25,-4)
 assert mul(nu,(109,0))==mul(de,target)
print('PASS: all 6-vertex inequalities and exact angle values verified')
