from collections import Counter, defaultdict
from itertools import combinations,permutations
verts=range(8);edges=list(combinations(verts,2));ei={x:i for i,x in enumerate(edges)}
E=len(edges); col=[-1]*E; used=[0]*8
for j in range(1,8):
 col[ei[0,j]]=j-1
 used[0] |=1<<(j-1);used[j] |=1<<(j-1)
unknown=[ei[u,v] for u,v in combinations(range(1,8),2)]
words=[]
def dfs(rem):
 if not rem:
  words.append(tuple(col));return
 best=None;best_options=None
 for e in rem:
  u,v=edges[e];allowed=0x7f & ~(used[u]|used[v]);k=allowed.bit_count()
  if k==0:return
  if best_options is None or k<best_options.bit_count():
   best,best_options=e,allowed
   if k==1:break
 u,v=edges[best]; nxt=[x for x in rem if x!=best]
 while best_options:
  bit=best_options&-best_options;best_options-=bit
  col[best]=bit.bit_length()-1;used[u]|=bit;used[v]|=bit
  dfs(nxt)
  used[u]^=bit;used[v]^=bit;col[best]=-1
dfs(unknown)
# All normalized proper edge-colorings have been enumerated.
assert len(words)==6240
index={x:i for i,x in enumerate(words)}
# each coloring a normalized symmetric Latin square; only an alternating intercalate is moved
adj=[set() for _ in words]
for z,word in enumerate(words):
 bycolor=[[] for _ in range(7)]
 for e,c in enumerate(word):bycolor[c].append(e)
 for a,b in combinations(range(7),2):
  ef=bycolor[a]+bycolor[b]
  nb=[[] for _ in range(8)]
  for e in ef:
   u,v=edges[e];nb[u].append((v,e));nb[v].append((u,e))
  reached={0};stack=[0];square=[]
  for x in stack:
   for y,e in nb[x]:
    square.append(e)
    if y not in reached:reached.add(y);stack.append(y)
  if len(reached)!=4:continue
  square=set(square)
  assert len(square)==4
  switched=list(word)
  for e in square:switched[e]=a+b-switched[e]
  permutation={switched[ei[0,j]]:j-1 for j in range(1,8)}
  candidate=tuple(permutation[c] for c in switched)
  target=index.get(candidate)
  assert target is not None and target!=z
  adj[z].add(target)
for i,neigh in enumerate(adj):
 for j in neigh:assert i in adj[j]
assert sum(map(len,adj))//2==17640
assert Counter(map(len,adj))=={0:960,3:1680,7:2520,9:420,13:630,21:30}
components=[];seen=set()
for i in range(len(words)):
 if i in seen:continue
 q=[i];seen.add(i)
 for x in q:
  for y in adj[x]:
   if y not in seen:seen.add(y);q.append(y)
 components.append(q)
assert Counter(map(len,components))=={1:960,5280:1}
reps={}
for i,neigh in enumerate(adj):reps.setdefault(len(neigh),i)
# All six degree types are full symmetric-group orbits: relabel and recanonicalize colors
for degree,root in sorted(reps.items()):
 w=words[root];orbit=set()
 for p in permutations(range(8)):
  rel=[0]*E
  for e,(u,v) in enumerate(edges):rel[ei[tuple(sorted((p[u],p[v])))] ]=w[e]
  ren={rel[ei[0,j]]:j-1 for j in range(1,8)}
  orbit.add(index[tuple(ren[c] for c in rel)])
 assert {len(adj[k]) for k in orbit}=={degree}
 expected=sum(len(a)==degree for a in adj)
 assert len(orbit)==expected
 if degree:
  dist={root:0};q=[root]
  for x in q:
   for y in adj[x]:
    if y not in dist:dist[y]=dist[x]+1;q.append(y)
  assert len(dist)==5280
  assert max(dist.values())=={3:11,7:10,9:10,13:10,21:9}[degree]
 else:assert len(orbit)==960
print('LATIN_EDGE_COLORING_6240_INDEPENDENT_CENSUS_PASS')
print('INTERCALATE_17640_EDGES_SIX_ORBITS_PASS')
print('ONE_5280_COMPONENT_AND_RADIUS9_DIAMETER11_PASS')
