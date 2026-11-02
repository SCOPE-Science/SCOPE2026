#!/usr/bin/env python3
"""Exact finite-field classification for possible tangent-filling smooth cubics at p=11,13."""
from collections import Counter

def inv(a,p): return pow(a%p,-1,p)
def normalize(P,p):
 for a in P:
  if a%p:
   u=inv(a,p)
   return tuple(x*u%p for x in P)
 raise ValueError

def point_space(p):
 return sorted({normalize((x,y,z),p) for x in range(p) for y in range(p) for z in range(p) if x or y or z})

def add(P,Q,a,p):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v)%p==0:return None
 m=(v-y)*inv(u-x,p)%p if x!=u else (3*x*x+a)*inv(2*y,p)%p
 xx=(m*m-x-u)%p
 return xx,(m*(x-xx)-y)%p

def mul(n,P,a,p):
 R=None
 while n:
  if n&1:R=add(R,P,a,p)
  P=add(P,P,a,p);n>>=1
 return R

def epoints(a,b,p):
 return [None]+[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x-a*x-b)%p==0]

def cubic(a,b,T,p):
 # monomial order x³,x²y,x²z,xy²,xyz,xz²,y³,y²z,yz²,z³
 if T is None:return [-1%p,0,0,0,0,-a%p,0,1,0,-b%p]
 r,s=T
 return [0,0,-1%p,1,0,-r%p,0,-r%p,-2*s%p,-(r*r+a)%p]

def test_model(p,coef,plane,linemasks):
 mon=((3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3))
 cover=0; npt=0;tang=set()
 for x,y,z in plane:
  F=0;grad=[0,0,0]
  for c,(i,j,k) in zip(coef,mon):
   if not c:continue
   F+=c*pow(x,i,p)*pow(y,j,p)*pow(z,k,p)
   for t,(v,exp) in enumerate(((x,i),(y,j),(z,k))):
    if not exp:continue
    grad[t]+=c*exp*pow(x,i-(t==0),p)*pow(y,j-(t==1),p)*pow(z,k-(t==2),p)
  if F%p:continue
  npt+=1
  L=normalize(grad,p)
  tang.add(L)
  cover|=linemasks[L]
 return npt,len(tang),cover.bit_count()

def check(p):
 plane=point_space(p)
 assert len(plane)==p*p+p+1
 linemasks={L:sum(1<<idx for idx,P in enumerate(plane) if sum(a*b for a,b in zip(L,P))%p==0) for L in plane}
 threshold=3*(p+1)//2
 allab={}
 for a in range(p):
  for b in range(p):
   if (4*a**3+27*b*b)%p==0:continue
   pts=epoints(a,b,p)
   if len(pts)<threshold:continue
   assert len(pts)==threshold,(a,b,len(pts))
   representative=min((a*pow(u,4,p)%p,b*pow(u,6,p)%p) for u in range(1,p))
   allab.setdefault(representative,[]).append((a,b))
 print('p',p,'classes with #E=',threshold,allab)
 for a,b in allab:
  pts=epoints(a,b,p)
  triple={mul(3,P,a,p) for P in pts}
  quotient=[];remaining=set(pts)
  while remaining:
   T=next(iter(remaining))
   coset={add(T,P,a,p) for P in triple}
   assert coset<=remaining
   remaining-=coset
   quotient.append(T)
  assert len(quotient)==3,(p,a,b,len(quotient))
  for T in quotient:
   if T is not None and T[1]==0:
    T=next(Q for Q in {add(T,P,a,p) for P in triple} if Q is not None and Q[1])
   co=cubic(a,b,T,p)
   N,nt,cov=test_model(p,co,plane,linemasks)
   assert N==threshold and nt==threshold
   print('MODEL',p,'a,b',a,b,'T',T,'coeff',co,'N',N,'tangents',nt,'coverage',cov,'missing',len(plane)-cov)
   assert cov<len(plane)
 print('EXACT_PRIME_CHECK_OK',p)
if __name__=='__main__':
 for p in (11,13):check(p)
