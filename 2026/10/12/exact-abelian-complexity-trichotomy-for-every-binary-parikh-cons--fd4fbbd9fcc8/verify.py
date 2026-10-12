#!/usr/bin/env python3
"""Reproducible finite portion of the binary ternary-uniform classification.

The infinite induction and factor-interval argument appear in RESULT.md.
"""
from itertools import product

FULL = {(a,b) for a in (0,1) for b in (0,1)}
A = {('001','001'),('010','010'),('011','011')}
B = {('001','010'),('010','001'),('010','100'),('011','101')}
C = {('001','100'),('011','110')}
FAMILY = sorted(A|B|C)
assert len(FAMILY)==9


def word(zero,one,target):
    w='0'
    while len(w)<target:
        w=''.join((zero,one)[int(a)] for a in w)
    return w


def spectrum(w,n):
    sums=[]
    s=0
    for k,c in enumerate(w):
        s+=int(c)
        if k>=n:s-=int(w[k-n])
        if k+1>=n:sums.append(s)
    return min(sums),max(sums)


def envelope(zero,one,r):
    cc=zero.count('1')
    pref=[[sum(map(int,w[:j])) for j in range(4)] for w in (zero,one)]
    return [int(j+r>=3)*cc-pref[a][j]+pref[b][(j+r)%3]
            for j in range(3) for a,b in FULL]


def predicted(pair,n):
    if pair in A:return 1 if n%3==0 else 2
    if pair in B:return 3 if n%3==0 else 2
    if pair in C:return 2 if n==1 else 3
    raise ValueError(pair)

all_lag_checks=0
all_envelope_checks=0
all_prefix_checks=0
all_distinct_checks=0
for zero,one in FAMILY:
    w=word(zero,one,3**8)[:3**8]
    if (zero,one) not in A:
        # Literal finite witnesses for all four ordered pairs, for d=3..8.
        for d in range(3,9):
            pairs={(int(w[i]),int(w[i+d])) for i in range(len(w)-d)}
            assert pairs==FULL,(zero,one,d,pairs)
            all_lag_checks+=1
        # Symbolic induction step: complete pair sets at k,k+1 force
        # complete pair sets at 3k,3k+1,3k+2.
        for s in range(3):
            image_pairs=set()
            for r in range(3):
                for a,b in FULL:
                    image_pairs.add((int((zero,one)[a][r]),
                                     int((zero,one)[b][(r+s)%3])))
            assert image_pairs==FULL,(zero,one,s,image_pairs)
            all_lag_checks+=1
        # Exact boundary envelopes for each residue.
        expected={'001010':[(-1,1),(0,1),(0,1)],
                  '001100':[(-1,1),(-1,1),(0,2)],
                  '010001':[(-1,1),(0,1),(0,1)],
                  '010100':[(-1,1),(0,1),(0,1)],
                  '011101':[(-1,1),(0,1),(1,2)],
                  '011110':[(-1,1),(0,2),(0,2)]}[zero+one]
        for r in range(3):
            e=envelope(zero,one,r)
            assert (min(e),max(e))==expected[r]
            all_envelope_checks+=1
        # The finite cases n=1..8, not subject to pair-set induction.
        for n in range(1,9):
            mn,mx=spectrum(w,n)
            assert mx-mn+1==predicted((zero,one),n), (zero,one,n,mn,mx)
            if n>=3:
                k,r=divmod(n,3)
                e=envelope(zero,one,r)
                assert (mn,mx)==(k*zero.count('1')+min(e),k*zero.count('1')+max(e))
            all_envelope_checks+=1
    else:
        # Equal images -> periodic word, with period 3.
        assert zero==one
    # Independent finite sliding-window test well past the induction basis.
    for n in range(1,1025):
        got=spectrum(w,n)
        assert got[1]-got[0]+1==predicted((zero,one),n),(zero,one,n,got)
        all_prefix_checks+=1
        if n<=64:
            prefix=[0]
            for c in w: prefix.append(prefix[-1]+int(c))
            full_classes={prefix[i+n]-prefix[i] for i in range(len(w)-n+1)}
            assert len(full_classes)==predicted((zero,one),n)
            all_distinct_checks+=1

print('VERIFY_OK morphisms=9 nonconstant=6 pair_base_and_step=%d boundary=%d prefix_checks=%d direct_class_checks=%d'
      %(all_lag_checks,all_envelope_checks,all_prefix_checks,all_distinct_checks))
