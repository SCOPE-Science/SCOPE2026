from itertools import combinations
from functools import lru_cache
from collections import defaultdict
from math import factorial,prod
N=8
triples=list(combinations(range(N),3))
triple_idx={t:i for i,t in enumerate(triples)}

def partitions(n, minpart=1, maxpart=None):
 if n==0:yield ();return
 if maxpart is None:maxpart=n
 for k in range(min(n,maxpart),minpart-1,-1):
  for p in partitions(n-k, 1,k):yield(k,)+p

def classify_cycle(typ):
 perm=list(range(N));offset=0
 for k in typ:
  for j in range(k):perm[offset+j]=offset+(j+1)%k
  offset+=k
 return tuple(perm)

def inv_ind_poly_minus_one(cyc):
 p=classify_cycle(cyc)
 action=tuple(triple_idx[tuple(sorted(p[v] for v in t))] for t in triples)
 seen=set();orbits=[]
 for s in range(len(triples)):
  if s in seen:continue
  orbit=[];cur=s
  while cur not in seen:
   seen.add(cur);orbit.append(cur);cur=action[cur]
  orbits.append(orbit)
 m=len(orbits)
 adj=[0]*m
 for i,oi in enumerate(orbits):
  if any(not set(triples[a]).intersection(triples[b]) for a,b in combinations(oi,2)):
   adj[i]=(1<<m)-1 # A chosen orbit itself contains a forbidden disjoint pair.
  for j,oj in enumerate(orbits[:i]):
   if any(not set(triples[a]).intersection(triples[b]) for a in oi for b in oj):adj[i]|=1<<j;adj[j]|=1<<i
 allow=(1<<m)-1
 for i in range(m):
  if adj[i]==(1<<m)-1: allow&=~(1<<i)
 # Independence polynomial at minus one: F(G)=F(G-v)-F(G-N[v]).
 @lru_cache(None)
 def f(mask):
  if mask==0:return 1
  b=mask&-mask;v=b.bit_length()-1
  return f(mask^b)-f(mask&~b&~adj[v])
 val=f(allow)
 return val,m,f.cache_info().currsize

@lru_cache(None)
def rimrem(lam, m):
 n=sum(lam)
 if m>n:return ()
 choices=[]
 for nu in partitions(n-m):
  if any((nu[i] if i<len(nu) else 0) > (lam[i] if i<len(lam) else 0) for i in range(max(len(nu),len(lam)))):continue
  cells={(i,j) for i,v in enumerate(lam) for j in range(v)} - {(i,j) for i,v in enumerate(nu) for j in range(v)}
  if len(cells)!=m:continue
  if any(all((i+di,j+dj) in cells for di,dj in [(0,0),(1,0),(0,1),(1,1)]) for i,j in cells):continue
  frontier={next(iter(cells))}; seen=set(frontier)
  while frontier:
   x,y=frontier.pop()
   for uv in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
    if uv in cells and uv not in seen:seen.add(uv);frontier.add(uv)
  if len(seen)!=len(cells):continue
  h=len({i for i,j in cells})-1
  choices.append((nu,(-1)**h))
 return tuple(choices)

@lru_cache(None)
def char(lam,cyc):
 if sum(lam)!=sum(cyc):return 0
 if not cyc:return int(not lam)
 return sum(s*char(nu,cyc[1:]) for nu,s in rimrem(lam,cyc[0]))


types=list(partitions(8))
L={}
for typ in types:
 val,m,num=inv_ind_poly_minus_one(typ)
 L[typ]=-val
 print('cycle', '-'.join(map(str,typ)), 'reduced_lefschetz', L[typ], 'orbit_count',m)
chi9={}
for typ in types:
 p=[0]*7;p[0]=1
 for k in typ:
  sign=(-1)**(k-1)
  for j in range(6,k-1,-1): p[j]+=sign*p[j-k]
 chi9[typ]=p[6]

from fractions import Fraction
classes={}
for cyc in types:
 groups=defaultdict(int)
 for k in cyc: groups[k]+=1
 classes[cyc]=prod(k**v*factorial(v) for k,v in groups.items())
def inner(v,lam):return sum((Fraction(v[cyc]*char(lam,cyc),classes[cyc]) for cyc in types))
for lam in types:
 for nu in types:
  assert sum(Fraction(char(lam,cyc)*char(nu,cyc),classes[cyc]) for cyc in types)==int(lam==nu)
chi6={typ:chi9[typ]+L[typ] for typ in types}
print('degree9_irreducibles',[(p,int(inner(chi9,p))) for p in types if inner(chi9,p)])
print('degree6_irreducibles',[(p,int(inner(chi6,p))) for p in types if inner(chi6,p)])
print('identity',chi6[(1,)*8],chi9[(1,)*8],flush=True)
assert chi6[(1,)*8]==233 and chi9[(1,)*8]==28
assert all(inner(chi6,p)>=0 and inner(chi6,p).denominator==1 for p in types)
expected6={(8,),(7,1),(5,3),(4,4),(4,3,1),(3,2,2,1),(2,2,2,2),(2,2,2,1,1),(1,1,1,1,1,1,1,1)}
expected9={(3,1,1,1,1,1),(2,1,1,1,1,1,1)}
assert {p for p in types if inner(chi6,p)}==expected6
assert {p for p in types if inner(chi9,p)}==expected9
assert all(inner(chi6,p)==1 for p in expected6)
assert all(inner(chi9,p)==1 for p in expected9)
print('VERIFY_OK: 22 S8 conjugacy classes; rank6=233; rank9=28; character orthogonality exact')

# The generator of the six-point cross-polytope transforms by the sign
# character: one ground-point transposition permutes the 10 antipodal
# axes by an odd permutation and flips an even number of their directions.
six=set(range(6))
pairs=[]
for A in combinations(range(6),3):
 B=tuple(sorted(six-set(A)))
 if A<B:pairs.append((A,B))
assert len(pairs)==10
transposition=(1,0,2,3,4,5)
axis=[]
flips=0
for A,B in pairs:
 mapped=tuple(sorted(transposition[v] for v in A))
 for j,(P,Q) in enumerate(pairs):
  if mapped in (P,Q):
   axis.append(j)
   flips+=int(mapped==Q)
   break
assert len(set(axis))==10
inversions=sum(axis[i]>axis[j] for i in range(10) for j in range(i+1,10))
assert (inversions,flips)==(15,6)
assert (-1)**(inversions+flips)==-1
print('ORIENTATION_OK: one transposition has 15 antipodal-pair inversions, 6 antipodal flips')
