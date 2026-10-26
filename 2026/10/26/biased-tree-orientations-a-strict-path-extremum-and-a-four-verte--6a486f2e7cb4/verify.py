from fractions import Fraction as F
from itertools import product
import networkx as nx

def formula(G,p):
 q=1-p; d=dict(G.degree()); h=lambda k:(p*q)**k; g=lambda k:q*p**(k-1)+p*q**(k-1)
 return sum(g(d[u]+d[v]) for u,v in G.edges())-sum(h(x) for x in d.values())

def brute(G,p):
 q=1-p; A=set(nx.bipartite.color(G,color={0:0}) if False else [])
 c=nx.bipartite.color(G); edges=list(G.edges()); dist={}
 for bits in product((0,1),repeat=len(edges)):
  prob=F(1); indeg={v:0 for v in G}; outdeg={v:0 for v in G}
  for (u,v),bit in zip(edges,bits):
   a,b=(u,v) if (c[u]==0)==bool(bit) else (v,u)
   prob*=p if bit else q
   outdeg[a]+=1;indeg[b]+=1
  s=sum(v==0 for v in indeg.values());k=sum(v==0 for v in outdeg.values());dist[(s,k)]=dist.get((s,k),0)+prob
 ES=sum(s*x for(s,k),x in dist.items());EK=sum(k*x for(s,k),x in dist.items());ESK=sum(s*k*x for(s,k),x in dist.items()); return ESK-ES*EK

for n in range(2,9):
 for G in nx.generators.nonisomorphic_trees(n):
  for p in (F(1,3),F(2,5),F(1,2)):
   assert formula(G,p)==brute(G,p),(n,p,G.edges())
   if n>=4 and sorted(dict(G.degree()).values())!=sorted(dict(nx.path_graph(n).degree()).values()):
    assert formula(nx.path_graph(n),p)>formula(G,p),(n,p)
 print('EXACT_TREE_ORDER_PASS',n)
print('VERIFY_OK')
