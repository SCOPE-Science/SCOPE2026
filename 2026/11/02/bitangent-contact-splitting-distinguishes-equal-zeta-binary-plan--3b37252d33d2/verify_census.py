"""Exact self-contained census of smooth binary plane quartics.

Mask bit index for the monomial X**a*Y**b*Z**c uses the nested order
(a,b)=(0,0),(0,1),...,(0,4),(1,0),...,(4,0), c=4-a-b.
A line is encoded by a nonzero normal vector over GF(2).
Requires Python 3 and SymPy; writes a deterministic 78-row CSV next to this script.
"""
import itertools, collections, sympy as s, time, csv
from pathlib import Path
from functools import lru_cache
start=time.monotonic()
monoms=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
assert len(monoms)==15
idx={a:i for i,a in enumerate(monoms)}
# polynomials as sets of exponent tuples in F2
@lru_cache(None)
def times(p,q):
 d=set()
 for a in p:
  for b in q:
   e=tuple(x+y for x,y in zip(a,b))
   if e in d:d.remove(e)
   else:d.add(e)
 return frozenset(d)
one=frozenset([(0,0,0)])
def powpoly(f,n):
 z=one
 for _ in range(n):z=times(z,f)
 return z
# linear forms (columns given in substitution)
xf=frozenset([(1,0,0)]); yf=frozenset([(0,1,0)]); zf=frozenset([(0,0,1)])
tr=[(yf,xf,zf),(frozenset(xf^yf),yf,zf),(yf,zf,xf)] # swap, shear, cycle
# These three elementary coordinate transformations generate GL_3(F_2).
matrices=[((0,1,0),(1,0,0),(0,0,1)),
          ((1,1,0),(0,1,0),(0,0,1)),
          ((0,1,0),(0,0,1),(1,0,0))]
def matrix_product(a,b):
 return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
identity=((1,0,0),(0,1,0),(0,0,1))
group={identity};queue=[identity]
for h in queue:
 for gen in matrices:
  new=matrix_product(h,gen)
  if new not in group:
   group.add(new);queue.append(new)
assert len(group)==168
trans=[]
for forms in tr:
 mapping=[]
 for a,b,c in monoms:
  p=times(times(powpoly(forms[0],a),powpoly(forms[1],b)),powpoly(forms[2],c))
  mapping.append(sum(1<<idx[e] for e in p))
 trans.append(mapping)
def mapmask(m, mapping):
 ans=0
 while m:
  bit=m&-m; ans ^= mapping[bit.bit_length()-1];m^=bit
 return ans
unseen=set(range(1,1<<15)); orbits=[]
while unseen:
 x=min(unseen);todo=[x]; unseen.remove(x);orb=[x]
 for m in todo:
  for t in trans:
   y=mapmask(m,t)
   if y in unseen:
    unseen.remove(y);todo.append(y);orb.append(y)
 orbits.append((x,len(orb)))
assert len(orbits)==279 and sum(sz for _,sz in orbits)==32767
x,y,z=s.symbols('x y z')
polys=[x**a*y**b*z**c for a,b,c in monoms]
def groebner_smooth(mask):
 f=sum(polys[i] for i in range(15) if (mask>>i)&1)
 fx=s.diff(f,x);fy=s.diff(f,y);fz=s.diff(f,z)
 for v in (x,y,z):
  others=[u for u in (x,y,z) if u!=v]
  arr=[h.subs(v,1) for h in (f,fx,fy,fz)]
  g=s.groebner(arr,*others,order='grevlex',modulus=2)
  if not g.is_zero_dimensional and not (len(g.polys)==1 and g.polys[0].is_one):
   return False
  if not (len(g.polys)==1 and g.polys[0].is_one):return False
 return True
smooth=[]
for k,(rep,sz) in enumerate(orbits):
 if groebner_smooth(rep):smooth.append((rep,sz))

