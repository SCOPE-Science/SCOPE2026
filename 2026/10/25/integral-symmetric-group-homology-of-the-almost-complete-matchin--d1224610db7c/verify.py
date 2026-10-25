#!/usr/bin/env python3
"""Finite exact signed simplex traces and mod-2 homology for M_{n-2}(K_n)."""
from itertools import combinations
from math import comb


def representatives(n):
    def partitions(rest, top):
        if rest == 0:
            yield ()
        else:
            for k in range(min(rest, top), 0, -1):
                for suffix in partitions(rest - k, k):
                    yield (k,) + suffix
    for shape in partitions(n, n):
        permutation = list(range(n))
        j = 0
        for length in shape:
            for k in range(length):
                permutation[j+k] = j+(k+1) % length
            j += length
        yield shape, tuple(permutation)


def valid(mask, n, edges):
    deg = [0] * n
    for j, (u,v) in enumerate(edges):
        if mask & (1 << j):
            deg[u] += 1
            deg[v] += 1
            if deg[u] > n-2 or deg[v] > n-2:
                return False
    return True


def trace(n, perm):
    edges = list(combinations(range(n), 2))
    edgeindex = {e:i for i,e in enumerate(edges)}
    sigmaedge = [edgeindex[tuple(sorted((perm[a],perm[b])))] for a,b in edges]
    seen = set()
    orbits = []
    for i in range(len(edges)):
        if i not in seen:
            cycle=[]
            j=i
            while j not in seen:
                seen.add(j)
                cycle.append(j)
                j=sigmaedge[j]
            orbits.append(cycle)
    signed_euler=0
    for selected in range(1 << len(orbits)):
        face=0
        for j, orbit in enumerate(orbits):
            if selected & (1 << j):
                for e in orbit:
                    face |= 1 << e
        if valid(face,n,edges):
            signed_euler += -1 if selected.bit_count() % 2 == 0 else 1
    inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
    parity=(-1)**inversions
    predicted = parity**(n-1) * (sum(perm[i]==i for i in range(n)) -1)
    d=comb(n-1,2)-1
    measured=(-1)**d * signed_euler
    assert measured == predicted, (n,perm,measured,predicted)
    return measured


def mod2_betti(n):
    edges=list(combinations(range(n),2))
    graded={}
    for mask in range(1<<len(edges)):
        if valid(mask,n,edges):
            graded.setdefault(mask.bit_count()-1,[]).append(mask)
    ranks={}
    for d, faces in graded.items():
        if d<1: continue
        lower_idx = {m:i for i,m in enumerate(graded[d-1])}
        pivots={}
        for m in faces:
            vec=0
            bits=m
            while bits:
                one=bits & -bits
                bits-=one
                vec ^= (1 << lower_idx[m ^ one])
            while vec:
                p=vec.bit_length()-1
                if p in pivots: vec ^= pivots[p]
                else: pivots[p]=vec;break
        ranks[d]=len(pivots)
    # reduced complex: boundary C0 to empty augmentation, rank 1
    ranks[0]=1 if len(graded.get(0,[])) else 0
    betti={}
    for d in sorted(graded):
        if d<0:continue
        b=len(graded[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if b:betti[d]=b
    expected={comb(n-1,2)-1: n-1}
    assert betti==expected,(n,betti,expected)
    return betti


def main():
    cases=0
    for n in range(3,7):
        for shape,perm in representatives(n):
            trace(n,perm)
            cases+=1
    for n in range(3,6):
        mod2_betti(n)
    print('SIMPLE_COMPLETE_HIGHER_MATCHING_EQUIVARIANT_VERIFIED', cases, 'conjugacy_classes', 'n_3_to_6', 'mod2_n_3_to_5')

if __name__ == '__main__': main()
