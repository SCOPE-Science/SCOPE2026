#!/usr/bin/env python3
"""Exhaustive algebra multiplication and stabilizer census over F2/F3."""
from itertools import product,permutations
from fractions import Fraction
from math import factorial,prod,comb,ceil

def invertible(A,p):
 n=len(A); a=[list(row) for row in A]; r=0
 for j in range(n):
  piv=next((i for i in range(r,n) if a[i][j]%p!=0),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r]
  inv=pow(a[r][j],-1,p)
  a[r]=[(x*inv)%p for x in a[r]]
  for i in range(r+1,n):
   k=a[i][j]
   a[i]=[(v-k*w)%p for v,w in zip(a[i],a[r])]
  r+=1
 return r==n

def symmetries(A,p):
 n=len(A); ans=[]
 for sigma in permutations(range(n)):
  for t in product(range(1,p),repeat=n):
   # Compare the products for each basis square directly.
   # phi(e_i^2) vs phi(e_i)^2, in each coordinate.
   valid=True
   for i in range(n):
    lhs=[0]*n
    for j in range(n):lhs[sigma[j]]=A[i][j]*t[j]%p
    rhs=[t[i]*t[i]*x%p for x in A[sigma[i]]]
    if lhs!=rhs:valid=False;break
   if valid:ans.append((sigma,t))
 return ans

def err_bound(n,q):
 from math import floor
 delta=Fraction(0)
 if q>2:
  # Replace real exponent n/(q-2) by floor, thus a slightly looser rational bound.
  b=Fraction(n*(q-2),q**(n//(q-2)))
  delta+=sum((b**s for s in range(1,n+1)),Fraction(0))
 delta+=sum(Fraction((q-1)**n*n**s,q**((2*n*s-s*s+1)//2)) for s in range(2,n+1))
 return delta

def run(q,n):
 total=0; n_nontriv=0; sum_aut=0; by_size={}
 for seq in product(range(q),repeat=n*n):
  A=[seq[i*n:(i+1)*n] for i in range(n)]
  if not invertible(A,q):continue
  total+=1
  auts=symmetries(A,q)
  n_aut=len(auts)
  assert n_aut>=1
  sum_aut+=n_aut
  if n_aut>1:n_nontriv+=1
  by_size[n_aut]=by_size.get(n_aut,0)+1
 assert total==prod(q**n-q**j for j in range(n))
 Gsize=factorial(n)*(q-1)**n
 assert sum_aut%Gsize==0
 num_isom=sum_aut//Gsize
 p_inv=Fraction(total,q**(n*n))
 error=Fraction(sum_aut-total,total)
 assert error<=err_bound(n,q)/p_inv
 assert Fraction(n_nontriv,total)<=error
 print(f'q={q};n={n};GL={total};nontriv={n_nontriv};sum_aut={sum_aut};orbits={num_isom};orbit_ratio={Fraction(sum_aut,total)};distribution={by_size}')

if __name__=='__main__':
 for q,n in [(2,2),(2,3),(3,2),(3,3)]:run(q,n)
 print('VERIFY_OK')
