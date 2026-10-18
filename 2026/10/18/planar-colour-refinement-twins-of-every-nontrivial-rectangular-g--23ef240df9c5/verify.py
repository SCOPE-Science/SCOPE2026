#!/usr/bin/env python3
"""Finite consistency checks for the planar grid-switch theorem.
Requires networkx >= 2.8 for planarity; the mathematical proof is all-size.
"""
import json
from collections import Counter
import networkx as nx


def grid(m, n):
    return nx.grid_2d_graph(m, n)


def switch(G, m, n):
    if m > n:
        raise ValueError('Use 2 <= m <= n')
    if m < 2 or n < 3:
        raise ValueError('The positive witness domain is 2 <= m <= n, n >= 3')
    if m == 2 and n == 4:
        a, b, c, d = (0,0), (0,3), (0,1), (0,2)
    elif m == 2:
        a, b, c, d = (0,0), (1,n-1), (1,0), (0,n-1)
    else:
        a, b, c, d = (0,0), (m-1,n-1), (1,0), (m-2,n-1)
    assert len({a,b,c,d}) == 4
    assert G.has_edge(a,c) and G.has_edge(b,d)
    assert not G.has_edge(a,d) and not G.has_edge(b,c)
    H = G.copy()
    H.remove_edge(a,c)
    H.remove_edge(b,d)
    H.add_edge(a,d)
    H.add_edge(b,c)
    return H, (a,b,c,d)


def square_count(G):
    # Every 4-cycle has exactly two pairs of opposite vertices.
    return sum(len(set(G[u]) & set(G[v])) * (len(set(G[u]) & set(G[v]))-1) // 2
               for u in G for v in G if u < v) // 2


def refinement_signatures(G, H):
    assert set(G) == set(H)
    colors_G = {u:0 for u in G}
    colors_H = {u:0 for u in H}
    for iteration in range(len(G)+2):
        sg = {u:(colors_G[u],tuple(sorted(colors_G[w] for w in G[u]))) for u in G}
        sh = {u:(colors_H[u],tuple(sorted(colors_H[w] for w in H[u]))) for u in H}
        symbols = {t:i for i,t in enumerate(sorted(set(sg.values()) | set(sh.values())))}
        ng = {u:symbols[sg[u]] for u in G}
        nh = {u:symbols[sh[u]] for u in H}
        assert ng == nh, ('refinement mismatch', iteration)
        if ng == colors_G and nh == colors_H:
            return iteration
        colors_G,colors_H = ng,nh
    raise AssertionError('refinement did not stabilize')


def run(max_side=18):
    trials=0; exceptional=[]; max_iter=0
    for m in range(2,max_side+1):
        for n in range(m,max_side+1):
            if m==2 and n==2: continue
            G=grid(m,n); H,(a,b,c,d)=switch(G,m,n)
            expected=2 if (m,n)==(3,3) else -2
            delta=square_count(H)-square_count(G)
            assert delta==expected,(m,n,delta,expected)
            assert nx.is_connected(H),(m,n,'disconnected')
            assert nx.check_planarity(H)[0],(m,n,'nonplanar')
            assert sorted(dict(G.degree()).values())==sorted(dict(H.degree()).values())
            step=refinement_signatures(G,H)
            max_iter=max(max_iter,step)
            trials+=1
            if m==2 and n<=6 or m==3 and n<=4:
                exceptional.append({'m':m,'n':n,'C4_before':square_count(G),'C4_after':square_count(H),'refinement_rounds':step})
    Q=grid(2,2)
    assert len(Q)==4 and all(d==2 for _,d in Q.degree())
    return {'max_side_inclusive':max_side,'witness_cases_tested':trials,
            'all_connected':True,'all_planar':True,'all_same_global_refinement_colors':True,
            'all_C4_change_proved_formula_in_test':True,'max_refinement_rounds':max_iter,
            'special_cases':exceptional,
            'limitation':'Finite checks supplement, but do not prove, the all-size statement.'}

if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
