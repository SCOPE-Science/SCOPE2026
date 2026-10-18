"""Verify the two explicit rooted counterexamples and their graph structures."""
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

def orbits(G,r):
    H=G.copy();nx.set_node_attributes(H,{u:int(u==r) for u in H},'r')
    M=GraphMatcher(H,H,node_match=nx.algorithms.isomorphism.categorical_node_match('r',0))
    parent=list(G)
    def find(u):
        while parent[u]!=u:u=parent[u]
        return u
    for mapping in M.isomorphisms_iter():
        for u in G: parent[find(u)]=find(mapping[u])
    classes={}
    for u in G:classes.setdefault(find(u),set()).add(u)
    return sorted((sorted(c) for c in classes.values()),key=lambda c:(len(c),c))

def refinement(G,r):
    groups={u:int(u==r) for u in G}
    while True:
        signatures={u:(groups[u],tuple(sorted(groups[v] for v in G[u]))) for u in G}
        tab={s:i for i,s in enumerate(sorted(set(signatures.values())))}
        nxt={u:tab[signatures[u]] for u in G}
        if all((groups[u]==groups[v])==(nxt[u]==nxt[v]) for u in G for v in G):break
        groups=nxt
    parts={}
    for u in G:parts.setdefault(groups[u],[]).append(u)
    return sorted((sorted(x) for x in parts.values()),key=lambda c:(len(c),c))

A=nx.disjoint_union(nx.complete_graph(3),nx.cycle_graph(4))
B=nx.complement(A)
for label,F in [('direct',A),('complement',B)]:
    G=nx.Graph();G.add_nodes_from(range(8));G.add_edges_from(F.edges());G.add_edges_from((7,u) for u in range(7))
    P=refinement(G,7);O=orbits(G,7)
    print(label, 'nodes',len(G), 'edges',len(G.edges()),'pointed_classes',list(map(len,P)), 'rooted_orbits',list(map(len,O)))
    assert list(map(len,P))==[1,7]
    assert list(map(len,O))==[1,3,4]
    assert len(G.edges())==(14 if label=='direct' else 21)
print('explicit_witnesses_verified')
