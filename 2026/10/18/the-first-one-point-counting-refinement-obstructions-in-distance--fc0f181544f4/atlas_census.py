"""Atlas-seeded independent one-step census: no dependence on recursive_census.py.
Run: python atlas_census.py. Requires NetworkX 3.x."""
import networkx as nx
from functools import lru_cache
from collections import defaultdict

@lru_cache(None)
def is_dh(edge_code):
    # Hereditary reverse of pendant/true-twin/false-twin construction.
    n, encoded = edge_code
    G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(encoded)
    if n == 1: return True
    if not nx.is_connected(G): return False
    for v in G:
        if len(G[v]) == 1 or any((set(G[v])-{u}) == (set(G[u])-{v}) for u in G if u != v):
            H = nx.convert_node_labels_to_integers(nx.subgraph(G, set(G)-{v}),ordering='sorted')
            if len(H) and nx.is_connected(H) and is_dh((n-1,tuple(sorted(tuple(sorted(e)) for e in H.edges())))):
                return True
    return False

def k(G):
    return (len(G.edges), nx.weisfeiler_lehman_graph_hash(G), tuple(sorted(dict(G.degree()).values())))

def dedup(graphs):
    buckets=defaultdict(list)
    for G in graphs:
        grp=buckets[k(G)]
        if not any(nx.is_isomorphic(G,H) for H in grp): grp.append(G)
    return [G for group in buckets.values() for G in group]

def rooted_fail(G,root):
    # Equitable refinement via neighbour counts, plus pointed *existence* test
    # for each same-colour pair: distinct from full automorphism enumeration.
    n=len(G); cls={v:int(v==root) for v in G}
    while True:
        tags=sorted(set(cls.values()))
        signatures={v:(cls[v],tuple(sum(cls[u]==j for u in G[v]) for j in tags)) for v in G}
        enum={s:i for i,s in enumerate(sorted(set(signatures.values())))}
        nxt={v:enum[signatures[v]] for v in G}
        if all((cls[a]==cls[b])==(nxt[a]==nxt[b]) for a in G for b in G):
            cls=nxt;break
        cls=nxt
    H=G.copy();nx.set_node_attributes(H,{v: int(v==root) for v in H},'root')
    # Testing one representative against every other member of its colour
    # is sufficient: automorphism orbit equivalence is an equivalence relation.
    classes={}
    for v,color in cls.items():classes.setdefault(color,[]).append(v)
    for vertices in classes.values():
        if len(vertices)<2:continue
        a=vertices[0]
        K=H.copy(); nx.set_node_attributes(K,{v:int(v==a) for v in K},'test')
        for b in vertices[1:]:
            L=H.copy(); nx.set_node_attributes(L,{v:int(v==b) for v in L},'test')
            matched=nx.algorithms.isomorphism.GraphMatcher(K,L,
               node_match=nx.algorithms.isomorphism.categorical_node_match(['root','test'],[0,0])).is_isomorphic()
            if not matched:return True
    return False

def main():
    atlas = nx.graph_atlas_g()
    historical=[]
    for n in range(1,8):
        layer=[nx.convert_node_labels_to_integers(G) for G in atlas if len(G)==n and nx.is_connected(G) and is_dh((n,tuple(sorted(tuple(sorted(e)) for e in G.edges()))))]
        historical.append(layer)
        print(f'atlas n={n} graphs={len(layer)}',flush=True)
    seven=historical[-1]
    assert [len(x) for x in historical]==[1,1,2,6,18,73,308]
    eight=[]
    for G in seven:
        for u in G:
            nbr=set(G[u])
            for S in [{u},{u}|nbr,nbr]:
                if not S:continue
                H=G.copy();H.add_node(7);H.add_edges_from((7,v) for v in S);eight.append(H)
    eight=dedup(eight)
    print('eight graph types',len(eight),flush=True)
    assert len(eight)==1484
    bad=[]
    for i,G in enumerate(eight):
        roots=[r for r in G if rooted_fail(G,r)]
        if roots:bad.append((G,roots))
    print('eight failing graph types',len(bad),'failing_rootings',sum(len(r) for _,r in bad),flush=True)
    for G,roots in bad:
        print('witness', 'root',roots, 'edges',sorted(tuple(sorted(e)) for e in G.edges()),flush=True)
    assert len(bad)==2 and sum(len(r) for _,r in bad)==2
if __name__=='__main__':main()
