#!/usr/bin/env python3
"""Exact VC/online-shattering checks for nonempty connected subtrees of a three-arm tree.

Python 3.10+, standard library only. Both enumerators construct all eligible hypotheses;
all dimensions are computed from their entire sets, without random sampling.
"""
from functools import lru_cache
from itertools import product
from math import floor, log2


def spine_adjacencies(m):
    n=3*m+1
    adj=[set() for _ in range(n)]
    for arm in range(3):
        last=0
        for k in range(1,m+1):
            v=1+arm*m+k-1
            adj[last].add(v);adj[v].add(last);last=v
    return adj


def by_intervals(m):
    # 0 is the hub, vertices 1+arm*m+j at distance j+1 on arm.
    arms=[[1+arm*m+j for j in range(m)] for arm in range(3)]
    out=set()
    for arm in arms:
        for begin in range(m):
            mask=0
            for end in range(begin,m):
                mask |= 1<<arm[end]
                out.add(mask)
    for a,b,c in product(range(m+1),repeat=3):
        mask=1
        for t,arm in zip((a,b,c),arms):
            for v in arm[:t]:mask|=1<<v
        out.add(mask)
    return tuple(sorted(out))


def by_connected_expansion(m):
    # Independent graph-based enumeration: grow sets from singletons.
    adj=spine_adjacencies(m)
    neighbors=[sum(1<<w for w in row) for row in adj]
    seen={1<<v for v in range(len(adj))}
    queue=list(seen)
    head=0
    while head<len(queue):
        mask=queue[head];head+=1
        avail=0
        for v in range(len(adj)):
            if mask>>v&1:avail|=neighbors[v]
        avail &= ~mask
        while avail:
            bit=avail&-avail;avail-=bit
            nxt=mask|bit
            if nxt not in seen:
                seen.add(nxt);queue.append(nxt)
    return tuple(sorted(seen))


def online_dimension(hypotheses,n):
    col=[]
    for v in range(n):
        col.append(sum(1<<i for i,h in enumerate(hypotheses) if h>>v&1))
    full=(1<<len(hypotheses))-1
    @lru_cache(None)
    def possible(S,k):
        if k==0:return bool(S)
        if S.bit_count()<(1<<k):return False
        for q in col:
            positive=S&q; negative=S&~q
            if positive.bit_count() < (1<<(k-1)):continue
            if negative.bit_count() < (1<<(k-1)):continue
            if possible(positive,k-1) and possible(negative,k-1):return True
        return False
    d=0
    while possible(full,d+1):d+=1
    # Explicitly check the sharp upper obstruction; not merely a timed search.
    assert not possible(full,d+1)
    return d, possible.cache_info().currsize


def online_dimension_alternative(hypotheses,n):
    # An independent set/frozenset representation for the same exact induction.
    allset=frozenset(hypotheses)
    vbits=tuple(1<<v for v in range(n))
    @lru_cache(None)
    def can(S,k):
        if k==0:return len(S)>0
        if len(S)<(1<<k):return False
        for bit in vbits:
            yes=frozenset(h for h in S if h&bit)
            if len(yes)<1<<(k-1) or len(S)-len(yes)<1<<(k-1):continue
            if can(yes,k-1) and can(S-yes,k-1):return True
        return False
    d=0
    while can(allset,d+1):d+=1
    return d,can.cache_info().currsize


def verify_abstract_lower_bound(m):
    # Restrict all three arms to prefix lengths 0..2^r-1, with hub included.
    # The membership queries on arm j binary-search its prefix length,
    # providing r decisions per arm. These 2^(3r) hypotheses are distinct.
    r=(m+1).bit_length()-1
    bits=1<<r
    prefixes=tuple(product(range(bits),repeat=3))
    assert len(prefixes)==(1<<(3*r))
    by= set(by_intervals(m))
    for a,b,c in prefixes:
        mask=1
        for i,L in enumerate((a,b,c)):
            for j in range(L):mask|=1<<(1+i*m+j)
        assert mask in by
    return 3*r


def main():
    vals=[]
    for m in range(1,13):
        H=by_intervals(m)
        H2=by_connected_expansion(m)
        assert H==H2, ('enumerator_disagreement',m)
        assert len(H)==(m+1)**3+3*m*(m+1)//2
        a,states=online_dimension(H,3*m+1)
        b,states2=online_dimension_alternative(H,3*m+1)
        assert a==b, ('independent_dim_disagreement',m,a,b)
        assert a>=verify_abstract_lower_bound(m)
        entropy=len(H).bit_length()-1
        vals.append((m,len(H),a,entropy,entropy-a))
        print('EXACT',m,len(H),a,entropy,entropy-a,'states',states,states2,flush=True)
    assert [v[2] for v in vals]==[3,4,6,6,7,8,9,9,9,9,9,9]
    assert all(v[4]<=1 for v in vals[:-1])
    assert vals[-1][4]==2
    print('FIRST_TWO_BIT_ENTROPY_GAP_PASS m=12 count=2431 VC=3 Ldim=9 entropy_bound=11')
    print('SPIDER_CONNECTED_SUBTREES_ALL_CHECKS_PASS')

if __name__=='__main__':main()
