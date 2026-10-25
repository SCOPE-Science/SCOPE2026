#!/usr/bin/env python3
"""Independent, finite obstruction check for open-neighborhood VC-dimension of KG(n,3).

The proof outside this program reduces a hypothetical shattered family of seven
triples to a seven-edge multigraph with a vertex cover of at most three points.
Core edges and peripheral incidence vectors enumerate every such multigraph,
with arbitrary parallel edges. A private element per triple adds singleton stars.
No randomized test, external library, network resource, or partial enumeration.
"""
from itertools import combinations
from math import comb


def peripheral_types(m):
    return sorted(
        ((a,b,c) for a in range(m+1) for b in range(m+1-a)
         for c in range(m+1-a-b) if a+b+c>0),
        key=lambda t:(sum(t),t)
    )


def peripheral_multisets(types,left,start=0):
    if left==0:
        yield ()
        return
    for i in range(start,len(types)):
        size=sum(types[i])
        if size>left:
            break
        for suffix in peripheral_multisets(types,left-size,i):
            yield (i,)+suffix


def stars_for_profile(m,core,outer,types):
    masks=[0,0,0]
    bit=0
    for a,b,count in ((0,1,core[0]),(0,2,core[1]),(1,2,core[2])):
        for _ in range(count):
            masks[a]|=1<<bit
            masks[b]|=1<<bit
            bit+=1
    for i in outer:
        peripheral_star=0
        for a,count in enumerate(types[i]):
            for _ in range(count):
                masks[a]|=1<<bit
                peripheral_star|=1<<bit
                bit+=1
        masks.append(peripheral_star)
    assert bit==m
    return masks


def patterns_using_at_most_three(m,stars):
    options={0}|{1<<i for i in range(m)}|set(stars)
    attained={0}
    for _ in range(3):
        attained={x|y for x in attained for y in options}
    return attained


def classify(m):
    types=peripheral_types(m)
    total=full=0
    most=0
    minimum_shared=None
    witness=None
    for a in range(m+1):
        for b in range(m-a+1):
            for c in range(m-a-b+1):
                core=(a,b,c)
                for outer in peripheral_multisets(types,m-a-b-c):
                    total+=1
                    stars=stars_for_profile(m,core,outer,types)
                    size=len(patterns_using_at_most_three(m,stars))
                    most=max(most,size)
                    if size==1<<m:
                        full+=1
                        shared=sum(mask!=0 for mask in stars)
                        if minimum_shared is None or shared<minimum_shared:
                            minimum_shared=shared
                            witness=(core,tuple(types[i] for i in outer))
    return total,full,most,minimum_shared,witness


def verify_explicit_witness(block_sizes):
    # One common point occurs in every triple; one block-specific point
    # occurs in each block, alongside the individual private point.
    triples=[]
    common=0
    next_vertex=1+len(block_sizes)
    for block,size in enumerate(block_sizes):
        for _ in range(size):
            triples.append({common,block+1,next_vertex})
            next_vertex+=1
    extras=list(range(next_vertex,next_vertex+3))
    ground=set(range(next_vertex+3))
    m=len(triples)
    patterns=set()
    for center in combinations(sorted(ground),3):
        hit=sum(1<<i for i,t in enumerate(triples) if any(x in t for x in center))
        patterns.add(hit)
    assert len(patterns)==1<<m, (block_sizes,len(patterns))
    return len(ground),m


def verify_single_common_pair(m):
    triples=[{0,1,i+2} for i in range(m)]
    ground=set(range(m+5))
    patterns=set()
    for C in combinations(sorted(ground),3):
        patterns.add(sum(1<<i for i,F in enumerate(triples) if not F.isdisjoint(C)))
    assert len(patterns)==1<<m
    return len(ground)


def independent_profile_count(m):
    # Ordinary generating function: three core edge types plus peripheral
    # incidence types; coefficient extraction independent of enumeration.
    p=[1]+[0]*m
    for size in range(1,m+1):
        types=comb(size+2,2)+(3 if size==1 else 0)
        for _ in range(types):
            for j in range(size,m+1):
                p[j]+=p[j-size]
    return p[m]


def main():
    for m in (1,2,3,4):
        assert verify_single_common_pair(m)==m+5
    assert verify_explicit_witness((2,3))==(11,5)
    assert verify_explicit_witness((2,2,2))==(13,6)
    print('Explicit witnesses: m<=4 at n=m+5, m=5 at n=11, m=6 at n=13: PASS')
    for m in (5,6,7):
        data=classify(m)
        assert data[0]==independent_profile_count(m)
        print('m=',m,'number_of_profiles=',data[0],
              'full_trace_profiles=',data[1],
              'max_distinct_traces=',data[2],
              'minimum_shared_vertices=',data[3])
        if m==5:assert data[3]==3
        if m==6:assert data[3]==4
        if m==7:assert data[:3]==(9177,0,124)
    print('COMPLETE FINITE OBSTRUCTION CERTIFICATE: PASS')

if __name__=='__main__':
    main()
