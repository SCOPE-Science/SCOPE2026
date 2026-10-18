"""Exhaustive connected bicyclic small-order census and theta/barbell checks.

Run with Python >=3.9 and NetworkX >=2.6: python bicyclic_verifier.py
A graph is a simple undirected graph. No external graph atlas is used.
"""
from collections import Counter, defaultdict
from itertools import combinations
import networkx as nx


def degree_neighborhood_signature(g):
    d = dict(g.degree())
    return tuple(sorted((d[x], tuple(sorted(d[y] for y in g.neighbors(x))))
                        for x in g))


def color_refinement_equiv(g, h):
    j = nx.disjoint_union(g, h)
    colors = {v: 0 for v in j}
    for _ in range(len(j)+1):
        keys = {v: (colors[v], tuple(sorted(Counter(colors[w] for w in j[v]).items()))) for v in j}
        rank = {key: i for i, key in enumerate(sorted(set(keys.values())))}
        newer = {v:rank[keys[v]] for v in j}
        if newer == colors:
            break
        colors = newer
    else:
        raise AssertionError('Color refinement did not stabilize')
    n = len(g)
    return Counter(colors[x] for x in range(n)) == Counter(colors[x] for x in range(n,len(j)))


def classes(n):
    edges = list(combinations(range(n), 2))
    bysig = defaultdict(list)
    connected_labelled = 0
    for sel in combinations(edges,n+1):
        g = nx.Graph()
        g.add_nodes_from(range(n))
        g.add_edges_from(sel)
        if not nx.is_connected(g):
            continue
        connected_labelled += 1
        s = degree_neighborhood_signature(g)
        bucket = bysig[s]
        if not any(nx.is_isomorphic(g, h) for h in bucket):
            bucket.append(g)
    reps = [(s,g) for s,bucket in bysig.items() for g in bucket]
    ambiguous = [(s,bucket) for s,bucket in bysig.items() if len(bucket)>1]
    for s,bucket in ambiguous:
        for x,y in combinations(bucket,2):
            assert color_refinement_equiv(x,y), 'Signature equal but later split'
            assert not nx.is_isomorphic(x,y)
    print(f'n={n} labelled_connected={connected_labelled} isomorphism_classes={len(reps)} degree_neighborhood_classes={len(bysig)} ambiguous_buckets={len(ambiguous)}')
    return ambiguous


def theta(a,c):
    # Two poles 0 and 1. Internally disjoint paths of lengths a,a,c.
    g=nx.Graph(); g.add_nodes_from((0,1))
    next_vertex = 2
    for length in (a,a,c):
        previous = 0
        for _ in range(length-1):
            g.add_edge(previous, next_vertex)
            previous=next_vertex
            next_vertex+=1
        g.add_edge(previous, 1)
    return g


def barbell(a,c):
    # Two disjoint a-cycles joined by a path of length c.
    assert a>=3 and c>=1
    g=nx.disjoint_union(nx.cycle_graph(a), nx.cycle_graph(a))
    v=0
    n=2*a
    for _ in range(c-1):
        g.add_edge(v,n)
        v=n;n+=1
    g.add_edge(v,a)
    return g


def main():
    for n in (4,5,6):
        ambiguous=classes(n)
        assert [len(bucket) for _,bucket in ambiguous] == ([2] if n==6 else [])
        if n==6:
            x,y=ambiguous[0][1]
            t,b=theta(3,1),barbell(3,1)
            assert any(nx.is_isomorphic(x,z) for z in (t,b))
            assert any(nx.is_isomorphic(y,z) for z in (t,b))
            assert not nx.is_isomorphic(x,y)
            print('  unique ambiguous pair: theta(3,3,1) and two triangles joined by one edge')
    for a in range(3,8):
        for c in range(1,7):
            t,b=theta(a,c),barbell(a,c)
            assert len(t)==len(b)==2*a+c-1
            assert t.number_of_edges()==b.number_of_edges()==2*a+c
            assert nx.is_connected(t) and nx.is_connected(b)
            assert not nx.is_isomorphic(t,b)
            assert color_refinement_equiv(t,b)
    print('theta/barbell comparisons: 30 parameter pairs, all nonisomorphic and CR-equivalent')

if __name__=='__main__': main()
