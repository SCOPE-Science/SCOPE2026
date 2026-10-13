"""Finite-field test of the star evolution algebra subalgebra classification.
Recompute independent RREF subspaces and direct closure, not the classification proof.
Python 3 standard library.
"""
from itertools import combinations, product
from math import comb

class Field:
 def __init__(self,q):
  assert q in (2,3,4,5,7)
  self.q=q;self.p=2 if q in (2,4) else q
 def add(self,a,b): return (a^b) if self.p==2 else (a+b)%self.p
 def neg(self,a):return a if self.p==2 else (-a)%self.p
 def mul(self,a,b):
  if self.q==4:
   v=0
   while b:
    if b&1:v^=a
    b>>=1;a<<=1
    if a&4:a^=7
   return v
  return (a*b)%self.p
 def pow(self,a,n):
  b=1
  while n:
   if n&1:b=self.mul(a,b)
   a=self.mul(a,a);n>>=1
  return b
 def inv(self,a):assert a;return self.pow(a,self.q-2)
 def sm(self,a,b):return self.mul(a,b)
 def dot(self,a,b):
  z=0
  for x,y in zip(a,b):z=self.add(z,self.mul(x,y))
  return z
 def sum(self,a):
  z=0
  for x in a:z=self.add(z,x)
  return z

def rrefs(q,n,r):
 for piv in combinations(range(n),r):
  non=[j for j in range(n) if j not in piv]
  free=[(i,j) for i in range(r) for j in non if j>piv[i]]
  for coeff in product(range(q),repeat=len(free)):
   rows=[[0]*n for _ in piv]
   for i,j in enumerate(piv):rows[i][j]=1
   for (i,j),a in zip(free,coeff):rows[i][j]=a
   yield tuple(map(tuple,rows))

def member(f,rows,z):
 z=list(z)
 for v in rows:
  p=next((i for i,x in enumerate(v) if x),None)
  if p is not None and z[p]:
   a=z[p]
   z=[f.add(x,f.neg(f.mul(a,y))) for x,y in zip(z,v)]
 return all(x==0 for x in z)

def prod_star(f,u,v,m):
 # coordinate 0: hub; remaining m entries: leaves
 a=[0]*(m+1)
 a[0]=f.dot(u[1:],v[1:])
 h=f.mul(u[0],v[0])
 for i in range(1,m+1):a[i]=h
 return a

def iso_counts(f,n,kernel_sum=False):
 out=[]
 for d in range(n+1):
  total=0
  for B in rrefs(f.q,n,d):
   if kernel_sum and any(f.sum(v) for v in B):continue
   if all(f.dot(v,w)==0 for i,v in enumerate(B) for w in B[i:]):total+=1
  out.append(total)
 return out

def compare(q,m):
 f=Field(q)
 assert m%f.p!=0
 actual=[]
 for d in range(m+2):
  n=0
  for B in rrefs(q,m+1,d):
   if all(member(f,B,prod_star(f,v,w,m)) for i,v in enumerate(B) for w in B[i:]):n+=1
  actual.append(n)
 I=iso_counts(f,m)
 J=[]
 # Isotropic r-subspaces of U0 counted by RREF in U with sum zero
 for d in range(m):
  n=0
  for B in rrefs(q,m,d):
   if all(f.sum(v)==0 for v in B) and all(f.dot(v,w)==0 for i,v in enumerate(B) for w in B[i:]):n+=1
  J.append(n)
 c=sum(1 for x in range(q) if f.pow(x,3)==m%f.p)
 # Type I contains Z: subspaces correspond to subspaces of m-1-dimensional quotient.
 def gb(n,k):
  if k<0 or k>n:return 0
  a=1;b=1
  for i in range(k):a*=q**(n-i)-1;b*=q**(k-i)-1
  return a//b
 predict=[(I[d] if d<len(I) else 0)+ (c*J[d-1] if 0<=d-1<len(J) else 0)+gb(m-1,d-2) for d in range(m+2)]
 assert actual==predict,(q,m,actual,predict,I,J,c)
 print('VERIFIED',q,m,actual,'cubic_roots',c)

if __name__=='__main__':
 for q,m in [(2,1),(2,3),(2,5),(3,1),(3,2),(3,4),(4,1),(4,3),(5,1),(5,2),(5,3),(7,1),(7,2)]:
  compare(q,m)
 print('VERIFY_OK')
