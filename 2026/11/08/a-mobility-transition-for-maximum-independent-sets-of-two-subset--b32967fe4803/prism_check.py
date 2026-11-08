from itertools import combinations
from collections import Counter,deque

def check(n):
 edges=list(combinations(range(n),2));N=len(edges)
 fam={}
 for k in range(n-3,n):
  if k<0:continue
  fam[k]=[]
  for ids in combinations(range(N),k):
   E=[edges[i] for i in ids]
   if all(set(a)&set(b) for a,b in combinations(E,2)):fam[k].append(frozenset(ids))
 opt=2*n-3 if n>=5 else 6
 vv=[]
 for a in range(opt-(n-1),n):
  b=opt-a
  if a in fam and b in fam:
   vv.extend((A,B) for A in fam[a] for B in fam[b] if not (A&B))
 print('N',n,'max',opt,'state',len(vv),'layer count',Counter(map(lambda x:len(x[0]),vv)))
 I={v:i for i,v in enumerate(vv)}
 AD=[[] for _ in vv]
 for i,(a,b) in enumerate(vv):
  for k in a:
   for h in range(N):
    if h not in a:
     v=(a-{k}|{h},b)
     if v in I:AD[i].append(I[v])
  for k in b:
   for h in range(N):
    if h not in b:
     v=(a,b-{k}|{h})
     if v in I:AD[i].append(I[v])
  for k in a:
   v=(a-{k},b|{k})
   if v in I:AD[i].append(I[v])
  for k in b:
   v=(a|{k},b-{k})
   if v in I:AD[i].append(I[v])
 components=[];seen=set()
 for i in range(len(vv)):
  if i in seen:continue
  q=[i];seen.add(i)
  for j in q:
   for k in AD[j]:
    if k not in seen:seen.add(k);q.append(k)
  components.append(len(q))
 print('degree',Counter(map(len,AD)),'edges',sum(map(len,AD))//2,'components',Counter(components))
 if n==5:
  diam=0
  for i in range(len(vv)):
   ds={i:0};q=deque([i]);
   while q:
    v=q.popleft()
    for w in AD[v]:
     if w not in ds:ds[w]=ds[v]+1;q.append(w)
   assert len(ds)==len(vv)
   diam=max(diam,max(ds.values()))
  print('diameter',diam)
for n in [5,6,7]: check(n)
