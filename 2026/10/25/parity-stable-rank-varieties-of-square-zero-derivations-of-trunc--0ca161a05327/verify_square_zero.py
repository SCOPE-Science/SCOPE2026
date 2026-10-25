from itertools import product
from collections import Counter

def gf_mul(a,b,q):
 if q==2:return a*b
 if q==4:
  z=0
  while b:
   if b&1:z^=a
   b>>=1
   a<<=1
   if a&4:a^=7
  return z
 raise ValueError

def rk(mat,q):
 M=[x[:] for x in mat]; m=len(M);n=len(M[0]); i=0
 for j in range(n):
  pivot=next((z for z in range(i,m) if M[z][j]),None)
  if pivot is None:continue
  M[i],M[pivot]=M[pivot],M[i]
  if q==4 and M[i][j]!=1:
   inv={1:1,2:3,3:2}[M[i][j]]
   M[i]=[gf_mul(z,inv,q) for z in M[i]]
  for z in range(i+1,m):
   if M[z][j]:
    a=M[z][j]
    M[z]=[x^gf_mul(a,y,q) for x,y in zip(M[z],M[i])]
  i+=1
  if i==m:break
 return i

def brute(q,n):
 cnt=Counter()
 for aa in product(range(q),repeat=n):
  if n%2 and aa[0]:continue
  # differentiate and multiply
  der=[aa[j+1] if (j+1)&1 else 0 for j in range(n-1)]+[0]
  z=[0]*n
  for i,x in enumerate(aa):
   if x:
    for j,y in enumerate(der[:n-i]):
     if y:z[i+j]^=gf_mul(x,y,q)
  if any(z):continue
  mat=[[0]*n for _ in range(n)]
  for j in range(1,n,2):
   for i,x in enumerate(aa[:n-j+1]):mat[i+j-1][j]=x
  cnt[rk(mat,q)]+=1
 return dict(sorted(cnt.items()))

def formula(q,n):
 m=n//2;h=m//2
 return {0:1,**{r:((q*q-1)*q**(2*r-2) if r<=h else (q-1)*q**(m-1)) for r in range(1,m+1)}}
for q,maxn in [(2,12),(4,7)]:
 for n in range(2,maxn+1):
  a=brute(q,n);b=formula(q,n)
  print(q,n,a, 'PASS' if a==b else f'FAIL {b}')
  assert a==b
print('SQUARE_ZERO_DERIVATION_RANK_OK')
