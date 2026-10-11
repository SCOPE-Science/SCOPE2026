#!/usr/bin/env python3
"""Separate exact binary homology and independence-polynomial check.

Constructs the H(5,2) graph, rather than relying on generalized Petersen's
adjacency lists, to check the same simplicial invariant from another model.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

N = 20
COUNTS = (1, 20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)

def h52():
    k2 = [sum(1 << i for i in pair) for pair in combinations(range(5), 2)]
    k3 = [sum(1 << i for i in triple) for triple in combinations(range(5), 3)]
    a = [0] * 20
    for i, s in enumerate(k2):
        for j, t in enumerate(k3):
            if s & t == s:
                a[i] |= 1 << (j + 10)
                a[j+10] |= 1 << i
    assert all(z.bit_count() == 3 for z in a)
    return a

def fpolynomial(adj):
    @lru_cache(None)
    def poly(vertices):
        if vertices == 0:
            return (1,)
        bit = vertices & -vertices
        v = bit.bit_length() - 1
        rest = vertices ^ bit
        minus = poly(rest)
        plus = poly(rest & ~adj[v])
        answer = [0] * max(len(minus), len(plus)+1)
        for k,x in enumerate(minus):answer[k] += x
        for k,x in enumerate(plus):answer[k+1] += x
        while answer and not answer[-1]:answer.pop()
        return tuple(answer)
    return poly((1<<N)-1)

def enumerate_independent(adj):
    groups=defaultdict(list)
    groups[0].append(0)
    def extend(part, options):
        while options:
            bit=options&-options
            options^=bit
            new=part|bit
            groups[new.bit_count()].append(new)
            extend(new, options & ~adj[bit.bit_length()-1])
    extend(0,(1<<N)-1)
    return groups

def rank_binary(columns):
    pivots={}
    for z in columns:
        while z:
            d=z.bit_length()-1
            if d in pivots:z^=pivots[d]
            else:
                pivots[d]=z
                break
    return len(pivots)

def main():
    adj=h52()
    # Explicit isomorphism: GP(10,3) labels -> H(5,2) labels.
    phi=(0,10,4,16,7,19,9,15,3,12,11,1,17,5,13,8,18,2,14,6)
    assert sorted(phi)==list(range(N))
    gp_edges=set()
    for i in range(10):
        for u,v in ((i,(i+1)%10),(10+i,10+(i+3)%10),(i,10+i)):
            gp_edges.add(tuple(sorted((phi[u],phi[v]))))
    h_edges={tuple(sorted((i,j))) for i in range(N) for j in range(N)
             if adj[i] & (1<<j)}
    assert len(gp_edges)==len(h_edges)==30 and gp_edges==h_edges
    f=fpolynomial(adj)
    assert f==COUNTS,(f,COUNTS)
    groups=enumerate_independent(adj)
    assert tuple(len(groups[k]) for k in range(11))==COUNTS
    ranks={}
    for k in range(1,11):
        prev={face:i for i,face in enumerate(groups[k-1])}
        cols=[]
        for face in groups[k]:
            bitset=0
            for j in range(N):
                if face & (1<<j):bitset^=1 << prev[face^(1<<j)]
            cols.append(bitset)
        ranks[k-1]=rank_binary(cols)
    reduced_betti={}
    for d in range(10):
        dimC=len(groups[d+1]); down = ranks[d] if d else ranks[0]
        # reduced C_0 -> C_{-1} has rank one
        if d==0: down=1
        up=ranks[d+1] if d+1 in ranks else 0
        reduced_betti[d]=dimC-down-up
    # Recompute GF(2) ranks independently from Morse output, including
    # nonpure maximal simplices in size 10.
    assert reduced_betti == {d:({4:1,5:5}.get(d,0)) for d in range(10)},reduced_betti
    euler=sum((-1)**(size-1)*cnt for size,cnt in enumerate(f) if size>0)
    assert euler==1+1-5 == -3, euler
    print('DESARGUES_H52_HOMOLOGY_OK', 'fvector=',f,'boundary_ranks=',ranks,
          'reduced_F2_betti=',reduced_betti,'euler=',euler)

if __name__=='__main__':
    main()
