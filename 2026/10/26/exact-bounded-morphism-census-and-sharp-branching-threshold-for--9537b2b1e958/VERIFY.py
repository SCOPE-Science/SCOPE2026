from itertools import product
from math import comb, prod

def count_by_dp(parents,m):
 n=len(parents);children=[[] for _ in range(n)]
 for i in range(1,n):children[parents[i]].append(i)
 A=[0]*n; B=[0]*n
 for u in range(n-1,-1,-1):
  C=children[u]
  B[u]=0 if not C else prod(1+B[c] for c in C)
  A[u]=prod(1+m*B[c]+A[c] for c in C)+sum((-1)**j*comb(m,j)*prod(1+(m-j)*B[c] for c in C) for j in range(1,m+1))
 return A[0],B[0],A,B,children

def brute(parents,m):
 n=len(parents); children=[[] for _ in range(n)]
 for i in range(1,n):children[parents[i]].append(i)
 des=[{i} for i in range(n)]
 for i in range(n-1,-1,-1):
  for c in children[i]:des[i]|=des[c]
 C=0; D=0
 for f in product(range(m+2),repeat=n):
  if f[0]!=0:continue
  if any((f[parents[i]]==m+1 and f[i]!=m+1) or (1<=f[parents[i]]<=m and f[i]!=f[parents[i]] and f[i]!=m+1) for i in range(1,n)):continue
  if any(any(k not in {f[v] for v in des[u]} for k in (range(1,m+2) if f[u]==0 else ([m+1] if f[u]<=m else []))) for u in range(n)) :continue
  C+=1
 return C

def surjection_part(n, k):
 # Stirling number of the second kind, independent recurrence.
 memo=[[0]*(k+1) for _ in range(n+1)]
 memo[0][0]=1
 for i in range(1,n+1):
  for j in range(1,k+1):
   memo[i][j]=j*memo[i-1][j]+memo[i-1][j-1]
 return memo[n][k]

if __name__=='__main__':
 checks=0
 for n in range(1,9):
  for j,tail in enumerate(product(*(range(i) for i in range(1,n)))):
   if n>=7 and j%max(1, (n-1)//2+1):continue
   parents=(-1,)+tail
   for m in (2,3):
    if n>=8 and m==3:continue
    d=count_by_dp(parents,m)[0]
    b=brute(parents,m)
    assert d==b,(parents,m,d,b)
    children=count_by_dp(parents,m)[4]
    threshold=any(sum(bool(children[c]) for c in children[v])>=m for v in range(n))
    assert (d>0)==threshold,(parents,m,d,threshold)
    checks+=1
 for d in range(1,9):
  for m in range(2,7):
   b0,a0=0,0
   b1=1
   a2=(1+m*b1)**d+sum((-1)**j*comb(m,j)*(1+(m-j)*b1)**d for j in range(1,m+1))
   exp_a2=sum(comb(d,s)*__import__('math').factorial(m)*surjection_part(s,m) for s in range(m,d+1))
   assert a2==exp_a2 and (a2>0)==(d>=m)
 print('ALL_TESTS_PASS',checks,'REGULAR_CASES_PASS',8*5)
