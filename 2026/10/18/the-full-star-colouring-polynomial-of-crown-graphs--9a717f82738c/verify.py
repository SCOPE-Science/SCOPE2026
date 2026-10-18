from collections import Counter
from math import comb,factorial
from itertools import permutations

def S(n,k):
 a=[[0]*(n+2) for _ in range(n+2)]
 a[0][0]=1
 for i in range(1,n+1):
  for j in range(1,i+1):a[i][j]=j*a[i-1][j]+a[i-1][j-1]
 return a[n][k]

def formula(n):
 out=Counter()
 for r in range(n+1):
  if r==0:out[n]+=1;continue
  for b in range(1,r+1):out[n+b]+=2*comb(n,r)*S(r,b)
  out[n+r]-=comb(n,r)
  if r>=2:out[n+r-2]+=comb(n,r)*comb(r,2)
 return {k:v for k,v in sorted(out.items()) if v}

def enumerate_graph(n):
 N=2*n
 E=set()
 for i in range(n):
  for j in range(n):
   if i!=j:E.add((i,n+j))
 neigh=[[False]*N for _ in range(N)]
 for u,v in E:neigh[u][v]=neigh[v][u]=True
 P4=[]
 for a in range(N):
  for b in range(N):
   if not neigh[a][b]:continue
   for c in range(N):
    if c in (a,b) or not neigh[b][c]:continue
    for d in range(N):
     if d in (a,b,c) or not neigh[c][d]:continue
     if a<d:P4.append((a,b,c,d))
 # full independent direct verification of all star coloring partitions, no theorem assumption
 classes=[0]*N; counts=Counter(); checked=0
 def rec(i,k):
  nonlocal checked
  if i==N:
   checked+=1
   for a,b,c,d in P4:
    if classes[a]==classes[c] and classes[b]==classes[d]:return
   counts[k]+=1;return
  for color in range(k+1):
   if color==k and k==N:continue
   if any(neigh[i][j] and classes[j]==color for j in range(i)):continue
   classes[i]=color
   rec(i+1,k+(color==k))
 classes[0]=0
 rec(1,1)
 return dict(counts),checked,len(P4)

if __name__=='__main__':
 for n in range(2,8):
  direct,c,p=enumerate_graph(n);expected=formula(n)
  assert direct==expected,(n,direct,expected)
  assert direct[n]==1+comb(n,2)
  print('n',n,'checked_proper_partitions',c,'P4_paths',p,'distribution',direct)
 for n in range(3,51):
  f=formula(n)
  assert set(f)==set(range(n,2*n+1))
  assert f[n]==1+comb(n,2) and f[2*n]==1
  for j in range(n+1):
   assert f[n+j]==2*S(n+1,j+1)-comb(n,j)+(comb(n,2)*comb(n-2,j) if j<=n-2 else 0)
 print('VERIFICATION_OK star_crown exhaustive_n=2..7 direct_checks=1189120 identity_n=3..50')
