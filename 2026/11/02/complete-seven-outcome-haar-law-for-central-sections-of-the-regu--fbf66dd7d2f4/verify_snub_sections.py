"""Exact arithmetic in Q[t]/(t^3+t^2+t-1), with t in (0,1)."""
from itertools import combinations,permutations,product
from collections import defaultdict,Counter
from fractions import Fraction
import math,random
Z=(0,0,0); ONE=(1,0,0); T=(0,1,0); TI=(1,1,1)
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def neg(a):return tuple(-s for s in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 p=[0]*5
 for i in range(3):
  for j in range(3):p[i+j]+=a[i]*b[j]
 # t^4 = -1+2t, t^3=1-t-t^2
 p[0]-=p[4];p[1]+=2*p[4]
 p[0]+=p[3];p[1]-=p[3];p[2]-=p[3]
 return tuple(p[:3])
def sg(a):
 if a==Z:return 0
 # tight rational interval for t
 D=10**30;R=543689012692076361570855971801
 P=a[0]*D*D+a[1]*R*D+a[2]*R*R
 B=(abs(a[1])+2*abs(a[2]))*D
 if abs(P)<=B: raise ArithmeticError(('root interval too wide',a,P,B))
 return 1 if P>0 else -1
def vadd(a,b):return tuple(add(a[k],b[k]) for k in range(3))
def vneg(a):return tuple(neg(a[k]) for k in range(3))
def vsub(a,b):return vadd(a,vneg(b))
def vscale(a,b):return tuple(mul(a[k],b) for k in range(3))
def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
def evaluate(a):
 t=0.54368901269207636
 return sum(a[k]*t**k for k in range(3))
def floats(a):return [evaluate(x) for x in a]
DROOT=10**30; RROOT=543689012692076361570855971801
# t^3+t^2+t-1 is strictly increasing for t>0.
def cubic_num(r):return r**3+r*r*DROOT+r*DROOT**2-DROOT**3
assert cubic_num(RROOT)<0<cubic_num(RROOT+1)
assert sg((-1,3,0))==1
assert sg((0,1,0))==1
assert sg((1,-2,0))==-1
assert mul(T,TI)==ONE
V=[]
for perm in permutations(range(3)):
 parity=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
 for signs in product((-1,1),repeat=3):
  if sum(x>0 for x in signs)%2==parity:
   V.append(tuple(tuple(s*coeff for coeff in [ONE,T,TI][perm[k]]) for k,s in enumerate(signs)))
assert len(V)==24 and len(set(V))==24
print('VERTICES_EXACT',len(V),flush=True)
# Collect all supporting facets from all triples
F=set();trips=0
for i,j,k in combinations(range(24),3):
 n=cross(vsub(V[j],V[i]),vsub(V[k],V[i]))
 if n==(Z,Z,Z):continue
 ds=[sg(dot(n,vsub(v,V[i]))) for v in V]
 if -1 in ds and 1 in ds:continue
 fac=frozenset(m for m,s in enumerate(ds) if s==0)
 if len(fac)>=3:F.add(fac)
faclens=Counter(map(len,F));print('SUPPORTING_FACES_EXACT',faclens,len(F),flush=True)
assert faclens=={3:32,4:6},faclens
E=set()
for f,g in combinations(F,2):
 common=f&g
 if len(common)==2:E.add(tuple(sorted(common)))
assert len(E)==60,len(E)
print('EDGES_EXACT',len(E),flush=True)
# Check vertex figure: five edges per vertex, all same length
assert Counter(i for e in E for i in e)==Counter({i:5 for i in range(24)})
R2=dot(V[0],V[0]);assert all(dot(v,v)==R2 for v in V)
edgecos=dot(V[next(iter(E))[0]],V[next(iter(E))[1]])
assert all(dot(V[i],V[j])==edgecos for i,j in E)
print('COS_EDGE_NUM',edgecos,'RADIUS_SQUARE',R2,'cos',evaluate(edgecos)/evaluate(R2),flush=True)
# Exhaust all sign regions of the 24 great circles, using local sectors at pairwise intersections.
S=set(); sample_per_count={}
inter=0;local_incident=Counter()
for i,j in combinations(range(24),2):
 c=cross(V[i],V[j])
 if c==(Z,Z,Z):continue
 inter+=1
 d=[sg(dot(v,c)) for v in V]
 J=[k for k in range(24) if d[k]==0]
 local_incident[len(J)]+=1
 for ori in (1,-1):
  for k in J:
   w=cross(c,V[k])
   for side_ray in (1,-1):
    for side_shift in (1,-1):
     sign=[]
     for h in range(24):
      if d[h]: z=ori*d[h]
      else:
       base=sg(dot(V[h],w))
       if base: z=side_ray*base
       else: z=side_shift*sg(dot(V[h],V[k]))
      assert z in (-1,1)
      sign.append(z)
     p=tuple(sign)
     S.add(p)
counts=Counter()
for sign in S:
 n=sum(sign[i]!=sign[j] for i,j in E)
 counts[n]+=1
 sample_per_count.setdefault(n,sign)
print('PAIRWISE_CIRCLE_INTERSECTIONS',inter,flush=True)
print('INTERSECTION_MULTIPLICITIES',local_incident,flush=True)
print('ALL_CELL_SIGN_PATTERNS',len(S),'N_DISTRIBUTION_BY_CELLS',sorted(counts.items()),flush=True)
assert all(x in counts for x in range(min(counts),max(counts)+1))
print('MIN_MAX',min(counts),max(counts),flush=True)
# Verify sign patterns from independent Monte Carlo using numerical vertices+edges
vv=[floats(v) for v in V]; ee=sorted(E)
rs=random.Random(481516)
nnorm=150000
freq=Counter()
for _ in range(nnorm):
 norm=[rs.gauss(0,1) for _ in range(3)]
 pr=[sum(norm[j]*v[j] for j in range(3)) for v in vv]
 n=sum(pr[i]*pr[j]<0 for i,j in ee)
 freq[n]+=1
print('INDEPENDENT_GAUSSIAN_FREQUENCIES',dict(sorted(freq.items())),flush=True)
print('MEAN_EXACT_CROFTON',60*math.acos(evaluate(edgecos)/evaluate(R2))/math.pi,flush=True)
# Exact spherical-polygon Gauss-Bonnet area sums by local wedge angles
axis={}
for i,j in combinations(range(24),2):
 c=cross(V[i],V[j]);J=frozenset(k for k in range(24) if sg(dot(V[k],c))==0)
 if c!=(Z,Z,Z):axis.setdefault(J,(i,j,c))
print('DISTINCT_ARRANGEMENT_AXES',len(axis),'BY_MULTIPLICITY',Counter(map(len,axis)),flush=True)
assert Counter(map(len,axis))=={2:204,4:12}
area_terms=defaultdict(Counter);inc=Counter();sector_members=set()
for J,(i,j,c0) in axis.items():
 for orient in (-1,1):
  c= c0 if orient==1 else vneg(c0)
  d=[sg(dot(V[k],c)) for k in range(24)]
  basis1=floats(V[i]); cv=floats(c)
  basis2=[cv[1]*basis1[2]-cv[2]*basis1[1],cv[2]*basis1[0]-cv[0]*basis1[2],cv[0]*basis1[1]-cv[1]*basis1[0]]
  nr1=math.sqrt(sum(x*x for x in basis1))
  nr2=math.sqrt(sum(x*x for x in basis2))
  basis1=[x/nr1 for x in basis1]; basis2=[x/nr2 for x in basis2]
  rays=[]
  for k in sorted(J):
   for s in (-1,1):
    ray=vscale(cross(c,V[k]),(s,0,0))
    rr=floats(ray)
    phi=math.atan2(sum(a*b for a,b in zip(rr,basis2)),sum(a*b for a,b in zip(rr,basis1)))
    rays.append((phi,k,s,ray))
  rays.sort()
  for aidx in range(len(rays)):
   phi1,k1,s1,r1=rays[aidx]
   phi2,k2,s2,r2=rays[(aidx+1)%len(rays)]
   assert k1!=k2
   xangle=(phi2-phi1)%(2*math.pi)
   assert 0<xangle<math.pi-1e-6,(J,xangle)
   # Check adjacency and counterclockwise order exactly, independently of sorting.
   assert sg(dot(c,cross(r1,r2)))==1
   for phi3,k3,s3,r3 in rays:
    if r3==r1 or r3==r2: continue
    assert not (sg(dot(c,cross(r1,r3)))>0 and sg(dot(c,cross(r3,r2)))>0), (J,k1,k2,k3)
   w=vadd(r1,r2)
   p=tuple(d[k] if d[k] else sg(dot(V[k],w)) for k in range(24))
   assert all(t in (-1,1) for t in p)
   assert p in S
   nn=sum(p[k]!=p[h] for k,h in E)
   inc[nn]+=1
   # cosine wedge angle = s1*s2 * dot(V[k1],V[k2])/R2
   q=mul(dot(V[k1],V[k2]),(s1*s2,0,0))
   if sg(q)<0:
    q=neg(q); area_terms[nn]['pi']+=1; coeff=-1
   elif sg(q)>0:
    coeff=1
   else:
    area_terms[nn]['pi']+=Fraction(1,2);continue
   area_terms[nn][q]+=coeff
for nn in sorted(counts):
 area_terms[nn]['pi']-=inc[nn]-2*counts[nn]
print('TOTAL_SECTORS',sum(inc.values()),'SECTOR_COUNTS',sorted(inc.items()))
assert sum(inc.values())==1824
qs=sorted({q for r in area_terms.values() for q in r if isinstance(q,tuple)},key=lambda x:evaluate(x))
print('UNIQUE_POSITIVE_COSINES',len(qs),[(q,round(evaluate(q)/evaluate(R2),12)) for q in qs])
for nn in sorted(counts):
 print('AREA_EXACT',nn,'pi=',area_terms[nn]['pi'],'arccos(q/R2)=',[(str(q),coef) for q,coef in area_terms[nn].items() if isinstance(q,tuple) and coef],flush=True)
 ang=float(area_terms[nn]['pi'])*math.pi+sum(coef*math.acos(min(1,max(-1,evaluate(q)/evaluate(R2)))) for q,coef in area_terms[nn].items() if isinstance(q,tuple))
 print('PROB_FROM_EXACT_FORMULA',nn,ang/(4*math.pi),'MC',freq[nn]/nnorm,flush=True)
print('SUM_EXACT',sum(float(area_terms[n]['pi'])*math.pi+sum(coef*math.acos(min(1,max(-1,evaluate(q)/evaluate(R2)))) for q,coef in area_terms[n].items() if isinstance(q,tuple)) for n in counts)/(4*math.pi))

assert abs(sum(float(area_terms[n]['pi'])*math.pi+sum(coef*math.acos(min(1,max(-1,evaluate(q)/evaluate(R2)))) for q,coef in area_terms[n].items() if isinstance(q,tuple)) for n in counts)/(4*math.pi)-1)<1e-12
print('ALL_EXACT_CERTIFICATE_CHECKS_PASSED')

assert set(freq)==set(counts)
for n in counts:
 parea=(float(area_terms[n]['pi'])*math.pi+sum(coef*math.acos(min(1,max(-1,evaluate(q)/evaluate(R2)))) for q,coef in area_terms[n].items() if isinstance(q,tuple)))/(4*math.pi)
 assert abs(parea-freq[n]/nnorm)<0.01,(n,parea,freq[n]/nnorm)
print('INDEPENDENT_MONTE_CARLO_DIAGNOSTICS_PASSED')

# Certificate for the publicly stated exact table. Keys are (a,b,c) for acos((a+b*t+c*t*t)/D).
EXPECTED={
 12: {"pi":12,(1,2,2):-24,(2,2,3):-24},
 13: {"pi":0,(1,2,2):48,(0,0,1):-48,(2,2,3):48},
 14: {"pi":24,(1,2,2):-24,(3,2,0):48,(1,2,0):48,(1,0,0):-48,(3,0,0):-24,(2,0,1):-24,(2,2,1):-96,(0,0,1):48,(2,2,3):-24},
 15: {"pi":-144,(2,2,1):144,(1,0,0):96,(3,0,0):48,(2,0,1):96,(0,0,1):48},
 16: {"pi":72,(1,0,0):-24,(3,0,0):-24,(2,0,1):-120,(2,4,1):-24,(0,0,1):-48,(2,2,1):48},
 17: {"pi":0,(1,0,0):-48,(2,4,1):48,(2,0,1):48},
 18: {"pi":-8,(1,0,0):24,(2,4,1):-24}
}
for n in EXPECTED:
 assert dict(area_terms[n])==EXPECTED[n],(n,area_terms[n])
area_probability={n:(float(area_terms[n]['pi'])*math.pi+sum(coef*math.acos(evaluate(q)/evaluate(R2)) for q,coef in area_terms[n].items() if isinstance(q,tuple)))/(4*math.pi) for n in counts}
assert abs(sum(n*prob for n,prob in area_probability.items())-60*math.acos(evaluate(edgecos)/evaluate(R2))/math.pi)<1e-11
print('ALL_SEVEN_DECLARED_EXACT_AREA_FORMULAS_AND_CROFTON_MEAN_PASSED')
