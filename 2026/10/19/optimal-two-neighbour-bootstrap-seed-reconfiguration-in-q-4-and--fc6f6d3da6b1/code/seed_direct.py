#!/usr/bin/env python3
"""Direct synchronous two-neighbour bootstrap closure and optimal-seed exchange graphs."""
import itertools, collections, time

def check(d):
 n=1<<d
 adj=[sum(1<<(i^(1<<b)) for b in range(d)) for i in range(n)]
 def percs(t):
  active=sum(1<<v for v in t)
  while 1:
   new=active
   for v in range(n):
    if not active>>v&1 and (adj[v]&active).bit_count()>=2:new|=1<<v
   if new==active:return active.bit_count()==n
   active=new
 for k in range(1,d+2):
  sets=[t for t in itertools.combinations(range(n),k) if percs(t)]
  print('d',d,'k',k,'n',len(sets),flush=True)
  if sets: break
 ids={t:i for i,t in enumerate(sets)}
 alln=[set() for _ in sets];slide=[set() for _ in sets]
 for i,t in enumerate(sets):
  for x in t:
   for v in range(n):
    if v not in t:
     s=tuple(sorted((set(t)-{x})|{v})); j=ids.get(s)
     if j is not None and j!=i:
      alln[i].add(j)
      if adj[x]>>v&1:slide[i].add(j)
 def comps(g):
  seen=set();cs=[]
  for i in range(len(g)):
   if i in seen:continue
   todo=[i];seen.add(i);c=[]
   for u in todo:
    c.append(u)
    for v in g[u]:
     if v not in seen:seen.add(v);todo.append(v)
   cs.append(c)
  return sorted(cs,key=len,reverse=True)
 for name,g in [('jump',alln),('slide',slide)]:
  cs=comps(g);print('  ',name,'edges',sum(map(len,g))//2,'degrees',sorted(collections.Counter(map(len,g)).items()),'compdist',collections.Counter(map(len,cs)),flush=True)
  if len(sets)<1000:
   E=[]
   for u in range(len(g)):
    q=collections.deque([u]);dist={u:0}
    while q:
     z=q.popleft()
     for v in g[z]:
      if v not in dist:dist[v]=dist[z]+1;q.append(v)
    E.append(max(dist.values()))
   print('   ecc',collections.Counter(E),'radii per comps?',flush=True)
 return sets,alln,slide

