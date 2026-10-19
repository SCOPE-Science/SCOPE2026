from math import gcd
from collections import Counter

def formula(k,r,u):
 n=1<<k; m=2*n
 A=max(gcd(n,r+u),gcd(n,r-u))
 if r%2 != u%2:return 1
 if r%2:return A+1
 def v2(x):
  if x==0:return 1000
  return (x&-x).bit_length()-1
 t=v2(r)
 if t==v2(u) and 1<=t<k:return A+(1<<t)
 if r==n and u==n:return 3*n
 return A

def matrix(n,r,u,t):
 S=[(0,0),(r,0),(t,1),((t+u)%(2*n),1)]
 elements=[(i,e) for e in (0,1) for i in range(2*n)]
 ids={g:i for i,g in enumerate(elements)}
 M=[[0]*(4*n) for z in elements]
 for col,(a,b) in enumerate(elements):
  for i,e in S:
   j=(i+(-1)**e*a+n*e*b)%(2*n)
   f=(e+b)%2
   M[ids[(j,f)]][col]+=1
 return M

def rank_mod(A,p=1000003):
 A=[row[:] for row in A];n=len(A);m=n;rank=0
 for j in range(m):
  pivot=next((i for i in range(rank,n) if A[i][j]%p),None)
  if pivot is None:continue
  A[rank],A[pivot]=A[pivot],A[rank]
  inv=pow(A[rank][j],-1,p);A[rank][j:]=[(v*inv)%p for v in A[rank][j:]]
  for i in range(rank+1,n):
   if A[i][j]%p:
    x=A[i][j]
    A[i][j:]=[(a-x*b)%p for a,b in zip(A[i][j:],A[rank][j:])]
  rank+=1
 return rank

if __name__=='__main__':
 for k in (2,3,4,5):
  n=1<<k
  c=Counter(formula(k,r,u) for r in range(1,2*n) for u in range(1,2*n))
  expected=(4*k+2)*n*n+(1-2*k)*n
  print('k',k,'n',n,'distrib',sorted(c.items()),'sum',sum(a*b for a,b in c.items()),'expect',expected)
  assert sum(a*b for a,b in c.items())==expected
  assert min(c)==1 and max(c)==3*n and c[3*n]==1
 for k in (2,3):
  n=1<<k;count=0
  for r in range(1,2*n):
   for u in range(1,2*n):
    for t in (0,1,n):
     M=matrix(n,r,u,t)
     got=4*n-rank_mod(M)
     expected=formula(k,r,u)
     if got!=expected:raise AssertionError((k,r,u,t,got,expected))
     count+=1
  print('exact modular rank checks k=',k,'total',count,'pass')
 for k in (4,5):
  n=1<<k;import random
  random.seed(k)
  for test in range(150 if k==4 else 45):
   r=random.randrange(1,2*n);u=random.randrange(1,2*n);t=random.randrange(2*n)
   got=4*n-rank_mod(matrix(n,r,u,t))
   assert got==formula(k,r,u),(k,r,u,t,got,formula(k,r,u))
  print('modular random k',k,'passed')
