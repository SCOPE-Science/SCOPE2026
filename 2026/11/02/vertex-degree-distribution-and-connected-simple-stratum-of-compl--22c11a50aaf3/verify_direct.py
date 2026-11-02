from itertools import product,permutations
from math import factorial
from collections import Counter

def test(r,s):
 n=r+s; es=[(i,j) for i in range(n) for j in range(i+1,n) if i<r or j<r]; ed=set(es)
 ac=[]
 for x in range(1<<len(es)):
  dir_edges=[(u,v) if x>>k&1 else (v,u) for k,(u,v) in enumerate(es)]
  graph={i:[] for i in range(n)}
  for u,v in dir_edges:graph[u].append(v)
  def reachable(a,b):
   stack=[a];vis={a}
   while stack:
    w=stack.pop()
    if w==b:return True
    for t in graph[w]:
     if t not in vis:vis.add(t);stack.append(t)
   return False
  if any(reachable(v,u) for u,v in dir_edges):continue
  degree=sum(not any(reachable(u,z) and reachable(z,v) for z in range(n) if z not in (u,v)) for u,v in dir_edges)
  ac.append(degree)
 print('r,s',r,s,'actual',Counter(ac),'nac',len(ac))
 pred=Counter()
 for pp in permutations(range(r)):
  for gaps in product(range(r+1),repeat=s):
   cnt=[gaps.count(j) for j in range(r+1)]
   degree=sum(1 for i in range(1,r) if cnt[i]==0)+cnt[0]+cnt[r]+2*sum(cnt[1:r]);pred[degree]+=1
 assert Counter(ac)==pred, (r,s,Counter(ac),pred)
 assert len(ac)==factorial(r)*(r+1)**s
 print('predict',pred,'simple',pred[r+s-1])
for r,s in [(2,1),(2,2),(2,3),(3,1),(3,2)]:test(r,s)
