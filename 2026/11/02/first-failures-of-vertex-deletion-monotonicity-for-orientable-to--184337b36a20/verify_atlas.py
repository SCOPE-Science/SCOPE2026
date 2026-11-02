import networkx as nx
from itertools import combinations
from functools import lru_cache

@lru_cache(None)
def value(n,edges):
    m=len(edges); best=-1; full=(1<<n)-1
    subsets=sorted(range(1,1<<n), key=int.bit_count)
    for code in range(1<<m):
        ins=[0]*n
        for j,(u,v) in enumerate(edges):
            if code>>j&1:u,v=v,u
            ins[v] |= 1<<u
        if any(x==0 for x in ins):continue
        k=next(s.bit_count() for s in subsets if all(ins[v]&s for v in range(n)))
        best=max(best,k)
    return best

R=[]
for graph in nx.graph_atlas_g():
    if graph.number_of_nodes()!=6:continue
    G=nx.convert_node_labels_to_integers(graph)
    n=6
    ed=tuple(sorted(tuple(sorted(e)) for e in G.edges()))
    high=value(n,ed)
    if high!=5:continue
    for v in G.nodes:
        H=nx.convert_node_labels_to_integers(G.copy().subgraph(x for x in range(6) if x!=v))
        e2=tuple(sorted(tuple(sorted(e)) for e in H.edges()))
        if value(5,e2)==3:R.append((G,v))
classes=[]
for G,v in R:
    A=G.copy();nx.set_node_attributes(A,{x:int(x==v) for x in A.nodes()},'marked')
    if not any(nx.is_isomorphic(A,B,node_match=lambda x,y:x['marked']==y['marked']) for B in classes):classes.append(A)
print('ATLAS_PAIR_CLASSES',len(classes),'ATLAS_PAIRS',len(R))
assert len(classes)==18
