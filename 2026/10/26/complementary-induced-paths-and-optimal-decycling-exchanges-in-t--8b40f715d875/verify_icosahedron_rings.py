"""Exhaustive icosahedral optimal induced-forest/exchange certificate. Python 3 standard library."""
from itertools import combinations
from collections import Counter,deque
N=12
adj=[set() for _ in range(N)]
def edge(x,y): adj[x].add(y);adj[y].add(x)
for i in range(5):
 u=1+i;l=6+i
 edge(0,u);edge(11,l)
 edge(u,1+(i+1)%5);edge(l,6+(i+1)%5)
 edge(u,l);edge(u,6+(i-1)%5)
assert sum(map(len,adj))==60 and set(map(len,adj))=={5}

def tree_path(mask):
 vs={i for i in range(N) if mask>>i&1}
 if len(vs)!=6:return False
 edges=sum(len(adj[v]&vs) for v in vs)//2
 if edges!=5:return False
 seen={next(iter(vs))}; todo=list(seen)
 while todo:
  for w in adj[todo.pop()]&vs:
   if w not in seen: seen.add(w);todo.append(w)
 return len(seen)==6 and sorted(len(adj[v]&vs) for v in vs)==[1,1,2,2,2,2]

def acyclic(mask):
 verts={i for i in range(N) if mask>>i&1}; seen=set()
 for start in verts:
  if start in seen:continue
  stack=[(start,-1)]
  while stack:
   v,p=stack.pop()
   if v in seen: return False
   seen.add(v)
   stack.extend((w,v) for w in adj[v]&verts if w!=p)
 return True
sets=[]; bysize=Counter()
for mask in range(1<<N):
 if acyclic(((1<<N)-1)^mask):bysize[mask.bit_count()]+=1
 if mask.bit_count()==6 and acyclic(((1<<N)-1)^mask):sets.append(mask)
assert not any(bysize.get(k) for k in range(6)) and len(sets)==60
assert all(tree_path(m) and tree_path(((1<<N)-1)^m) for m in sets)
pos={m:i for i,m in enumerate(sets)}; H=[set() for _ in sets];slide=0
for i,m in enumerate(sets):
 for u in range(N):
  if (m>>u)&1:
   for v in range(N):
    if not (m>>v)&1:
     n=m^(1<<u)^(1<<v)
     if n in pos:
      assert v in adj[u],('nonadjacent valid jump',i,u,v)
      H[i].add(pos[n]);slide+=1
assert all(len(row)==4 for row in H)
assert all(i in H[j] for i,row in enumerate(H) for j in row)
dists=[];pair=Counter();ecc=Counter(); bipartite={};
for i in range(len(sets)):
 dist={i:0};q=deque([i])
 while q:
  v=q.popleft()
  for w in H[v]:
   if w not in dist:dist[w]=dist[v]+1;q.append(w)
 assert len(dist)==60
 ecc[max(dist.values())]+=1
 for j,d in dist.items():pair[((sets[i]&sets[j]).bit_count(),d)]+=1
 assert dist[pos[((1<<N)-1)^sets[i]]]==6
assert ecc=={6:60}
q=deque([0]);bipartite[0]=0
while q:
 u=q.popleft()
 for v in H[u]:
  if v not in bipartite:bipartite[v]=1-bipartite[u];q.append(v)
  else:assert bipartite[v]!=bipartite[u]
assert len(bipartite)==60
print('ICOSAHEDRON Ring-model 12 vertices 30 edges')
print('MAXIMUM_INDUCED_FORESTS minimum_deletions=6 minimum_sets=60')
print('INDUCED_STRUCTURE each minimum set and complement are P6')
print('SINGLE_VERTEX_EXCHANGES undirected_edges=120 all_are_token_slides=True')
print('EXCHANGE_CONNECTED=True degree=4 bipartite=True radius=6 diameter=6')
print('DISTANCE_INTERSECTION_TABLE',sorted(pair.items()))
print('COMPLEMENT_DISTANCE=6 always')
print('TOTAL_12_BIT_MASKS',1<<N,'SETS_PER_DELETION_SIZE',sorted(bysize.items()))
print('CERTIFICATE_VERIFIED')
