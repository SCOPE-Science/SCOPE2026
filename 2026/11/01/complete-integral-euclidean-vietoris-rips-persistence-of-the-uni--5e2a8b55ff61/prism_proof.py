import collections,heapq,networkx as nx,itertools,random
from hexprism import verts,d2
n=12;g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from((i,j) for i in range(n) for j in range(i+1,n) if d2(verts[i],verts[j])<=3)
F=set()
for s in nx.find_cliques(g):
 mask=sum(1<<i for i in s);a=mask
 while a:F.add(a);a=(a-1)&mask
co=collections.Counter()
for face in F:
 a=face
 while a:
  b=a&-a; sub=face^b
  if sub:co[sub]+=1
  a-=b
H=[(-f.bit_count(),f) for f in F if co[f]==1];heapq.heapify(H)
pairs=[]
while H:
 _,f=heapq.heappop(H)
 if f not in F or co[f]!=1:continue
 sup=next(t for i in range(n) if (t:=f|(1<<i))!=f and t in F)
 F.remove(f);F.remove(sup);pairs.append((f,sup))
 for face in (f,sup):
  a=face
  while a:
   b=a&-a;sub=face^b
   if sub in F:
    co[sub]-=1
    if co[sub]==1:heapq.heappush(H,(-sub.bit_count(),sub))
   a-=b
print('core',len(F),'pairs',len(pairs))
triangles=[tuple(i for i in range(n) if f&(1<<i)) for f in F if f.bit_count()==3]
G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from(tuple(i for i in range(n) if f&(1<<i)) for f in F if f.bit_count()==2)
assert nx.is_connected(G)
def reduce_word(w):
 stack=[]
 for x in w:
  if stack and stack[-1]==-x:stack.pop()
  else:stack.append(x)
 return stack

def test(seed):
 R=random.Random(seed)
 tree=nx.minimum_spanning_tree(G,weight=None) if seed==-1 else nx.minimum_spanning_tree(nx.Graph((u,v,{'weight':R.random()}) for u,v in G.edges()))
 te={tuple(sorted(x)) for x in tree.edges()}
 edges=sorted(tuple(sorted(x)) for x in G.edges() if tuple(sorted(x)) not in te)
 ids={x:i+1 for i,x in enumerate(edges)}
 def word(t):
  a,b,c=t
  return [ids[(u,v)]*s for u,v,s in [(a,b,1),(b,c,1),(a,c,-1)] if (u,v) in ids]
 rel=[reduce_word(word(t)) for t in triangles]
 eliminated=[]
 for _ in range(40):
  # pick relation containing generator once; minimize length
  candidates=[]
  for j,w in enumerate(rel):
   cc=collections.Counter(abs(x) for x in w)
   for k,val in cc.items():
    if val==1:candidates.append((len(w),j,k))
  if not candidates:break
  _,j,k=min(candidates)
  w=rel.pop(j); idx=next(i for i,x in enumerate(w) if abs(x)==k)
  # w=A+[sign*k]+B, so k -> inv(A)*inv(B) if sign positive; if negative, k -> B*A
  A=w[:idx]; B=w[idx+1:]
  sub=([-x for x in reversed(A)]+[-x for x in reversed(B)]) if w[idx]>0 else (B+A)
  for r in range(len(rel)):
   out=[]
   for x in rel[r]:
    if abs(x)!=k:out.append(x)
    elif x>0:out.extend(sub)
    else:out.extend(-y for y in reversed(sub))
   rel[r]=reduce_word(out)
  eliminated.append(k)
  if max(map(len,rel),default=0)>10000:break
 return len(eliminated),len(rel),len([r for r in rel if r]),max(map(len,rel),default=0),eliminated,te
best=None
for seed in range(300):
 r=test(seed)
 if best is None or (r[0],-r[2])>(best[0],-best[2]):best=r;print('best seed',seed,'stats',r[:4],flush=True)
 if r[0]==20 and r[2]==0:print('SOLVED',seed,r[:4]);break
print('final best',best[:4])
assert len(pairs)==29 and len(F)==66
assert best[0]==20 and best[1]==3 and best[2]==0 and best[3]==0
print('VERIFY_OK')
