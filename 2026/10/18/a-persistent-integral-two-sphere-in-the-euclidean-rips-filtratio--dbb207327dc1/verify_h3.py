#!/usr/bin/env python3
"""Exact integral-combinatorial certificate generator/reader for H3 roots.
Pure Python standard library; no floating point.
"""
import itertools,heapq,collections,json,sys,hashlib

PHI_COORD = [(1,0),(0,1),(-1,1)]
V=[]
for i in range(3):
 for s in [-1,1]:
  z=[(0,0)]*3;z[i]=(2*s,0);V.append(tuple(z))
for perm in [(0,1,2),(1,2,0),(2,0,1)]:
 for signs in itertools.product([-1,1],repeat=3):
  V.append(tuple(tuple(signs[i]*n for n in PHI_COORD[perm[i]]) for i in range(3)))
assert len(set(V)) == 30

def sq(i,j):
 a=b=0
 for (x,y),(u,v) in zip(V[i],V[j]):
  x-=u;y-=v
  a+=x*x+y*y;b+=2*x*y+y*y
 assert a%4==0 and b%4==0
 return (a//4,b//4)

DIST={ij:sq(*ij) for ij in itertools.combinations(range(30),2)}
THRESHOLDS=[(2,-1),(1,0),(3,-1),(2,0),(1,1),(3,0),(2,1),(4,0)]
assert collections.Counter(DIST.values())=={x:60 for x in THRESHOLDS[:-1]}|{THRESHOLDS[-1]:15}

def maximal_cliques(adj):
 ans=[]
 def bk(R,P,X):
  if not P and not X:
   ans.append(R);return
  u=max(P|X,key=lambda y:len(P&adj[y]),default=None)
  for v in sorted(P-(adj[u] if u is not None else set())):
   bk(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
 bk(set(),set(range(30)),set())
 return [sum(1<<i for i in cl) for cl in ans]

def faces_at(rank):
 valid=set(THRESHOLDS[:rank+1]);adj=[set() for _ in range(30)]
 for (i,j),d in DIST.items():
  if d in valid:adj[i].add(j);adj[j].add(i)
 facets=maximal_cliques(adj);faces=set()
 for facet in facets:
  sub=facet
  while sub:
   faces.add(sub);sub=(sub-1)&facet
 return faces,facets,adj

def free_collapse(complex_faces,target,certificate=None):
 fs=set(complex_faces)
 assert target <= fs
 cofaces=collections.defaultdict(set)
 counts={f:0 for f in fs}
 for f in fs:
  bits=f
  while bits:
   b=bits&-bits;bits-=b
   if f^b in fs:
    cofaces[f^b].add(f);counts[f^b]+=1
 def unique_parent(f):
  parents=[p for p in cofaces[f] if p in fs]
  assert len(parents)==1
  return parents[0]
 if certificate is None:
  work=[]
  for f in fs:
   if f not in target and counts[f]==1:
    heapq.heappush(work,(-f.bit_count(),f))
  seq=[]
  while work:
   _,f=heapq.heappop(work)
   if f not in fs or f in target or counts[f]!=1:continue
   p=unique_parent(f)
   if p in target:continue
   seq.append(f)
   for cell in (f,p):
    fs.remove(cell)
    bits=cell
    while bits:
     b=bits&-bits;bits-=b;sub=cell^b
     if sub in counts:
      counts[sub]-=1
      if sub in fs and sub not in target and counts[sub]==1:
       heapq.heappush(work,(-sub.bit_count(),sub))
 else:
  seq=certificate
  for f in seq:
   assert f in fs and f not in target and counts[f]==1,(f,len(fs))
   p=unique_parent(f)
   assert p not in target and f.bit_count()+1==p.bit_count()
   for cell in (f,p):
    fs.remove(cell)
    bits=cell
    while bits:
     b=bits&-bits;bits-=b;sub=cell^b
     if sub in counts:counts[sub]-=1
 assert fs==target,(len(fs-target),len(target-fs))
 return seq

def construct_surface(K0,K1,facets1,adj0):
 pentagons=[f for f in facets1 if f.bit_count()==5]
 tris=[f for f in facets1 if f.bit_count()==3]
 assert len(pentagons)==12 and len(tris)==20
 target=set(K0)
 for f in pentagons:
  vertices=[i for i in range(30) if (f>>i)&1]
  assert all(len(adj0[v]&set(vertices))==2 for v in vertices)
  start=min(vertices);neighbors=sorted(adj0[start]&set(vertices))
  order=[start,neighbors[0]]
  while len(order)<5:
   previous,cur=order[-2:]
   nxt=list((adj0[cur]&set(vertices))-{previous})
   assert len(nxt)==1 and nxt[0] not in order
   order.append(nxt[0])
  assert order[0] in adj0[order[-1]]
  # Fan triangulate the convex pentagonal face from a chosen boundary vertex.
  for j in [1,2,3]:
   tri=sum(1<<u for u in [order[0],order[j],order[j+1]])
   for sub in itertools.combinations([order[0],order[j],order[j+1]],1):target.add(1<<sub[0])
   for sub in itertools.combinations([order[0],order[j],order[j+1]],2):target.add(sum(1<<x for x in sub))
   target.add(tri)
 assert target <= K1
 assert collections.Counter(x.bit_count() for x in target)=={1:30,2:84,3:56}
 # Verify an abstract closed connected 2-manifold of Euler characteristic 2.
 faces2=[f for f in target if f.bit_count()==3]
 for e in (f for f in target if f.bit_count()==2):
  assert sum(1 for t in faces2 if e&t==e)==2
 for v in range(30):
  link_edges=[]
  for t in faces2:
   if (t>>v)&1:link_edges.append(t^(1<<v))
  link_vertices=set()
  link_adj=collections.defaultdict(set)
  for e in link_edges:
   a,b=[i for i in range(30) if (e>>i)&1]
   link_vertices.update((a,b));link_adj[a].add(b);link_adj[b].add(a)
  assert all(len(link_adj[u])==2 for u in link_vertices)
  seen={next(iter(link_vertices))};stack=list(seen)
  while stack:
   for u in link_adj[stack.pop()]:
    if u not in seen:seen.add(u);stack.append(u)
  assert len(seen)==len(link_vertices)
 return target

def main():
 data_path=sys.argv[2] if len(sys.argv)>2 else 'H3_COLLAPSES.json'
 k0,f0,a0=faces_at(0)
 assert len(f0)==20 and all(t.bit_count()==3 for t in f0)
 face_edges={t:[t^(1<<v) for v in range(30) if (t>>v)&1] for t in f0}
 multiplicity=collections.Counter(e for els in face_edges.values() for e in els)
 assert len(multiplicity)==60 and all(n==1 for n in multiplicity.values())
 removed={min(es) for es in face_edges.values()}
 graph_edges={f for f in k0 if f.bit_count()==2}-removed
 assert len(graph_edges)==40
 adjgraph=[set() for _ in range(30)]
 for edge in graph_edges:
  a,b=[v for v in range(30) if (edge>>v)&1]
  adjgraph[a].add(b);adjgraph[b].add(a)
 reached={0};todo=[0]
 while todo:
  for v in adjgraph[todo.pop()]:
   if v not in reached:reached.add(v);todo.append(v)
 assert len(reached)==30
 k1,f1,a1=faces_at(1)
 target=construct_surface(k0,k1,f1,a0)
 stages={'sphere_at_1':(k1,target)}
 for j in (2,3,4):
  f,_,_=faces_at(j)
  stages['threshold_'+str(j)]=(f,k1)
 if len(sys.argv)>1 and sys.argv[1]=='generate':
  cert={name:free_collapse(src,dst) for name,(src,dst) in stages.items()}
  with open(data_path,'w',encoding='utf-8') as out:json.dump(cert,out,separators=(',',':'),sort_keys=True);out.write('\n')
 else:
  cert=json.load(open(data_path,encoding='utf-8'))
  assert set(cert)==set(stages)
  for name,(src,dst) in stages.items():
   free_collapse(src,dst,cert[name])
 print('CERTIFIED', {name:len(cert[name]) for name in stages})
 print('F_COUNTS',{str(i):len(faces_at(i)[0]) for i in range(5)})
 print('SURFACE_F_VECTOR',[30,84,56])
 print('ROOTS',len(V),'DISTANCE_HISTOGRAM',sorted((str(k),v) for k,v in collections.Counter(DIST.values()).items()))
 print('VERIFY_OK')

if __name__=='__main__':main()
