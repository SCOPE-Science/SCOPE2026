import itertools,math,networkx as nx,collections,heapq
n=6; verts=[(i,h) for h in (0,1) for i in range(n)]
def d2(u,v):
 a,h=u;b,k=v;cy=min((a-b)%n,(b-a)%n)
 return [0,1,3,4][cy]+(h!=k)
for t in [1,2,3,4,5]:
 g=nx.Graph();g.add_nodes_from(range(12));g.add_edges_from((i,j) for i in range(12) for j in range(i+1,12) if d2(verts[i],verts[j])<=t)
 maximal=list(nx.find_cliques(g));F=set()
 for s in maximal:
  mask=sum(1<<i for i in s);a=mask
  while a:F.add(a);a=(a-1)&mask
 f=collections.Counter(x.bit_count()-1 for x in F)
 chi=sum((-1)**k*v for k,v in f.items())-1
 print('t',t,'f',dict(f),'redchi',chi,'maximal',len(maximal),'ncells',len(F))
 if t==3:
  co=collections.Counter()
  for face in F:
   a=face
   while a:
    b=a&-a;sub=face^b
    if sub:co[sub]+=1
    a-=b
  H=[(-f.bit_count(),f) for f in F if co[f]==1];heapq.heapify(H)
  pairs=0
  while H:
   _,f=heapq.heappop(H)
   if f not in F or co[f]!=1:continue
   sup=next(t for i in range(12) if (t:=f|(1<<i))!=f and t in F)
   F.remove(f);F.remove(sup);pairs+=1
   for face in (f,sup):
    a=face
    while a:
     b=a&-a;sub=face^b
     if sub in F:
      co[sub]-=1
      if co[sub]==1:heapq.heappush(H,(-sub.bit_count(),sub))
     a-=b
  print('collapsed',pairs,'core',len(F),collections.Counter(x.bit_count()-1 for x in F))
