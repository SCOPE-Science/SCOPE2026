"""Check the first C2-invisible orbit split for a pair of named equivalences."""
from verify_matching_cycles import incidence_graph,class_color
import networkx as nx
E=((0,1),(2,3),(4,5),(6,7),(8,9))
F=((0,2),(1,3),(4,6),(5,8),(7,9))
H=incidence_graph(E,F)
components=sorted(len(c) for c in nx.connected_components(H))
assert components==[4,6],components
assert len(class_color(E,F))==1
edge_map={}
for i,e in enumerate(E):
 for x in e:edge_map.setdefault(x,[]).append(('E',i))
for i,e in enumerate(F):
 for x in e:edge_map.setdefault(x,[]).append(('F',i))
undirected_to_x={frozenset(v):x for x,v in edge_map.items()}
parent=list(range(10))
def find(x):
 while parent[x]!=x:x=parent[x]
 return x
ct=0
for auto in nx.algorithms.isomorphism.GraphMatcher(H,H,node_match=lambda a,b:a['side']==b['side']).isomorphisms_iter():
 ct+=1
 for x,ends in edge_map.items():
  y=undirected_to_x[frozenset(auto[vertex] for vertex in ends)]
  parent[find(x)]=find(y)
orbits=sorted(Counter(find(x) for x in range(10)).values()) if False else sorted([sum(find(y)==r for y in range(10)) for r in set(find(y) for y in range(10))])
assert orbits==[4,6],orbits
print('PASS: n=10 same first-round C2 colour on every element; side-preserving automorphisms yield orbit sizes 4,6; automorphisms',ct)
