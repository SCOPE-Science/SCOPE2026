"""Compare refinement on rooted block graphs to refinement on their block-incidence trees."""
import collections
import itertools
import random
import networkx as nx


def wl(G,initial):
    c=dict(initial)
    while True:
        s={v:(c[v],tuple(sorted(collections.Counter(c[u] for u in G[v]).items()))) for v in G}
        keys={k:i for i,k in enumerate(sorted(set(s.values())))}
        d={v:keys[s[v]] for v in G}
        if len(set(c.values()))==len(set(d.values())):return d
        c=d


def same_partition(c,d,vertices):
    for u,v in itertools.combinations(vertices,2):
        if (c[u]==c[v]) != (d[u]==d[v]):return (u,v)
    return None


def incidence_tree(G):
    B=nx.Graph()
    for v in G:B.add_node(('v',v))
    for i,block in enumerate(nx.biconnected_components(G)):
        b=('b',i)
        B.add_node(b)
        for v in block:B.add_edge(b,('v',v))
    assert nx.is_tree(B)
    return B


def random_block_graph(rng,n):
    G=nx.empty_graph(1)
    while len(G)<n:
        size=min(rng.choice((2,2,2,3,3,4,5,6)),n-len(G)+1)
        ap=rng.choice(list(G));k=len(G)
        leaves=list(range(k,k+size-1))
        G.add_nodes_from(leaves)
        G.add_edges_from(itertools.combinations([ap]+leaves,2))
    return G


def main():
    rng=random.Random(12093)
    counts=0
    for n in [2,3,4,5,6,7,8,9,10,12,16,22,30,50,80]:
        for t in range(80):
            G=random_block_graph(rng,n)
            root=rng.randrange(n)
            base={v:(0 if v==root else rng.randint(1,4)) for v in G}
            c=wl(G,base)
            B=incidence_tree(G)
            cb=wl(B,{v:(('block',0) if v[0]=='b' else ('vertex',base[v[1]])) for v in B})
            q=same_partition(c,{v:cb[('v',v)] for v in G},G.nodes)
            assert q is None,(n,root,t,q,sorted(G.edges()))
            counts+=1
    print('BLOCK_CUT_TREE_PASS',counts,'rooted coloured block graphs (orders 2..80)')

if __name__=='__main__':main()
