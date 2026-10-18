from fractions import Fraction
from math import isqrt
from functools import lru_cache

def semi(n):
 k=0
 for p in range(2,isqrt(n)+1):
  if n%p==0:
   while n%p==0:n//=p;k+=1
   if n==1:return False
   if k>=2:return False
   if prime(n):return n!=p
   return False
 return False

def prime(n):
 if n<2:return False
 for p in range(2,isqrt(n)+1):
  if n%p==0:return False
 return True

@lru_cache(None)
def semis(N):return [x for x in range(6,N+1) if semi(x)]

# Enumerate divisors of b^2 via trial factor

def divs_square(b):
 fs=[];v=b
 for p in range(2,isqrt(v)+1):
  if v%p==0:
   e=0
   while v%p==0:v//=p;e+=1
   fs.append((p,e))
 if v>1:fs.append((v,1))
 ds=[1]
 for p,e in fs:ds=[d*p**j for d in ds for j in range(2*e+1)]
 return ds

def solve(k):
 nodes=[0]*(k+1); max_bound=[0]*(k+1); maxprime=[0]
 def rec(r,m,last,seq):
  nodes[m]+=1
  if m==2:
   a,b=r.numerator,r.denominator
   for t in divs_square(b):
    if (b+t)%a:continue
    x=(b+t)//a
    if x<=last or not semi(x):continue
    q=b*b//t
    if (b+q)%a:continue
    y=(b+q)//a
    if y<=x or not semi(y):continue
    print('solution!',k,seq,x,y)
    return True
   return False
  bound=m*r.denominator//r.numerator
  max_bound[m]=max(max_bound[m],bound)
  for d in semis(bound):
   if d<=last:continue
   rr=r-Fraction(1,d)
   if rr>0 and rec(rr,m-1,d,seq+[d]):return True
  return False
 print('solve k',k,'result',rec(Fraction(1,2),k,0,[]),'nodes',nodes,'max_bounds',max_bound)
for k in (7,8):solve(k)
