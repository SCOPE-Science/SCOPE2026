"""Independent finite-field enumeration of commuting symmetric rank-one nilpotents.
Supports prime fields of orders 2, 3, 5 and F4 via x^2+x+1.
No external dependencies. Run: python verify.py.
"""
from itertools import product
from math import prod

def gauss(n,k,q):
 if k<0 or k>n:return 0
 return prod(q**(n-j)-1 for j in range(k))//prod(q**(k-j)-1 for j in range(k))

def count_S(w,r,q):
 if r<0 or r>w:return 0
 return gauss(w,r,q)*prod(q**(w-j)+1 for j in range(r))

def I(n,q,r):
 if r==0:return 1
 if q%2==0:
  w=(n-1)//2
  if n%2:return count_S(w,r,q)
  return q**r*count_S(w,r,q)+count_S(w,r-1,q)
 if n%2: w=n//2;e=1
 else:
  m=n//2
  split=(m%2==0 or q%4==1)
  w=m if split else m-1
  e=0 if split else 2
 if r>w:return 0
 return gauss(w,r,q)*prod(q**(w+e-1-j)+1 for j in range(r))

def formula(n,q,t):
 return sum(I(n,q,r)*prod(q**t-q**j for j in range(r)) for r in range(n//2+1))

class F:
 def __init__(self,q):self.q=q
 def plus(self,a,b):return a^b if self.q==4 else (a+b)%self.q
 def mul(self,a,b):
  if self.q!=4:return a*b%self.q
  z=0
  for i in range(2):
   if (a>>i)&1:
    for j in range(2):
     if (b>>j)&1:z ^= 1 << (i+j)
  if z&8:z^=0b1100
  if z&4:z^=0b111
  return z
 def dot(self,u,v):
  r=0
  for a,b in zip(u,v):r=self.plus(r,self.mul(a,b))
  return r
 def mat(self,u,c):
  return tuple(self.mul(c,self.mul(a,b)) for a in u for b in u)
 def commute(self,A,B,n):
  for i in range(n):
   for j in range(n):
    x=y=0
    for k in range(n):
     x=self.plus(x,self.mul(A[n*i+k],B[n*k+j]))
     y=self.plus(y,self.mul(B[n*i+k],A[n*k+j]))
    if x!=y:return False
  return True

def experiment(n,q,t):
 f=F(q); mats={(0,)*(n*n)}
 for u in product(range(q),repeat=n):
  if f.dot(u,u):continue
  if all(x==0 for x in u):continue
  for c in range(1,q): mats.add(f.mat(u,c))
 mats=sorted(mats)
 pairs={(i,j) for i,A in enumerate(mats) for j,B in enumerate(mats) if f.commute(A,B,n)}
 pred=sum(1 for arr in product(range(len(mats)),repeat=t) if all((arr[i],arr[j]) in pairs for i in range(t) for j in range(i+1,t)))
 exp=formula(n,q,t)
 print((n,q,t),'elements',len(mats),'count',pred,'formula',exp,'I',[I(n,q,r) for r in range(n//2+1)])
 assert pred==exp

for args in [(2,2,3),(2,3,3),(2,5,2),(3,2,3),(3,3,3),(4,2,3),(4,3,2),(4,4,2),(4,5,2),(5,2,3),(6,2,2)]:experiment(*args)
print('VERIFY_OK_SYMMETRIC_RANKONE',11,'cases')
