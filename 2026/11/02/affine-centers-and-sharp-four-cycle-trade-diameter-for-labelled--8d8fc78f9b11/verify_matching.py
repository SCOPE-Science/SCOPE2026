from itertools import combinations
from collections import Counter,defaultdict,deque
n=8
edges=list(combinations(range(n),2)); ids={e:i for i,e in enumerate(edges)}
ALL=(1<<len(edges))-1
M=[];E=[]; V=[]
def matching(items,ls):
 if not items:
  e=sum(1<<ids[tuple(sorted(p))] for p in ls)
  M.append(tuple(tuple(sorted(p)) for p in ls)); E.append(e);V.append(tuple(sorted(ls)))
  return
 a=items[0]
 for b in items[1:]:
  matching([x for x in items if x not in (a,b)],ls+[(a,b)])
matching(list(range(n)),[])
pairs_by_edge=[[i for i,m in enumerate(E) if m>>e&1] for e in range(len(edges))]
FACT=[]
def recurse(rem, selected):
 if not rem:
  FACT.append(tuple(sorted(selected)));return
 e=(rem & -rem).bit_length()-1
 for m in pairs_by_edge[e]:
  if E[m]&rem==E[m]:
   recurse(rem ^ E[m],selected+[m])
recurse(ALL,[])
assert len(M)==105 and len(FACT)==6240
index={x:i for i,x in enumerate(FACT)}
N={}
for i in range(len(M)):
 for j in range(i+1,len(M)):
  union=E[i]|E[j]
  if E[i]&E[j] or union.bit_count()!=8: continue
  # each edge one of two matchings. split 2-color 2-regular structure into cycles
  ad=defaultdict(list)
  for e, (u,v) in enumerate(edges):
   if union>>e&1:
    ad[u].append((v,e));ad[v].append((u,e))
  vis=set(); comps=[]
  for v in range(8):
   if v in vis:continue
   st=[v]; verts=set([v]);vis.add(v);component=0
   while st:
    x=st.pop()
    for y,e in ad[x]:
     component |=1<<e
     if y not in vis:vis.add(y);st.append(y)
   comps.append(component)
  if len(comps)!=2: continue
  if {c.bit_count() for c in comps}!={4}: raise ValueError
  c=comps[0]
  ne_i=E[i] ^c; ne_j=E[j] ^c
  N[i,j]=tuple(sorted([next(k for k,z in enumerate(E) if z==ne_i),next(k for k,z in enumerate(E) if z==ne_j)]))
assert len(N)==630
adj=[set() for _ in FACT]
for i,f in enumerate(FACT):
 for a,b in combinations(f,2):
  if (a,b) not in N:continue
  aa,bb=N[a,b]; g=tuple(sorted(set(f)-{a,b}|{aa,bb}))
  if g not in index:raise ValueError(g)
  adj[i].add(index[g])
for i,neigh in enumerate(adj):
 for j in neigh:assert i in adj[j]
assert Counter(map(len,adj))=={0:960,3:1680,7:2520,9:420,13:630,21:30}
assert sum(map(len,adj))//2==17640
seen=set();CC=[]
for i in range(len(adj)):
 if i in seen:continue
 q=[i];seen.add(i)
 for x in q:
  for y in adj[x]:
   if y not in seen:seen.add(y);q.append(y)
 CC.append(q)
assert len(CC)==961 and Counter(map(len,CC))=={1:960,5280:1}
ecc_by_degree=Counter()
for comp in CC:
 if len(comp)==1:continue
 for i in comp:
  dist={i:0};q=[i]
  for x in q:
   for y in adj[x]:
    if y not in dist:dist[y]=dist[x]+1;q.append(y)
  assert len(dist)==len(comp)
  ecc_by_degree[len(adj[i]),max(dist.values())]+=1
assert ecc_by_degree=={(3,11):1680,(7,10):2520,(9,10):420,(13,10):630,(21,9):30}
# Every pair of affine translation matchings forms two four-cycles.
affine=[]
for a in range(1,8):
 mask=sum(1<<ids[(min(x,x^a),max(x,x^a))] for x in range(8) if x < (x^a))
 affine.append(E.index(mask))
affine=tuple(sorted(affine))
assert affine in index and len(adj[index[affine]])==21
# Its full vertex-relabeling orbit comprises the entire 30-element center.
from itertools import permutations
centers={i for i,x in enumerate(adj) if len(x)==21}
orbit=set()
for p in permutations(range(8)):
 f=[]
 for m in affine:
  mask=sum(1<<ids[(min(p[u],p[v]),max(p[u],p[v]))] for u,v in M[m])
  f.append(E.index(mask))
 orbit.add(index[tuple(sorted(f))])
assert orbit==centers and len(orbit)==30
print('MATCHING_EXACT_COVER_6240_AND_17640_EDGES_PASS')
print('ALL_5280_SOURCE_DISTANCES_RADIUS9_DIAMETER11_PASS')
print('AFFINE_30_CENTERS_AND_960_ISOLATES_PASS')
