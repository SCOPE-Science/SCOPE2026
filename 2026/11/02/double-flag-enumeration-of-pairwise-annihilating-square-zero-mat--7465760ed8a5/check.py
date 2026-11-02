"""Direct exhaustive finite-field check of the joint rank--image--kernel formula.
Computational side enumerates every ordered tuple of square-zero matrices and tests all ordered products.
Proof formula side uses double finite-subspace Möbius inversion.
"""
from collections import Counter
from itertools import product
from math import prod

def gauss(n,r,q):
 if r<0 or r>n:return 0
 return prod(q**(n-j)-1 for j in range(r))//prod(q**(r-j)-1 for j in range(r))

def n_rank(a,b,r,q):
 if r<0 or r>min(a,b):return 0
 return gauss(a,r,q)*prod(q**b-q**i for i in range(r))

def formula(n,q,ranks,t,k):
 if not(0<=t<=k<=n):return 0
 d=n-k
 count=0
 for j in range(t+1):
  x=gauss(t,j,q)*(-1)**(t-j)*q**((t-j)*(t-j-1)//2)
  for h in range(d+1):
   v=x*gauss(d,h,q)*(-1)**h*q**(h*(h-1)//2)
   for r in ranks:v*=n_rank(j,d-h,r,q)
   count+=v
 return gauss(n,k,q)*gauss(k,t,q)*count

def mul(A,B,n,q):
 return tuple(sum(A[i*n+s]*B[s*n+j] for s in range(n))%q for i in range(n) for j in range(n))

def rank_rect(M,rows,cols,q):
 A=[list(M[i*cols:(i+1)*cols]) for i in range(rows)]; r=0
 for j in range(cols):
  a=next((i for i in range(r,rows) if A[i][j]%q),None)
  if a is None:continue
  A[r],A[a]=A[a],A[r]
  inv=pow(A[r][j],-1,q)
  A[r]=[(v*inv)%q for v in A[r]]
  for i in range(r+1,rows):
   c=A[i][j]
   if c:A[i]=[(v-c*w)%q for v,w in zip(A[i],A[r])]
  r+=1
  if r==rows:break
 return r

def inspect(n,q,m):
 zero=(0,)*(n*n)
 square=[(A,rank_rect(A,n,n,q)) for A in product(range(q),repeat=n*n) if mul(A,A,n,q)==zero]
 observed=Counter()
 for tup in product(square,repeat=m):
  mats=[A for A,_ in tup]
  if any(mul(mats[i],mats[j],n,q)!=zero for i in range(m) for j in range(m)):continue
  rs=tuple(r for _,r in tup)
  horiz=tuple(mats[a][i*n+j] for i in range(n) for a in range(m) for j in range(n))
  vert=tuple(mats[a][i*n+j] for a in range(m) for i in range(n) for j in range(n))
  t=rank_rect(horiz,n,m*n,q)
  k=n-rank_rect(vert,n*m,n,q)
  observed[(rs,t,k)]+=1
 for rs in product(range(n//2+1),repeat=m):
  for t in range(n+1):
   for k in range(n+1):
    actual=observed.get((rs,t,k),0); expected=formula(n,q,rs,t,k)
    assert actual==expected,(n,q,m,rs,t,k,actual,expected)
 print('PASS',n,q,m,'tuple_count',sum(observed.values()),'nonzero_joint_strata',len(observed))
 return observed

if __name__=='__main__':
 for n,q,m in [(2,2,2),(2,3,3),(3,2,2),(3,2,3),(3,3,2),(4,2,2)]:inspect(n,q,m)
 print('DOUBLE_FLAG_ZERO_PRODUCT_RANK_CENSUS_OK 6_FULL_EQUATION_ENUMERATIONS')
