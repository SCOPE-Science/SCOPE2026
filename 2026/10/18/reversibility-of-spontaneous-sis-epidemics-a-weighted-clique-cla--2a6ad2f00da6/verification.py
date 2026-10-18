#!/usr/bin/env python3
"""Exact checks for reversibility of finite epidemic birth-death chains.

Public scientific verification: no simulation, only integer and rational identities.
"""
from fractions import Fraction as Q
from itertools import combinations
import json


def is_cluster(n, edges):
    nbr=[set() for _ in range(n)]
    for i,j in edges:
        nbr[i].add(j); nbr[j].add(i)
    for i,j in edges:
        if nbr[i]-{j} != nbr[j]-{i}:
            return False
    return True


def square_condition(n, weights, immigration):
    # weights[src][target] is an exact transmission rate.
    count=0
    for mask in range(1 << n):
        absent=[i for i in range(n) if not(mask >> i & 1)]
        for i,j in combinations(absent,2):
            bi=immigration[i]+sum(weights[k][i] for k in range(n) if mask>>k & 1)
            bj=immigration[j]+sum(weights[k][j] for k in range(n) if mask>>k & 1)
            if bi*(bj+weights[i][j]) != bj*(bi+weights[j][i]):
                return False,count+1
            count+=1
    return True,count


def full_stationary_check(immigration, recovery, weights, components, factors):
    n=len(immigration)
    def wt(mask):
        p=Q(1)
        for i in range(n):
            if mask>>i&1:p*=immigration[i]/recovery[i]
        for C in components:
            k=sum(mask>>i&1 for i in C)
            kap=factors[tuple(C)]
            for j in range(k):p*=1+kap*j
        return p
    cases=0
    for mask in range(1<<n):
        for i in range(n):
            if not(mask>>i&1):
                b=immigration[i]+sum(weights[j][i] for j in range(n) if mask>>j&1)
                assert wt(mask)*b==wt(mask|(1<<i))*recovery[i]
                cases+=1
    z=sum((wt(m) for m in range(1<<n)),Q(0))
    assert z>0
    return cases,str(z)


def main():
    stats={}
    total_graphs=total_squares=0
    noncluster=0
    by_size={}
    for n in range(1,6):
        possible=list(combinations(range(n),2))
        positive=negative=checks=0
        for indicator in range(1<<len(possible)):
            edges=[e for pos,e in enumerate(possible) if indicator>>pos&1]
            w=[[Q(0) for j in range(n)] for i in range(n)]
            for i,j in edges:w[i][j]=w[j][i]=Q(3)
            rv, c=square_condition(n,w,[Q(2)]*n)
            checks+=c
            expected=is_cluster(n,edges)
            assert rv==expected,(n,edges,rv,expected)
            if rv:positive+=1
            else:negative+=1
        total_graphs+=positive+negative
        total_squares+=checks
        noncluster+=negative
        by_size[str(n)]={'graphs':positive+negative,'reversible':positive,'nonreversible':negative,'squares_checked_until_first_failure':checks}
    stats['uniform_graph_census']=by_size
    stats['total_graphs']=total_graphs
    stats['nonreversible_graphs']=noncluster
    stats['square_comparisons']=total_squares
    # Heterogeneous, directed two-way transmission with target-dependent intensity.
    # Two cliques (of sizes 3 and 2) and one isolated site.
    comps=[[0,1,2],[3,4],[5]]
    kap={(0,1,2):Q(3,2),(3,4):Q(2,3),(5,):Q(0)}
    a=list(map(Q,[1,2,3,5,7,11])); d=list(map(Q,[2,3,5,7,11,13]))
    w=[[Q(0) for j in range(6)] for i in range(6)]
    for C in comps:
        for i in C:
            for j in C:
                if i!=j:w[i][j]=kap[tuple(C)]*a[j]
    rv,squares=square_condition(6,w,a)
    assert rv
    b,z=full_stationary_check(a,d,w,comps,kap)
    stats['weighted_reversible']={'state_edges':b,'square_faces':squares,'partition_function':z}
    # Unbalanced two-vertex transmission violates the elementary square.
    wbad=[[Q(0),Q(4)],[Q(1),Q(0)]]
    r,c=square_condition(2,wbad,[Q(1),Q(2)])
    assert not r
    stats['weighted_two_vertex_imbalance_detected']=True
    # Three-vertex induced path with uniform alpha=2,beta=3.
    alpha,beta=Q(2),Q(3)
    ratio=(alpha+beta)**2/(alpha*(alpha+2*beta))
    assert ratio==Q(25,16)
    stats['three_vertex_path_square_forward_reverse_ratio']=str(ratio)
    print(json.dumps(stats,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
