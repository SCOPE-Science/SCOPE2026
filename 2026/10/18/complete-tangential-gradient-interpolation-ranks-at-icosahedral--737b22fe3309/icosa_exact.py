#!/usr/bin/env python3
"""Exact Q(sqrt(5))-linear algebra for exceptional icosahedral tangent ranks."""
from fractions import Fraction as F
from functools import lru_cache
class Q:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
 def __add__(x,y):
  y=asq(y);return Q(x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return Q(-x.a,-x.b)
 def __sub__(x,y):return x+-asq(y)
 def __rsub__(x,y):return asq(y)+-x
 def __mul__(x,y):
  y=asq(y);return Q(x.a*y.a+5*x.b*y.b,x.a*y.b+x.b*y.a)
 __rmul__=__mul__
 def __truediv__(x,y):
  y=asq(y);d=y.a*y.a-5*y.b*y.b
  if d==0:raise ZeroDivisionError
  return Q((x.a*y.a-5*x.b*y.b)/d,(x.b*y.a-x.a*y.b)/d)
 def __rtruediv__(x,y):return asq(y)/x
 def __hash__(x):return hash((x.a,x.b))
 def __eq__(x,y):
  y=asq(y);return x.a==y.a and x.b==y.b
 def __bool__(x):return bool(x.a or x.b)
 def __repr__(x):return f'Q({x.a},{x.b})'
def asq(x):return x if isinstance(x,Q) else Q(x)
R=Q(0,1);one=Q(1);zero=Q(0)
phi=(1+R)/2
L=1+phi*phi
Qs=[[asq(t) for t in q] for q in [(0,1,phi),(0,1,-phi),(1,phi,0),(1,-phi,0),(phi,0,1),(phi,0,-1)]]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),zero)
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
U=[]
for q in Qs:
 i=q.index(zero);e=[asq(int(i==j)) for j in range(3)]
 U.extend([(q,e),(q,cross(q,e))])

@lru_cache(None)
def leg(l,t):
 if l==0:return zero,zero
 p0=one;p1=t
 for n in range(1,l):p0,p1=p1,((2*n+1)*t*p1-n*p0)/(n+1)
 der=(l*(p0-t*p1))/(1-t*t)
 sec=(2*t*der-l*(l+1)*p1)/(1-t*t)
 return der,sec

def matrix(l):
 out=[]
 for i,(q,u) in enumerate(U):
  row=[]
  for j,(r,v) in enumerate(U):
   if i//2==j//2: val=F(l*(l+1),2)*dot(u,v)
   else:
    t=dot(q,r)/L;a,b=leg(l,t)
    val=a*dot(u,v)+b*dot(u,r)*dot(v,q)/L
   row.append(asq(val))
  out.append(row)
 return out

def rank(A):
 a=[row[:] for row in A];m=len(a);n=len(a[0]);r=0
 for j in range(n):
  i=next((k for k in range(r,m) if a[k][j]),None)
  if i is None:continue
  a[r],a[i]=a[i],a[r]
  pivot=a[r][j];a[r]=[v/pivot for v in a[r]]
  for i in range(r+1,m):
   if a[i][j]:
    fac=a[i][j];a[i]=[v-fac*w for v,w in zip(a[i],a[r])]
  r+=1
  if r==m:break
 return r
if __name__=='__main__':
 rr=[rank(matrix(l)) for l in range(15)]
 print('exact_Qsqrt5_ranks',rr)
 assert rr==[0,3,5,4,9,8,12,12,9,12,12,12,12,12,9]
 print('PASS exact Q(sqrt5) ranks 0..14')
