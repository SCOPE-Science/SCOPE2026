from itertools import combinations
from math import comb

def fort(m,n, ww):
  W=set(ww)
  adj=lambda idx: {idx//n*n+j for j in range(n) if idx//n*n+j!=idx}|{i*n+idx%n for i in range(m) if i*n+idx%n!=idx}
  return bool(W) and all(len(adj(t)&W)!=1 for t in range(m*n) if t not in W)

def formula(m,n):
 m,n=sorted((m,n))
 if m==2 and n==2:return 2,2
 if (m,n)==(2,3):return 3,6
 if (m,n)==(3,3):return 3,6
 if m==2 and n==4:return 4,44
 if m==2 and n>=5:return 4,comb(n,2)**2
 if (m,n)==(3,4):return 4,54
 if (m,n)==(4,4):return 4,60
 return 4,comb(m,2)*comb(n,2)

c=0
for m in range(2,8):
 for n in range(m,8):
  if m*n > 48: continue
  mn=m*n
  out=[]
  for k in range(1,5):
   out=[W for W in combinations(range(mn),k) if fort(m,n,W)]
   if out:break
  expect=formula(m,n)
  assert (k,len(out))==expect,(m,n,k,len(out),expect)
  c+=sum(comb(mn,k) for k in range(1,k+1))
  print(m,n,k,len(out),'OK')
print('FORT_COUNTS_OK, subsets',c)

def fails(m,n,W):
 N=m*n
 blue=set(range(N))-set(W)
 while True:
  nxt=set()
  for x in blue:
   r=x//n; col=x%n
   whites=[y for y in W if (y//n==r or y%n==col)]
   if len(whites)==1:nxt.add(whites[0])
  if not nxt:return bool(W)
  blue|=nxt; W=set(W)-nxt
  if not W:return False

for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]:
 k,N=formula(m,n)
 total=0
 for W in combinations(range(m*n),k):
  f=fails(m,n,set(W))
  assert f==fort(m,n,W),(m,n,W,f)
  total+=f
 assert total==N
 print('ZERO_FORCING_OK',m,n,N)
