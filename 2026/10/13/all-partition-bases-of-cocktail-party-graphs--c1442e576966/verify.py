#!/usr/bin/env python3
from itertools import product


def vertices(n):
    return tuple((s,i) for i in range(n) for s in (0,1))

def mate(v):
    s,i=v; return (1-s,i)

def dist(u,v):
    if u==v: return 0
    if mate(u)==v: return 2
    return 1

def rep(v, part):
    return tuple(min(dist(v,x) for x in block) for block in part)

def resolves(part):
    seen=set()
    for block in part:
        for v in block:
            r=rep(v,part)
            if r in seen: return False
            seen.add(r)
    return True

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b:(len(b),b)))

def set_partitions(seq):
    seq=list(seq)
    def rec(i, blocks):
        if i==len(seq):
            yield canon(blocks); return
        x=seq[i]
        for j in range(len(blocks)):
            nb=[set(b) for b in blocks]
            nb[j].add(x)
            yield from rec(i+1, nb)
        yield from rec(i+1, blocks+[set([x])])
    seen=set()
    for p in rec(0,[]):
        if p not in seen:
            seen.add(p); yield p

def classify(n,p):
    blocks=[set(b) for b in p]
    singles=[next(iter(b)) for b in blocks if len(b)==1]
    nons=[b for b in blocks if len(b)>1]
    if len(singles)==n and len(nons)==1 and len(nons[0])==n:
        C=nons[0]
        return 'I' if all(sum((s,i) in C for s in (0,1))==1 for i in range(n)) else None
    if len(singles)==n-1 and len(nons)==2 and sum(map(len,nons))==n+1:
        sing=set(singles)
        split=[]; whole=[]
        for i in range(n):
            c=sum((s,i) in sing for s in (0,1))
            if c==1: split.append(i)
            elif c==0: whole.append(i)
            else: return None
        if len(split)!=n-1 or len(whole)!=1: return None
        r=whole[0]
        if not all(any((s,r) in B for s in (0,1)) for B in nons): return None
        if any(len(B)<2 for B in nons): return None
        return 'II'
    return None

def generate_bases(n):
    V=set(vertices(n))
    out=set()
    # Type I.
    for bits in product((0,1), repeat=n):
        C={(bits[i],i) for i in range(n)}
        blocks=[C]+[{v} for v in V-C]
        out.add(canon(blocks))
    # Type II.
    for r in range(n):
        others=[i for i in range(n) if i!=r]
        for singleton_bits in product((0,1), repeat=n-1):
            singles={(singleton_bits[j],i) for j,i in enumerate(others)}
            mates=[mate(v) for v in singles]
            # U is canonically the nonsingleton block containing (0,r).
            for mask in range(1,(1<<(n-1))-1):
                U={(0,r)}; W={(1,r)}
                for j,v in enumerate(mates):
                    (U if (mask>>j)&1 else W).add(v)
                blocks=[U,W]+[{v} for v in singles]
                out.add(canon(blocks))
    return out

def formula(n):
    return 2**n + n*(2**(n-1))*(2**(n-1)-2)

partitions_tested=0
basis_counts=[]
for n in range(3,6):
    V=vertices(n)
    resolving=[]
    min_k=None
    for p in set_partitions(V):
        partitions_tested+=1
        k=len(p)
        if min_k is not None and k>min_k: continue
        if resolves(p):
            if min_k is None or k<min_k:
                min_k=k; resolving=[p]
            elif k==min_k:
                resolving.append(p)
    assert min_k==n+1, (n,min_k)
    assert len(resolving)==formula(n), (n,len(resolving),formula(n))
    assert all(classify(n,p) in ('I','II') for p in resolving)
    gen=generate_bases(n)
    assert len(gen)==formula(n)
    assert set(resolving)==gen
    basis_counts.append(len(resolving))

construction_checks=0
for n in range(3,9):
    gen=generate_bases(n)
    assert len(gen)==formula(n)
    for p in gen:
        assert resolves(p)
        assert classify(n,p) in ('I','II')
        construction_checks+=1

print('VERIFY_OK exhaustive_n=3..5 partitions_tested=%d basis_counts=%s construction_n=3..8 construction_checks=%d' % (
    partitions_tested, ','.join(map(str,basis_counts)), construction_checks))
