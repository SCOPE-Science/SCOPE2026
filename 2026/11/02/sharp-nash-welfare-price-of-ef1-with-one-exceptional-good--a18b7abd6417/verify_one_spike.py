from fractions import Fraction
from itertools import product
from math import floor,ceil

def compositions(total,n):
 if n==1:
  yield (total,);return
 for k in range(total+1):
  for rest in compositions(total-k,n-1):yield (k,)+rest

def balanced(r,k):
 q,t=divmod(r,k)
 return q**(k-t)*(q+1)**t

def true_ef1(n,H,alloc):
 # heavy is held by agent0, others get only light items
 u=(H+alloc[0],)+alloc[1:]
 for i in range(n):
  for j in range(n):
   if i==j:continue
   if j==0:
    best=alloc[0] if H>=1 else H+alloc[0]-1
   else:
    best=max(0,alloc[j]-1)
   if u[i]<best: return False
 return True

k=0
for n in range(2,6):
 for L in range(n-1,12):
  for H in (Fraction(1),Fraction(3,2),Fraction(2),Fraction(7,2),Fraction(10),Fraction(1000)):
   vals=[((H+a[0])* __import__('math').prod(a[1:]),a) for a in compositions(L,n) if true_ef1(n,H,a)]
   got_min=min(x[0] for x in vals)
   got_max=max((H+a[0])*__import__('math').prod(a[1:]) for a in compositions(L,n))
   sf=min(s for _,a in vals for s in [a[0]])
   st=max(s for _,a in vals for s in [a[0]])
   f=lambda s: (H+s)*balanced(L-s,n-1)
   lower=max(0,ceil(Fraction(L-(n-1)*(floor(H)+1),n)))
   upper=L//n
   assert (sf,st)==(lower,upper),(n,L,H,sf,st,lower,upper)
   assert got_min==min(f(lower),f(upper)),(n,L,H,got_min,min(f(lower),f(upper)))
   assert got_max==max(f(s) for s in range(L+1)),(n,L,H,got_max)
   universal=Fraction(n-1,n)**(n-1)
   assert got_min/got_max>=universal,(n,L,H,got_min,got_max,universal)
   k+=1
print('VERIFY_OK cases',k,'n=2..5 L=n-1..11 H=1,1.5,2,3.5,10,1000; independent exhaustive count-composition enumeration')
