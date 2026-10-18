"""Cross-check exceptional graphs from independently generated records."""
import ast,networkx as nx
from pathlib import Path
P=Path(__file__).parent

def records(name):
  result=[]
  for line in (P/name).read_text().splitlines():
    if line.startswith('witness '):
      E=ast.literal_eval(line[line.index('edges ')+6:]);G=nx.Graph();G.add_nodes_from(range(8));G.add_edges_from(E)
      result.append(G)
  return result
A,B=records('recursive_census.out'),records('atlas_census.out')
assert len(A)==len(B)==2
assert all(sum(nx.is_isomorphic(g,h) for h in B)==1 for g in A)
C=nx.disjoint_union(nx.complete_graph(3),nx.cycle_graph(4))
D=nx.complement(C)
models=[]
for H in [C,D]:
  K=nx.Graph();K.add_nodes_from(range(8));K.add_edges_from(H.edges());K.add_edges_from((7,i) for i in range(7));models.append(K)
assert all(sum(nx.is_isomorphic(g,h) for h in models)==1 for g in A+B)
print('all_exceptional_types_agree_across_censuses')
print('model_edge_counts',[len(g.edges()) for g in models])
