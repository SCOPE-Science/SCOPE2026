#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def rank(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

def span(basis):
    out={0}
    for b in basis:
        out |= {x^b for x in list(out)}
    return frozenset(out)

def all_subspaces(n,r):
    if r==0:
        return [frozenset({0})]
    seen=set()
    for B in combinations(range(1,1<<n),r):
        if rank(B)==r:
            seen.add(span(B))
    return list(seen)

CACHE={}
def subs(n,r):
    key=(n,r)
    if key not in CACHE:
        CACHE[key]=all_subspaces(n,r)
    return CACHE[key]

def canonical_basis(S):
    basis=[]
    for x in sorted(S):
        if x and rank(basis+[x])>len(basis):
            basis.append(x)
    return basis

def support_size(words):
    u=0
    for x in words:
        u |= x
    return u.bit_count()

def image_subspace(message_subspace, generators):
    out=[]
    for msg in message_subspace:
        v=0
        for i,g in enumerate(generators):
            if (msg>>i)&1:
                v ^= g
        out.append(v)
    return out

def support_histogram(generators,r):
    k=len(generators)
    H=Counter()
    for M in subs(k,r):
        H[support_size(image_subspace(M,generators))]+=1
    return H

def ghw(generators,r):
    H=support_histogram(generators,r)
    return min(H)

checked_codes=0
checked_pairs=0
for m in CERT['verification_range']['all_binary_source_lengths']:
    Hcut=2*m
    for k in range(1,m+1):
        for Cmsg in subs(m,k):
            # Treat Cmsg itself as a k-dimensional source code in F_2^m.
            cbasis=canonical_basis(Cmsg)
            assert len(cbasis)==k
            checked_codes += 1

            # Verify the binary support-sum identity on every source r-subspace.
            for r in range(1,k+1):
                for M in subs(k,r):
                    U=image_subspace(M,cbasis)
                    lhs=sum(x.bit_count() for x in U)
                    rhs=(1<<(r-1))*support_size(U)
                    assert lhs==rhs

            # tau duplicates the m coordinates; the final block is disjoint and
            # has weight 2m+1, so words using it lie strictly above H=2m.
            tau_gens=[g | (g<<m) for g in cbasis]
            high=((1<<(2*m+1))-1)<<(2*m)
            agens=tau_gens+[high]

            # Check exact low-word isolation in the surrogate.
            source_words=set(image_subspace(frozenset(range(1<<k)),tau_gens))
            ext_words=set(image_subspace(frozenset(range(1<<(k+1))),agens))
            low={x for x in ext_words if x.bit_count()<=Hcut}
            assert low==source_words

            for r in range(1,k+1):
                HC=support_histogram(cbasis,r)
                HA=support_histogram(agens,r)
                shortA=Counter({j:c for j,c in HA.items() if j<=Hcut})
                expected=Counter({2*j:c for j,c in HC.items()})
                assert shortA==expected
                assert ghw(agens,r)==2*ghw(cbasis,r)
                checked_pairs += 1

assert checked_codes>0 and checked_pairs>0
print('VERIFY_OK')
print('checked_codes',checked_codes)
print('checked_dimension_pairs',checked_pairs)
