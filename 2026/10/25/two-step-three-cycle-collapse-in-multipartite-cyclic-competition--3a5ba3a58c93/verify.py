#!/usr/bin/env python3
"""Finite quotient and independent graph-level checks for three-color CCA.

The seven coordinates in the quotient count vertex-part support types, with
multiplicities saturated at two. This is an exact finite factor for any number
of nonempty parts: neighboring successor availability depends only on whether
a color occurs in zero, one, or at least two distinct parts.
Requires Python 3.8+ and no third-party packages.
"""
from itertools import product
from collections import Counter
from math import comb

MASKS=tuple(range(1,8))


def cap2(a): return min(a,2)


def shift_color(mask):
    return sum(1<<((i+1)%3) for i in range(3) if (mask>>i)&1)


def support_step(z):
    """On part-support vectors, for any number of graph parts."""
    nxt=[]
    for k,m in enumerate(z):
        other=0
        for h,s in enumerate(z):
            if h!=k:other|=s
        mm=0
        for i in range(3):
            if m>>i&1:
                target=(i+1)%3
                mm|=1<<(target if other>>target&1 else i)
        nxt.append(mm)
    return tuple(nxt)


def signature(z):
    return tuple(cap2(z.count(m)) for m in MASKS)


def step_counts(cs):
    """Exact transition on saturated multiplicities of 7 nonempty masks."""
    cover=tuple(cap2(sum(cs[k] for k,m in enumerate(MASKS) if m>>i&1)) for i in range(3))
    out=[0]*7
    for k,m in enumerate(MASKS):
        if cs[k]==0:continue
        successor_mask=0
        for i in range(3):
            if m>>i&1:
                target=(i+1)%3
                outside = cover[target]==2 or (cover[target]==1 and not (m>>target&1))
                successor_mask |= 1<<(target if outside else i)
        out[successor_mask-1]=cap2(out[successor_mask-1]+cs[k])
    return tuple(out)


def all_rotating_counts(cs):
    cover=tuple(cap2(sum(cs[k] for k,m in enumerate(MASKS) if m>>i&1)) for i in range(3))
    for k,m in enumerate(MASKS):
        if not cs[k]:continue
        for i in range(3):
            if m>>i&1:
                target=(i+1)%3
                if cover[target]==0 or (cover[target]==1 and (m>>target&1)):
                    return False
    return True


def all_rotating_parts(z):
    return all(any((z[j]>>((i+1)%3))&1 for j in range(len(z)) if j!=k)
               for k,m in enumerate(z) for i in range(3) if (m>>i)&1)


def mono_signature(i):
    return tuple(2 if mask==1<<i else 0 for mask in MASKS)

MONO={mono_signature(i) for i in range(3)}


def onto(k,n):
    return sum((-1)**j * comb(k,j)*(k-j)**n for j in range(k+1))


def exact_periodic_states(part_sizes):
    """Exact formula, computed by a 7^r support sum for small r."""
    total=3
    for z in product(MASKS,repeat=len(part_sizes)):
        if all_rotating_parts(z):
            p=1
            for n,mask in zip(part_sizes,z):p*=onto(mask.bit_count(),n)
            total+=p
    return total


def vertex_step(x,sizes):
    """Independently implemented graph adjacency update, no quotient logic."""
    ends=[0]
    for n in sizes:ends.append(ends[-1]+n)
    y=list(x)
    for p in range(len(sizes)):
        others=[x[v] for v in range(len(x)) if not (ends[p]<=v<ends[p+1])]
        for v in range(ends[p],ends[p+1]):
            s=(x[v]+1)%3
            if s in others:y[v]=s
    return tuple(y)


def test():
    # All realizable saturated profiles with at least three nonempty parts.
    profiles=[p for p in product(range(3),repeat=7) if sum(p)>=3 or (sum(p)==2 and 2 in p)]
    assert len(profiles)==2158
    layers=Counter()
    for p in profiles:
        q=step_counts(p)
        r=step_counts(q)
        good=all_rotating_counts(p) or p in MONO
        assert (step_counts(step_counts(step_counts(p)))==p)==good
        assert all_rotating_counts(r) or r in MONO
        assert step_counts(step_counts(step_counts(r)))==r
        if p in MONO:assert q==p
        if all_rotating_counts(p):
            assert step_counts(p)==signature(tuple(shift_color(m) for m in MASKS for _ in range(p[m-1])))
        layers[0 if good else (1 if all_rotating_counts(q) or q in MONO else 2)]+=1
    assert layers=={0:1972,1:165,2:21}, layers
    print('QUOTIENT_OK: 2158 realizable saturated support signatures')
    print('QUOTIENT_TAIL_COUNTS: 0=1972 1=165 2=21')
    # Explicit finite support vectors, and a separate componentwise implementation.
    for r in range(3,6):
        states=0
        for z in product(MASKS,repeat=r):
            states+=1
            assert step_counts(signature(z))==signature(support_step(z))
            z1=support_step(z)
            z2=support_step(z1)
            assert all_rotating_parts(z2) or len(set(z2))==1 and z2[0] in (1,2,4)
        print('PART_SUPPORT_OK:',r,'parts:',states,'support vectors')
    # Direct vertex dynamics: independent from the quotient and support-count sum.
    samples=((1,1,1),(1,1,2),(1,2,2),(2,2,2),(3,1,1),(2,2,3),
             (3,3,3),(1,1,1,1),(2,1,1,1),(2,2,1,1))
    tested=0
    for sizes in samples:
        observed=Counter()
        for x in product(range(3),repeat=sum(sizes)):
            seen={};y=x; t=0
            while y not in seen and t<7:
                seen[y]=t; y=vertex_step(y,sizes);t+=1
            assert y in seen
            tail,period=seen[y],t-seen[y]
            assert tail<=2 and period in (1,3)
            observed[(tail,period)]+=1
            tested+=1
        value=exact_periodic_states(sizes)
        assert sum(q for (tail,period),q in observed.items() if tail==0)==value
        assert observed[(0,1)]==3
        assert observed[(0,3)]==value-3
        if all(n==1 for n in sizes): assert all(k[0]<=1 for k in observed)
        else: assert any(k[0]==2 and q for k,q in observed.items())
        print('VERTICES_OK:',sizes,'periodic',value,'transients',dict(observed))
    print('VERIFY_OK total labeled configurations:',tested)

if __name__=='__main__':test()
