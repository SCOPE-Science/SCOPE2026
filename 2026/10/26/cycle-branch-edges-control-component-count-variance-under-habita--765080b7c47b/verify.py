#!/usr/bin/env python3
"""Exact checks for site-retention component-variance identities on unicyclic habitat graphs."""
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict
import json

def cycle_vertices(n, edges):
    # Iterative leaf-pruning of an undirected unicyclic graph.
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    alive=set(range(n))
    while True:
        leaves={v for v in alive if len(adj[v]&alive)<=1}
        if not leaves: break
        alive-=leaves
    return alive

def components(mask,n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        if mask>>u&1 and mask>>v&1:adj[u].add(v);adj[v].add(u)
    todo={u for u in range(n) if mask>>u&1};out=0
    while todo:
        out+=1;front=[todo.pop()]
        while front:
            u=front.pop()
            for v in adj[u]&todo:todo.remove(v);front.append(v)
    return out

def moments(n,edges,probability=None,k=None):
    assert (probability is None)!=(k is None)
    outcomes=[]
    if k is not None:
        masks=[sum(1<<i for i in subset) for subset in combinations(range(n),k)]
        outcomes=[(m,Q(1,len(masks))) for m in masks]
    else:
        p=probability
        outcomes=[(m,p**m.bit_count()*(1-p)**(n-m.bit_count())) for m in range(1<<n)]
    expectation=sum((w*components(m,n,edges) for m,w in outcomes),Q(0))
    second=sum((w*components(m,n,edges)**2 for m,w in outcomes),Q(0))
    return expectation,second-expectation**2

def coeff(n,k,ell):
    def a(j):
        if j>k:return Q(0)
        out=Q(1)
        for i in range(j):out*=Q(k-i,n-i)
        return out
    return a(ell+1)-a(ell+2)

def invariant(n,edges):
    cv=cycle_vertices(n,edges)
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    B=sum((u in cv)!=(v in cv) for u,v in edges)
    return (len(cv),tuple(sorted(deg)),B)

A=[(0,2),(1,2),(1,3),(1,4),(2,4),(3,5)]
B=[(0,1),(0,2),(0,3),(3,4),(3,5),(4,5)]
n=6;ia=invariant(n,A);ib=invariant(n,B)
assert ia[:2]==ib[:2] and ia[2]-ib[2]==1,(ia,ib)
ell=ia[0]; report={'graph_A':A,'graph_B':B,'cycle_length':ell,'boundary_edges':[ia[2],ib[2]],'fixed_quota':[],'bernoulli':[]}
for k in range(1,n):
    ea,va=moments(n,A,k=k);eb,vb=moments(n,B,k=k)
    assert ea==eb
    assert va-vb==-2*(ia[2]-ib[2])*coeff(n,k,ell),(k,va,vb)
    report['fixed_quota'].append({'k':k,'mean':str(ea),'variance_A':str(va),'variance_B':str(vb),'difference':str(va-vb)})
for p in [Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(4,5)]:
    ea,va=moments(n,A,probability=p);eb,vb=moments(n,B,probability=p)
    assert ea==eb
    assert va-vb==-2*(ia[2]-ib[2])*p**(ell+1)*(1-p)
    report['bernoulli'].append({'p':str(p),'mean':str(ea),'variance_A':str(va),'variance_B':str(vb),'difference':str(va-vb)})
# Exhaustively inspect *all* labeled connected unicyclic graphs on n<=5,
# group by (n, cycle length, degree multiset), and test pair differences.
report['exhaustive_small']={}
for n in [3,4,5]:
    universe=list(combinations(range(n),2));groups=defaultdict(list)
    for edge_indices in combinations(range(len(universe)),n):
        ed=tuple(universe[i] for i in edge_indices)
        # n edges and connectivity exactly characterizes unicyclic graphs.
        if components((1<<n)-1,n,ed)!=1:continue
        ell,degs,b=invariant(n,ed)
        groups[(ell,degs)].append((ed,b))
    total=sum(len(items) for items in groups.values());pairs=0
    for (ell,degs), items in groups.items():
        reference,bb=items[0]
        moments_fixed=[moments(n,reference,k=k) for k in range(1,n)]
        moments_bern=moments(n,reference,probability=Q(1,2))
        for ed,b in items[1:]:
            for k in range(1,n):
                e,v=moments(n,ed,k=k);e0,v0=moments_fixed[k-1]
                assert e==e0 and v-v0==-2*(b-bb)*coeff(n,k,ell)
            e,v=moments(n,ed,probability=Q(1,2));e0,v0=moments_bern
            assert e==e0 and v-v0==-2*(b-bb)*Q(1,2)**(ell+2)
            pairs+=1
    report['exhaustive_small'][str(n)]={'labeled_unicyclic_graphs':total,'comparison_to_reference':pairs,'strata':len(groups)}
print(json.dumps(report,indent=2,sort_keys=True))
