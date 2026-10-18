#!/usr/bin/env python3
"""Independent clique-path recognition and direct counterexample certificate.
No code imported from the primary enumerator.
"""
import itertools
import networkx as nx


def is_interval_via_clique_order(g):
    # Maximal cliques can be linearly ordered with consecutive appearances
    # of each vertex, iff this graph is an interval graph.
    cc=[frozenset(x) for x in nx.find_cliques(g)]
    for perm in itertools.permutations(range(len(cc))):
        if all((lambda indices: not indices or indices[-1]-indices[0]+1==len(indices))(
            [i for i,j in enumerate(perm) if v in cc[j]]) for v in g):
            return True
    return False


def partition_g(g):
    colors={v:0 for v in g}
    while True:
        sig={v:(colors[v],tuple(sorted(colors[w] for w in g[v]))) for v in g}
        types=sorted(set(sig.values()))
        d={v:types.index(sig[v]) for v in g}
        if len(set(d.values()))==len(set(colors.values())):
            break
        colors=d
    return sorted(sorted(v for v in g if d[v]==x) for x in set(d.values()))


def automorphism_classes(g):
    automorphisms=list(nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())
    unseen=set(g)
    out=[]
    while unseen:
        v=min(unseen)
        orb=sorted({a[v] for a in automorphisms})
        assert set(orb)<=unseen
        unseen-=set(orb)
        out.append(orb)
    return sorted(out),len(automorphisms)


def main():
    g=nx.from_graph6_bytes(b'GIc`KO')
    assert nx.is_connected(g) and len(g)==8 and g.number_of_edges()==9
    assert is_interval_via_clique_order(g)
    # The path of maximal cliques, expressed in the original vertex labels.
    Q=[{0,4,7},{3,4},{1,3},{1,2},{2,5,6}]
    assert set(map(frozenset,Q))==set(map(frozenset,nx.find_cliques(g)))
    assert all([i for i,q in enumerate(Q) if v in q]
               ==list(range(min(i for i,q in enumerate(Q) if v in q),
                           max(i for i,q in enumerate(Q) if v in q)+1)) for v in g)
    ref=partition_g(g)
    aut,count=automorphism_classes(g)
    assert list(sorted(map(len,ref)))==[2,6]
    assert list(sorted(map(len,aut)))==[2,2,4]
    assert count==8
    assert len([x for x,d in g.degree if d==3])==2
    print('clique path:',Q)
    print('1-WL cells:',ref)
    print('automorphism orbits:',aut)
    print('automorphism group order:',count)
    print('PASS: explicit eight-vertex interval graph and orbital obstruction')

if __name__=='__main__':main()
