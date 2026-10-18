#!/usr/bin/env python3
"""Standalone finite checks of two-modality constructive neighborhood semantics on chains."""
from itertools import combinations,product
from math import comb

def families(n):
    sets=[frozenset(j for j in range(n) if mask>>j&1) for mask in range(1,1<<n)]
    for mask in range(1,1<<len(sets)):
        yield tuple(sets[j] for j in range(len(sets)) if mask>>j&1)

def profile(n, frame):
    b=[max(min(a) for a in N) for N in frame]
    d=[min(max(a) for a in N) for N in frame]
    return (tuple(min(b[i:]) for i in range(n)),tuple(min(d[i:]) for i in range(n)))

def upsets(n):
    return [frozenset(range(t,n)) for t in range(n+1)]

def direct_modal(n,frame,U,mode):
    if mode=='box':
        return frozenset(i for i in range(n) if all(any(a<=U for a in frame[j]) for j in range(i,n)))
    return frozenset(i for i in range(n) if all(all(bool(a&U) for a in frame[j]) for j in range(i,n)))

def threshold_modal(n,p,U,mode):
    t=min(U) if U else n
    v=p[0 if mode=='box' else 1]
    return frozenset(i for i,x in enumerate(v) if x>=t)

def representative(B,D):
    f=[]
    for b,d in zip(B,D):
        if b<=d:
            f.append((frozenset((b,d)),))
        else:
            f.append((frozenset((b,)),frozenset((d,))))
    return tuple(f)

def all_sequences(n):
    return tuple(combinations(range(2*n-1),n))

def increasing_profiles(n):
    return tuple(__import__('itertools').combinations_with_replacement(range(n),n))

def check():
    for n in (1,2):
        fams=tuple(families(n)); seen=set(); checked=0
        for fr in product(fams,repeat=n):
            p=profile(n,fr); seen.add(p);checked+=1
            for U in upsets(n):
                for op in ('box','diamond'):
                    assert direct_modal(n,fr,U,op)==threshold_modal(n,p,U,op)
        want=comb(2*n-1,n)**2
        assert len(seen)==want,(n,len(seen),want)
        print('exhaustive_raw',n,checked,'classes',len(seen))
    for n in range(1,6):
        seq=increasing_profiles(n)
        found=set()
        for B,D in product(seq,repeat=2):
            f=representative(B,D)
            assert profile(n,f)==(B,D)
            for U in upsets(n):
                for op in ('box','diamond'):
                    assert direct_modal(n,f,U,op)==threshold_modal(n,(B,D),U,op)
            found.add((B,D))
        want=comb(2*n-1,n)**2
        assert len(found)==want
        print('all_quotient_classes',n,len(found))
    # When n=2 the last world's Box/Diamond maps with b>d cannot
    # arise from a single nonempty neighbourhood.
    n=2; b,d=1,0
    assert all((min(a),max(a))!=(b,d) for a in (frozenset({0}),frozenset({1}),frozenset({0,1})))
    print('two_neighborhoods_sharp_at_terminal_world',True)
if __name__=='__main__':check()
