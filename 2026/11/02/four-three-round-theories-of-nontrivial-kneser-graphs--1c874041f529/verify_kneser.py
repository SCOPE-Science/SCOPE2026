#!/usr/bin/env python3
"""Finite checks of exact third-vertex adjacency-extension spectra of Kneser graphs.
No infinite-range claim is inferred from this finite check.
"""
from itertools import combinations
from math import comb


def predicted_class(n,k):
    assert 2 <= k and 2*k <= n
    if n == 2*k: return 'M'
    if n <= 3*k-2: return 'L'
    if n == 3*k-1: return 'T'
    return 'S'


def symbolic_pair_spectrum(n,k):
    # Pair encoding: (edge_bit, four-bit mask for third vertices in
    # order nonneighbor/nonneighbor, neighbor-of-first only,
    # neighbor-of-second only, neighbor-of-both).
    if n == 2*k:
        return frozenset({(1,1),(0,7)})
    out=set()
    for overlap in range(k):
        edge=int(overlap==0)
        third_mask=7+(8 if n >= 3*k-overlap else 0)
        out.add((edge,third_mask))
    return frozenset(out)


def brute_pair_spectrum(n,k):
    vertices=[sum(1<<i for i in s) for s in combinations(range(n),k)]
    N=len(vertices)
    adjacency=[0]*N
    for i in range(N):
        xi=vertices[i]
        for j in range(i+1,N):
            if not xi & vertices[j]:
                adjacency[i] |= 1<<j
                adjacency[j] |= 1<<i
    full=(1<<N)-1
    out=set()
    for j in range(1,N):
        active=full ^ 1 ^ (1<<j)
        xadj=adjacency[0] & active
        yadj=adjacency[j] & active
        presence=(int(bool(active & ~(xadj|yadj)))
                  | 2*int(bool(xadj & ~yadj))
                  | 4*int(bool(yadj & ~xadj))
                  | 8*int(bool(xadj & yadj)))
        out.add((int(bool(adjacency[0]&(1<<j))),presence))
    return frozenset(out)


def main():
    base={(4,2):'M',(7,3):'L',(5,2):'T',(6,2):'S'}
    target={c:symbolic_pair_spectrum(n,k) for (n,k),c in base.items()}
    assert len(set(target.values())) == 4
    checks=0
    maximum=0
    visited=[]
    for k in range(2,8):
        for n in range(2*k,4*k+4):
            if comb(n,k)>950: continue
            sym=symbolic_pair_spectrum(n,k)
            brute=brute_pair_spectrum(n,k)
            assert sym==brute, (n,k,sym,brute)
            c=predicted_class(n,k)
            assert sym==target[c], (n,k,c,sym,target[c])
            checks+=1
            maximum=max(maximum,comb(n,k))
            visited.append((n,k,c,comb(n,k)))
    print('verified_parameter_pairs',checks)
    print('largest_graph_order',maximum)
    print('representative_signatures', {c:sorted(x) for c,x in sorted(target.items())})
    print('verified_examples',visited)
    print('PASS')

if __name__=='__main__': main()
