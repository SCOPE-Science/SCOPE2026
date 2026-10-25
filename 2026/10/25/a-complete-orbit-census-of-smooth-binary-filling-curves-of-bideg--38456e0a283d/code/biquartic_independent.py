"""Exact bidegree-(4,4) filling-curve census over F2; pure Python."""
from itertools import product
from collections import Counter
import json
A,B=4,4
terms=[(i,j) for i in range(A+1) for j in range(B+1)]
P=[(1,0),(1,1),(0,1)]
# nine point evaluations and chart-derivative linear functionals
eval_rows=[];deriv_rows=[]
for X in P:
 for Y in P:
  fx=fy=ev=0
  cx=0 if X[0] else 1; cy=0 if Y[0] else 1
  xx=X[1] if cx==0 else X[0]; yy=Y[1] if cy==0 else Y[0]
  for k,(i,j) in enumerate(terms):
   u=i if cx==0 else A-i
   v=j if cy==0 else B-j
   if (xx or u==0) and (yy or v==0):ev|=1<<k
   if (u&1) and (xx or u==1) and (yy or v==0):fx|=1<<k
   if (v&1) and (xx or u==0) and (yy or v==1):fy|=1<<k
  eval_rows.append(ev)
  deriv_rows.append((fx,fy))
assert len(eval_rows)==9
# Independent construction of the vanishing ideal: Dx=X0^2 X1+X0 X1^2 and Dy=Y0^2 Y1+Y0 Y1^2.
# At bidegree (4,4) their 20 natural products span the 16-dimensional filling space.
def pos(i,j):return terms.index((i,j))
gens=[]
for i in range(2):
 for j in range(5):gens.append((1<<pos(i+1,j))^(1<<pos(i+2,j)))
for i in range(5):
 for j in range(2):gens.append((1<<pos(i,j+1))^(1<<pos(i,j+2)))
pivs={};basis=[]
for z in gens:
 for p in sorted(pivs,reverse=True):
  if z>>p&1:z^=pivs[p]
 if z:
  p=z.bit_length()-1;pivs[p]=z;basis.append(z)
assert len(basis)==16,(len(basis),basis)
fill=[]
for idx in range(1,1<<len(basis)):
 m=0
 for k,g in enumerate(basis):
  if idx>>k&1:m^=g
 fill.append(m)
assert len(set(fill))==65535
assert all(all((m&r).bit_count()%2==0 for r in eval_rows) for m in fill)
locally=[]
for m in fill:
 if all(((m&dx).bit_count()%2 or (m&dy).bit_count()%2) for dx,dy in deriv_rows):locally.append(m)
assert len(locally)==3648,len(locally)
# GF2 polynomial arithmetic with pairs (exponent_x, exponent_y)
def add(*pp):
 z=set()
 for p in pp:z.symmetric_difference_update(p)
 return frozenset(z)
def shift(poly,t):return frozenset((i+t[0],j+t[1]) for i,j in poly)
def lead(poly):return max(poly)
def rem(poly,G):
 p=set(poly)
 while p:
  lm=max(p)
  found=False
  for g in G:
   n=lead(g)
   if n[0]<=lm[0] and n[1]<=lm[1]:
    p.symmetric_difference_update(shift(g,(lm[0]-n[0],lm[1]-n[1])));found=True;break
  if not found:return False # nonzero remainder: nonunit after Groebner completion
 return True

def unit_ideal(polys):
 G=[frozenset(p) for p in polys if p]
 if any(g==frozenset({(0,0)}) for g in G):return True
 pairs=[(i,j) for i in range(len(G)) for j in range(i)]
 while pairs:
  i,j=pairs.pop()
  u,v=lead(G[i]),lead(G[j]); w=(max(u[0],v[0]),max(u[1],v[1]))
  s=add(shift(G[i],(w[0]-u[0],w[1]-u[1])),shift(G[j],(w[0]-v[0],w[1]-v[1])))
  # Buchberger polynomial division preserving residual terms
  r=set(); p=set(s)
  while p:
   lm=max(p)
   for g in G:
    n=lead(g)
    if n[0]<=lm[0] and n[1]<=lm[1]:
     p.symmetric_difference_update(shift(g,(lm[0]-n[0],lm[1]-n[1])));break
   else:
    p.remove(lm);r.add(lm)
  if r:
   h=frozenset(r)
   if h==frozenset({(0,0)}):return True
   pairs.extend((len(G),k) for k in range(len(G)))
   G.append(h)
 return False

