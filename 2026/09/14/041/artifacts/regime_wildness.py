"""Recovery test: is the no-maximal-SIL regime uniformly tractable?
For random graphs in the regime (>=1 SIL, every SIL-pair joined outside lk-cap-lk):
  - count transvections (strict), check support-graph forests (Day-Wade condition),
  - verify Wiedmer Gamma(Lambda) control cases.
Wildness (transvections / non-forest support graphs in-regime) evidences that no
uniform JSJ/HNN or PSO=RAAG argument can cover the whole regime.
"""
import itertools, json, random
import networkx as nx

def link(G,v): return set(G.neighbors(v))
def star(G,v): return set(G.neighbors(v))|{v}

def sil_pairs(G):
    out=[]
    for a,b in itertools.combinations(G.nodes(),2):
        if G.has_edge(a,b): continue
        H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
        if any((a not in C and b not in C) for C in nx.connected_components(H)):
            out.append((a,b))
    return out

def vw_path(G,a,b):
    H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
    return H.has_node(a) and H.has_node(b) and nx.has_path(H,a,b)

def in_regime(G):
    s=sil_pairs(G)
    return len(s)>=1 and all(vw_path(G,a,b) for a,b in s)

def strict_transvections(G):
    return [(u,w) for u in G.nodes() for w in G.nodes()
            if u!=w and link(G,u)<=star(G,w)]

def support_forest_status(G):
    """Return (all_forest, bad_vertex_count). S_v: nodes=comps of G-st(v);
    edge A-B iff exists b in B with A a component of G-st(b) (or vice versa)."""
    bad=0
    for v in G.nodes():
        rest=set(G.nodes())-star(G,v)
        if not rest: continue
        H=G.subgraph(rest)
        comps=[set(c) for c in nx.connected_components(H)]
        idx={frozenset(c):i for i,c in enumerate(comps)}
        S=nx.Graph(); S.add_nodes_from(range(len(comps)))
        for i,A in enumerate(comps):
            for j,B in enumerate(comps):
                if j<=i: continue
                edge=False
                for b in B:
                    Hb=G.subgraph(set(G.nodes())-star(G,b))
                    if any(set(c)==A for c in nx.connected_components(Hb)):
                        edge=True; break
                if not edge:
                    for a in A:
                        Ha=G.subgraph(set(G.nodes())-star(G,a))
                        if any(set(c)==B for c in nx.connected_components(Ha)):
                            edge=True; break
                if edge: S.add_edge(i,j)
        if not nx.is_forest(S): bad+=1
    return bad==0, bad

random.seed(20260914)
regime_stats=[]
wild_trans=0; wild_nonforest=0; n_regime=0
for trial in range(400):
    n=random.choice([6,7,8])
    p=random.choice([0.25,0.35,0.5,0.65])
    G=nx.erdos_renyi_graph(n,p,seed=trial)
    if G.number_of_edges()==0: continue
    if not in_regime(G): continue
    n_regime+=1
    st=strict_transvections(G)
    forest,bad=support_forest_status(G)
    if st: wild_trans+=1
    if not forest: wild_nonforest+=1
    regime_stats.append({"n":n,"p":p,"nsil":len(sil_pairs(G)),
                         "ntrans":len(st),"support_all_forest":forest,
                         "bad_vertices":bad})
print(f"regime graphs found: {n_regime}/400")
print(f"with strict transvections: {wild_trans}")
print(f"with non-forest support graph: {wild_nonforest}")
for r in regime_stats[:15]:
    print(json.dumps(r))
with open("output/artifacts/regime_wildness.json","w") as f:
    json.dump({"n_regime":n_regime,"wild_trans":wild_trans,
               "wild_nonforest":wild_nonforest,"examples":regime_stats[:40]},f,indent=1)
print("saved")
