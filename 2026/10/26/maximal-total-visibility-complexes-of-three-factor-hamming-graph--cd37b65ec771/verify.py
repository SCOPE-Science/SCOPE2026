"""Independent finite checks for maximal total-visibility sets on 3-factor Hamming graphs.

Run: python verify.py. Requires networkx (only for maximal-clique enumeration).
"""
from collections import Counter
from itertools import product, combinations
import networkx as nx


def vertices(a,b):
    return list(product(range(2), range(a), range(b)))


def distance(u,v):
    return sum(x != y for x,y in zip(u,v))


def forbidden_pairwise(V,mask):
    S=[i for i in range(len(V)) if (mask >> i)&1]
    return all(distance(V[i],V[j])!=2 for i,j in combinations(S,2))


def original_visibility(V,mask):
    """Original all-endpoint geodesic definition without using distance-two equivalence."""
    N=len(V)
    adjacency=[[j for j in range(N) if distance(V[i],V[j])==1] for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            target_dist=distance(V[i],V[j])
            if target_dist<=1:
                continue
            frontier={i}
            for step in range(target_dist):
                frontier={w for v in frontier for w in adjacency[v]
                          if distance(V[i],V[w])==step+1
                          and (w==j or not ((mask>>w)&1))}
                if not frontier:
                    return False
            if j not in frontier:
                return False
    return True


def compatibility_graph(V):
    B=nx.Graph()
    B.add_nodes_from(range(len(V)))
    B.add_edges_from((i,j) for i,j in combinations(range(len(V)),2)
                     if distance(V[i],V[j])!=2)
    return B


def facets_pairwise(V):
    return {frozenset(s) for s in nx.find_cliques(compatibility_graph(V))}


def predicted_complete(m,V):
    dct={v:i for i,v in enumerate(V)}
    pred=set()
    for diag in [((0,0),(1,1)), ((0,1),(1,0))]:
        for choices in product(range(2),repeat=m):
            pred.add(frozenset(dct[(*diag[choices[t]],t)] for t in range(m)))
    for t in range(m):
        for corner1,corner2 in [((0,0),(0,1)),((0,0),(1,0)),
                                 ((1,1),(0,1)),((1,1),(1,0))]:
            pred.add(frozenset([dct[(*corner1,t)],dct[(*corner2,t)]]))
    return pred


def min_pair_count(a,b,V):
    count=0
    for i,j in combinations(range(len(V)),2):
        if distance(V[i],V[j])==2: continue
        if all(distance(V[k],V[i])==2 or distance(V[k],V[j])==2
               for k in range(len(V)) if k not in (i,j)):
            count+=1
    expected=a*b + (2*b if a==2 else 0) + (2*a if b==2 else 0) + (4 if a==2 and b==2 else 0)
    assert count==expected,(a,b,count,expected)
    return count


def main():
    raw=0
    for a,b in [(2,2),(2,3)]:
        V=vertices(a,b)
        for mask in range(1<<len(V)):
            assert original_visibility(V,mask)==forbidden_pairwise(V,mask),(a,b,mask)
            raw+=1
    full=0
    all_faces=0
    for m in range(2,9):
        V=vertices(2,m)
        actual=facets_pairwise(V)
        predicted=predicted_complete(m,V)
        assert actual==predicted,(m,len(actual),len(predicted),list(actual-predicted)[:3])
        expected_facets=Counter({m:2**(m+1),2:4*m}) if m>2 else Counter({2:16})
        assert Counter(map(len,actual))==expected_facets
        all_counts=Counter(len(face) for face in nx.enumerate_all_cliques(compatibility_graph(V)))
        all_counts[0]=1
        expected_counts=Counter({0:1})
        for k in range(1,m+1):
            from math import comb
            expected_counts[k]=2*comb(m,k)*(2**k)
        expected_counts[2]+=4*m
        assert all_counts==expected_counts,(m,all_counts,expected_counts)
        all_faces+=sum(all_counts.values())
        full+=len(actual)
    pair_cases=0
    pair_total=0
    for a in range(2,7):
        for b in range(2,7):
            V=vertices(a,b)
            pair_total+=min_pair_count(a,b,V)
            pair_cases+=1
    print('VERIFICATION_OK original_subsets=',raw,
          ' full_facet_parameters=2..8 full_facets=',full,
          ' all_faces=',all_faces,
          ' pair_parameters=',pair_cases,' maximal_pairs=',pair_total,sep='')

if __name__=='__main__':
    main()
