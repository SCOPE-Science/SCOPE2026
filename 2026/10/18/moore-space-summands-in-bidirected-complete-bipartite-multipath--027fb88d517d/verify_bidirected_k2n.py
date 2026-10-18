#!/usr/bin/env python3
"""Exact simplicial and discrete-Morse verification for multipath complexes
of the bidirected complete bipartite digraphs K_{2,n}, n=3,4,5,6.
Requires only Python 3 standard library.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

EXPECTED = {
    3: {'faces':115, 'f':(12,42,48,12), 'crit':{1:1,2:6}, 'betti':{1:1,2:6}, 'incidence_content':0},
    4: {'faces':313, 'f':(16,80,144,72), 'crit':{2:8,3:1}, 'betti':{2:8,3:1}, 'incidence_content':2},
    5: {'faces':711, 'f':(20,130,320,240), 'crit':{2:1,3:32}, 'betti':{2:1,3:32}, 'incidence_content':2},
    6: {'faces':1417,'f':(24,192,600,600), 'crit':{3:169}, 'betti':{3:169}, 'incidence_content':0},
}

def oriented_edges(n):
    return [(u,v) for i in range(n) for u,v in
            ((0,2+i),(2+i,0),(1,2+i),(2+i,1))]

def is_multipath(edge_ids, edges):
    # Every vertex has indegree and outdegree at most one, and no cycle.
    tails={}; heads=set()
    for j in edge_ids:
        u,v=edges[j]
        if u in tails or v in heads:
            return False
        tails[u]=v
        heads.add(v)
    for x in tails:
        seen=set()
        y=x
        while y in tails:
            if y in seen:
                return False
            seen.add(y)
            y=tails[y]
    return True

def build_faces(n):
    E=oriented_edges(n)
    # There are at most four directed edges: the two left vertices have
    # at most one incoming and one outgoing arc each.
    out=[()]
    for r in range(1,5):
        out.extend(f for f in combinations(range(len(E)),r)
                   if is_multipath(f,E))
    return out

def morse_pairs(faces,n):
    # Sequential element toggles: A_0,...,A_(n-1), B_0,...,
    # C_0,..., D_0,... ; A_i=0->i, B_i=i->0,
    # C_i=1->i, D_i=i->1, with leaves labeled i+2.
    remain=set(faces)
    pairs=[]
    for j in range(4):
        for i in range(n):
            v=4*i+j
            for face in sorted(remain):
                if v in face:
                    continue
                upper=tuple(sorted(face+(v,)))
                if upper in remain:
                    remain.remove(face)
                    remain.remove(upper)
                    pairs.append((face,upper))
    return pairs, remain

def check_acyclic(faces, pairs):
    index={f:i for i,f in enumerate(faces)}
    paired=set(pairs)
    edges=[[] for f in faces]
    indeg=[0]*len(faces)
    count=0
    for upper in faces:
        if not upper:continue
        for j in range(len(upper)):
            lower=upper[:j]+upper[j+1:]
            if (lower,upper) in paired:
                source,target=index[lower],index[upper]
            else:
                source,target=index[upper],index[lower]
            edges[source].append(target)
            indeg[target]+=1
            count+=1
    q=deque(x for x,v in enumerate(indeg) if v==0)
    seen=0
    while q:
        u=q.popleft();seen+=1
        for v in edges[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert seen==len(faces), (seen,len(faces),'directed cycle')
    return count

def morse_incidence(critical, pairs, lower_dimension):
    """Signed gradient-path differential on the residual free chain groups.

    A matched upper generator is killed, and a matched lower generator
    is expanded through the other facets of its paired upper simplex.
    Acyclicity ensures that this recursion terminates.
    """
    lower_to_upper={low:high for low,high in pairs}
    upper_to_lower={high:low for low,high in pairs}
    lower_critical={x for x in critical if len(x)==lower_dimension+1}
    upper_critical={x for x in critical if len(x)==lower_dimension+2}
    def signed_facets(face):
        return [(face[:i]+face[i+1:], 1 if i%2==0 else -1)
                for i in range(len(face))]
    @lru_cache(None)
    def projection(face):
        if face in lower_critical:return {face:1}
        if face in upper_to_lower:return {}
        assert face in lower_to_upper and len(face)==lower_dimension+1
        upper=lower_to_upper[face]
        incidence=[s for f,s in signed_facets(upper) if f==face]
        assert len(incidence)==1 and abs(incidence[0])==1
        result=defaultdict(int)
        for facet,sign in signed_facets(upper):
            if facet==face:continue
            for generator,coefficient in projection(facet).items():
                result[generator]-=incidence[0]*sign*coefficient
        return {g:c for g,c in result.items() if c}
    all_coeffs=[]
    for cell in sorted(upper_critical):
        result=defaultdict(int)
        for facet,sign in signed_facets(cell):
            for gen,coef in projection(facet).items():
                result[gen]+=sign*coef
        all_coeffs.append({g:c for g,c in result.items() if c})
    from math import gcd
    from functools import reduce
    content=reduce(gcd,(abs(c) for row in all_coeffs for c in row.values()),0)
    return (len(lower_critical),len(upper_critical)),content,sum(map(len,all_coeffs))

def mod2_homology(faces):
    by_dim=defaultdict(list)
    for f in faces:
        if f:by_dim[len(f)-1].append(f)
    ranks={0:1}
    # Augmented complex: rank(C_0 -> C_{-1})=1.
    for k in range(1,4):
        indexes={f:i for i,f in enumerate(by_dim[k-1])}
        pivots={}
        for upper in by_dim[k]:
            col=0
            for i in range(k+1):
                col ^= 1<<indexes[upper[:i]+upper[i+1:]]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:
                    pivots[p]=col
                    break
        ranks[k]=len(pivots)
    return {k:len(by_dim[k])-ranks[k]-ranks.get(k+1,0)
            for k in range(4) if len(by_dim[k])-ranks[k]-ranks.get(k+1,0)}

def verify(n):
    F=build_faces(n)
    assert len(F)==EXPECTED[n]['faces']
    assert tuple(sum(len(f)==k for f in F) for k in range(1,5)) == EXPECTED[n]['f']
    face_set=set(F)
    assert len(F)==len(face_set)
    for f in F:
        for j in range(len(f)):
            assert f[:j]+f[j+1:] in face_set
    pairs,critical=morse_pairs(F,n)
    assert len(critical)+2*len(pairs)==len(F)
    assert sum((a==() for a,b in pairs))==1
    critical_dims=dict(Counter(len(c)-1 for c in critical))
    assert critical_dims==EXPECTED[n]['crit'],critical_dims
    arcs=check_acyclic(F,pairs)
    assert len(pairs)==(len(F)-len(critical))//2
    k=1 if n==3 else 2
    shape, content, nonzeros=morse_incidence(critical,pairs,k)
    assert content==EXPECTED[n]['incidence_content'],(n,shape,content,nonzeros)
    betti=mod2_homology(F)
    assert betti==EXPECTED[n]['betti'],betti
    return f'n={n} faces={len(F)} pairs={len(pairs)} Hasse_arcs={arcs} critical={critical_dims} F2_Betti={betti} signed_Morse_boundary_shape={shape} content={content} nonzeros={nonzeros}'

if __name__=='__main__':
    for n in sorted(EXPECTED):
        print(verify(n))
    print('VERIFY_OK')
