from fractions import Fraction as F
from math import comb
for n in range(2,7):
 edges=[(i,j) for i in range(n) for j in range(i+1,n)]
 M=1<<len(edges)
 B=[F(comb(n-1,k),2**(n-1)) for k in range(n)]
 mats=[[F(0) for k in range(n)] for _ in range(n)]
 H=[F(0) for k in range(n)]
 for mask in range(M):
  deg=[0]*n
  for h,(i,j) in enumerate(edges):
   if mask>>h&1: deg[i]+=1
   else: deg[j]+=1
  counts=[deg.count(k) for k in range(n)]
  for k in range(n):
   H[k]+=F(counts[k],M)
   for l in range(n): mats[k][l]+=F(counts[k]*counts[l],M)
 for k in range(n):
  assert H[k]==n*B[k]
  for l in range(n):
   d=lambda t:F(comb(n-2,t-1) if 0<=t-1<=n-2 else 0,2**(n-2))-F(comb(n-2,t) if 0<=t<=n-2 else 0,2**(n-2))
   expected=n*(B[k]*(k==l)-B[k]*B[l])-F(n*(n-1),4)*d(k)*d(l)
   assert mats[k][l]-H[k]*H[l]==expected,(n,k,l)
 Q=sum((mats[k][k]-H[k]*H[k])/(n*B[k]) for k in range(n))
 assert Q==n-2,(n,Q)
 print(n,'checked',M,'tournaments',n*n,'cov entries','Pearson expectation',Q)
print('VERIFY_OK')
