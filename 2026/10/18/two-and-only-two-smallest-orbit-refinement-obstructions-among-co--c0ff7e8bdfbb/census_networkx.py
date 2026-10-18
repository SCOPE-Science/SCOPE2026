#!/usr/bin/env python3
"""Independent NetworkX graph-atlas/vertex-augmentation verification.
Requires NetworkX >= 2.8.  All isomorphism and orbit checks are exact.
"""
import collections
import itertools
import json
import networkx as nx


def cactus(g):
    if not nx.is_connected(g):return False
    for comp in nx.biconnected_components(g):
        k=len(comp)
        if k>2 and g.subgraph(comp).number_of_edges()!=k:return False
    return True


def color_refinement(g):
    cc={u:0 for u in g}
    for _ in range(len(g)):
        ss={u:(cc[u],tuple(sorted(cc[v] for v in g.neighbors(u)))) for u in g}
        colors={s:i for i,s in enumerate(sorted(set(ss.values())))}
        dd={u:colors[ss[u]] for u in g}
        if all((cc[u]==cc[v])==(dd[u]==dd[v]) for u,v in itertools.combinations(g.nodes,2)):
            return dd
        cc=dd
    raise RuntimeError('colour refinement exceeded vertex count')


def same_orbit(g,u,v):
    a=g.copy();b=g.copy()
    nx.set_node_attributes(a,{x:x==u for x in g},'mark')
    nx.set_node_attributes(b,{x:x==v for x in g},'mark')
    return nx.is_isomorphic(a,b,node_match=lambda x,y:x['mark']==y['mark'])


def nonrefinable(g):
    c=color_refinement(g)
    for u,v in itertools.combinations(g.nodes,2):
        if c[u]==c[v] and not same_orbit(g,u,v):return True
    return False


def edge_form(g):
    return sorted([sorted((int(a),int(b))) for a,b in g.edges()])


def main():
    levels={n:[] for n in range(1,8)}
    for g in nx.graph_atlas_g():
        if 1<=len(g)<=7 and cactus(g):levels[len(g)].append(g)
    assert [len(levels[n]) for n in range(1,8)]==[1,1,2,4,9,23,63]
    all8=[]
    bykey=collections.defaultdict(list)
    for g in levels[7]:
        for neighbor_mask in range(1,1<<7):
            h=g.copy();h.add_node(7)
            h.add_edges_from((i,7) for i in range(7) if (neighbor_mask>>i)&1)
            if not cactus(h):continue
            key=(h.number_of_edges(),tuple(sorted(dict(h.degree()).values())))
            if not any(nx.is_isomorphic(h,z) for z in bykey[key]):
                bykey[key].append(h);all8.append(h)
    assert len(all8)==188
    issues=[]
    for g in all8:
        if nonrefinable(g):issues.append(g)
    assert len(issues)==2
    assert sorted(g.number_of_edges() for g in issues)==[9,10]
    print(json.dumps({'atlas_counts':[len(levels[n]) for n in range(1,8)],'eight_vertex_types':len(all8),
        'eight_vertex_nonrefinable':len(issues),'witnesses':[edge_form(g) for g in sorted(issues,key=lambda g:g.number_of_edges())]},sort_keys=True))

if __name__=='__main__': main()
