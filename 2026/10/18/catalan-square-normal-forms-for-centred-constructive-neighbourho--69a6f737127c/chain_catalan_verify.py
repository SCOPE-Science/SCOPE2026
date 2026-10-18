#!/usr/bin/env python3
"""Finite tests for the chain constructive-neighbourhood interval theorem.
Uses only the standard library. Run: python3 chain_catalan_verify.py
"""
import itertools
from math import comb


def upsets(n):
    return [frozenset(range(j,n)) for j in range(n+1)]


def nonempty_centered_families(n, i):
    # All nonempty neighbourhood families whose each member contains i.
    candidates=[frozenset(k for k in range(n) if mask & (1<<k))
                for mask in range(1<<n) if mask & (1<<i)]
    return [tuple(candidates[j] for j in range(len(candidates)) if bits&(1<<j))
            for bits in range(1,1<<len(candidates))]


def raw_signature(frame):
    n=len(frame)
    res=[]
    for U in upsets(n):
        box=[]; dia=[]
        for i in range(n):
            box.append(all(any(a<=U for a in frame[v]) for v in range(i,n)))
            dia.append(all(all(bool(a & U) for a in frame[v]) for v in range(i,n)))
        res.append((tuple(box),tuple(dia)))
    return tuple(res)


def normal_endpoints(frame):
    n=len(frame)
    local_left=[max(min(a) for a in frame[i]) for i in range(n)]
    local_right=[min(max(a) for a in frame[i]) for i in range(n)]
    return tuple(min(local_left[i:]) for i in range(n)),tuple(min(local_right[i:]) for i in range(n))


def canonical_frame(B,D):
    return tuple((frozenset(range(b,d+1)),) for b,d in zip(B,D))


def catalan(n):
    return comb(2*n,n)//(n+1)


def canonical_pairs(n):
    B=[a for a in itertools.combinations_with_replacement(range(n),n)
       if all(a[i]<=i for i in range(n))]
    D=[a for a in itertools.combinations_with_replacement(range(n),n)
       if all(a[i]>=i for i in range(n))]
    assert len(B)==len(D)==catalan(n), (n,len(B),len(D),catalan(n))
    return [(b,d) for b in B for d in D]


def check(n):
    expected=catalan(n)**2
    pairs=canonical_pairs(n)
    signatures={}
    for B,D in pairs:
        s=raw_signature(canonical_frame(B,D))
        assert s not in signatures, (n,B,D,signatures.get(s))
        signatures[s]=(B,D)
    assert len(signatures)==expected
    print('canonical',n,'Catalan',catalan(n),'classes',expected)
    if n>3: return
    count=0
    actual=set()
    fams=[nonempty_centered_families(n,i) for i in range(n)]
    for frame in itertools.product(*fams):
        count+=1
        B,D=normal_endpoints(frame)
        s=raw_signature(frame)
        assert s==raw_signature(canonical_frame(B,D))
        assert s in signatures
        actual.add(s)
    assert len(actual)==expected, (n,len(actual),expected)
    print('all_raw',n,'frames',count,'distinct_classes',len(actual))


if __name__=='__main__':
    for n in range(1,6): check(n)
    print('CHAIN_CONSTRUCTIVE_NEIGHBOURHOOD_CATALAN_VERIFY_OK')