irr={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def mul(a,b,n):
 z=0;mod=irr[n];bit=1<<n
 while b:
  if b&1:z^=a
  a<<=1
  if a&bit:a^=mod
  b>>=1
 return z
def counts(mask,n):
 q=1<<n
 pp=[[1]*5 for _ in range(q)]
 for a in range(q):
  for k in range(1,5):pp[a][k]=mul(pp[a][k-1],a,n)
 ts=[e for i,e in enumerate(monoms) if (mask>>i)&1]
 ct=0
 for x in range(q):
  for y in range(q):
   z=1
   f=0
   for a,b,c in ts:f ^= mul(pp[x][a],pp[y][b],n)
   if f==0:ct+=1
 for x in range(q):
  y,z=1,0
  f=0
  for a,b,c in ts:
   if c==0:f ^= pp[x][a]
  if f==0:ct+=1
 if sum(1 for a,b,c in ts if (a,b,c)==(4,0,0))==0:ct+=1 # [1,0,0]
 return ct
# subspaces of rational F2^3: 7 lines kernels
points=[(x,y,z) for x,y,z in itertools.product(range(2),repeat=3) if (x,y,z)!=(0,0,0)]
def evalF(mask,p):
 return sum((p[0]**a*p[1]**b*p[2]**c) for i,(a,b,c) in enumerate(monoms) if mask>>i&1)%2
lines=[]
for ell in points:
 ker=[v for v in points if sum(a*b for a,b in zip(ell,v))%2==0]
 assert len(ker)==3
 lines.append((ell,ker[0],ker[1]))
def theta(mask):
 n=[0,0,0]
 for ell,u,v in lines:
  # restriction at (1,0), (0,1), (1,1) gets t^4 coefficients, but char2 t^3s etc could be nonzero. Need compute restriction polynomial coefficients by direct symbolic or bit expansion
  ft=[0]*5
  for j,(a,b,c) in enumerate(monoms):
   if not mask>>j&1:continue
   f=[1]
   for exp,i in ((a,0),(b,1),(c,2)):
    for _ in range(exp):
     ff=[0]*(len(f)+1)
     for k,w in enumerate(f):
      ff[k]^=w*u[i]
      ff[k+1]^=w*v[i]
     f=ff
   ft=[u^w for u,w in zip(ft,f)]
  if ft[1] or ft[3] or not any(ft):continue
  a,b,c=ft[0],ft[2],ft[4]
  roots=(a==0)+(c==0)+(a^b^c==0)
  n[roots]+=1
 return tuple(n)
rows=[]
for mask,orbit in smooth:
 ns=tuple(counts(mask,n) for n in (1,2,3))
 N1,N2,N3=ns
 S1=3-N1; S2=5-N2;S3=9-N3
 a1=-S1;a2=(S1*S1-S2)//2;a3=(-S1**3+3*S1*S2-2*S3)//6
 assert a2*2==S1*S1-S2 and a3*6==(-S1**3+3*S1*S2-2*S3)
 prof=theta(mask)
 rows.append(dict(mask=mask,orbit=orbit,ns=ns,coeffs=(a1,a2,a3),theta=prof))


assert len(smooth)==78 and sum(sz for _,sz in smooth)==10920
by_zeta=collections.defaultdict(list)
for row in rows:by_zeta[row['coeffs']].append(row)
assert len(by_zeta)==73
assert sorted(len(group) for group in by_zeta.values()).count(2)==5
assert len(set((row['coeffs'],row['theta']) for row in rows))==75
assert {key for key,group in by_zeta.items() if len(set(r['theta'] for r in group))>1} == {(-1,1,0),(0,0,3)}
expected={(-1,1,0): {4249:(0,1,0),4469:(1,0,0)}, (0,0,3):{4347:(0,1,0),4415:(0,0,1)}}
for key,group in by_zeta.items():
 if key in expected:
  assert {r['mask']:r['theta'] for r in group}==expected[key]
with open(Path(__file__).with_name('quartic_joint_census.csv'),'w',newline='',encoding='utf-8') as f:
 w=csv.writer(f)
 w.writerow(['coefficient_mask','orbit_size','N1','N2','N3','a1','a2','a3','theta_n0','theta_n1','theta_n2'])
 for r in rows:
  w.writerow([r['mask'],r['orbit'],*r['ns'],*r['coeffs'],*r['theta']])
print('CENSUS_OK',len(orbits),len(smooth),sum(r['orbit'] for r in rows),len(by_zeta),len(set((r['coeffs'],r['theta']) for r in rows)))
