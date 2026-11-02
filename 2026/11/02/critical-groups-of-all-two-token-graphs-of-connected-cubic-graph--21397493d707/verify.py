"""Exact finite critical-group census for two-token graphs of cubic order eight.
Requires networkx and sympy; no external files or network access.
"""
from itertools import combinations
from collections import Counter
import networkx as nx
from sympy import Matrix, factorint, prod
from sympy.matrices.normalforms import hermite_normal_form

REPRESENTATIVES = [
[(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,7),(4,7),(5,6),(6,7)]]
EXPECTED = [
[2,2,4,4,8,8,136,12512,6193440],
[2,2,4,4,36,936,33603216192],
[10,3727350,2269956150],
[2]*6+[4]*2+[8,16,64,64,192,960,960],
[2,2,4,4,16,1790768,53723040]]

def all_cubics():
 """Recursion enumerates each labeled simple cubic graph exactly once."""
 reps=[];labeled=0;connected=0
 def rec(deg,edges):
  nonlocal labeled,connected
  if not any(deg):
   labeled+=1
   G=nx.Graph();G.add_nodes_from(range(8));G.add_edges_from(edges)
   if not nx.is_connected(G):return
   connected+=1
   if not any(nx.is_isomorphic(G,H) for H in reps):reps.append(G)
   return
  u=next(i for i in range(8) if deg[i])
  can=[v for v in range(u+1,8) if deg[v]]
  if len(can)<deg[u]:return
  for vv in combinations(can,deg[u]):
   d=deg.copy();d[u]=0
   for v in vv:d[v]-=1
   rec(d,edges+[(u,v) for v in vv])
 rec([3]*8,[])
 return labeled,connected,reps

def token_graph(G):
 states=list(combinations(range(8),2)); T=nx.Graph();T.add_nodes_from(range(28))
 for a in range(28):
  for b in range(a+1,28):
   d=set(states[a])^set(states[b])
   if len(d)==2 and G.has_edge(*d): T.add_edge(a,b)
 return T

def valuation(a,p,Qmax):
 if not a:return Qmax
 v=0
 while a%p==0:a//=p;v+=1
 return v

def diagonal_p_valuations(A,p,E):
 # Gauss elimination over the finite ring Z/p^(E+1); row/column operations
 # with unit multipliers and invertible pivots are unimodular over that ring.
 modulus=p**(E+1);B=[r[:] for r in A];N=len(B);res=[]
 for i in range(N):
  v,r,c=min((valuation(B[j][k],p,E+1),j,k) for j in range(i,N) for k in range(i,N))
  assert v<=E,('rank loss',p,i)
  B[i],B[r]=B[r],B[i]
  for j in range(N):B[j][i],B[j][c]=B[j][c],B[j][i]
  q=modulus//(p**v)
  inv=pow((B[i][i]//(p**v))%q,-1,q)
  for j in range(i+1,N):
   mult=((B[j][i]//(p**v))*inv)%q
   for k in range(i,N):B[j][k]=(B[j][k]-mult*B[i][k])%modulus
  for k in range(i+1,N):
   mult=((B[i][k]//(p**v))*inv)%q
   for j in range(i,N):B[j][k]=(B[j][k]-mult*B[j][i])%modulus
  res.append(v)
 assert res==sorted(res)
 return res

def run():
 labeled,connected,classes=all_cubics()
 assert (labeled,connected,len(classes))==(19355,19320,5),(labeled,connected,len(classes))
 assert all(sum(nx.triangles(H).values())//3 in (0,1,2,4) for H in classes)
 print('CUBIC_CLASS_CENSUS_OK',labeled,connected,len(classes))
 graphs=[]
 for e in REPRESENTATIVES:
  G=nx.Graph();G.add_nodes_from(range(8));G.add_edges_from(e)
  assert nx.is_connected(G) and set(dict(G.degree()).values())=={3}
  graphs.append(G)
 assert all(any(nx.is_isomorphic(H,G) for G in graphs) for H in classes)
 assert all(not nx.is_isomorphic(graphs[a],graphs[b]) for a in range(5) for b in range(a+1,5))
 for i,G in enumerate(graphs):
  T=token_graph(G)
  assert (T.number_of_nodes(),T.number_of_edges())==(28,72)
  assert Counter(dict(T.degree()).values())==Counter({4:12,6:16})
  A=Matrix(nx.laplacian_matrix(T).toarray().tolist())[:-1,:-1]
  H=hermite_normal_form(A)
  determinant=int(prod(H[j,j] for j in range(27)))
  factors=factorint(determinant)
  pparts={p:diagonal_p_valuations(A.tolist(),p,e) for p,e in factors.items()}
  assert all(sum(pparts[p])==e for p,e in factors.items())
  smith=[int(prod(p**pparts[p][j] for p in factors)) for j in range(27)]
  assert all(smith[j+1]%smith[j]==0 for j in range(26))
  assert int(prod(smith))==determinant
  nontrivial=[x for x in smith if x>1]
  assert nontrivial==EXPECTED[i],(i,nontrivial,EXPECTED[i])
  print(f'CLASS_{i+1}_OK triangles={sum(nx.triangles(G).values())//3} trees={determinant} invariant_factors={nontrivial}',flush=True)
 print('COMPLETE_CUBIC_EIGHT_TOKEN_CRITICAL_GROUP_CENSUS_OK')
if __name__=='__main__':run()
