"""Exact 15-plane rational tritangent census for smooth (3,3) curves on P1 x P1/F2.

Requires sympy; full 2^16-1 equation space and all 72 quadric automorphisms.
Unit Groebner ideals on four affine charts certify geometric smoothness.
"""
from collections import Counter,defaultdict
import time
T=time.monotonic()
# bidegree (3,3) section: basis U^(3-i) V^i S^(3-j) T^j, indexed i*4+j
basis=[(i,j) for i in range(4) for j in range(4)]
# maps bit representation action for source substitution
# factor x->x+1 means U->U+V; index i power V^i expands U^(3-i) -> choose all k in [0,3-i] w mod2 binomial
from math import comb
# new monomial coordinates on first factor
def action_monomial(i,j,op):
 if op=='u_flip':return [(3-i,j)]
 if op=='s_flip':return [(i,3-j)]
 if op=='swap':return [(j,i)]
 if op=='u_add':return [(i+k,j) for k in range(4-i) if comb(3-i,k)%2]
 if op=='s_add':return [(i,j+k) for k in range(4-j) if comb(3-j,k)%2]
ops=['u_flip','u_add','s_flip','s_add','swap']
trans={}
for op in ops:
 e=[]
 for i,j in basis:
  out=0
  for ni,nj in action_monomial(i,j,op):out^=1<<(4*ni+nj)
  e.append(out)
 trans[op]=e

def act(f,op):
 row=trans[op];g=0
 while f:
  s=f&-f;g^=row[s.bit_length()-1];f^=s
 return g
# Build orbits
reps=[];members=[]
seen=bytearray(65536)
for f in range(1,65536):
 if seen[f]:continue
 orb={f};front=[f];seen[f]=1
 for v in front:
  for op in ops:
   w=act(v,op)
   if w not in orb:
    assert not seen[w]
    orb.add(w);front.append(w);seen[w]=1
 reps.append(f);members.append(front)
assert len(reps)==1075 and sum(map(len,members))==65535
# six smooth (1,1) hyperplane graphs: (S,T)=(aU+bV,cU+dV)
ms=[]
for a in range(2):
 for b in range(2):
  for c in range(2):
   for d in range(2):
    if (a*d+b*c)%2:ms.append((a,b,c,d))
assert len(ms)==6

def poly_mult(a,b):
 # binary poly dict exponent V
 out=0
 for i in range(7):
  if not (a>>i)&1:continue
  for j in range(7-i):
   if (b>>j)&1:out^=1<<(i+j)
 return out

def restrict_basis(i,j,a,b,c,d):
 # binary sextic powers U,V; (aU+bV)^(3-j)*(cU+dV)^j * U^(3-i)V^i
 def power_linear(p,q,n):
  z=1
  for k in range(n):z=poly_mult(z,(p|(q<<1)))
  return z
 p=poly_mult(power_linear(a,b,3-j),power_linear(c,d,j));return p<<i
restr=[]
for m in ms:restr.append([restrict_basis(i,j,*m) for i,j in basis])

def square_free_cubic(g):
 # polynomial g(U,V), degree3; squarefree on P1 over alg closure: gcd(h,partial U,partial V)=1
 # directly roots at infinity + affine binary polynomial
 import sympy as sp
 t=sp.Symbol('t')
 p=sp.Poly(sum((g>>i&1)*t**i for i in range(4)),t, modulus=2)
 if p.degree()<2:return False # infinity multiplicity >=2
 return sp.gcd(p,p.diff()).degree()==0
sf=[square_free_cubic(g) for g in range(16)]
assert sum(sf)==6
# precompute masks per plane for odd bits and squarefree; even sextic = g^2 (degree6), coeff even at 0,2,4,6 = g bits
contact=[]
for f in range(65536):
 pl=[]
 for row in restr:
  s=0;v=f
  while v:
   low=v&-v;s^=row[low.bit_length()-1];v^=low
  if s & 0b101010:continue
  g=sum(((s>>(2*j))&1)<<j for j in range(4))
  pl.append((g,sf[g]))
 contact.append(pl)
