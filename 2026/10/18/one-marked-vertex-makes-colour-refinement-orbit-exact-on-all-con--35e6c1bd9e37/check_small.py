"""Reproduce finite colour-refinement/orbit checks for rooted block graphs."""
import itertools
import collections
import random
import networkx as nx


def refinement(G, initial):
    colors=dict(initial)
    while True:
        keys={v:(colors[v],tuple(sorted(collections.Counter(colors[w] for w in G[v]).items()))) for v in G}
        types={x:i for i,x in enumerate(sorted(set(keys.values())))}
        nxt={v:types[keys[v]] for v in G}
        if len(set(nxt.values()))==len(set(colors.values())):return nxt
        colors=nxt


def orbit_equiv(G, colors, u, v):
    A=G.copy();B=G.copy()
    for x in G:
        A.nodes[x]['w']=(colors[x],int(x==u))
        B.nodes[x]['w']=(colors[x],int(x==v))
    return nx.is_isomorphic(A,B,node_match=lambda a,b:a['w']==b['w'])


def verify(G, initial):
    stable=refinement(G, initial)
    cells=collections.defaultdict(list)
    for v,c in stable.items():cells[c].append(v)
    for members in cells.values():
        for v in members[1:]:
            if not orbit_equiv(G,initial,members[0],v):
                return False,(members[0],v)
    return True,None


def block_graphs(up_to):
    by={1:[nx.empty_graph(1)]}
    for n in range(2,up_to+1):
        seen=collections.defaultdict(list);result=[]
        for x,gs in by.items():
            if x>=n:continue
            for H in gs:
                for apex in H:
                    G=H.copy()
                    extra=list(range(x,n))
                    G.add_nodes_from(extra)
                    G.add_edges_from(itertools.combinations([apex]+extra,2))
                    key=nx.weisfeiler_lehman_graph_hash(G)
                    if not any(nx.is_isomorphic(G,K) for K in seen[key]):
                        seen[key].append(G);result.append(G)
        by[n]=result
    return by


def main():
    graphs=block_graphs(9)
    expected={1:1,2:1,3:2,4:4,5:9,6:22,7:59,8:165,9:496}
    for n, gs in graphs.items():
        assert len(gs)==expected[n], (n,len(gs))
        for G in gs:
            for r in G:
                init={v:int(v==r) for v in G}
                ok,bad=verify(G,init)
                assert ok,(n,G.edges(),r,bad)
    print('ROOTED_ORBITS_PASS exhaustive block graphs n<=9:',sum(len(x) for x in graphs.values()),'unlabelled graphs')
    rng=random.Random(89221)
    for n in range(2,10):
        for G in graphs[n][:min(40,len(graphs[n]))]:
            for _ in range(3):
                r=rng.choice(list(G))
                initial={v:(0 if v==r else rng.choice([1,2,3])) for v in G}
                ok,bad=verify(G,initial)
                assert ok,(n,G.edges(),r,bad)
    print('ARBITRARY_PRECOLOURS_PASS 3 randomized profiles per selected rooted block graph')
    # An unmarked graph of order eight can have a stable class that merges orbits.
    examples=[]
    for n in range(1,9):
        for G in graphs[n]:
            colors={v:0 for v in G}
            ok,_=verify(G,colors)
            if not ok:examples.append(n)
    assert examples==[8],examples
    print('UNMARKED_SHARPNESS_PASS unique failing connected block graph up to order eight')

if __name__=='__main__':main()
