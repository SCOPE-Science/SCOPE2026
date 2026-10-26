"""Exact census for the occupied-isolate variance theorem.
Run with Python 3.10+, networkx, and sympy: python verify.py.
Outputs one canonical UTF-8 JSON certificate on stdout.
"""
import collections
import itertools
import json
from fractions import Fraction
import networkx as nx
import sympy as sp

q = sp.Symbol('q')
A_EDGES = [(0, 4), (0, 7), (1, 0), (1, 2), (2, 3), (4, 5), (4, 6), (7, 8)]
B_EDGES = [(0, 5), (1, 0), (1, 2), (1, 4), (2, 3), (5, 6), (5, 8), (6, 7)]

def statistic(T):
    degrees = dict(T.degree())
    distances = dict(nx.all_pairs_shortest_path_length(T))
    terms = collections.Counter()
    for u in T:
        for v in T:
            if u < v and distances[u][v] > 1:
                terms[degrees[u] + degrees[v] - (distances[u][v] == 2)] += 1
    return dict(terms)

def difference(a, b):
    return sp.Poly(sum((a.get(k,0)-b.get(k,0))*q**k
                       for k in set(a)|set(b)), q)

def interior_roots(poly):
    if poly.is_zero: return 0
    while poly.eval(0) == 0:poly = poly.exquo(sp.Poly(q,q))
    while poly.eval(1) == 0:poly = poly.exquo(sp.Poly(q-1,q))
    return poly.count_roots(sp.Rational(0),sp.Rational(1))

def brute_variance(T, p):
    n=len(T); vertices=sorted(T); deg=dict(T.degree()); qval=1-p
    mean=Fraction(0); raw2=Fraction(0)
    for mask in range(1<<n):
        occupied={vertices[i] for i in range(n) if mask>>i & 1}
        c=sum(v in occupied and all(w not in occupied for w in T[v]) for v in vertices)
        prob=p**len(occupied)*qval**(n-len(occupied))
        mean+=c*prob; raw2+=c*c*prob
    return mean, raw2-mean*mean

def main():
    classes=[]; differing=[]; crossing=[]; zero_pairs=[]
    witnesses=[]
    for n in range(2,10):
        groups=collections.defaultdict(list)
        for T in nx.nonisomorphic_trees(n):
            degree_key=tuple(sorted(d for _,d in T.degree()))
            groups[degree_key].append((T.copy(),statistic(T)))
        total=nonzero=roots=zero=0
        for degkey,group in groups.items():
            for i in range(len(group)):
                for j in range(i):
                    total+=1
                    poly=difference(group[i][1],group[j][1])
                    if poly.is_zero:zero+=1;continue
                    nonzero+=1
                    k=int(interior_roots(poly))
                    if k:
                        roots+=1
                        witnesses.append({'n':n,'degree_multiset':list(degkey),
                          'edges_first':sorted([list(sorted(e)) for e in group[i][0].edges()]),
                          'edges_second':sorted([list(sorted(e)) for e in group[j][0].edges()]),
                          'difference_factorization':str(sp.factor(poly.as_expr())),
                          'interior_roots':k})
        classes.append({'n':n,'unlabeled_trees':sum(len(g) for g in groups.values()),
          'degree_matched_pairs':total,'nonidentical_variance_pairs':nonzero,
          'identical_variance_pairs':zero,'reversal_pairs':roots})
    A=nx.Graph();A.add_edges_from(A_EDGES)
    B=nx.Graph();B.add_edges_from(B_EDGES)
    D=difference(statistic(A),statistic(B))
    assert sp.factor(D.as_expr()) == -q*(q-1)**2*(2*q*q+2*q-1)
    assert not nx.is_isomorphic(A,B)
    assert tuple(sorted(dict(A.degree()).values()))==tuple(sorted(dict(B.degree()).values()))
    exact={}
    for p in (Fraction(1,2),Fraction(4,5)):
        ma,va=brute_variance(A,p);mb,vb=brute_variance(B,p)
        assert ma==mb
        assert va-vb==2*p*p*Fraction(D.eval(1-p))
        exact[str(p)]={'mean':str(ma),'variance_A':str(va),
                       'variance_B':str(vb),'variance_difference':str(va-vb)}
    assert [c['reversal_pairs'] for c in classes]==[0,0,0,0,0,0,0,3]
    assert [c['degree_matched_pairs'] for c in classes]==[0,0,0,0,1,5,23,96]
    assert len(witnesses)==3
    return {'schema_version':1,'method':'all nonisomorphic trees; exact polynomial and rational Sturm root counting; independent subset enumeration for witness',
       'classifications':classes,'nine_vertex_reversal_pairs':witnesses,
       'chosen_witness':{'edges_A':A_EDGES,'edges_B':B_EDGES,
                          'variance_difference_factorization':str(sp.factor(2*(1-q)**2*D.as_expr())),
                          'switch_survival_probability':'(3-sqrt(3))/2',
                          'exact_independent_subset_checks':exact},
       'checks_passed':True}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
