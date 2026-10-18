#!/usr/bin/env python3
"""Exact complete discrete-Morse certificate for Ind(Q5). Python 3 stdlib only."""
from collections import Counter, deque
from functools import lru_cache

DIM=5
V=1<<DIM
FULL=(1<<V)-1
NEIGHBORS=tuple(sum(1<<(i^(1<<b)) for b in range(DIM)) for i in range(V))
EXPECTED_POLYNOMIAL=(1,32,416,2880,11760,29856,48960,54304,44240,29920,17952,9088,3672,1120,240,32,2)
EXPECTED_CRITICAL={0:1,5:1,7:10}
EXPECTED_CRITICAL_MASKS=(0x1,0x90010106,0x6996,0x690096,0x6090906,0x12212112,0x14414112,0x16680082,0x82282882,0x84484882,0x90606082,0x96006082)


def enumerate_faces():
    faces=[]
    def walk(allowed, chosen):
        faces.append(chosen)
        while allowed:
            bit=allowed & -allowed
            allowed ^= bit
            i=bit.bit_length()-1
            walk(allowed & ~NEIGHBORS[i],chosen|bit)
    walk(FULL,0)
    assert len(faces)==len(set(faces))==254475
    return faces


def matching(faces):
    alive=set(faces)
    alive.remove(0)  # Standard nonaugmented face poset.
    low_high={}
    order=sorted(range(V),key=lambda v:(v.bit_count()%2,v))
    for v in order:
        bit=1<<v
        for low in tuple(alive):
            upper=low|bit
            if not (low & bit) and upper in alive:
                assert upper.bit_count()==low.bit_count()+1
                low_high[low]=upper
                alive.remove(low)
                alive.remove(upper)
    assert 2*len(low_high)+len(alive)==len(faces)-1
    return low_high,alive


def prove_acyclic(low_high):
    # Forman V-path graph: each paired upper simplex can descend through
    # every OTHER codimension-one facet paired as a lower simplex.
    indices={low:i for i,low in enumerate(low_high)}
    outgoing=[[] for _ in indices]
    indegrees=[0]*len(indices)
    arcs=0
    for low,i in indices.items():
        upper=low_high[low]
        bits=upper
        while bits:
            b=bits & -bits
            bits ^= b
            other=upper^b
            if other==low:
                continue
            j=indices.get(other)
            if j is not None:
                assert other.bit_count()==low.bit_count()
                outgoing[i].append(j)
                indegrees[j]+=1
                arcs+=1
    assert arcs==99497
    ready=deque(i for i,d in enumerate(indegrees) if d==0)
    consumed=0
    while ready:
        i=ready.popleft();consumed+=1
        for j in outgoing[i]:
            indegrees[j]-=1
            if indegrees[j]==0:
                ready.append(j)
    assert consumed==len(indices)==127231, (consumed,len(indices))
    return arcs,consumed


def polynomial_independent():
    @lru_cache(maxsize=None)
    def recurse(mask):
        if mask==0:
            return (1,)
        b=mask & -mask
        v=b.bit_length()-1
        a=recurse(mask^b)
        c=recurse(mask & ~(NEIGHBORS[v]|b))
        out=[0]*max(len(a),len(c)+1)
        for i,k in enumerate(a):out[i]+=k
        for i,k in enumerate(c):out[i+1]+=k
        return tuple(out)
    return recurse(FULL)


def run():
    faces=enumerate_faces()
    pair,critical=matching(faces)
    count=Counter(mask.bit_count()-1 for mask in critical)
    assert dict(count)==EXPECTED_CRITICAL,dict(count)
    assert set(critical)==set(EXPECTED_CRITICAL_MASKS)
    assert len(pair)==127231
    assert sum(count.values())==12
    arcs,vertices=prove_acyclic(pair)
    counts=Counter(mask.bit_count() for mask in faces)
    polynomial=tuple(counts[i] for i in range(17))
    assert polynomial==EXPECTED_POLYNOMIAL
    assert polynomial_independent()==EXPECTED_POLYNOMIAL
    reduced_euler=sum(((-1)**(k-1))*a for k,a in enumerate(polynomial))
    assert reduced_euler==-11
    print('PASS: 254475 faces, 127231 matched pairs, 12 critical cells')
    print('PASS: critical dimensions: 0 (1), 5 (1), 7 (10)')
    print('PASS: gradient graph: %d vertices, %d arcs, acyclic' % (vertices,arcs))
    print('PASS: independence polynomial from two independent methods')
    print('PASS: reduced Euler characteristic -11')
    print('Theorem: integral reduced Ind(Q5) homology Z in degree 5, Z^10 in degree 7.')
    print('Corollary: integral reduced Theta(Cube(5,1)) homology Z^10 in degree 22, Z in degree 24.')


if __name__=='__main__':
    run()
