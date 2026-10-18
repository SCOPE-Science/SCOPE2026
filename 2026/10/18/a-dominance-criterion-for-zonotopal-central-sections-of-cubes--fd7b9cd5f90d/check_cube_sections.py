from fractions import Fraction as F
from itertools import product, combinations_with_replacement

def section_vertices(u,t):
 m=len(u);u=tuple(map(F,u));t=F(t);ans=set()
 for j in range(m):
  other=[k for k in range(m) if k!=j]
  for signs in product((-1,1),repeat=m-1):
   v=[None]*m
   for k,s in zip(other,signs):v[k]=F(s)
   v[j]=(t-sum(u[k]*v[k] for k in other))/u[j]
   if abs(v[j])<=1:ans.add(tuple(v))
 return ans

def centrally_symmetric(vertices):
 if not vertices:return False
 m=len(next(iter(vertices)));N=len(vertices)
 c=tuple(sum(v[j] for v in vertices)/N for j in range(m))
 return all(tuple(2*c[j]-v[j] for j in range(m)) in vertices for v in vertices)

nchecks=0
for coeff in combinations_with_replacement(range(1,9),4):
 a=sorted(coeff,reverse=True)
 if a[0]>=sum(a[1:]):continue
 verts=section_vertices(a[1:],a[0]);assert len(verts)>=3,(a,verts)
 assert not centrally_symmetric(verts),(a,verts)
 nchecks+=1
print('exact non-dominant 4-cube coefficient cases:',nchecks)
for a in [(1,1,1,1,1),(2,2,1,1,1),(2,2,2,1,1),(3,2,2,2,1),(4,3,3,3,2), (5,5,5,5,5)]:
 u=sorted(a,reverse=True)
 v=section_vertices(u[1:],u[0]);assert not centrally_symmetric(v)
 print('5-cube',a,'facet vertices',len(v),'non-central')
for a in [(3,1,1,1),(4,2,1,1),(7,5,1,1),(4,1,1,1,1),(6,2,2,1,1)]:
 u=sorted(a,reverse=True)
 assert u[0]>=sum(u[1:])
 print('dominant',a,'affine cube by graph')

# Independently test the off-center-section lemma, including equality boundaries.
offcenter_cases=0
for u in product(range(1,5), repeat=3):
 total=sum(u)
 for twice_t in range(1,2*total):
  t=F(twice_t,2)
  vertices=section_vertices(u,t)
  expected=any(u[k]>=t+sum(u[j] for j in range(3) if j!=k) for k in range(3))
  assert centrally_symmetric(vertices)==expected,(u,t,vertices)
  offcenter_cases+=1
print('exact off-center cube-section lemma cases:',offcenter_cases)
