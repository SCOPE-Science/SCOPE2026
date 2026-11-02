#!/usr/bin/env python3
"""Direct finite-field PGL2 orbit census supporting a lattice classification."""
from itertools import product

MODULI={(2,2):(1,1,1),(2,3):(1,0,1,1),(2,4):(1,0,0,1,1),
        (2,5):(1,0,0,1,0,1),(3,2):(1,0,1),(3,3):(1,0,2,1),
        (3,4):(1,0,1,1,1)}

class GF:
 def __init__(self,p,d):
  self.p,self.d,self.mod=p,d,MODULI[p,d]
  self.q=p**d
  self.digits=[tuple((i//p**j)%p for j in range(d)) for i in range(self.q)]
 def fromdigits(self,c):return sum((int(v)%self.p)*self.p**i for i,v in enumerate(c))
 def add(self,a,b):return self.fromdigits([(x+y)%self.p for x,y in zip(self.digits[a],self.digits[b])])
 def neg(self,a):return self.fromdigits([(-x)%self.p for x in self.digits[a]])
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  p,d=self.p,self.d
  A=self.digits[a]; B=self.digits[b]
  tmp=[0]*(2*d-1)
  for i in range(d):
   for j in range(d):tmp[i+j]=(tmp[i+j]+A[i]*B[j])%p
  for k in range(2*d-2,d-1,-1):
   t=tmp[k]
   if t:
    for j in range(d):tmp[k-d+j]=(tmp[k-d+j]-t*self.mod[j])%p
  return self.fromdigits(tmp[:d])
 def pow(self,a,n):
  r=1
  while n:
   if n&1:r=self.mul(r,a)
   a=self.mul(a,a);n>>=1
  return r
 def inv(self,a):
  assert a
  return self.pow(a,self.q-2)
 def degree(self,a):
  b=a
  for i in range(1,self.d+1):
   b=self.pow(b,self.p)
   if b==a:return i
  raise AssertionError(a)

def pgl(p):
 out=set()
 for a,b,c,d in product(range(p),repeat=4):
  if (a*d-b*c)%p==0:continue
  m=(a,b,c,d)
  z=next(x for x in m if x)
  v=pow(z,-1,p)
  out.add(tuple((v*x)%p for x in m))
 return sorted(out)

def orbit_census(p,d):
 K=GF(p,d); group=pgl(p);Q=K.q
 assert len(group)==p*(p*p-1)
 assert all(K.mul(x,K.inv(x))==1 for x in range(1,K.q))
 def transform(t,m):
  a,b,c,e=m
  if t==Q:
   return Q if c==0 else K.mul(e,K.inv(c))
  num=K.add(b,K.mul(e,t));den=K.add(a,K.mul(c,t))
  return K.mul(num,K.inv(den)) if den else Q
 left=set(range(Q+1)); actual=[]
 while left:
  t=min(left)
  orbit={transform(t,m) for m in group}
  assert orbit<=left, (p,d,t,orbit-left)
  left-=orbit
  degree=1 if t==Q else K.degree(t)
  assert all((x==Q and degree==1) or (x!=Q and K.degree(x)==degree) for x in orbit)
  actual.append((degree,len(orbit)))
 eps=int(d%2==0)
 predicted=1+eps+(Q-p-eps*(p*p-p))//(p*(p*p-1))
 assert (Q-p-eps*(p*p-p)) % (p*(p*p-1))==0
 assert len(actual)==predicted,(p,d,len(actual),predicted)
 assert actual.count((1,p+1))==1
 if eps:assert actual.count((2,p*p-p))==1
 assert all(size==p*(p*p-1) for deg,size in actual if deg>=3)
 counts={}
 for deg,sz in actual:counts[(deg,sz)]=counts.get((deg,sz),0)+1
 print(f'p={p} d={d}: total_intermediate={Q+3}, classes={len(actual)}, orbit_details={counts}')
 return predicted

if __name__=='__main__':
 for p,d in MODULI:orbit_census(p,d)
 print('VERIFY_OK')
