"""Exact finite geometric certificate for a stretched regular dodecahedron.

Requires Python 3.10+ and SymPy.  Coefficients are in Z[phi], phi^2=phi+1.
No sampled orientations enter the certificate; numerical spot checks are auxiliary.
"""
from itertools import product, combinations
from collections import Counter
import sympy as sp
from math import acos,pi,sqrt

ZERO=(0,0);ONE=(1,0); PHI=(0,1); INVPHI=(-1,1)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return a*c+b*d,a*d+b*c+b*d
def sign(x):
 a,b=x; A=2*a+b
 if not b:return (A>0)-(A<0)
 if not A:return (b>0)-(b<0)
 if A*b>0:return (b>0)-(b<0)
 z=A*A-5*b*b
 assert z!=0
 return ((z>0)-(z<0)) if A>0 else ((z<0)-(z>0))
def signed(v,e):return v if e>0 else neg(v)
def vect(v,e):return tuple(signed(x,e) for x in v)
def dot(v,w):
 out=ZERO
 for x,y in zip(v,w):out=add(out,mul(x,y))
 return out
def cross(v,w):
 return (sub(mul(v[1],w[2]),mul(v[2],w[1])),
         sub(mul(v[2],w[0]),mul(v[0],w[2])),
         sub(mul(v[0],w[1]),mul(v[1],w[0])))
def difference(v,w):return tuple(sub(x,y) for x,y in zip(v,w))
def vertices():
 V=[tuple((int(x),0) for x in xyz) for xyz in product((-1,1), repeat=3)]
 for s,t in product((-1,1),repeat=2):V.append((ZERO,signed(INVPHI,s),signed(PHI,t)))
 for s,t in product((-1,1),repeat=2):V.append((signed(INVPHI,s),signed(PHI,t),ZERO))
 for s,t in product((-1,1),repeat=2):V.append((signed(PHI,s),ZERO,signed(INVPHI,t)))
 return V

def certificate():
 V=vertices()
 assert len(V)==len(set(V))==20
 assert all(dot(v,v)==(3,0) for v in V)
 E=[(i,j) for i,j in combinations(range(20),2) if dot(difference(V[i],V[j]),difference(V[i],V[j]))==(8,-4)]
 assert len(E)==30
 W=[v for v in V if next(sign(x) for x in v if sign(x))==1]
 assert len(W)==10
 lookup={v:(i,1) for i,v in enumerate(W)}
 lookup.update({vect(v,-1):(i,-1) for i,v in enumerate(W)})
 assert len(lookup)==20
 assert all(sign(dot(W[k],cross(W[i],W[j])))!=0 for i,j,k in combinations(range(10),3))
 rays=[]
 for i,j in combinations(range(10),2):
  for eps in (1,-1):
   v=vect(cross(W[i],W[j]),eps)
   ss=[sign(dot(v,w)) for w in W]
   assert ss.count(0)==2
   plus=sum(1<<i for i,x in enumerate(ss) if x>0)
   minus=sum(1<<i for i,x in enumerate(ss) if x<0)
   rays.append((i,j,plus,minus))
 assert len(rays)==90
 by=Counter();types=Counter();n_full=0
 for choice in range(1024):
  rr=[(i,j) for i,j,p,m in rays if (choice&p)==p and (choice&m)==0]
  if not rr:continue
  occupied=0
  for i,j in rr:
   v=cross(W[i],W[j])
   # record which hyperplane inequalities can be strictly satisfied
   for eps in (1,-1):
    ss=[sign(dot(vect(v,eps),w)) for w in W]
    if all((z>=0 if ((choice>>k)&1) else z<=0) for k,z in enumerate(ss)):
     occupied|=sum(1<<k for k,z in enumerate(ss) if z!=0)
     break
  if occupied!=1023:continue
  n_full+=1
  N=0
  for i,j in E:
   a,e=lookup[V[i]];b,f=lookup[V[j]]
   N+=(e*(1 if (choice>>a)&1 else -1)!=f*(1 if (choice>>b)&1 else -1))
  by[(N,len(rr))]+=1
  if N!=10:continue
  for i,j in rr:
   si=1 if choice>>i&1 else -1
   sj=1 if choice>>j&1 else -1
   a=mul(W[i][0],W[i][0]);b=mul(W[j][0],W[j][0]);a,b=sorted((a,b))
   dot0=dot(W[i],W[j]); dot1=mul(W[i][0],W[j][0])
   if si!=sj:dot0,dot1=neg(dot0),neg(dot1)
   assert dot0==ONE
   types[(a,b,dot1)]+=1
 assert n_full==92
 assert by=={(6,6):20,(8,3):60,(10,5):12},by
 assert sum(types.values())==60
 expected={
  ((1,0),(1,0),(1,0)):8,
  ((1,0),(2,-1),(1,-1)):8,
  ((1,1),(2,-1),(1,0)):8,
  ((0,0),(1,0),(0,0)):8,
  ((0,0),(2,-1),(0,0)):8,
  ((1,0),(1,0),(-1,0)):4,
  ((1,0),(1,1),(0,1)):8,
  ((0,0),(1,1),(0,0)):8,
 }
 assert types==expected,(types,expected)
 # Exact third-order Taylor coefficient of the numerator of the probability:
 sqrt5=sp.sqrt(5); phi=(1+sqrt5)/2
 q=lambda z:sp.Integer(z[0])+sp.Integer(z[1])*phi
 f1=-3*sp.sqrt(2)/4;f2=9*sp.sqrt(2)/32;f3=-297*sp.sqrt(2)/256
 coeff=[sp.S.Zero]*3
 for (aa,bb,cc),m in expected.items():
  a,b,c=q(aa),q(bb),q(cc)
  A=(a+b)/3;B=a*b/9
  Q1=-A/2;Q2=-B/2+3*A*A/8;Q3=3*A*B/4-5*A**3/16
  x1=-(c+Q1)/3;x2=-(c*Q1+Q2)/3;x3=-(c*Q2+Q3)/3
  g1=f1*x1;g2=f1*x2+f2*x1*x1/2;g3=f1*x3+f2*x1*x2+f3*x1**3/6
  for i,z in enumerate((g1,g2,g3)):coeff[i]+=m*z
 coeff=[sp.simplify(sp.radsimp(sp.expand(x))) for x in coeff]
 assert coeff==[0,0,-125*sp.sqrt(2)/6912],coeff
 # Compare exact-corner formula with an independent spherical-area evaluation
 def number(z):return z[0]+float(phi)*z[1]
 def p10_from_table(t):
  s=t*t-1;total=0
  for (aa,bb,cc),m in expected.items():
   a,b,c=number(aa),number(bb),number(cc)
   cosv=-(1+c*s)/sqrt((3+a*s)*(3+b*s))
   total+=m*acos(max(-1,min(1,cosv)))
  return (total-36*pi)/(4*pi)
 for t,low,high in [(0.5,.12,.14),(1,.12,.13),(2,.11,.13),(5,.07,.08)]:
  p=p10_from_table(t)
  assert low<p<high,(t,p)
 print('PASS: exact 20-vertex / 30-edge / 10-circle arrangement; all 1024 sign patterns')
 print('PASS: 92 full-dimensional spherical regions with side counts 20/60/12')
 print('PASS: 8 signed corner types, integer-pair exact matching; 60 corners')
 print('PASS: 1st and 2nd Taylor terms vanish; 3rd equals -125 sqrt(2)/6912')
 print('PASS: 4 numerical spot checks of closed formula')

if __name__=='__main__':certificate()
