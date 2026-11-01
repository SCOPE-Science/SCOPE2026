#!/usr/bin/env python3
"""Exact mod-2 homology and signed Lefschetz tests for higher independence of uniformly subdivided stars.
Uses only the Python standard library. Does not assume the proposed formula when building chains.
"""
from itertools import permutations
from math import comb


def graph_faces(m, r):
    # hub 0; near vertices 1..m; far vertices m+1..2m.
    n = 2*m + 1
    faces = []
    for s in range(1 << n):
        if not (s & 1):
            if r >= 2:
                faces.append(s)
            else:
                # Each selected near vertex excludes its far vertex.
                if all(not ((s >> (i+1)) & 1 and (s >> (i+m+1)) & 1) for i in range(m)):
                    faces.append(s)
            continue
        near = sum((s >> (i+1)) & 1 for i in range(m))
        both = sum(((s >> (i+1)) & 1)*((s >> (i+m+1)) & 1) for i in range(m))
        if 1 + near + both <= r:
            faces.append(s)
    return faces


def gf2_reduced_betti(faces, n):
    dimensions = {}
    for s in faces:
        dimensions.setdefault(s.bit_count()-1, []).append(s)
    ranks = {}
    for d in range(0, max(dimensions)+1):
        previous = {s: i for i,s in enumerate(dimensions.get(d-1, []))}
        pivots = {}
        for face in dimensions.get(d, []):
            bd = 0
            for v in range(n):
                if (face >> v) & 1:
                    bd ^= 1 << previous[face ^ (1<<v)]
            while bd:
                p = bd.bit_length()-1
                if p in pivots:
                    bd ^= pivots[p]
                else:
                    pivots[p] = bd
                    break
        ranks[d] = len(pivots)
    return {d:len(dimensions.get(d, []))-ranks.get(d, 0)-ranks.get(d+1, 0)
            for d in range(0, max(dimensions)+1)
            if len(dimensions.get(d, []))-ranks.get(d, 0)-ranks.get(d+1, 0) != 0}


def permutation_parity(images):
    return -1 if sum(images[i] > images[j] for i in range(len(images)) for j in range(i+1,len(images))) % 2 else 1


def lefschetz_reduced(faces, m, p):
    perm = [0] + [1+p[i] for i in range(m)] + [m+1+p[i] for i in range(m)]
    total = 0
    for s in faces:
        verts=[v for v in range(2*m+1) if (s>>v)&1]
        images=[perm[v] for v in verts]
        if set(images) == set(verts):
            total += (-1 if len(verts)%2==0 else 1) * permutation_parity(images)
    return total


def trace_exterior_augmentation(p, q):
    # det(I+t*permutation)=(1+t) det(I+t*augmentation) over Q.
    cycles=[];seen=set()
    for i in range(len(p)):
        if i in seen:continue
        cur=i; length=0
        while cur not in seen:
            seen.add(cur);length+=1;cur=p[cur]
        cycles.append(length)
    num=[1]+[0]*len(p)
    for length in cycles:
        sign=(-1)**(length+1)
        for i in range(len(p)-length,-1,-1):
            num[i+length] += sign*num[i]
    quotient=[]
    for i in range(q+1):
        quotient.append(num[i]-(quotient[i-1] if i else 0))
    return quotient[q]


def expected(m,r):
    q=r-m-1
    if m+1 <= r <= 2*m:
        return {r-1:comb(m-1,q)}
    return {}


def run():
    cases=0;chars=0
    for m in range(1,6):
        for r in range(2,2*m+2):
            f=graph_faces(m,r)
            actual=gf2_reduced_betti(f,2*m+1)
            predicted=expected(m,r)
            assert actual==predicted, ('betti',m,r,actual,predicted)
            cases+=1
            if m <= 5:
                for p in permutations(range(m)):
                    signed_elt=lefschetz_reduced(f,m,p)
                    if predicted:
                        q=r-m-1
                        hom_trace=permutation_parity(p)*trace_exterior_augmentation(p,q)
                        expected_euler=(-1)**(r-1)*hom_trace
                    else:
                        expected_euler=0
                    assert signed_elt==expected_euler, ('Lefschetz',m,r,p,signed_elt,expected_euler)
                    chars+=1
        print('m=',m,'all thresholds passed')
    print('PASS: %d independent mod-2 chain homology tests; %d signed Lefschetz-character tests.' %(cases,chars))

if __name__=='__main__':run()
