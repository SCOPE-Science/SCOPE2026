#!/usr/bin/env python3
"""Separate surjection-side enumeration and connectivity verification, without board adjacency."""
import itertools,collections,json,math,networkx as nx

def profile(m,r):
  states=[x for x in itertools.product(range(r),repeat=m) if min(x.count(j) for j in range(r))>=2]
  lookup={s:i for i,s in enumerate(states)}
  edges=set()
  for i,s in enumerate(states):
    for p in range(m):
      if s.count(s[p])<3: continue
      for j in range(r):
        if j!=s[p]:
          t=s[:p]+(j,)+s[p+1:]
          k=lookup[t]
          if i<k:edges.add((i,k))
  g=nx.Graph();g.add_nodes_from(range(len(states)));g.add_edges_from(edges)
  degree_ok=all(g.degree(i)==(r-1)*sum(s.count(j) for j in range(r) if s.count(j)>=3) for i,s in enumerate(states))
  return {'m':m,'r':r,'states':len(states),'edges':len(edges),'components':nx.number_connected_components(g),'degree_formula':degree_ok,'regular_degree':(next(iter(dict(g.degree()).values())) if len(set(dict(g.degree()).values()))==1 else None)},g

def theoretical(n,m):
  ct=0;edges=0; comp=0; shapes=collections.Counter()
  for r in range(1,m//2+1):
    data,g=profile(m,r)
    ways=math.comb(n,r)
    ct+=ways*data['states'];edges+=ways*data['edges'];comp+=ways*data['components']
    for c in nx.connected_components(g):shapes[len(c)]+=ways
  scale=2 if n==m else 1
  return {'rows':n,'cols':m,'count':ct*scale,'edge_count':edges*scale,'component_sizes':sorted((k,v*scale) for k,v in shapes.items())}

if __name__=='__main__':
  for m in range(3,9):
    for r in range(1,m//2+1):
      data,g=profile(m,r)
      assert data['degree_formula']
      assert data['components']==(data['states'] if m==2*r or r==1 else 1)
      if m==5 and r==2:assert nx.is_isomorphic(g,nx.desargues_graph())
      print(json.dumps(data,sort_keys=True))
    print('TOTAL',json.dumps(theoretical(m,m),sort_keys=True))
