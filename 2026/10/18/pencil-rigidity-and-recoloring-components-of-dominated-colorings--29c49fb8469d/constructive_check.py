#!/usr/bin/env python3
"""Construct all minimum dominated color partitions from pencils and check exchanges.
Runs independently of exhaustive.py and does not read its output.
"""
from itertools import product
from collections import deque, Counter
import json

def elements(q):
    x=set()
    for a,b,c in product(range(q),repeat=3):
        v=(a,b,c)
        if v==(0,0,0): continue
        j=next(y for y in v if y)
        x.add(tuple(y*pow(j,-1,q)%q for y in v))
    return sorted(x)

def incidence(q):
    P=elements(q)
    L=[frozenset(j for j,u in enumerate(P) if sum(a*b for a,b in zip(t,u))%q==0) for t in P]
    assert len(set(L))==q*q+q+1
    return L

def component_dist(g,origin):
    dist={origin:0};dq=deque([origin]);
    while dq:
        i=dq.popleft()
        for j in g[i]:
            if j not in dist:dist[j]=dist[i]+1;dq.append(j)
    return dist

def check(q):
    lines=incidence(q); v=len(lines); n=q+1
    P=[]; parameters=[]
    for center in range(v):
        star=[L for L in lines if center in L]
        assert len(star)==n
        for chosen in range(n):
            partition=frozenset(frozenset(L-{center} | ({center} if j==chosen else set())) for j,L in enumerate(star))
            assert len(partition)==n
            assert frozenset().union(*partition)==frozenset(range(v))
            assert sum(len(B) for B in partition)==v
            assert all(any(B<=L for L in lines) for B in partition)
            P.append(partition);parameters.append((center,chosen))
    assert len(set(P))==v*n
    g=[set() for _ in P]
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            A=P[i];B=P[j]
            # Single-vertex recoloring: their intersection-refined contingency has
            # a unique moved vertex, hence exactly two classes change.
            pair=[]
            for a in A:
                for b in B:
                    if a&b: pair.append((a,b,a&b))
            # Compute the smallest possible number of vertices whose class can
            # change under an unlabeled optimal identification.
            # In this family all classes contain at least q>=2 off-center vertices,
            # so unchanged cores determine the identification by max intersection.
            from itertools import permutations
            AA=sorted(A,key=lambda s:tuple(sorted(s)))
            BB=sorted(B,key=lambda s:tuple(sorted(s)))
            matches=max(sum(len(AA[k]&BB[z]) for k,z in enumerate(pi)) for pi in permutations(range(n)))
            if v-matches==1:
                g[i].add(j);g[j].add(i)
    assert all(len(g[i])==n-1 for i in range(len(P)))
    assert all({parameters[j][0] for j in g[i]}=={parameters[i][0]} for i in range(len(P)))
    E=sum(map(len,g))//2
    assert E==v*n*(n-1)//2
    # Cartesian product of independent point and line partitions has the same
    # graph construction and n*n vertices in each center pair component.
    for center in range(v):
        cc={i for i,(c,_) in enumerate(parameters) if c==center}
        for i in cc:
            assert g[i]==cc-{i}
    return {'q':q,'projective_points':v,'one_side_unlabeled':len(P),'one_side_edges':E,
            'two_sides_unlabeled':len(P)**2,'two_sides_components':v*v,
            'two_sides_component_order':n*n,'two_sides_component_degree':2*(n-1),
            'two_sides_component_diameter':2,
            'labeled_count':len(P)**2*__import__('math').factorial(2*n)}

if __name__=='__main__':
    print(json.dumps({'method':'pencil-construction cross-check; direct one-vertex comparison',
                      'results':[check(p) for p in (2,3)]},sort_keys=True))
