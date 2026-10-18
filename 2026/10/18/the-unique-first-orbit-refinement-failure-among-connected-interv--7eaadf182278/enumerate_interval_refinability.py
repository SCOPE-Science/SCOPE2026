#!/usr/bin/env python3
"""Complete isomorphism-free census of connected interval graphs of order <=8.
Requires Python 3 and networkx >=3.2. See RESULT.md for the completeness proof.
"""
from collections import defaultdict
from itertools import combinations
import networkx as nx


def contains_asteroidal_triple(g):
    for a,b,c in combinations(g.nodes,3):
        if g.has_edge(a,b) or g.has_edge(a,c) or g.has_edge(b,c):
            continue
        for u,v,z in ((a,b,c),(a,c,b),(b,c,a)):
            forbidden={z}|set(g.neighbors(z))
            h=g.subgraph(set(g.nodes)-forbidden)
            if not nx.has_path(h,u,v):
                break
        else:
            return True
    return False


def interval_graph(g):
    return nx.is_chordal(g) and not contains_asteroidal_triple(g)


def cells(color):
    return tuple(sorted(tuple(sorted(v for v in color if color[v]==c))
                        for c in set(color.values())))


def refinement(g):
    color={v:0 for v in g}
    for _ in range(g.number_of_nodes()):
        sig={v:(color[v],tuple(sorted(color[w] for w in g[v]))) for v in g}
        cid={s:i for i,s in enumerate(sorted(set(sig.values())))}
        new={v:cid[sig[v]] for v in g}
        if len(set(new.values()))==len(set(color.values())):
            return cells(new)
        color=new
    raise AssertionError('refinement did not stabilize')


def orbit_cells(g):
    parent={v:v for v in g}
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for p in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter():
        for v,w in p.items():
            a,b=root(v),root(w)
            if a!=b:parent[a]=b
    return cells({v:root(v) for v in g})


def key(g):
    return (g.number_of_edges(),tuple(sorted(d for _,d in g.degree())),
            nx.weisfeiler_lehman_graph_hash(g))


def extension_catalogue():
    atlas=nx.graph_atlas_g()
    counts=[]
    all_g=[]
    for n in range(1,8):
        level=[g.copy() for g in atlas if len(g)==n and nx.is_connected(g)
               and interval_graph(g)]
        counts.append(len(level))
        all_g.extend((n,g) for g in level)
    seven=[g for n,g in all_g if n==7]
    groups=defaultdict(list)
    for g in seven:
        vlist=list(g)
        for k in range(1,8):
            for subset in combinations(vlist,k):
                if any(not g.has_edge(u,v) for u,v in combinations(subset,2)):
                    continue
                h=g.copy()
                h.add_node(7)
                h.add_edges_from((7,u) for u in subset)
                # A clique-attachment preserves chordality; now test AT-freeness.
                if contains_asteroidal_triple(h):
                    continue
                bucket=groups[key(h)]
                if not any(nx.is_isomorphic(h,x) for x in bucket):
                    bucket.append(h)
    eight=[g for bucket in groups.values() for g in bucket]
    counts.append(len(eight))
    all_g.extend((8,g) for g in eight)
    bad=[]
    for n,g in all_g:
        r,o=refinement(g),orbit_cells(g)
        if r!=o:
            bad.append((n,g.number_of_edges(),
                        nx.to_graph6_bytes(g,header=False).decode().strip(),
                        tuple(sorted(map(len,r))),tuple(sorted(map(len,o)))))
    return counts,bad


def main():
    counts,bad=extension_catalogue()
    print('connected interval graph counts orders 1..8:',counts)
    print('nonrefinable examples:',bad)
    assert counts==[1,1,2,5,15,56,250,1328]
    assert bad==[(8,9,'GIc`KO',(2,6),(2,2,4))]
    print('PASS: unique non-refinable connected interval graph through order eight')

if __name__=='__main__':main()
