"""Exact finite certificate for transmissibility-dependent one-vertex prophylaxis on trees.

Requires networkx and sympy. Run `python verify.py` from this directory.
"""
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
import networkx as nx
import sympy as sp

P=sp.symbols('p')

def trees_by_leaf_extension(nmax):
    levels={2:[nx.path_graph(2)]}
    for n in range(3,nmax+1):
        next_level=[]
        for tree in levels[n-1]:
            for x in list(tree.nodes):
                g=tree.copy();g.add_edge(x,n-1)
                if not any(nx.is_isomorphic(g,h) for h in next_level):next_level.append(g)
        levels[n]=next_level
    return levels

def distance_profile(tree,vertex):
    g=tree.copy();g.remove_node(vertex)
    counts=[0]*len(tree)
    for nodes in nx.connected_components(g):
        sub=g.subgraph(nodes)
        for source,ds in nx.all_pairs_shortest_path_length(sub):
            for target,d in ds.items():counts[d]+=1
    return tuple(counts)

def score(profile):return sp.Poly(sum(v*P**i for i,v in enumerate(profile)),P)

def nonnegative_without_interior_roots(poly):
    if poly.is_zero:return True
    if poly.eval(sp.Rational(1,2))<0:return False
    factors=sp.factor_list(poly)[1]
    return all(f.as_expr() in (P,P-1) or f.count_roots(0,1)==0 for f,k in factors)

def components_score_by_edges(tree,deleted,probability):
    nodes=[v for v in tree if v!=deleted]
    edges=[e for e in tree.edges if deleted not in e]
    total=Fraction(0)
    for mask in range(1<<len(edges)):
        sub=nx.Graph();sub.add_nodes_from(nodes)
        m=mask.bit_count()
        sub.add_edges_from(e for j,e in enumerate(edges) if mask>>j&1)
        sum_squares=sum(len(c)**2 for c in nx.connected_components(sub))
        total+=probability**m*(1-probability)**(len(edges)-m)*sum_squares
    return total

def cert():
    levels=trees_by_leaf_extension(8)
    counts={str(n):len(ts) for n,ts in levels.items()}
    assert counts=={'2':1,'3':1,'4':2,'5':3,'6':6,'7':11,'8':23}
    root_checks=0
    for n in range(2,8):
        for tree in levels[n]:
            polys=[score(distance_profile(tree,v)) for v in tree]
            exists=False
            for c in polys:
                root_checks+=len(polys)
                if all(nonnegative_without_interior_roots(q-c) for q in polys):
                    exists=True;break
            assert exists,(n,list(tree.edges))
    # 8-node witness: a branch at node 2 and a long arm from node 1.
    edges=[(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)]
    tree=nx.Graph();tree.add_edges_from(edges)
    low=2;high=1
    Plow=score(distance_profile(tree,low))
    Phigh=score(distance_profile(tree,high))
    assert Plow.as_expr()==7+8*P+6*P**2+4*P**3+2*P**4
    assert Phigh.as_expr()==7+10*P+6*P**2+2*P**3
    assert sp.factor(Plow.as_expr()-Phigh.as_expr())==2*P*(P**3+P**2-1)
    for v in tree:
        F=score(distance_profile(tree,v))
        if v not in (low,high):
            assert nonnegative_without_interior_roots(F-Plow) or nonnegative_without_interior_roots(F-Phigh)
    # Root isolation is exact: one simple root inside (0,1).
    q=sp.Poly(P**3+P**2-1,P)
    assert q.count_roots(0,1)==1
    assert q.eval(sp.Rational(3,4))<0<q.eval(sp.Rational(4,5))
    independent={}
    for p in (Fraction(1,2),Fraction(3,4),Fraction(9,10)):
        f_low=sum(Fraction(v)*p**i for i,v in enumerate(distance_profile(tree,low)))
        f_high=sum(Fraction(v)*p**i for i,v in enumerate(distance_profile(tree,high)))
        assert components_score_by_edges(tree,low,p)==f_low
        assert components_score_by_edges(tree,high,p)==f_high
        independent[str(p)]={'vertex_2_total':str(f_low),'vertex_1_total':str(f_high),'preferred_vertex':2 if f_low<f_high else 1}
    return dict(tree_counts=counts, universal_minimizers_through_seven=True,
        polynomial_comparisons_performed=root_checks,
        witness_edges=[list(x) for x in edges],
        witness_candidate_profiles={'vertex_2':list(distance_profile(tree,low)),'vertex_1':list(distance_profile(tree,high))},
        exact_transition_equation='p^3 + p^2 - 1 = 0',
        unique_transition_interval=['3/4','4/5'],
        independent_edge_configuration_checks=independent,
        witness_all_vertices_compared=True)

if __name__=='__main__':print(json.dumps(cert(),sort_keys=True,indent=2))
