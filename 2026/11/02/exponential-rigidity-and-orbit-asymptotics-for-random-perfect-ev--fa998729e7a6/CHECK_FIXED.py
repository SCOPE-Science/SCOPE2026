#!/usr/bin/env python3
"""Independent fixed-linear-constraint and Burnside consistency checks."""
from itertools import product,permutations
from math import prod,factorial,ceil
from fractions import Fraction

def good(M,q):
 n=len(M); a=[list(r) for r in M]; rank=0
 for j in range(n):
  piv=next((i for i in range(rank,n) if a[i][j]%q),None)
  if piv is None:continue
  a[piv],a[rank]=a[rank],a[piv]
  inv=pow(a[rank][j],-1,q)
  a[rank]=[(x*inv)%q for x in a[rank]]
  for i in range(n):
   if i==rank:continue
   fac=a[i][j]%q
   a[i]=[(x-fac*y)%q for x,y in zip(a[i],a[rank])]
  rank+=1
 return rank==n

def fixed_count_all_matrices(s,t,q):
 n=len(s); seen=set(); exponent=0
 for a in range(n):
  for b in range(n):
   if (a,b) in seen:continue
   x,y=a,b; mul=1
   while (x,y) not in seen:
    seen.add((x,y))
    mul=(mul*t[y]*pow(t[x]*t[x],-1,q))%q
    x,y=s[x],s[y]
   assert (x,y)==(a,b)
   if mul==1:exponent+=1
 return q**exponent

def direct_count_all_matrices(s,t,q):
 n=len(s); count=0
 for flat in product(range(q),repeat=n*n):
  M=[flat[i*n:(i+1)*n] for i in range(n)]
  if all((t[i]*t[i]*M[s[i]][s[j]]-t[j]*M[i][j])%q==0
       for i in range(n) for j in range(n)):
   count+=1
 return count

def run(q,n):
 idt=tuple(range(n)); one=(1,)*n
 maxfix=0
 for s in permutations(range(n)):
  for t in product(range(1,q),repeat=n):
   pred=fixed_count_all_matrices(s,t,q)
   actual=direct_count_all_matrices(s,t,q)
   assert pred==actual,(q,n,s,t,pred,actual)
   if s!=idt:
    moved=sum(i!=s[i] for i in range(n))
    assert pred<=q**(n*n-ceil(moved*(2*n-moved)/2))
   else:
    exotic=[x for x in t if x!=1]
    if exotic:
     m=len(exotic); assert pred<=q**(n*n-m*n//(q-2))
   maxfix=max(maxfix,pred)
 print(f'q={q};n={n};max_all_matrix_fixed_fiber={maxfix};all_linear_constraint_counts_match=yes')

if __name__=='__main__':
 for q,n in [(2,2),(2,3),(3,2),(3,3)]:run(q,n)
 print('VERIFY_OK')
