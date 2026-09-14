"""Build Wiedmer Gamma(Lambda) (first construction, n>=3) and test SIL/no-maximal
structure + acylindrical hyperbolicity proxies.
Refs: Wiedmer arXiv:2209.02033 Sec 3 (Fig 3.1); Baik-Kim arXiv:2405.19702 Def 2.5,
Lemma 3.6, Remark 3.7.
"""
import itertools, json
import networkx as nx

def build_gamma(Lambda):
    # Lambda: nx Graph with vertices 0..n-1
    n = Lambda.number_of_nodes()
    G = nx.Graph()
    vs = [f"v{i}" for i in range(n)]
    cs = [f"c{i}" for i in range(n)]
    extra = ["a1","a2","b1","b2","d1","d2"]
    G.add_nodes_from(vs+cs+extra)
    # Lambda edges among v's
    for u,v in Lambda.edges():
        G.add_edge(f"v{u}", f"v{v}")
    # gadget edges (Fig 3.1 description)
    G.add_edges_from([("b1","a1"),("b2","a2"),("a1","a2")])
    for v in vs:
        G.add_edges_from([(v,"b1"),(v,"b2")])
    for i in range(n):
        ci = f"c{i}"
        G.add_edges_from([(ci,"d1"),(ci,"d2"),(ci,f"v{i}"),(ci,f"v{(i+1)%n}")])
    G.add_edge("d1","b1"); G.add_edge("d2","b2")
    G.add_edge("d1","v0")
    for j in range(1,n):
        G.add_edge("d2",f"v{j}")
    for c in cs:
        G.add_edge("d1",c); G.add_edge("d2",c)
    # d1 connected to all ci and v1; d2 to all ci and vj j>1 (done above)
    return G

def link(G,v): return set(G.neighbors(v))
def star(G,v): return set(G.neighbors(v))|{v}

def sil_pairs(G):
    out=[]
    for a,b in itertools.combinations(G.nodes(),2):
        if G.has_edge(a,b): continue
        H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
        # SIL iff some component contains neither a nor b
        comps=list(nx.connected_components(H))
        if any((a not in C and b not in C) for C in comps):
            out.append((a,b))
    return out

def has_vw_path_outside_int(G,a,b):
    H=G.copy(); H.remove_nodes_from(link(G,a)&link(G,b))
    try: return nx.has_path(H,a,b)
    except Exception: return False

def check(G,label):
    sils=sil_pairs(G)
    bad=[(a,b) for (a,b) in sils if not has_vw_path_outside_int(G,a,b)]
    # transvections: lk(u)<=st(w), u!=w
    trans=[(u,w) for u in G.nodes() for w in G.nodes() if u!=w and link(G,u)<=star(G,w)]
    # support-graph forest check via number of star-complement components per vertex
    ncomp={v: nx.number_connected_components(G.subgraph(set(G.nodes())-star(G,v))) if len(set(G.nodes())-star(G,v))>0 else 0 for v in G.nodes()}
    return {"label":label,"n":G.number_of_nodes(),"nsil":len(sils),
            "nsil_no_path":len(bad),"ntrans":len(trans),
            "max_starcomp":max(ncomp.values()),
            "two_comp_vertices":[v for v,c in ncomp.items() if c==2]}

results=[]
tests={
 "empty3": nx.empty_graph(3),
 "edge+isolated": nx.Graph([(0,1)]),
 "path3": nx.path_graph(3),
 "complete3": nx.complete_graph(3),
 "empty4": nx.empty_graph(4),
 "cycle4": nx.cycle_graph(4),
 "path4": nx.path_graph(4),
 "star4": nx.star_graph(3),
 "complete4": nx.complete_graph(4),
 "disconn4": nx.Graph([(0,1),(2,3)]),
 "empty5": nx.empty_graph(5),
 "tree5": nx.Graph([(0,1),(1,2),(2,3),(3,4)]),
}
for label,L in tests.items():
    L=nx.convert_node_labels_to_integers(L)
    G=build_gamma(L)
    r=check(G,label)
    results.append(r)
    print(json.dumps(r))
with open("output/artifacts/wiedmer_scan.json","w") as f:
    json.dump(results,f,indent=1)
print("saved")
