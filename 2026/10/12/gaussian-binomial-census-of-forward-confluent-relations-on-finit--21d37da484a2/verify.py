#!/usr/bin/env python3
from itertools import combinations_with_replacement
checks=0
def ok(c,m='assertion failed'):
 global checks; checks+=1
 if not c: raise AssertionError(m)
def bit(mask,n,i,j): return (mask>>(i*n+j))&1
def fc(mask,n):
 for x in range(n):
  for z in range(x+1):
   for y in range(n):
    if bit(mask,n,z,y) and not any(bit(mask,n,x,t) and t>=y for t in range(n)): return False
 return True
def char(mask,n):
 seen=False; prev=-1
 for i in range(n):
  row=[j for j in range(n) if bit(mask,n,i,j)]
  if not row:
   if seen: return False
  else:
   seen=True; m=max(row)
   if m<prev: return False
   prev=m
 return True
def qb(N,K,q=2):
 if K<0 or K>N:return 0
 dp=[[0]*(K+1) for _ in range(N+1)]
 for n in range(N+1):
  dp[n][0]=1
  for k in range(1,min(n,K)+1): dp[n][k]=dp[n-1][k]+q**(n-k)*dp[n-1][k-1]
 return dp[N][K]
def formula(n): return 1+sum(qb(n+r-1,r,2) for r in range(1,n+1))
expected=[None,2,11,198,13377]
for n in range(1,5):
 c=0
 for mask in range(1<<(n*n)):
  a=fc(mask,n); b=char(mask,n); ok(a==b,f'characterization n={n} mask={mask}'); c+=a
 ok(c==formula(n)); ok(c==expected[n])
for n in range(1,11):
 structured=1
 for r in range(1,n+1):
  subtotal=sum(2**sum(ms) for ms in combinations_with_replacement(range(n),r))
  ok(subtotal==qb(n+r-1,r,2),f'Gaussian n={n} r={r}')
  structured+=subtotal
 ok(structured==formula(n))
for N in range(1,31):
 for K in range(1,N):
  a=qb(N,K,2)
  ok(a==qb(N-1,K,2)+2**(N-K)*qb(N-1,K-1,2))
  ok(a==2**K*qb(N-1,K,2)+qb(N-1,K-1,2))
vals=[formula(n) for n in range(1,9)]
ok(vals==[2,11,198,13377,3523028,3661468103,15111867969754,248548812768592621])
print(f'VERIFY_OK {checks} exact assertions; exhaustive all relations through n=4')
