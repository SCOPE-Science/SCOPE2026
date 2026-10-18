"""Exhaustive computational checks of locating-domination identities for private-leaf blowups.

Pure Python 3 standard library. Vertex subsets and neighborhoods are bitmasks.
"""
from itertools import product
from collections import Counter
from math import prod


def make_graph(n, sizes, core_mask):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    total = n + sum(sizes)
    adj = [0]*total
    for pos,(i,j) in enumerate(pairs):
        if (core_mask>>pos)&1:
            adj[i] |= 1<<j
            adj[j] |= 1<<i
    idx=n
    for i,k in enumerate(sizes):
        for _ in range(k):
            adj[i] |= 1<<idx
            adj[idx] |= 1<<i
            idx+=1
    return adj


def dominates(S,adj):
    outsiders=(1<<len(adj))-1 ^ S
    while outsiders:
        bit = outsiders & -outsiders
        v=bit.bit_length()-1
        if not (adj[v] & S): return False
        outsiders ^= bit
    return True


def locating_dominates(S,adj):
    outsiders=(1<<len(adj))-1 ^ S
    seen=set()
    while outsiders:
        bit=outsiders & -outsiders
        v=bit.bit_length()-1
        signal=adj[v] & S
        if not signal or signal in seen: return False
        seen.add(signal)
        outsiders ^= bit
    return True


def expected_polynomial(sizes):
    out = {sum(sizes):1}
    for k in sizes:
        new=Counter()
        for deg, coeff in out.items():
            new[deg] += (k+1)*coeff
            new[deg+1] += coeff
        out=dict(new)
    return out


def check(n,sizes,core_mask):
    adj=make_graph(n,sizes,core_mask)
    N=len(adj)
    freq=Counter()
    good_partitions=0
    both_ld=0
    dommin=N
    for L in range(1<<N):
        D=((1<<N)-1)^L
        if dominates(D,adj):
            dommin=min(dommin,D.bit_count())
        if locating_dominates(L,adj):
            freq[L.bit_count()]+=1
            if dominates(D,adj):
                good_partitions+=1
                if locating_dominates(D,adj):
                    both_ld+=1
    want = expected_polynomial(sizes)
    s=sum(k==1 for k in sizes)
    assert dict(freq)==want, (n,sizes,core_mask,'locating polynomial',dict(freq),want)
    assert good_partitions==2**s, (n,sizes,core_mask,'DLDS',good_partitions,2**s)
    assert both_ld==(2**n if s==n else 0), (n,sizes,core_mask,'double LD',both_ld)
    assert dommin==n, (n,sizes,core_mask,'domination number',dommin)
    return 1<<N


def main():
    tests=0; vertex_subsets=0
    for n in range(1,5):
        num_core_edges=n*(n-1)//2
        for sizes in product((1,2),repeat=n):
            for core_mask in range(1<<num_core_edges):
                vertex_subsets+=check(n,sizes,core_mask)
                tests+=1
    # Larger leaf bunches, disconnected and connected core graphs.
    for n in range(1,4):
        num_core_edges=n*(n-1)//2
        for sizes in product((1,2,3),repeat=n):
            for core_mask in range(1<<num_core_edges):
                vertex_subsets+=check(n,sizes,core_mask)
                tests+=1
    print(f'VERIFY_OK graphs={tests} vertex_subsets={vertex_subsets} full_LD_polynomial=pass DLDS_partition_count=pass two_LD_partition_count=pass domination_number=pass')

if __name__=='__main__': main()
