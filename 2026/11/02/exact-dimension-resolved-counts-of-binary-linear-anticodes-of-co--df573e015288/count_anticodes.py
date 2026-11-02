#!/usr/bin/env python3
"""Exact dimension-resolved binary linear anticodes at codiameter 2.
An RREF enumeration independently checks the character-sum / Moebius formula.
"""
from itertools import combinations,product
from math import prod

def gaussian(n,k):
 if k<0 or k>n:return 0
 # Exact Gaussian quotient of numerator and denominator products.
 return prod(2**(n-i)-1 for i in range(k))//prod(2**(k-i)-1 for i in range(k))

def gl2(r):return prod((1<<r)-(1<<i) for i in range(r))

def f(n,j):
 m=(1<<j)-1
 x=m**n-(m if n&1 else 1)
 assert x%(1<<j)==0
 return x//(1<<j)

def theoretical(n,r):
 if r==0:return 0
 s=0
 for j in range(1,r+1):
  k=r-j
  s+=gaussian(r-1,j-1)*((-1)**k)*(1<<(k*(k-1)//2))*f(n,j)
 out=s*((1<<r)-1)
 assert out%gl2(r)==0,(n,r,out,gl2(r))
 return out//gl2(r)

def enumerated(n,r):
 # Each RREF matrix is unique r-dimensional dual subspace, representing a code C.
 found=0
 for pivots in combinations(range(n),r):
  free=[(i,j) for i in range(r) for j in range(pivots[i]+1,n) if j not in pivots]
  for z in range(1<<len(free)):
   rows=[1<<p for p in pivots]
   for k,(i,j) in enumerate(free):
    if(z>>k)&1:rows[i]^=1<<j
   s=sum(((row.bit_count()&1)<<i) for i,row in enumerate(rows))
   if not s:continue
   if any(sum((((row>>j)&1)<<i) for i,row in enumerate(rows))==s for j in range(n)): continue
   found+=1
  
 return found

if __name__=='__main__':
 for n in range(2,9):
  vals=[]
  for r in range(1,n+1):
   t=theoretical(n,r)
   b=enumerated(n,r)
   assert t==b,(n,r,t,b)
   vals.append(t)
  print('n',n,'r=1..n',','.join(map(str,vals)))
 for n in range(2,15):
  print('n',n,'codim2',theoretical(n,2),'codim3',theoretical(n,3))
 print('ALL CHECKS PASS')
