"""Independent full root-fixing automorphism check on selected small products."""
from itertools import product
import networkx as nx
from collections import defaultdict


def run(dims):
    vs = list(product(*(range(n) for n in dims)))
    G = nx.Graph()
    for v in vs:
        G.add_node(v, root=int(all(x == 0 for x in v)))
        for i in range(len(dims)):
            if v[i] + 1 < dims[i]:
                w = v[:i] + (v[i] + 1,) + v[i + 1:]
                G.add_edge(v, w)
    colors = {v: G.nodes[v]['root'] for v in G}
    for step in range(len(vs)):
        sig = {v: (colors[v], tuple(sorted(colors[w] for w in G.neighbors(v)))) for v in G}
        names = {s:k for k,s in enumerate(sorted(set(sig.values())))}
        new = {v:names[sig[v]] for v in G}
        if len(set(new.values())) == len(set(colors.values())):
            colors = new
            break
        colors = new
    par = {v:v for v in G}
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    gm = nx.algorithms.isomorphism.GraphMatcher(G, G,
        node_match=lambda a,b: a['root']==b['root'])
    aut_count=0
    for iso in gm.isomorphisms_iter():
        aut_count+=1
        for x,y in iso.items(): par[find(x)] = find(y)
    assert all(colors[x]!=colors[y] or find(x)==find(y) for x in vs for y in vs)
    assert all(find(x)!=find(y) or colors[x]==colors[y] for x in vs for y in vs)
    return aut_count,len(set(colors.values()))

if __name__=='__main__':
    dims_list=[(2,2),(2,3),(2,2,2),(2,3,4),(2,2,2,2),(2,2,3,3),(3,3,3)]
    for dims in dims_list:
        count,classes=run(dims)
        print('PASS',dims,'automorphisms',count,'classes',classes)
