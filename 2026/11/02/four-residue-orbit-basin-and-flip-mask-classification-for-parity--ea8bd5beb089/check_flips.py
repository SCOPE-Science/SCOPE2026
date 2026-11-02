#!/usr/bin/env python3
"""Independent finite test of exact periodic XOR flip masks on KG(n,2)."""
from itertools import combinations
from math import comb

def span_generators(vectors):
    b={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p not in b:
                b[p]=v
                break
            v^=b[p]
    return list(b.values())

def bit_image(mask, columns):
    y=0
    while mask:
        bit=mask&-mask
        j=bit.bit_length()-1
        y^=columns[j]
        mask-=bit
    return y

def all_span(basis):
    states={0}
    for v in basis:
        states.update(x^v for x in tuple(states))
    return states

for n in range(5,17):
    pairs=list(combinations(range(n),2))
    N=len(pairs)
    universe=(1<<N)-1
    a_cols=[]
    for s in pairs:
        a_cols.append(sum(1<<i for i,t in enumerate(pairs) if s[0] not in t and s[1] not in t))
    # D=A+I, so D(Ae_j)=(A+I)A e_j if noninvertible and D(e_j) if n is 0 mod 4.
    flip=[]
    for j in range(N):
        p=(1<<j) if n%4==0 else a_cols[j]
        f=bit_image(p,a_cols)
        flip.append(f^p)
    observed=all_span(span_generators(flip))
    expected={0}
    if n%4==1:
        expected.add(universe)
    if n%4 in (0,2):
        for S in range(1<<n):
            if S.bit_count()%2: continue
            cut=sum(1<<i for i,(u,v) in enumerate(pairs) if bool(S>>u&1)!=bool(S>>v&1))
            expected.add(cut)
            if n%4==0: expected.add(universe^cut)
    assert observed==expected,(n,len(observed),len(expected))
    rank_a={0:N,1:N-n+1,2:N-1,3:N-n}[n%4]
    rank_flip=(len(observed)).bit_length()-1
    each= (1<<(rank_a-rank_flip-1)) if rank_flip else 0
    q2=sum(each for d in observed if d)
    total_periodic=1<<rank_a
    fixed=1<<(N-n+(n%2==0))
    assert 2*q2+fixed==total_periodic
    print('n',n,'masks',len(observed)-1,'flip_rank',rank_flip,'each_mask_two_orbits',each,'two_orbits',q2)
print('FLIPS_VERIFY_OK')