# smoothness exact symbolic criterion, use sympy groebner for each orbit representative on each of four charts
import sympy as sp
x,y=sp.symbols('x y')
mons=[[x**(3-i)*y**(3-j) for j in range(4)] for i in range(4)]
# coordinates affine U=x,V=1; S=y,T=1; swap U,V -> exponent i instead of 3-i, similarly second
polys={}
for c1 in range(2):
 for c2 in range(2):
  bm=[(x**(i if c1 else 3-i))*(y**(j if c2 else 3-j)) for i,j in basis]
  polys[c1,c2]=bm

def is_smooth(f):
 for bm in polys.values():
  p=sp.Poly(sum(bm[i] for i in range(16) if f&(1<<i)),x,y,modulus=2)
  gp=sp.groebner([p.as_expr(),p.diff(x).as_expr(),p.diff(y).as_expr()],x,y, modulus=2,order='lex')
  if not (len(gp.polys)==1 and gp.polys[0].is_one):return False
 return True
smooth=[];cnt=Counter();cnt2=Counter();smooth_reps=[]
for k,(f,orbit) in enumerate(zip(reps,members)):
 if is_smooth(f):
  smooth_reps.append(f);smooth.extend(orbit)
  cnt[(len(contact[f]),sum(t for g,t in contact[f]))]+=len(orbit)
  cnt2[len(contact[f])]+=len(orbit)
assert len(smooth)==16020 and len(smooth_reps)==252
# all nine tangent hyperplanes Q|H reducible: one factor line in each ruling
lines=[(1,0),(0,1),(1,1)]
roots=[(0,1),(1,0),(1,1)]

def vec_eval_linear(h,v):return ((h[0]&v[0])^(h[1]&v[1]))

def cubiline(g,line,root):
 if not g:return (False,False)
 a,b=line;v0,v1=root
 for h0 in range(2):
  for h1 in range(2):
   mask=(a*h0)|((b*h0)<<1)|((a*h1)<<2)|((b*h1)<<3)
   if mask==g:return (True,(h0*v0^h1*v1)==1)
 return (False,False)

def plane_restrict(f,u,s,which):
 # restrict first factor at u=(U,V), yields cubic in S,T if which=0; else restrict second factor at s=(S,T)
 z=0
 for i,j in basis:
  if f&(1<<(4*i+j)):
   if which==0:
    coef=(u[0]**(3-i)*u[1]**i)&1
    if coef:z^=1<<j
   else:
    coef=(s[0]**(3-j)*s[1]**j)&1
    if coef:z^=1<<i
 return z

def tangent_contact(f):
 out=[]
 for L,u in zip(lines,roots):
  for M,s in zip(lines,roots):
   g1=plane_restrict(f,u,s,0)
   g2=plane_restrict(f,u,s,1)
   e1,p1=cubiline(g1,M,s)
   e2,p2=cubiline(g2,L,u)
   if e1 and e2:out.append((L,M,p1 and p2))
 return out
cc=Counter();cc_orbits=Counter();fullmax=defaultdict(list);mult=Counter()
for f,orb in zip(reps,members):
 if f not in smooth_reps:continue
 s=sum(t for g,t in contact[f]);w=len(contact[f]); t=tangent_contact(f)
 total=s+sum(p for L,M,p in t)
 even=w+len(t)
 cc[(even,total,w,s,len(t))]+=len(orb)
 mult[(total,even)]+=len(orb)
 fullmax[total].append((f,len(orb),w,s,len(t),sum(p for L,M,p in t)))
proper=Counter()
for (k,_),n in mult.items():proper[k]+=n
assert proper=={0:10656,1:5022,2:324,3:18}
print('PROPER_TOTAL',dict(sorted(proper.items())))
print('PROPER_VS_EVEN',dict(sorted(mult.items())))
assert max(fullmax)==3 and fullmax[3]==[(10723,18,2,1,2,2)]
print('UNIQUE_EXTREMAL_ORBIT',fullmax[3])

plane_types=Counter()
for r,orb in zip(reps,members):
 if r not in smooth_reps:continue
 a=sum(s for g,s in contact[r]); b=sum(v for _,_,v in tangent_contact(r))
 plane_types[(a,b)]+=len(orb)
assert plane_types=={(0,0):10656,(0,1):2088,(1,0):2934,(1,1):252,(1,2):18,(2,0):72}
print('TWO_PLANE_TYPES',dict(sorted(plane_types.items())))
print('FULL_CENSUS_PASS')
