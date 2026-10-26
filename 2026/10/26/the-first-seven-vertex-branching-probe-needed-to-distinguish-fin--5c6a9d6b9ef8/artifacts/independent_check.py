#!/usr/bin/env python3
"""Independent exact enumeration with NetworkX (version 3 or later).
Uses an unrelated generator, order-aware dictionary arithmetic and direct path walks.
"""
import collections
import networkx as nx

def walk_profile(G):
    n=len(G); vec={v:1 for v in G};out=[]
    for k in range(2*n):
        out.append(sum(vec.values()))
        vec={v:sum(vec[u] for u in G[v]) for v in G}
    return tuple(out)

def hom(S,G):
    root=next(iter(S)); parents={root:None};order=[root]
    for u in order:
        for v in S[u]:
            if v not in parents:
                parents[v]=u;order.append(v)
    q={}
    for v in reversed(order):
        children=[w for w in S[v] if parents[w]==v]
        q[v]={x:__import__('math').prod(sum(q[w][y] for y in G[x]) for w in children) for x in G}
    return sum(q[root].values())

def spider(arms):
    s=nx.Graph();s.add_node(0);u=1
    for length in arms:
        prev=0
        for k in range(length):
            s.add_edge(prev,u);prev=u;u+=1
    return s

def main():
    counts=[];pair_count=[]
    probes=[spider(z) for z in ((1,1,3),(1,2,2),(1,1,4),(1,2,3))]
    unresolved=[]
    for n in range(1,15):
        groups=collections.defaultdict(list)
        for G in nx.nonisomorphic_trees(n):groups[walk_profile(G)].append(G)
        counts.append(sum(map(len,groups.values())))
        pair_count.append(sum(1 for a in groups.values() if len(a)==2))
        assert all(len(a)<=2 for a in groups.values())
        for g in groups.values():
            if len(g)==2:
                a,b=g
                d6=[hom(f,a)!=hom(f,b) for f in probes[:2]]
                d7=[hom(f,a)!=hom(f,b) for f in probes[2:]]
                assert d6==[True,True] or (n==14 and d6==[False,False])
                assert d7==[True,True]
                if not any(d6):
                    unresolved.append((n, [(hom(s,a),hom(s,b)) for s in probes[2:]]))
    assert counts==[1,1,1,2,3,6,11,23,47,106,235,551,1301,3159]
    assert pair_count==[0]*11+[1,2,6]
    assert unresolved==[(14,[(1506,1504),(1472,1473)])]
    print('NETWORKX_TARGET_COUNTS',counts)
    print('NETWORKX_PATH_COLLISION_PAIRS',pair_count)
    print('SEVEN_VERTEX_SHARP_EXCEPTION',unresolved)
    print('INDEPENDENT_14_VERTEX_CHECKS_PASS')
if __name__=='__main__':main()
