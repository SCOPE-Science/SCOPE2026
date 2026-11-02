"""Exact template construction and exchange table verification for circular ladders.

Usage: python verify_templates.py
Checks every template and possible single exchange for 6 <= n <= 38.
The infinite theorem is proved separately by the structural argument.
"""
from collections import Counter,defaultdict,deque

def B(n,y,d,s):
 S=set()
 for j in range(1,n):
  col=(y+j)%n
  if j==d:S.update((col,col+n))
  elif j<d:
   r=s if d!=1 else None
   if r is not None:S.add(col+n*r)
  elif j>d:
   r=1-s if 1<d<n-1 else s
   S.add(col+n*r)
 return frozenset(S)

def C(n,y,s):
 S={(y-1)%n,(y+2)%n,(y-1)%n+n,(y+2)%n+n}
 for j in range(3,n-1):S.add((y+j)%n+n*s)
 return frozenset(S)

def A(n,s):return frozenset(range(n*s,n*(s+1)))

def families(n):
 D={}
 for s in range(2):D[A(n,s)]=('A',s)
 for y in range(n):
  for d in range(1,n):
   for s in range(2):
    z=B(n,y,d,s)
    assert len(z)==n,(n,y,d,s,z)
    if z in D:raise Exception(('B duplicate',n,y,d,s,D[z]))
    D[z]=('B',y,d,s)
 for y in range(n):
  for s in range(2):
   z=C(n,y,s)
   if z in D:raise Exception(('C duplicate',n,y,s,D[z]))
   D[z]=('C',y,s)
 return D

def adj(D,n):
 N={k:[] for k in D}
 for s in D:
  for u in s:
   for v in range(2*n):
    if v in s:continue
    t=frozenset((s-{u})|{v})
    if t in D:N[s].append((t,u,v))
  assert len({a for a,b,c in N[s]})==len(N[s])
 return N
def expected(n,t):
 if t[0]=='A':
  s=t[1]
  return {('B',y,d,s) for y in range(n) for d in (1,n-1)}
 if t[0]=='C':
  _,y,s=t
  return {('B',y,n-1,s),('B',(y+1)%n,n-2,s),('B',(y+1)%n,1,s),('B',y,2,1-s)}
 _,y,d,s=t
 z=lambda off,d,s:('B',(y+off)%n,d,s)
 c=lambda off,s:('C',(y+off)%n,s)
 if d==1:
  return {('A',s),z(0,2,1-s),z(2,n-1,s),z(-1,2,1-s),c(-1,s),z(0,n-1,s)}
 if d==n-1:
  return {('A',s),z(1,n-2,s),c(0,s),z(-2,1,s),z(0,n-2,s),z(0,1,s)}
 if d==2:
  return {c(0,1-s),z(1,1,1-s),z(0,1,1-s),z(0,3,s),z(-1,3,s)}
 if d==n-2:
  return {z(1,n-3,s),z(0,n-3,s),z(0,n-1,s),z(-1,n-1,s),c(-1,s)}
 return {z(1,d-1,s),z(0,d-1,s),z(0,d+1,s),z(-1,d+1,s)}

for n in range(6,39):
 D=families(n);N=adj(D,n)
 for s,tag in D.items():
  actual={D[t] for t,u,v in N[s]}
  expect=expected(n,tag)
  assert actual==expect,(n,tag,'unexpected',actual-expect,'missing',expect-actual)
 for k,ss in D.items():
  for t,u,v in N[k]:assert any(w==k for w,a,b in N[t])
 degrees=Counter(map(len,N.values()))
 assert len(D)==2*n*n+2
 assert degrees==Counter({2*n:2,6:4*n,5:4*n,4:2*n*(n-4)})
 assert sum(map(len,N.values()))//2==4*n*(n+2)
 start=next(iter(D));vis={start};queue=[start]
 for s in queue:
  for t,u,v in N[s]:
   if t not in vis:vis.add(t);queue.append(t)
 assert len(vis)==len(D)
 if n in [6,7,8,12,24,38]: print(n,len(D),sum(map(len,N.values()))//2, degrees,flush=True)
print('ALL_ADJACENCY_RULES_AND_CONNECTIVITY_PASS')