def curve_smooth(m):
 for cx in range(2):
  for cy in range(2):
   f=frozenset((i if not cx else A-i,j if not cy else B-j) for k,(i,j) in enumerate(terms) if m>>k&1)
   dx=frozenset((i-1,j) for i,j in f if i%2==1)
   dy=frozenset((i,j-1) for i,j in f if j%2==1)
   if not unit_ideal((f,dx,dy)):return False
 return True
print('ambient',1<<25,'filling',len(fill),'locally_smooth',len(locally),flush=True)
# Group: generate affine GL2(F2) substitution on bihomogeneous monomials.
matrices=[(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if (a*d+b*c)%2]
assert len(matrices)==6

def mul_poly(p,q):
 res=set()
 for t in p:
  for s in q:
   v=tuple(t[i]+s[i] for i in range(4))
   if v in res:res.remove(v)
   else:res.add(v)
 return res
unit={(0,0,0,0)}

def linear_coeffs(A, k):
 c=A[:2] if k==0 else A[2:]
 idx=0 if k==0 else 1
 p=set()
 for j in (0,1):
  if c[j]:p.add(tuple(int(t==j) for t in range(4)))
 return p

def linear_coeffs_y(A,k):
 c=A[:2] if k==0 else A[2:]
 p=set()
 for j in (0,1):
  if c[j]:p.add(tuple(int(t==2+k*0+j) for t in range(4)))
 return p

def powers(p,n):
 q=[unit]
 for _ in range(n):q.append(mul_poly(q[-1],p))
 return q

actions=[]
for U,V in product(matrices,repeat=2):
 p0=powers(linear_coeffs(U,0),4);p1=powers(linear_coeffs(U,1),4)
 q0=powers(linear_coeffs_y(V,0),4);q1=powers(linear_coeffs_y(V,1),4)
 columns=[]
 for i,j in terms:
  p=mul_poly(mul_poly(mul_poly(p0[4-i],p1[i]),q0[4-j]),q1[j])
  mask=0
  for k,(u,v) in enumerate(terms):
   if (4-u,u,4-v,v) in p:mask|=1<<k
  columns.append(mask)
 actions.append(columns)

swap=[1<<terms.index((j,i)) for i,j in terms]
acts0=actions[:]
actions += [[sum(swap[k] for k in range(len(terms)) if z>>k&1) for z in act] for act in acts0]
assert len(actions)==72
def apply(m,act):
 ans=0
 while m:
  low=m&-m;ans^=act[low.bit_length()-1];m^=low
 return ans
unseen=set(locally);orbs=[];smooth=set(); all_orbs=[]
while unseen:
 m=min(unseen);orb={apply(m,a) for a in actions}
 assert orb<=unseen
 unseen-=orb
 all_orbs.append((m,len(orb)))
 if curve_smooth(m):
  smooth.update(orb)
  orbs.append((m,len(orb)))
assert len(smooth)==2328
print('orbits',len(orbs),sorted(orbs,key=lambda r:-r[1])[:4],'sizes',dict(Counter(k for m,k in orbs)),flush=True)
assert Counter(k for m,k in orbs)==Counter({72:31,36:2,24:1})
with open('biquartic_independent_output.json','w') as o:json.dump({'ambient':1<<25,'filling':len(fill),'rationally_smooth':len(locally),'smooth':len(smooth),'smooth_masks':sorted(smooth),'orbit_reps':orbs,'orbit_sizes':dict(Counter(k for m,k in orbs))},o,sort_keys=True)
