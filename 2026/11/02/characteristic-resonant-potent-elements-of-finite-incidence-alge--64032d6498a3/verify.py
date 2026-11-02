#!/usr/bin/env python3
"""Direct small-field tests for potent elements in incidence algebras."""
from itertools import product
from math import comb

def transitive(n,covers):
 R={(i,i) for i in range(n)}|set(covers)
 for k in range(n):
  for i in range(n):
   for j in range(n):
    if (i,k) in R and (k,j) in R:R.add((i,j))
 assert not any(i>j for i,j in R)
 return sorted(R)

def count(p,n,covers):
 P=transitive(n,covers); m=len(P)-n; q=p
 pairs=P; indices={(i,j):k for k,(i,j) in enumerate(pairs)}
 def mult(a,b):
  c=[0]*len(pairs)
  for t,(i,j) in enumerate(pairs):
   c[t]=sum(a[indices[(i,k)]]*b[indices[(k,j)]] for k in range(i,j+1) if (i,k) in indices and (k,j) in indices)%q
  return tuple(c)
 num=0
 for a in product(range(q),repeat=len(pairs)):
  pa=a
  for _ in range(p):pa=mult(pa,a)
  if pa==a:num+=1
 # direct independent finite-sum structural count
 eq=0
 strict=[(i,j) for (i,j) in P if i<j]
 for mask in range(1<<n):
  S={i for i in range(n) if (mask>>i)&1}
  cut=sum((i in S)!=(j in S) for i,j in strict)
  strict_s=[(i,j) for i,j in strict if i in S and j in S]
  cnt=0
  for vals in product(range(q),repeat=len(strict_s)):
   mat=[0]*len(P)
   for (i,j),x in zip(strict_s,vals):mat[indices[(i,j)]]=x
   a=tuple(mat);pa=a
   for _ in range(1,p):pa=mult(pa,a)
   if not any(pa):cnt+=1
  eq+=q**cut*cnt
 assert num==eq,(p,n,covers,num,eq)
 # short-height simplification
 def height(S):
  h=[0]*n
  for i in range(n):
   if i in S:h[i]=1+max([h[j] for j in range(i) if (j,i) in P]+[0])
  return max(h,default=0)
 if height(set(range(n)))<=p:
  predicted=sum(q**(m-sum(i in T and j in T for i,j in strict)) for z in range(1<<n) for T in [set(i for i in range(n) if z>>i&1)])
  assert num==predicted,(num,predicted)
 if covers==[(i,i+1) for i in range(n)] and n<=p+1:
  expected=sum(comb(n,r)*q**(r*(n-r)+r*(r-1)//2) for r in range(n+1))-(q-1)**p*q**(p*(p-1)//2) if n==p+1 else sum(comb(n,r)*q**(r*(n-r)+r*(r-1)//2) for r in range(n+1))
  assert num==expected,(num,expected)
 print(f'PASS p={p} n={n} m={m} total={num} cover={covers}')

if __name__=='__main__':
 for p,n,covers in [(2,2,[(0,1)]),(2,3,[(0,1),(1,2)]),(2,4,[(i,i+1) for i in range(3)]),(3,3,[(i,i+1) for i in range(2)]),(3,4,[(i,i+1) for i in range(3)]),(2,3,[(0,2),(1,2)]),(2,4,[(0,2),(1,2),(2,3)]),(3,4,[(0,2),(1,2),(2,3)]),(2,4,[(0,2),(1,2),(0,3),(1,3)])]:
  count(p,n,covers)
 print('VERIFY_OK')
