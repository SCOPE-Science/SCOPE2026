from itertools import combinations
from collections import Counter
V=range(8); edges=list(combinations(V,2)); inside=list(combinations(range(1,8),2)); colors=list(range(7)); coloring={(0,j):j-1 for j in range(1,8)}
used=[set() for _ in V]
for j in range(1,8):used[0].add(j-1);used[j].add(j-1)
states=[]
def dfs(rem):
 if not rem:
  states.append(tuple(coloring[e] for e in edges));return
 items=[]
 for e in rem:
  a,b=e;opts=set(colors)-used[a]-used[b]
  if not opts:return
  items.append((len(opts),e,opts))
 _,e,opts=min(items)
 a,b=e;more=[z for z in rem if z!=e]
 for t in sorted(opts):
  coloring[e]=t;used[a].add(t);used[b].add(t);dfs(more);used[a].remove(t);used[b].remove(t);del coloring[e]
dfs(inside);idex={c:i for i,c in enumerate(states)};print('count',len(states),flush=True)
adj=[set() for _ in states];cycles=Counter();tally=Counter()
for i,c in enumerate(states):
 ecolor=dict(zip(edges,c));M=[[0]*8 for _ in range(8)]
 for (a,b),t in ecolor.items():M[a][b]=M[b][a]=t
 for a,b in combinations(V,2):
  f=M[a][b]; av=[v for v in V if v not in (a,b)];cd={M[a][v]:v for v in av};dd={M[b][v]:v for v in av}
  # each alternating component in 6 vertex / 6 color network
  graph={v:set() for v in av}
  for color in colors:
   if color!=f:
    v,w=cd[color],dd[color]
    graph[v].add(w);graph[w].add(v)
  unseen=set(av); comps=[]
  while unseen:
   v=min(unseen);q=[v];S={v};unseen.remove(v)
   for x in q:
    for y in graph[x]:
     if y not in S:S.add(y);unseen.discard(y);q.append(y)
   comps.append(S)
  cycles[tuple(sorted(map(len,comps)))]+=1
  if len(comps)==1:continue # exclude global vertex label swap
  for S in comps:
   new=M.copy(); newcolor=ecolor.copy()
   for v in S:
    aa,bb=tuple(sorted((a,v))),tuple(sorted((b,v)))
    newcolor[aa],newcolor[bb]=newcolor[bb],newcolor[aa]
   cc=tuple(newcolor[e] for e in edges)
   # global relabel colors such that (0,j) gets j-1
   phi={cc[edges.index((0,j))]:j-1 for j in range(1,8)}
   cc=tuple(phi[t] for t in cc)
   j=idex[cc]
   if i!=j:adj[i].add(j)
for i,nb in enumerate(adj):
 for j in nb:assert i in adj[j]
visited=set();components=[]
for i in range(len(states)):
 if i not in visited:
  group={i};q=[i]
  for v in q:
   for w in adj[v]:
    if w not in group: group.add(w);q.append(w)
  visited|=group;components.append(q)
print('vertex cycles',cycles)
print('components',Counter(map(len,components)),'degrees',Counter(map(len,adj)),'edges',sum(map(len,adj))//2,flush=True)
from collections import deque
key=[]
for c in states:
 color=dict(zip(edges,c));d=0
 for a,b in combinations(range(7),2):
  nb={v:[] for v in V}
  for (u,v),z in color.items():
   if z in (a,b):nb[u].append(v);nb[v].append(u)
  unseen=set(V);cnt=0
  while unseen:
   cnt+=1;queue=[unseen.pop()];visited1=set(queue)
   for u in queue:
    for v in nb[u]:
     if v not in visited1:visited1.add(v);unseen.discard(v);queue.append(v)
  if cnt>1:d+=1
 key.append((d,len(adj[idex[c]])))
groups={x:[] for x in set(key)}
for i,k in enumerate(key):groups[k].append(i)
print('invariant groups',dict((str(k),len(v)) for k,v in groups.items()),flush=True)
for k,ids in sorted(groups.items()):
 root=ids[0];dist=[-1]*len(states);dist[root]=0;q=deque([root]);
 while q:
  i=q.popleft()
  for j in adj[i]:
   if dist[j]<0:dist[j]=dist[i]+1;q.append(j)
 D=Counter(dist)
 print('root-type',k,'index',root,'ecc',max(dist),'dist',tuple(D[d] for d in range(max(dist)+1)),flush=True)
assert len(states)==6240
assert len(components)==1 and len(components[0])==6240
assert sum(map(len,adj))//2==66360
assert Counter(map(len,adj))=={9:420,14:960,21:30,23:4200,29:630}
print('VERIFY_OK')
