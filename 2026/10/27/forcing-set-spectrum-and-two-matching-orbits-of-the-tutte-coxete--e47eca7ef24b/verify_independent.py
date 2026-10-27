"""Independent 30-vertex exact-cover enumeration and direct forcing checks."""
from itertools import combinations
from collections import Counter,deque

D=tuple((1<<a)|(1<<b) for a,b in combinations(range(6),2))
S=set()
for a in range(6):
 for b in range(a+1,6):
  x=(1<<a)|(1<<b)
  others=[u for u in range(6) if not x&(1<<u)]
  for c in others:
   for d in others:
    if c<d:
     y=(1<<c)|(1<<d)
     z=63 ^ x ^ y
     if z.bit_count()==2:
      S.add(tuple(sorted((x,y,z))))
S=tuple(sorted(S,key=lambda ss: tuple(sorted(D.index(e) for e in ss))))
assert len(D)==len(S)==15
N=[[] for _ in range(30)]
for i,d in enumerate(D):
 for j,s in enumerate(S):
  if d in s:
   N[i].append(15+j);N[15+j].append(i)
assert all(len(a)==3 for a in N)
# Ensure this incidence graph really has girth 8, avoiding a wrong graph realization.
girth=30
for source in range(30):
 q=deque([source]);dist=[-1]*30;parent=[-1]*30;dist[source]=0
 while q:
  u=q.popleft()
  for v in N[u]:
   if dist[v]<0:
    dist[v]=dist[u]+1;parent[v]=u;q.append(v)
   elif parent[u]!=v:
    girth=min(girth,dist[u]+dist[v]+1)
assert girth==8
allm=[]
def traverse(unmatched, chosen):
 if not unmatched:
  allm.append(frozenset(chosen));return
 v=min(unmatched)
 for w in N[v]:
  if w in unmatched:
   traverse(unmatched-{v,w},chosen+[(min(v,w),max(v,w))])
traverse(set(range(30)),[])
assert len(allm)==len(set(allm))==288
# Candidate representatives expressed as chosen duad->syntheme partners.
representatives=((0,3,7,9,13,12,10,4,11,14,8,2,5,1,6),
                 (0,3,7,9,14,12,10,4,8,11,13,2,5,1,6))
for j,rep in enumerate(representatives):
 matched=frozenset((i,15+k) for i,k in enumerate(rep))
 assert matched in allm
 sorted_edges=tuple(sorted(matched))
 missing=[sum(1<<i for i,e in enumerate(sorted_edges) if e not in other) for other in allm if other!=matched]
 # chosen mask is forcing exactly if it intersects every missing-edge mask.
 vals=[]
 for k in (4,5,6):
  yes=0
  for choice in combinations(range(15),k):
   mask=sum(1<<i for i in choice)
   if all(mask&msk for msk in missing):yes+=1
  vals.append(yes)
 assert vals==([0,240,1380] if j==0 else [0,240,1355])
 print('REP_%d k4,k5,k6='%j,','.join(map(str,vals)))
print('GRAPH=30 vertices,45 edges,girth8; PERFECT_MATCHINGS=288')
print('INDEPENDENT_VERIFY_OK')
