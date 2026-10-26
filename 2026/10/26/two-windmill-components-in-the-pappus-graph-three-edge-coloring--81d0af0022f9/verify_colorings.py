#!/usr/bin/env python3
"""Direct edge-coloring backtrack and color-cycle flips; standard library only."""
import collections
import hashlib
import json

n=18
shift=[5,7,-7,7,-7,-5]
edge_list=sorted(set(tuple(sorted((v,(v+1)%n))) for v in range(n)) | set(tuple(sorted((v,(v+shift[v%6])%n))) for v in range(n)))
assert len(edge_list)==27
inc=[[] for v in range(n)]
for j,(u,v) in enumerate(edge_list):
 inc[u].append(j); inc[v].append(j)
assert all(len(z)==3 for z in inc)
root=inc[0]
# Fix 0's incident colors, taking one representative per global color permutation.
color=[-1]*27
for i,j in enumerate(root):color[j]=i
order=sorted((j for j in range(27) if j not in root),key=lambda j:(sum(k in root for v in edge_list[j] for k in inc[v]),j), reverse=True)
collected=set()
def search(t):
 if t==len(order):
  assert all(sorted(color[j] for j in inc[v])==[0,1,2] for v in range(n))
  collected.add(tuple(color));return
 j=order[t];u,v=edge_list[j]
 taken={color[k] for k in inc[u]+inc[v] if color[k]>=0}
 for c in range(3):
  if c in taken:continue
  color[j]=c;search(t+1)
 color[j]=-1
search(0)
configs=sorted(collected)
assert len(configs)==20
index={c:i for i,c in enumerate(configs)}

def normal(c):
 mapcolor={c[e]:i for i,e in enumerate(root)}
 return tuple(mapcolor[x] for x in c)

def recolor_neighbors(c):
 out=set()
 for A,B in [(0,1),(0,2),(1,2)]:
  adj=[[] for v in range(n)]
  for j,(a,b) in enumerate(edge_list):
   if c[j] in (A,B):
    adj[a].append((b,j));adj[b].append((a,j))
  assert all(len(q)==2 for q in adj)
  unseen=set(range(n))
  while unseen:
   v=min(unseen)
   stack=[v];segment=set();cycle_edges=set()
   while stack:
    w=stack.pop()
    if w in segment: continue
    segment.add(w)
    for other,ej in adj[w]:
     cycle_edges.add(ej)
     if other not in segment:stack.append(other)
   unseen-=segment
   d=list(c)
   for e in cycle_edges:d[e]=B if c[e]==A else A
   z=normal(d)
   if z!=c:out.add(z)
 return out

adj=[set() for _ in configs]
for i,c in enumerate(configs):
 neighbors=recolor_neighbors(c)
 assert neighbors<=set(configs)
 adj[i]={index[x] for x in neighbors}
assert all(i in adj[j] for i,s in enumerate(adj) for j in s)
all_edges=sorted((i,j) for i in range(20) for j in adj[i] if i<j)
remaining=set(range(20));components=[]
while remaining:
 stack=[min(remaining)]; seen=set()
 while stack:
  u=stack.pop()
  if u in seen:continue
  seen.add(u);stack.extend(adj[u]-seen)
 remaining-=seen;components.append(sorted(seen))
assert sorted(map(len,components))==[10,10]
for comp in components:
 assert sum(len(adj[i])==9 for i in comp)==1
 apex=next(i for i in comp if len(adj[i])==9)
 assert set(adj[apex])==set(comp)-{apex}
 leaves=set(comp)-{apex}
 assert all(len(adj[i] & leaves)==2 for i in leaves)
 cl=[]
 while leaves:
  i=min(leaves);triangle={i}|(adj[i]&leaves)
  assert len(triangle)==3
  assert all((adj[j] & triangle)==triangle-{j} for j in triangle)
  cl.append(triangle);leaves-=triangle
 assert len(cl)==3
encoded=json.dumps({'colorings':configs, 'edges':all_edges}, separators=(',', ':'), sort_keys=True)
print(json.dumps({'method':'direct_27_edge_three_color_backtrack', 'one_factorizations':len(configs), 'Kempe_edges':len(all_edges),
   'components':sorted(map(len,components)), 'degrees':dict(sorted(collections.Counter(map(len,adj)).items())),
   'full_graph_sha256':hashlib.sha256(encoded.encode()).hexdigest(),
   'conclusion':'2 copies of K_1 join (3 K_3)'},indent=2,sort_keys=True))
