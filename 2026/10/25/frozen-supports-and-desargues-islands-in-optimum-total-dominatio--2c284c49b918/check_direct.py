#!/usr/bin/env python3
"""Independent brute-force board verifier for optimum total domination and one-exchange components."""
import itertools,json,collections,hashlib,networkx as nx

def study(rows,cols):
  assert rows>=cols>=3
  positions=range(rows*cols)
  board=[(v//cols,v%cols) for v in positions]
  neighbor=[sum(1<<v for v,(r2,c2) in enumerate(board) if v!=u and (r2==r or c2==c)) for u,(r,c) in enumerate(board)]
  good=[]
  for comb in itertools.combinations(positions,cols):
    bits=sum(1<<x for x in comb)
    if all(neighbor[x]&bits for x in positions):good.append(bits)
  indices={x:i for i,x in enumerate(good)}
  H=nx.Graph(); H.add_nodes_from(range(len(good)))
  for a,i in indices.items():
    for u in positions:
      if a>>u&1:
        for v in positions:
          if not a>>v&1:
            b=a^(1<<u)^(1<<v)
            if b in indices and indices[b]>i:H.add_edge(i,indices[b])
  components=list(nx.connected_components(H))
  sz=collections.Counter(map(len,components))
  dis=collections.Counter(dict(H.degree()).values())
  return {'rows':rows,'cols':cols,'count':len(good),'edge_count':H.number_of_edges(),'component_sizes':sorted(sz.items()),'degree_profile':sorted(dis.items())},H

if __name__=='__main__':
  for n,m in [(3,3),(4,3),(4,4),(5,4),(5,5),(6,5)]:
    stat,H=study(n,m)
    if (n,m)==(5,5):
      cs=[H.subgraph(c) for c in nx.connected_components(H) if len(c)>1]
      assert len(cs)==20 and all(nx.is_isomorphic(Q,nx.desargues_graph()) for Q in cs)
      stat['nontrivial_is_desargues']=True
    print(json.dumps(stat,sort_keys=True))
