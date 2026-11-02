#!/usr/bin/env python3
"""Independent finite checks for exact consecutive-multiple binomial gcd formula."""
from math import comb,gcd

def factor(n):
 f={};d=2
 while d*d<=n:
  if n%d==0:
   a=0
   while n%d==0:n//=d;a+=1
   f[d]=a
  d+=1
 if n>1:f[n]=1
 return f

def kummer(k,t,p):
 a=k;b=k*t; carry=0;count=0
 while a or b or carry:
  carry=(a%p+b%p+carry)//p
  count+=carry
  a//=p;b//=p
 return count

def prediction(n,p,a):
 b=n//p**a;j=0
 while p**(j+1)<=b:j+=1
 return max(0,a-j),j,b

count=0; witness=0; direct=0
for n in range(3,451):
 k=n-1
 for p,a in factor(n).items():
  want,j,b=prediction(n,p,a)
  got=min(kummer(k,q-1,p) for q in range(2,n+1))
  assert got==want,(n,p,want,got)
  count+=1
  if b>1 and j<a:
   ell=((b-1)%(p**j))+1
   q=1+p**a*ell
   assert 2<=q<=n and kummer(k,q-1,p)==want,(n,p,q,want)
   witness+=1
  if b==1:
   assert kummer(k,1,p)==a
 if n<=65:
  g=0
  for q in range(2,n+1):g=gcd(g,comb(q*k,k))
  expected=1
  for p,a in factor(n).items():expected*=p**prediction(n,p,a)[0]
  assert g==expected,(n,g,expected)
  direct+=1
print(f'VERIFY_OK all_kummer_minima={count} explicit_mixed_witnesses={witness} direct_integer_gcds={direct} n_max=450 exact_integer_arithmetic=yes')
