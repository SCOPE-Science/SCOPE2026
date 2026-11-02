#!/usr/bin/env python3
"""Independent finite-field enumerations for reciprocal-trace incidence spectra."""
from itertools import product
from math import gcd, sqrt, pi
import cmath

FIELDS = [(3,[0,1]),(5,[0,1]),(7,[0,1]),(11,[0,1]),(13,[0,1]),(17,[0,1]),(19,[0,1]),(23,[0,1]),(29,[0,1]),(31,[0,1]),(37,[0,1]),(41,[0,1]),(3,[1,0,1]),(5,[2,0,1]),(3,[1,2,0,1]),(7,[1,0,1])]

class Field:
 def __init__(self,p,pol):
  self.p=p; self.pol=pol;self.degree=len(pol)-1
  if self.degree==0:raise ValueError('bad degree')
  self.q=p**self.degree
 def digits(self,a):
  return tuple((a//(self.p**i))%self.p for i in range(self.degree))
 def encode(self,ds):
  return sum((int(ds[i])%self.p)*self.p**i for i in range(self.degree))
 def add(self,a,b):
  da=self.digits(a);db=self.digits(b)
  return self.encode([(x+y)%self.p for x,y in zip(da,db)])
 def neg(self,a):return self.encode([(-x)%self.p for x in self.digits(a)])
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  da=self.digits(a);db=self.digits(b);out=[0]*(2*self.degree-1)
  for i,ai in enumerate(da):
   for j,bj in enumerate(db):out[i+j]=(out[i+j]+ai*bj)%self.p
  for k in range(len(out)-1,self.degree-1,-1):
   coef=out[k]
   for j in range(self.degree):out[k-self.degree+j]=(out[k-self.degree+j]-coef*self.pol[j])%self.p
  return self.encode(out[:self.degree])
 def power(self,a,n):
  z=1
  while n:
   if n&1:z=self.mul(z,a)
   a=self.mul(a,a);n//=2
  return z
 def inv(self,a):return self.power(a,self.q-2)
 def chi(self,a):
  if a==0:return 0
  return 1 if self.power(a,(self.q-1)//2)==1 else -1

def check(F):
 q=F.q; h=(q-1)//2
 Q=sorted({F.mul(x,x) for x in range(q)})
 H=[x for x in Q if x]
 assert len(Q)==h+1 and len(H)==h
 positives=set(Q)
 # Independent definition: x+a/x, tested against a prescribed trace square root.
 B=[]
 for a in range(1,q):
  traces={F.add(x,F.mul(a,F.inv(x))) for x in range(1,q)}
  row=[]
  for u in Q:
   roots=[t for t in range(q) if F.mul(t,t)==u]
   from_trace=any(t in traces for t in roots)
   discriminant=F.sub(u,F.mul(F.add(1,1),F.add(a,a)))
   assert from_trace==(discriminant in positives)
   row.append(int(from_trace))
  B.append(row)
 G=[[sum(row[i]*row[j] for row in B) for j in range(len(Q))] for i in range(len(Q))]
 eps=F.chi(F.neg(1))
 for i,u in enumerate(Q):
  for j,v in enumerate(Q):
   if i==j:assert G[i][j]==h
   else:
    top=q-3+(1+eps)*F.chi(F.sub(u,v))
    assert top%4==0 and G[i][j]==top//4,(q,u,v,G[i][j],top)
 if eps==-1:
  lambda0=(q*q-1)/8
  lambda1=(q+1)/4
  for i in range(h+1):
   assert sum(G[i])==lambda0
   for j in range(h+1):
    assert abs(G[i][j]-(lambda1*(i==j)+(lambda0-lambda1)/(h+1)))<1e-8
 else:
  lamplus=h*(h+2+sqrt(h*h+4))/4
  lamminus=h*(h+2-sqrt(h*h+4))/4
  assert lamminus>0
  assert all(G[0][j]==h//2 for j in range(1,h+1))
  assert all(sum(G[i][1:])==h*h//2 for i in range(1,h+1))
  generator=next(g for g in H if len({F.power(g,i) for i in range(h)})==h)
  pos={F.power(generator,j):j for j in range(h)}
  for k in range(1,h):
   vec=[0j]+[cmath.exp(2j*pi*k*pos[u]/h) for u in Q[1:]]
   S=sum(vec[1+Q[1:].index(t)]*F.chi(F.sub(1,t)) for t in H)
   eigen=(h+1+S)/2
   assert abs(eigen.imag)<1e-8
   assert eigen.real>(sqrt(q)-1)**2/4-1e-8
   for i in range(len(Q)):
    observed=sum(G[i][j]*vec[j] for j in range(len(Q)))
    assert abs(observed-eigen*vec[i])<1e-7,(q,k,i,observed,eigen*vec[i])
 return (q,len(Q),len(B))

if __name__=='__main__':
 checks=[]
 for p,pol in FIELDS:
  F=Field(p,pol)
  checks.append(check(F))
 print('VERIFY_OK', 'finite_fields=',len(checks),'individual_columns=',sum(c for _,c,_ in checks),'incidence_entries=',sum(c*r for _,c,r in checks),'square_character_spectra=validated')
 print('FIELDS',','.join(str(q) for q,_,_ in checks))
