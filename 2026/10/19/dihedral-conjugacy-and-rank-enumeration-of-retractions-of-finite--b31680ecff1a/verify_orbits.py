from itertools import product
from collections import Counter

def walks(k,L):
 def rec(p,t):
  if t==L:
   if p[-1]==0:yield p
   return
  for j in (p[-1]-1,p[-1]+1):
   if 0<=j<=k:yield from rec(p+[j],t+1)
 return rec([k],0)

def fixed_formula(k,L):
 N=k+1
 if L%2==0:
  if k%2:return 0
  target={k//2}
  H=L//2
 else:
  if k%2==0:return 0
  target={(k-1)//2,(k+1)//2}
  H=L//2
 dp=[0]*N;dp[k]=1
 for _ in range(H):
  nxt=[0]*N
  for j,a in enumerate(dp):
   if j:nxt[j-1]+=a
   if j<k:nxt[j+1]+=a
  dp=nxt
 return sum(dp[j] for j in target)

def all_id(n):
 items=[]
 for a in range(n):
  for signs in product((-1,1), repeat=n):
   seq=[a];cur=a
   for t in signs:
    cur=(cur+t)%n;seq.append(cur)
   if cur!=a:continue
   f=tuple(seq[:-1])
   if all(f[f[x]]==f[x] for x in range(n)):
    items.append(f)
 return items

def conj_perm(f, g):
 n=len(f)
 gin=[0]*n
 for i,y in enumerate(g):gin[y]=i
 return tuple(g[f[gin[x]]] for x in range(n))

def orbit_histo(n):
 items=all_id(n)
 left=set(items)
 hist=Counter()
 perms=[tuple((a+s*i)%n for i in range(n)) for a in range(n) for s in (-1,1)]
 while left:
  v=next(iter(left))
  orbit={conj_perm(v,p) for p in perms}
  assert orbit <= left | (set(items)-left)
  left-=orbit
  hist[len(set(v))]+=1
 return dict(hist)

for n in range(3,16):
 target={n:1}
 if n%2==0:
  m=n//2
  for k in range(1,m+1):
   L=n-k
   ww=list(walks(k,L))
   sy=sum(int(p==[k-v for v in reversed(p)]) for p in ww)
   f=fixed_formula(k,L)
   assert sy==f,(n,k,sy,f)
   assert (len(ww)+sy)%2==0
   target[k+1]=(len(ww)+sy)//2
 got=orbit_histo(n)
 print(n, got, target)
 assert got==target,(n,got,target)
print('SYMMETRY_OK')
