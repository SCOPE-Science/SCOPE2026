import networkx as nx
from itertools import combinations

def check(n,m):
 G=nx.Graph();V=[(i,a) for i in range(n) for a in range(m)];G.add_nodes_from(V)
 for x,y in combinations(V,2):
  d=min((x[0]-y[0])%n,(y[0]-x[0])%n)+(x[1]!=y[1])
  if d<=2:G.add_edge(x,y)
 faces=set()
 for M in nx.find_cliques(G):
  for k in range(1,len(M)+1):
   for s in combinations(M,k): faces.add(frozenset(s))
 initial=len(faces);pairs=0
 def remove(lower,upper):
  nonlocal pairs
  assert lower in faces and upper in faces and len(upper)==len(lower)+1
  # other cofaces would mean lower is not free
  for f in faces:
   if lower<f and f!=upper:raise AssertionError((n,m,lower,upper,f))
  faces.remove(lower);faces.remove(upper);pairs+=1
 for i in range(n):
  mid=[(i,b) for b in range(m)]; pivot=mid[0]
  for a in range(m):
   edge=frozenset({((i-1)%n,a),((i+1)%n,a)})
   for k in range(m-1,-1,-1):
    for ss in combinations(mid[1:],k):
     lower=edge|frozenset(ss);upper=lower|{pivot};remove(lower,upper)
 for i in range(n):
  pivot=(i,0)
  for a in range(1,m):
   v=(i,a)
   # match arbitrary simplices containing v but not pivot to same simplex plus pivot
   lower=[f for f in faces if v in f and pivot not in f]
   lower.sort(key=len,reverse=True)
   for f in lower: remove(f,f|{pivot})
 target={frozenset({(i,0)}) for i in range(n)}|{frozenset({(i,0),((i+1)%n,0)}) for i in range(n)}
 assert faces==target,(n,m,faces^target)
 count=n*(2**(2*m)+(m-1)*2**m-2)//2
 assert pairs==count and initial==2*n+2*count
 print('PASS',n,m,'faces',initial,'pairs',pairs,'max_dim',nx.graph_clique_number(G) - 1 if hasattr(nx,'graph_clique_number') else max(map(len,nx.find_cliques(G)))-1)
for n,m in [(7,3),(8,3),(9,3),(7,4),(8,4),(7,5)]:check(n,m)
