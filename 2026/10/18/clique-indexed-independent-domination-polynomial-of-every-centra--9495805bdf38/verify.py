from collections import Counter
from itertools import combinations

def formula(n,E):
 edges=set(tuple(sorted(e)) for e in E)
 out=Counter()
 for amask in range(1<<n):
  A={i for i in range(n) if amask>>i&1}
  if any((i,j) not in edges for i in A for j in A if i<j):continue
  if any({v for v in range(n) if tuple(sorted((u,v))) in edges and u!=v}==A for u in range(n) if u not in A):continue
  out[len(A)+sum(u not in A and v not in A for u,v in edges)]+=1
 return out

def brute(n,E):
 E=[tuple(sorted(e)) for e in E]
 N=n+len(E)
 adj=[0]*N
 for j,(u,v) in enumerate(E):
  for x in (u,v):
   adj[x]|=1<<(n+j);adj[n+j]|=1<<x
 EE=set(E)
 for u in range(n):
  for v in range(u+1,n):
   if (u,v) not in EE:adj[u]|=1<<v;adj[v]|=1<<u
 out=Counter()
 for mask in range(1<<N):
  if any((adj[u]&mask) for u in range(N) if mask>>u&1):continue
  if any(not(adj[u]&mask) for u in range(N) if not (mask>>u&1)):continue
  out[mask.bit_count()]+=1
 return out
cases=0
for n in range(1,6):
 e=list(combinations(range(n),2))
 for bitmap in range(1<<len(e)):
  E=[e[k] for k in range(len(e)) if bitmap>>k&1]
  if n==5 and len(E)>7:continue
  actual=brute(n,E);pred=formula(n,E)
  assert actual==pred,(n,E,actual,pred)
  cases+=1
print('ALL_OK cases',cases)
