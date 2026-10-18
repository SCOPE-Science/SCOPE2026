#!/usr/bin/env python3
"""Exact reproducibility of order-five binary de Bruijn LZ76 exhaustive histories.

No third-party dependencies. Lexicographic cyclic roots are all enumerated, including
non-innovative final components (the standard full-phrase convention).
"""
from collections import Counter

N=32
ALL_EDGES=(1<<N)-1

def switch_cycles():
    """Two incoming-to-outgoing pairings at each of 16 order-four vertices."""
    for selector in range(1<<16):
        next_edge=[0]*N
        for vertex in range(16):
            bit=(selector>>vertex)&1
            next_edge[vertex]=2*vertex+bit
            next_edge[16+vertex]=2*vertex+1-bit
        visited=0
        edge=0
        symbols=[]
        while not ((visited>>edge)&1):
            visited|=1<<edge
            symbols.append(str(edge&1))
            edge=next_edge[edge]
        if len(symbols)==N and edge==0:
            yield ''.join(symbols)

def euler_cycles():
    """Independent full-depth edge-trail enumeration with the edge 00000 fixed first."""
    edge_sequence=[0]
    def recurse(vertex, used):
        if len(edge_sequence)==N:
            if vertex==0:
                yield ''.join(str(edge&1) for edge in edge_sequence)
            return
        for bit in (0,1):
            edge=2*vertex+bit
            if not ((used>>edge)&1):
                edge_sequence.append(edge)
                yield from recurse(edge&15, used|(1<<edge))
                edge_sequence.pop()
    yield from recurse(0,1)

def lz_lpf(word):
    """Full exhaustive LZ76 component count; overlapping sources allowed."""
    p=0
    count=0
    length=len(word)
    while p<length:
        longest=0
        for previous in range(p):
            common=0
            while p+common<length and word[previous+common]==word[p+common]:
                common+=1
            if common>longest:
                longest=common
        p+=min(longest+1,length-p)
        count+=1
    return count

def lz_independent(word):
    """Literal shortest unseen factor; no longest-match computation."""
    p=0
    count=0
    length=len(word)
    while p<length:
        for size in range(1,length-p+1):
            pattern=word[p:p+size]
            # The source is permitted to overlap the current component, but
            # must start at a strictly smaller position.
            if not any(word[q:q+size]==pattern for q in range(p)):
                p+=size
                break
        else:
            # Final component entirely reproducible; counted, not discarded.
            p=length
        count+=1
    return count

def check_debruijn(word):
    return len(word)==N and len({(word+word[:4])[i:i+5] for i in range(N)})==N

def main():
    source_a=list(switch_cycles())
    source_b=list(euler_cycles())
    assert len(source_a)==2048 and len(source_b)==2048
    assert len(set(source_a))==len(source_a)
    assert set(source_a)==set(source_b)
    assert all(check_debruijn(word) for word in source_a)

    histogram=Counter()
    within_cycle=Counter()
    count_by_cycle=Counter()
    for word in source_a:
        values=[]
        for i in range(N):
            rotation=word[i:]+word[:i]
            a=lz_lpf(rotation)
            b=lz_independent(rotation)
            assert a==b,(word,i,a,b)
            values.append(a)
            histogram[a]+=1
        within_cycle[(min(values),max(values))]+=1
        count_by_cycle[sum(values)]+=1
    assert histogram=={8:6766,9:34836,10:23208,11:726}
    assert within_cycle=={(8,10):1228,(8,11):502,(9,10):226,(9,11):92}
    assert sum(histogram.values())==N*2048
    assert sum(within_cycle.values())==2048
    # Both parsers agree with the published sample in Nunes et al. (2013).
    assert lz_lpf('11011101000011')==lz_independent('11011101000011')==6
    assert lz_lpf('010011101101100')==lz_independent('010011101101100')==6
    print('VERIFY_OK debruijn_order5_cycles=2048 switch_assignments=65536 direct_Euler_cycles=2048 rooted_words=65536 independent_LZ76_parsers=2 histogram=8:6766,9:34836,10:23208,11:726 cycle_minmax=8-10:1228,8-11:502,9-10:226,9-11:92')

if __name__=='__main__': main()
