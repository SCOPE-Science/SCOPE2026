from itertools import combinations
from collections import deque
import networkx as nx

def case(m,n):
 U=[('u',i) for i in range(m)]; V=[('v',j) for j in range(n)]; E=[('e',i,j) for i in range(m) for j in range(n)];
 G=nx.Graph();G.add_nodes_from(U+V+E)
 for i in range(m):
  for j in range(n):G.add_edges_from([(U[i],('e',i,j)),(V[j],('e',i,j))])
 d=dict(nx.all_pairs_shortest_path_length(G)); R={r:nx.Graph() for r in (1,2,3,4)}
 for r,H in R.items():
  H.add_nodes_from(G); H.add_edges_from([(a,b) for a,b in combinations(G.nodes,2) if d[a][b]<=r]);
  if r==3:
   for a,b in combinations(G.nodes,2):
    cross=(a[0]=='e')!=(b[0]=='e')
    if cross: assert H.has_edge(a,b)
   for a,b in combinations(U+V,2):assert H.has_edge(a,b)==(a[0]!=b[0])
   for a,b in combinations(E,2):assert H.has_edge(a,b)==(a[1]==b[1] or a[2]==b[2])
  if r==4:assert nx.density(H)==1
 b=(m-1)*(n-1)
 N=m+n+m*n
 assert nx.cycle_basis(G).__len__()==b
 assert nx.is_connected(G)
 assert N==G.number_of_nodes()
 print('OK',m,n,'vertices',N,'graph_b1',b,'join third b3',b*b)
for m,n in [(2,2),(2,3),(3,3),(3,4),(4,5)]:case(m,n)
