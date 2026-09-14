"""Wiedmer rigidified construction Gamma'(Lambda) (Thm 3.4, Fig 3.3) checks:
no-transvection (finite-index cond Thm 2.2), SIL census, no-maximal regime test.
Edge list per p.11 text; ambiguities noted.
"""
import itertools, json
import networkx as nx

def build_gamma_prime(Lambda):
    n = Lambda.number_of_nodes()
    G = nx.Graph()
    vs = [f"v{i}" for i in range(n)]
    cs = [f"c{i}" for i in range(n)]
    G.add_nodes_from(vs+cs+["a1","a2","a3","b1","b2","b3","d1","d2","d3"])
    for u,v in Lambda.edges():
        G.add_edge(f"v{u}", f"v{v}")
    # a-triangle + b-a
    G.add_edges_from([("a1","a2"),("a1","a3"),("a2","a3"),
                      ("b1","a1"),("b2","a2"),("b3","a3")])
    for v in vs:
        G.add_edges_from([(v,"b1"),(v,"b2"),(v,"b3")])
    for i in range(n):
        G.add_edges_from([(f"c{i}",f"v{i}"),(f"c{i}",f"v{(i+1)%n}")])
        for d in ["d1","d2","d3"]:
            G.add_edge(f"c{i}",d)
    G.add_edge("d1","v0"); G.add_edge("d1","b1")
    G.add_edge("d2","v1"); G.add_edge("d2","d3")
    for k in range(2,n):
        G.add_edge("d3",f"v{k}")
    G.add_edge("d3","b3")
    return G

def link(G,v): return set(G.neighbors(v))
def star(G,v): return set(G.neighbors(v))|{v}

def sil_pairs(G):
    out=[]
    for a,b in itertools.combinations(sorted(G.nodes()),2):
        if G.has_edge(a,b): continue
        H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
        if any((a not in C and b not in C) for C in nx.connected_components(H)):
            out.append((a,b))
    return out

def vw_path(G,a,b):
    H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
    return H.has_node(a) and H.has_node(b) and nx.has_path(H,a,b)

def graph_aut_order_bound(G):
    # cheap invariant: degree-sequence signature per layer; just report #perms of first construction is skipped;
    return None

tests = {
 "empty3": nx.empty_graph(3), "path3": nx.path_graph(3),
 "complete3": nx.complete_graph(3), "empty4": nx.empty_graph(4),
 "cycle4": nx.cycle_graph(4), "path4": nx.path_graph(4),
 "complete4": nx.complete_graph(4), "disconn4": nx.Graph([(0,1),(2,3)]),
 "empty5": nx.empty_graph(5), "tree5": nx.path_graph(5),
 "join2+2": nx.complete_bipartite_graph(2,2),  # C4 = join? no; K_{2,2} is join of 2+2 empties
 "joinK2_K1": nx.complete_graph(3),
}
rows=[]
for label,L in tests.items():
    L=nx.convert_node_labels_to_integers(L)
    G=build_gamma_prime(L)
    sils=sil_pairs(G)
    bad=[(a,b) for (a,b) in sils if not vw_path(G,a,b)]
    trans=[(u,w) for u in G.nodes() for w in G.nodes() if u!=w and link(G,u)<=star(G,w)]
    # RAAG criterion for Lambda: acyl-hyp iff |V|>=2 and not a join
    is_join = nx.number_connected_components(nx.complement(L))>1 if L.number_of_nodes()>=2 else True
    rows.append({"Lambda":label,"nG":G.number_of_nodes(),"nsil":len(sils),
                 "nsil_no_path":len(bad),"ntrans":len(trans),
                 "Lambda_is_join":bool(is_join),
                 "Lambda_RAAG_acylhyp":bool(L.number_of_nodes()>=2 and not is_join)})
    print(json.dumps(rows[-1]))
with open("output/artifacts/gammaprime_scan.json","w") as f: json.dump(rows,f,indent=1)
print("saved")
