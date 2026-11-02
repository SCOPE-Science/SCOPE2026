import itertools,collections,time
start=time.monotonic()
edges=[(u,u^(1<<j)) for u in range(16) for j in range(4) if u<(u^(1<<j))];ei={tuple(sorted(x)):i for i,x in enumerate(edges)}
faces=[]
for a in range(16):
 for i in range(4):
  for j in range(i+1,4):
   b=a^(1<<i);c=a^(1<<j);d=b^(1<<j)
   if a<min(b,c,d):
    faces.append([ei[tuple(sorted(x))] for x in [(a,b),(b,d),(d,c),(c,a)]])
print('faces',len(faces))
base=[]
def rec(u,vis,m):
 if vis==65535:base.append(m);return
 for j in range(4):
  v=u^(1<<j)
  if not(vis>>v&1):rec(v,vis|(1<<v),m|(1<<ei[tuple(sorted((u,v)))]))
rec(0,1,0)
print('base',len(base))
allset=set()
for a in range(16):
 conv=[ei[tuple(sorted((u^a,v^a)))] for u,v in edges]
 for m in base:
  mm=0
  for i in range(32):
   if m>>i&1:mm|=1<<conv[i]
  allset.add(mm)
print('paths',len(allset),'enumeration',time.monotonic()-start)
states=list(allset);ids={m:i for i,m in enumerate(states)};adj=[[] for _ in states]
for k,m in enumerate(states):
 for face in faces:
  bs=[(m>>e)&1 for e in face]
  if bs==[1,0,1,0] or bs==[0,1,0,1]:
   mm=m
   for e in face:mm^=1<<e
   j=ids.get(mm)
   if j is not None:adj[k].append(j)
print('edge_count',sum(map(len,adj))//2,'degrees',sorted(collections.Counter(map(len,adj)).items()),'t',time.monotonic()-start)
seen=set(); comps=[]
for i in range(len(states)):
 if i in seen:continue
 stack=[i];seen.add(i); v=0
 while stack:
  x=stack.pop();v+=1
  for y in adj[x]:
   if y not in seen:seen.add(y);stack.append(y)
 comps.append(v)
print('components',len(comps),'hist',sorted(collections.Counter(comps).items()),'t',time.monotonic()-start)
bytype=collections.Counter();fr=collections.Counter()
for m in states:
 degv=[0]*16
 for i,(u,v) in enumerate(edges):
  if m>>i&1:degv[u]+=1;degv[v]+=1
 ends=[i for i in range(16) if degv[i]==1]
 assert len(ends)==2 and all(q in(1,2) for q in degv)
 dist=(ends[0]^ends[1]).bit_count()
 bytype[dist]+=1
 if len(adj[ids[m]])==0:fr[dist]+=1
print('endpoint-hamming-count',sorted(bytype.items()),'frozen',sorted(fr.items()))
assert len(states)==45696
assert sum(map(len,adj))//2==69120
assert collections.Counter(comps)=={1:5184,528:32,738:32}
assert bytype=={1:21504,3:24192} and fr=={1:4608,3:576}
assert collections.Counter(map(len,adj))=={0:5184,1:8064,2:6528,3:7296,4:9408,5:2304,6:2880,7:3456,8:576}
print('PRIMARY_PATH_PASS')
