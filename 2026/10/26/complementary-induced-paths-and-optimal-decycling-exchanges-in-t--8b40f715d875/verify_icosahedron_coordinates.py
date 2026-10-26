"""Independent icosahedron construction in exact Z[golden ratio] coordinates."""
from itertools import combinations
from collections import Counter,deque
# Coordinate pair (a,b) means a+b*phi, with phi^2=phi+1.
zero=(0,0);units=[(-1,0),(1,0)];phivals=[(0,-1),(0,1)]
vertices=[]
for s in units:
 for t in phivals:
  vertices.extend([(zero,s,t),(s,t,zero),(t,zero,s)])
assert len(vertices)==len(set(vertices))==12

def dsquared(u,v):
 c0=c1=0
 for x,y in zip(u,v):
  a=x[0]-y[0];b=x[1]-y[1]
  c0+=a*a+b*b;c1+=2*a*b+b*b
 return(c0,c1)
adj=[0]*12
for i in range(12):
 for j in range(i+1,12):
  if dsquared(vertices[i],vertices[j])==(4,0):adj[i]|=1<<j;adj[j]|=1<<i
assert all(m.bit_count()==5 for m in adj)

def induced_forest(mask):
 seen=0
 for root in range(12):
  if not(mask>>root&1) or seen>>root&1:continue
  stack=[(root,-1)]
  while stack:
   v,parent=stack.pop()
   if seen>>v&1:return False
   seen|=1<<v
   for w in range(12):
    if w!=parent and (mask>>w&1) and (adj[v]>>w&1):stack.append((w,v))
 return True

def path6(mask):
 if mask.bit_count()!=6:return False
 degrees=[(adj[v]&mask).bit_count() for v in range(12) if mask>>v&1]
 return sorted(degrees)==[1,1,2,2,2,2] and induced_forest(mask)
minimum=[]
for k in range(6):
 assert not any(induced_forest(((1<<12)-1)^sum(1<<v for v in vs)) for vs in combinations(range(12),k))
for vs in combinations(range(12),6):
 m=sum(1<<v for v in vs)
 if induced_forest(((1<<12)-1)^m): minimum.append(m)
assert len(minimum)==60
for mask in minimum:assert path6(mask) and path6(((1<<12)-1)^mask)
index={mask:i for i,mask in enumerate(minimum)};neighbors=[set() for _ in minimum];jumps=slides=0
for i,mask in enumerate(minimum):
 for j in range(i+1,len(minimum)):
  targ=minimum[j]
  if (mask^targ).bit_count()!=2:continue
  jumps+=1
  u=mask&~targ;v=targ&~mask
  if (adj[u.bit_length()-1]&v):slides+=1
  neighbors[i].add(j);neighbors[j].add(i)
assert jumps==slides==120 and Counter(map(len,neighbors))=={4:60}
profs=Counter();ec=Counter();pair=Counter()
for i,mask in enumerate(minimum):
 d=[-1]*len(minimum);d[i]=0;q=deque([i])
 while q:
  u=q.popleft()
  for v in neighbors[u]:
   if d[v]==-1:d[v]=d[u]+1;q.append(v)
 assert all(t>=0 for t in d)
 ec[max(d)]+=1
 if i==0:profs.update(d)
 for j,targ in enumerate(minimum):pair[((mask&targ).bit_count(),d[j])]+=1
assert ec=={6:60}
colors={0:0};q=deque([0])
while q:
 i=q.popleft()
 for j in neighbors[i]:
  if j in colors:assert colors[j]!=colors[i]
  else:colors[j]=1-colors[i];q.append(j)
assert len(colors)==60
print('ICOSAHEDRON Golden-ratio coordinate model 12 vertices 30 edges')
print('MIN_DELETION=6 COUNT=60 each removal and its complement induce P6')
print('TOKEN_JUMP_EDGES=120 TOKEN_SLIDE_EDGES=120')
print('EXCHANGE_CONNECTED=True 4_REGULAR=True BIPARTITE=True RADIUS=6 DIAMETER=6')
print('PAIRWISE_INTERSECTION_DISTANCE',sorted(pair.items()))
print('ROOT_DISTANCE_HISTOGRAM',sorted(profs.items()))
print('ALL_VERTEX_ECCENTRICITIES',sorted(ec.items()))
print('INDEPENDENT_CERTIFICATE_VERIFIED')
