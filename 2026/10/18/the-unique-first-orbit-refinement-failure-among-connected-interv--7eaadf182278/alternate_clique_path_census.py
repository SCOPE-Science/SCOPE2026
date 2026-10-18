#!/usr/bin/env python3
"""Independent eight-vertex census using maximal-clique consecutive-ones tests.
The base set is ALL connected seven-vertex chordal graphs, not the interval subset.
"""
from itertools import combinations,permutations
from collections import defaultdict
import networkx as nx

def interval_by_clique_path(g):
    mc=[frozenset(c) for c in nx.find_cliques(g)]
    for order in permutations(mc):
        good=True
        for v in g:
            ix=[k for k,c in enumerate(order) if v in c]
            if ix[-1]-ix[0]+1!=len(ix):
                good=False;break
        if good:return True
    return False

def iso_key(g):
    # Invariant only to speed up exact isomorphism filtering.
    return (g.number_of_edges(),tuple(sorted(d for _,d in g.degree)),nx.weisfeiler_lehman_graph_hash(g))

def is_bad(g):
    color={x:0 for x in g}
    for _ in range(len(g)):
        signature={x:(color[x],tuple(sorted(color[y] for y in g[x]))) for x in g}
        ids={s:i for i,s in enumerate(sorted(set(signature.values())))}
        newer={x:ids[signature[x]] for x in g}
        if len(set(newer.values()))==len(set(color.values())):break
        color=newer
    else:raise AssertionError('nonstabilization')
    # For each same-colour pair, check whether some automorphism maps first to second.
    aa=list(nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())
    for u,v in combinations(g,2):
        if color[u]==color[v] and not any(h[u]==v for h in aa):
            return True
    return False

def main():
    a=nx.graph_atlas_g()
    seven=[g for g in a if len(g)==7 and nx.is_connected(g) and nx.is_chordal(g)]
    assert len(seven)==272
    buckets=defaultdict(list)
    for parent in seven:
        for r in range(1,8):
            for S in combinations(list(parent),r):
                if any(not parent.has_edge(x,y) for x,y in combinations(S,2)):continue
                g=parent.copy();g.add_node(7);g.add_edges_from((x,7) for x in S)
                if not interval_by_clique_path(g):continue
                k=iso_key(g)
                if not any(nx.is_isomorphic(g,h) for h in buckets[k]):buckets[k].append(g)
    output=[g for b in buckets.values() for g in b]
    bad=[g for g in output if is_bad(g)]
    print('7-vertex connected chordal starting types:',len(seven))
    print('8-vertex connected interval types via clique-path test:',len(output))
    print('8-vertex nonrefinable types:',len(bad))
    print('all exceptions isomorphic to triangle--3-edge path--triangle:',
          all(nx.is_isomorphic(g,nx.from_graph6_bytes(b'GIc`KO')) for g in bad))
    assert len(output)==1328 and len(bad)==1
    assert nx.is_isomorphic(bad[0],nx.from_graph6_bytes(b'GIc`KO'))
    print('PASS: independent maximal-clique recognition census')

if __name__=='__main__':main()
