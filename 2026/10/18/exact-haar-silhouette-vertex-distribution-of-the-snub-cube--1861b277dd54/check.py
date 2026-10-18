#!/usr/bin/env python3
"""Exact combinatorial spherical-arrangement certificate for the snub cube.
Only standard Python; all topology, incidence and sidedness use exact
integer arithmetic in Q[t]/(t^3-t^2-t-1), with isolated positive root t.
Floating-point is used solely to evaluate explicit arccosine expressions.
"""
import math, itertools, json, functools, collections, random

# The isolated Tribonacci root lies strictly between these rationals.
DEN=10**14
LOW=183928675521416
HIGH=LOW+1
assert LOW**3-LOW**2*DEN-LOW*DEN**2-DEN**3<0
assert HIGH**3-HIGH**2*DEN-HIGH*DEN**2-DEN**3>0

Z=(0,0,0); ONE=(1,0,0); T=(0,1,0); TI=(-1,-1,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def neg(a):return (-a[0],-a[1],-a[2])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 p,q,r=a;s,t,u=b
 c0=p*s;c1=p*t+q*s;c2=p*u+q*t+r*s;c3=q*u+r*t;c4=r*u
 return(c0+c3+c4,c1+c3+2*c4,c2+c3+2*c4)
def sign(a):
 if a==Z:return 0
 x,y,z=a
 lo=x*DEN*DEN + y*(LOW if y>=0 else HIGH)*DEN + z*(LOW*LOW if z>=0 else HIGH*HIGH)
 hi=x*DEN*DEN + y*(HIGH if y>=0 else LOW)*DEN + z*(HIGH*HIGH if z>=0 else LOW*LOW)
 if lo>0:return 1
 if hi<0:return -1
 raise AssertionError('algebraic sign not resolved: '+str(a))
def vsum(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vneg(a):return tuple(neg(x) for x in a)
def vsub(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def dot(a,b):
 z=Z
 for x,y in zip(a,b):z=add(z,mul(x,y))
 return z
def cross(a,b):
 return(sub(mul(a[1],b[2]),mul(a[2],b[1])),
        sub(mul(a[2],b[0]),mul(a[0],b[2])),
        sub(mul(a[0],b[1]),mul(a[1],b[0])))
def parallel(a,b):return cross(a,b)==(Z,Z,Z)
def det(a,b,c):return dot(a,cross(b,c))
def real(a):
 t=1.83928675521416113255
 return a[0]+t*(a[1]+t*a[2])
def vreal(a):return tuple(real(x) for x in a)
def invnumer(a):
 p,q,r=a
 m00,m01,m02=p,r,q+r
 m10,m11,m12=q,p+r,q+2*r
 m20,m21,m22=r,q+r,p+q+2*r
 c0=m11*m22-m12*m21;c1=m12*m20-m10*m22;c2=m10*m21-m11*m20
 d=m00*c0+m01*c1+m02*c2
 assert d!=0
 return (c0,c1,c2),d

def projkey(v):
 # Exact canonical oriented algebraic ray as a tuple of rational coefficients.
 from fractions import Fraction
 k=next(i for i,x in enumerate(v) if x!=Z)
 n,d=invnumer(v[k]);sgn=sign(v[k])
 return(k,sgn,tuple(tuple(__import__('fractions').Fraction(y,d) for y in mul(x,n)) for x in v))

def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
BASE=(ONE,TI,T)
V=[]
for perm in itertools.permutations(range(3)):
 for s in itertools.product((-1,1),repeat=3):
  if parity(perm)==sum(x>0 for x in s)%2:
   V.append(tuple(BASE[perm[j]] if s[j]>0 else neg(BASE[perm[j]]) for j in range(3)))
assert len(V)==24
# Strict supporting-face candidates; certified from scratch below.
FACES=[[0,9,21],[0,10,12],[0,12,16],[0,16,21],[1,8,20],[1,11,13],[1,13,17],[1,17,20],[2,8,14],[2,11,23],[2,14,18],[2,18,23],[3,9,15],[3,10,22],[3,15,19],[3,19,22],[4,8,14],[4,8,20],[4,12,16],[4,16,20],[5,9,15],[5,9,21],[5,13,17],[5,17,21],[6,10,12],[6,10,22],[6,14,18],[6,18,22],[7,11,13],[7,11,23],[7,15,19],[7,19,23],[0,3,9,10],[1,2,8,11],[4,6,12,14],[5,7,13,15],[16,17,20,21],[18,19,22,23]]
assert len(FACES)==38 and sorted(map(len,FACES))==[3]*32+[4]*6
FN=[]
for face in FACES:
 v0=V[face[0]];n=cross(vsub(V[face[1]],v0),vsub(V[face[2]],v0))
 assert n!=(Z,Z,Z)
 vals=[sign(dot(n,vsub(V[k],v0))) for k in range(24)]
 assert len({vals[k] for k in range(24) if k not in face})==1
 if next(vals[k] for k in range(24) if k not in face)>0:
  n=vneg(n);vals=[-x for x in vals]
 assert all(vals[k]==0 for k in face) and all(vals[k]==-1 for k in range(24) if k not in face)
 FN.append(n)
EDGES=[];inc=collections.defaultdict(int)
for i,j in itertools.combinations(range(38),2):
 common=sorted(set(FACES[i])&set(FACES[j]))
 assert len(common)<=2
 if len(common)==2:
  EDGES.append((i,j,tuple(common)));inc[tuple(common)]+=1
assert len(EDGES)==60 and len(inc)==60
assert collections.Counter(len([f for f in FACES if i in f]) for i in range(24))=={5:24}
assert all(sum(set(e).issubset(f) for f in FACES)==2 for e in inc)
# Every vertex link is a connected degree-two cycle of its five incident faces.
for v in range(24):
 fs=[i for i,f in enumerate(FACES) if v in f]
 links=[(a,b) for a,b,_ in EDGES if a in fs and b in fs and v in _]
 assert len(links)==5 and all(sum(k in p for p in links)==2 for k in fs)
 seen={fs[0]};front=[fs[0]]
 while front:
  x=front.pop()
  for a,b in links:
   if x in (a,b):
    y=b if a==x else a
    if y not in seen:seen.add(y);front.append(y)
 assert len(seen)==5
print('EXACT_SNUB_CONVEX_HULL_FACETS_EDGES_VERTICES_OK',len(FN),len(EDGES),len(V))
# Great circles in the normal sphere: identify coincident planes EXACTLY.
G=[]
for n in FN:
 if not any(parallel(n,g) for g in G):G.append(n)
assert len(G)==31
# Ray intersections: exact projective rational function hash.
nodes={};circles_v=collections.defaultdict(set)
for i,j in itertools.combinations(range(len(G)),2):
 w=cross(G[i],G[j]);assert w!=(Z,Z,Z)
 for r in (w,vneg(w)):
  key=projkey(r)
  if key not in nodes:nodes[key]=len(nodes)
  idx=nodes[key]
  circles_v[i].add(idx);circles_v[j].add(idx)
A=[None]*len(nodes)
for k,idx in nodes.items():
 # Reconstruct representative from first two circle planes, after insertion below.
 pass
# Build representatives directly, redoing the intersections (no floating geometry).
B={}
for i,j in itertools.combinations(range(len(G)),2):
 w=cross(G[i],G[j])
 for r in (w,vneg(w)):
  key=projkey(r);B[key]=r
for key,idx in nodes.items():A[idx]=B[key]
assert len(A)==762
# Verify all incidences, including triple and higher great-circle concurrencies.
for i,g in enumerate(G):
 true={j for j,v in enumerate(A) if dot(g,v)==Z}
 assert true==circles_v[i]
print('EXACT_GREAT_CIRCLE_INTERSECTIONS_OK',len(G),len(A))

# Exact projective angular comparator for a great circle, with initial ray ref.
def order_on_circle(i):
 g=G[i];pts=list(circles_v[i]);r=A[pts[0]]
 def sector(q):
  v=A[q];orient=sign(det(g,r,v))
  if orient>0:return 1
  if orient<0:return 3
  return 0 if sign(dot(r,v))>0 else 2
 def cmp(a,b):
  sa,sb=sector(a),sector(b)
  if sa!=sb:return -1 if sa<sb else 1
  if a==b:return 0
  orient=sign(det(g,A[a],A[b]));assert orient!=0
  return -1 if orient>0 else 1
 return sorted(pts,key=functools.cmp_to_key(cmp))
C={};C_EDGES=collections.defaultdict(list)
arc_count=0
for i,g in enumerate(G):
 ids=order_on_circle(i)
 assert len(ids)>=4
 for a,b in zip(ids,ids[1:]+ids[:1]):
  arc_count+=1
  m=vsum(A[a],A[b]); assert m!=(Z,Z,Z)
  signs=[sign(dot(h,m)) for h in G]
  assert signs[i]==0 and all(signs[j]!=0 for j in range(len(G)) if j!=i)
  for side in (-1,1):
   key=tuple(side if j==i else signs[j] for j in range(len(G)))
   C.setdefault(key,set()).update((a,b))
   C_EDGES[key].append((a,b,i))
assert len(C)==2+arc_count-len(A)==848
assert len(C_EDGES)==len(C)
print('EXACT_CELL_EULER_CHAMBER_COUNT_OK',len(C),arc_count)

COUNT=collections.Counter();NUMERIC_AREA=collections.defaultdict(float)
FORMULA=collections.defaultdict(lambda:collections.Counter())
# Store simple algebraic arccos type: integer constant times pi, plus arccos(positive algebraic cosine)
def theta_type(i,j):
 # unordered positive cosine determined by exact algebraic square.
 d=dot(G[i],G[j]);sg=sign(d)
 if i==j:return ('same',0),1
 if sg==0:return ('right',0),1
 # Use 3-vector product ratio as exact field element with rational polynomial coefficients.
 den=mul(dot(G[i],G[i]),dot(G[j],G[j]));num=mul(d,d)
 n,dd=invnumer(den)
 from fractions import Fraction
 rat=tuple(__import__('fractions').Fraction(x,dd) for x in mul(num,n))
 return rat,sg

ANGLE_REPS={};AREA_ARC=[]
for bit,indices in C.items():
 arcs=C_EDGES[bit]
 adj=collections.defaultdict(list)
 for a,b,i in arcs:
  adj[a].append((b,i));adj[b].append((a,i))
 assert len(adj)==len(indices) and all(len(adj[v])==2 for v in indices)
 first=min(indices);cur=first;prev=None;ordered=[];sides=[]
 while True:
  ordered.append(cur)
  nbs=adj[cur]
  nex,lbl=next(((x,k) for x,k in nbs if x!=prev), (None,None))
  assert nex is not None
  sides.append(lbl);prev,cur=cur,nex
  if cur==first:break
  assert len(ordered)<len(indices)+1
 assert len(ordered)==len(indices)
 center=(Z,Z,Z)
 for q in ordered:center=vsum(center,A[q])
 assert all(sign(dot(g,center))==sgn for g,sgn in zip(G,bit))
 # Polygon area exact as a finite integer linear combination of arccosines.
 n=sum(sign(dot(center,FN[i]))*sign(dot(center,FN[j]))<0 for i,j,_ in EDGES)
 COUNT[n]+=1
 val=2*math.pi
 FORMULA[n]['pi']+=2
 for k in range(len(ordered)):
  i,j=sides[k-1],sides[k]
  angle_type,dotsign=theta_type(i,j)
  if angle_type[0]=='same':continue
  if angle_type[0]=='right':
   FORMULA[n]['pi_half']-=1
   val-=math.pi/2
   continue
  positive=(dotsign*bit[i]*bit[j]>0)
  if angle_type not in ANGLE_REPS:ANGLE_REPS[angle_type]=(i,j)
  cosine=abs(real(dot(G[i],G[j])))/math.sqrt(real(dot(G[i],G[i]))*real(dot(G[j],G[j])))
  beta=math.acos(max(-1,min(1,cosine)))
  if positive:
   FORMULA[n][angle_type]-=1
   val-=beta
  else:
   FORMULA[n]['pi']-=1
   FORMULA[n][angle_type]+=1
   val-=math.pi-beta
 assert 0<val<math.pi
 NUMERIC_AREA[n]+=val
 assert all(dot(G[i],A[ordered[k]])==Z and dot(G[i],A[ordered[(k+1)%len(ordered)]])==Z for k,i in enumerate(sides))
assert dict(COUNT)=={9:96,10:288,11:336,12:128},COUNT
assert abs(sum(NUMERIC_AREA.values())-4*math.pi)<1e-9
print('EXACT_SILHOUETTE_CHAMBER_COUNTS_OK',dict(sorted(COUNT.items())))
print('GAUSS_BONNET_AREAS_AND_PROBABILITIES_OK', {k:round(NUMERIC_AREA[k]/(4*math.pi),15) for k in sorted(COUNT)})
print('ANGLE_TYPES',len(ANGLE_REPS))
# The finite explicit arccos formula is indexed by exact rational polynomials in t,
# not by floating approximations.
def stype(q):return ','.join(str(p) for p in q)
for k in sorted(COUNT):
 dic=FORMULA[k]
 print('EXACT_AREA_FORMULA',k,'pi',dic['pi'],'half_pi',dic['pi_half'],'arccos_terms',sum(1 for p,v in dic.items() if isinstance(p,tuple) and v))
# Audit the shipped finite closed-form coefficients against the exact sphere enumeration.
from fractions import Fraction
from pathlib import Path
TABLE=json.loads(Path(__file__).with_name('ANGLE_FORMULA.json').read_text(encoding='utf-8'))
types=sorted(ANGLE_REPS)
assert len(types)==18
types=[tuple(Fraction(s) for s in row) for row in TABLE['angles_cosine_squared_coefficients']]
assert set(types)==set(ANGLE_REPS)
for count in (9,10,11,12):
 row=TABLE['probability_area_numerators'][str(count)]
 coeff=FORMULA[count]
 assert Fraction(row['pi_coefficient'])==coeff['pi']+Fraction(coeff['pi_half'],2)
 assert row['angle_coefficients']==[coeff[x] for x in types]
 assert TABLE['chamber_counts'][str(count)]==COUNT[count]
 assert abs(NUMERIC_AREA[count]/(4*math.pi)-float(TABLE['area_probability_approx'][str(count)]))<2e-12
print('EXACT_PACKAGED_18_ANGLE_FORMULA_CONSISTENCY_OK')
# independently assess random directions by projected convex-hull monotone chain
rng=random.Random(137)
tval=1.839286755214161
VN=[tuple(float(x[0]+x[1]*tval+x[2]*tval*tval) for x in v) for v in V]
def projected_vertices(u):
 un=math.sqrt(sum(x*x for x in u));u=tuple(x/un for x in u)
 a=(-u[1],u[0],0.)
 if math.hypot(*a[:2])<1e-4:a=(0.,-u[2],u[1])
 mag=math.sqrt(sum(x*x for x in a));a=tuple(x/mag for x in a)
 b=(u[1]*a[2]-u[2]*a[1],u[2]*a[0]-u[0]*a[2],u[0]*a[1]-u[1]*a[0])
 pts=sorted((sum(a[j]*v[j] for j in range(3)),sum(b[j]*v[j] for j in range(3))) for v in VN)
 def cross2(o,p,q):return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
 lower=[];upper=[]
 for p in pts:
  while len(lower)>=2 and cross2(lower[-2],lower[-1],p)<=1e-9:lower.pop()
  lower.append(p)
 for p in reversed(pts):
  while len(upper)>=2 and cross2(upper[-2],upper[-1],p)<=1e-9:upper.pop()
  upper.append(p)
 return len(lower)+len(upper)-2
for _ in range(3000):
 u=tuple(rng.gauss(0,1) for _ in range(3))
 exact=sum(sign(dot(FN[i],tuple((round(1e8*x),0,0) for x in u)))*sign(dot(FN[j],tuple((round(1e8*x),0,0) for x in u)))<0 for i,j,_ in EDGES)
 # Exact sign in rounded rational viewing direction excludes random tolerances.
 assert exact==projected_vertices(u),(exact,projected_vertices(u))
print('INDEPENDENT_3000_PROJECTED_HULLS_OK')
print('ALL_SNUB_CUBE_EXACT_CHAMBER_CERTIFICATES_OK')
