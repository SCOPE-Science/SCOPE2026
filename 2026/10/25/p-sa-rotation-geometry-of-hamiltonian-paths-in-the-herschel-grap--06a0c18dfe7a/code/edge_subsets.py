# Independent spanning-path edge-subset enumeration and one-edge replacement checks.
from itertools import combinations
from collections import Counter, deque
EDGES=[]
for a,b,r in ((0,1,(5,6)),(1,2,(7,8)),(2,0,(9,10))):
 for v in r:EDGES += [tuple(sorted((a,v))),tuple(sorted((b,v)))]
for v in (5,7,9): EDGES.append((3,v))
for v in (6,8,10): EDGES.append((4,v))
EDGES=sorted(set(EDGES))
assert len(EDGES)==18
states=[]
for inds in combinations(range(18),10):
    deg=[0]*11; adj=[[] for _ in range(11)]
    for i in inds:
        x,y=EDGES[i];deg[x]+=1;deg[y]+=1
        if deg[x]>2 or deg[y]>2:break
        adj[x].append(y);adj[y].append(x)
    else:
        if sorted(deg)!=[1,1]+[2]*9:continue
        start=deg.index(1); seen={start}; stack=[start]
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:seen.add(y);stack.append(y)
        if len(seen)==11:
            states.append(sum(1<<i for i in inds))
assert len(states)==222,len(states)
S=set(states)
G={u:set() for u in states}
for u in states:
 for e in range(18):
  if not u>>e&1:continue
  for f in range(18):
   if u>>f&1:continue
   v=(u^(1<<e))|(1<<f)
   if v in S:G[u].add(v)
assert all(len(x)==4 for x in G.values())
assert sum(len(x) for x in G.values())//2==444
Ecc=Counter()
for start in states:
 d={start:0};Q=deque([start])
 while Q:
  v=Q.popleft()
  for w in G[v]:
   if w not in d:d[w]=d[v]+1;Q.append(w)
 Ecc[(len(d),max(d.values()))]+=1
assert Ecc=={(222,8):198,(222,9):24},Ecc
print('EDGECHECK_OK graph=Herschel vertices=11 edges=18 undirected_hamiltonian_paths=222 exchange_edges=444 regular_degree=4 connected=1 radius=8 diameter=9 eccentricities={8:198,9:24}')
