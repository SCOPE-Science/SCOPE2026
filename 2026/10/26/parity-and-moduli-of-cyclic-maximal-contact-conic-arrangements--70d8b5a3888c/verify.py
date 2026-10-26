#!/usr/bin/env python3
"""Exact test of cyclic maximal-contact conic normal forms.
The universal theorem is proved separately; these are finite exact witnesses.
"""
from fractions import Fraction
from itertools import combinations

def pol_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b): c[i+j]+=v*w
 return tuple(c)

def evaluation(L,p,mod=None):
 r=L[0]*p[0]+L[1]*p[1]
 return r if mod is None else r%mod

def inv(v,mod):
 return Fraction(1,v) if mod is None else pow(v%mod,-1,mod)

def make(points,mod=None):
 n=len(points)
 assert len(set(points))==n
 L=[(b,-a) for a,b in points]
 c=[Fraction(1) if mod is None else 1]
 for i in range(n-1):
  prev=evaluation(L[(i-1)%n],points[i],mod)
  nxt=evaluation(L[(i+1)%n],points[i],mod)
  val=c[-1]*prev*inv(nxt,mod)
  c.append(val if mod is None else val%mod)
 closure=(c[0]*evaluation(L[0],points[-1],mod)-c[-1]*evaluation(L[-2],points[-1],mod))
 if mod:closure%=mod
 Q=[pol_mul(L[(i-1)%n], L[i]) for i in range(n)]
 Q=[tuple((c[i]*v if mod is None else c[i]*v%mod) for v in Q[i]) for i in range(n)]
 return L,c,Q,closure

# Each Q is represented by (x^2,x*z,z^2). For edge i require Q_{i+1}-Q_i proportional to L_i^2.
def check_edges(points,mod=None):
 n=len(points);L,c,Q,closure=make(points,mod)
 assert closure==0,(n,mod,closure)
 for i in range(n):
  diff=[Q[(i+1)%n][j]-Q[i][j] for j in range(3)]
  l=L[i];sq=(l[0]**2,2*l[0]*l[1],l[1]**2)
  if mod:
   diff=[v%mod for v in diff];sq=tuple(v%mod for v in sq)
  pos=next(j for j in range(3) if sq[j]!=0)
  u=diff[pos]*inv(sq[pos],mod)
  for j in range(3):
   assert diff[j] == (u*sq[j] if mod is None else u*sq[j]%mod)
  assert u!=0
 return c,Q

points6=[(0,1),(1,1),(2,1),(3,1),(4,1),(1,0)]
points4=[(0,1),(1,1),(2,1),(1,0)]
for pts in [points4,points6,[(i,1) for i in range(8)]]:
 c,Q=check_edges(pts)
 print('characteristic zero n=',len(pts),'coefficients=',c)
for n in [3,5,7]:
 # use extension points (t,1), polynomial arithmetic valid in char2 if coefficients reduced
 # For n=5/7 use GF(8) separately below via finite-field arithmetic
 if n==3:
  pts=[(0,1),(1,1),(1,0)]
  c,Q=check_edges(pts,mod=2)
  print('characteristic two n=3 coefficients=',c,'Q=',Q)
for n in [3,5,7]:
 # Odd-cycle multiplier from formal skew-bracket signs.
 # Under characteristic zero, the product is -1, not +1.
 pts=[(i,1) for i in range(n)]
 _,c,_,closure=make(pts)
 assert closure!=0
 print('odd n=',n,'closure-obstruction=',closure)
# Independent characteristic-two witnesses over the eight-element field.
# Polynomial basis F2[t]/(t^3+t+1); elements 0,...,7.
def mul8(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1; a<<=1
  if a&8:a^=11
 return out

def inv8(a):
 assert a
 for b in range(1,8):
  if mul8(a,b)==1:return b
 raise AssertionError(a)

def test_gf8(n):
 pts=[(i,1) for i in range(n)]
 L=[(b,a) for a,b in pts]
 def ev(l,p):return mul8(l[0],p[0])^mul8(l[1],p[1])
 c=[1]
 for i in range(n-1):
  r=mul8(ev(L[(i-1)%n],pts[i]),inv8(ev(L[(i+1)%n],pts[i])))
  c.append(mul8(c[-1],r))
 assert mul8(c[0],ev(L[0],pts[-1]))==mul8(c[-1],ev(L[-2],pts[-1]))
 def qprod(a,b):
  return (mul8(a[0],b[0]),mul8(a[0],b[1])^mul8(a[1],b[0]),mul8(a[1],b[1]))
 Q=[]
 for i in range(n):
  Q.append(tuple(mul8(c[i],v) for v in qprod(L[(i-1)%n],L[i])))
 assert all(q[1]!=0 for q in Q), 'smoothness via nonzero cross coefficient'
 assert len(set(Q))==n, 'distinct conics'
 for i in range(n):
  d=tuple(Q[(i+1)%n][j]^Q[i][j] for j in range(3))
  assert d[1]==0 and d!=(0,0,0)
  ll=L[i]
  square=(mul8(ll[0],ll[0]),0,mul8(ll[1],ll[1]))
  j=0 if square[0] else 2
  scale=mul8(d[j],inv8(square[j]))
  assert tuple(mul8(scale,v) for v in square)==d
 for i,j in combinations(range(n),2):
  d=tuple(Q[i][v]^Q[j][v] for v in range(3))
  assert d[1]==0 and d!=(0,0,0), 'all pairs maximally tangent'
 print('characteristic two F8 n=',n, 'coefficients=',c)

for n in [5,7]:test_gf8(n)
print('VERIFY_OK')
