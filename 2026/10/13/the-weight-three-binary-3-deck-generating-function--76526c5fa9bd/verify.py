#!/usr/bin/env python3
import json, math
from itertools import combinations
from pathlib import Path

def C2(x):
    return x*(x-1)//2

def C3(x):
    return x*(x-1)*(x-2)//6

def deck_from_gaps(g):
    a,b,c,d=g
    n=a+b+c+d+3
    return (
        C3(n-3),
        C2(a)+C2(a+b)+C2(a+b+c),
        a*(b+c+d)+(a+b)*(c+d)+(a+b+c)*d,
        3*a+b,
        C2(b+c+d)+C2(c+d)+C2(d),
        2*b+2*c,
        c+3*d,
        1,
    )

def word_from_gaps(g):
    a,b,c,d=g
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d

def deck_direct(w):
    out={format(i,'03b'):0 for i in range(8)}
    for I in combinations(range(len(w)),3):
        out[''.join(w[i] for i in I)] += 1
    return tuple(out[format(i,'03b')] for i in range(8))

def gaps_of_sum(s):
    for a in range(s+1):
        for b in range(s-a+1):
            for c in range(s-a-b+1):
                d=s-a-b-c
                yield (a,b,c,d)

def pair_count(n):
    total=0
    for t in range(1,(n-3)//4+1):
        r=n-3-4*t
        if r < 0:
            continue
        for c in range(r//2+1):
            total += r-2*c+1
    return total

def classified_partner(g):
    a,b,c,d=g
    diff=b-c
    if diff==0 or diff%3:
        return None
    t=diff//3
    gp=(a+t,b-3*t,c+3*t,d-t)
    if t==0 or min(gp)<0:
        return None
    return gp

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
# Independent direct subsequence enumeration validates the eight closed formulas.
for n in range(3,13):
    for g in gaps_of_sum(n-3):
        assert deck_from_gaps(g)==deck_direct(word_from_gaps(g))

# Exhaustive equivalence-class census and classification through n=35.
checked_words=0
max_class=0
for n in range(3,36):
    classes={}
    gaps=list(gaps_of_sum(n-3))
    for g in gaps:
        classes.setdefault(deck_from_gaps(g),[]).append(g)
    checked_words += len(gaps)
    max_class=max(max_class,max(map(len,classes.values())))
    assert max(map(len,classes.values())) <= 2
    two=[v for v in classes.values() if len(v)==2]
    assert len(two)==pair_count(n)
    assert len(classes)==math.comb(n,3)-pair_count(n)
    for pair in two:
        g,h=pair
        assert classified_partner(g)==h or classified_partner(h)==g

# Verify every oriented parameter tuple through n=50 produces exactly one paired class.
param_pairs=set()
for n in range(7,51):
    for t in range(1,(n-3)//4+1):
        r=n-3-4*t
        for c in range(r//2+1):
            for a in range(r-2*c+1):
                e=r-2*c-a
                g=(a,c+3*t,c,t+e)
                h=(a+t,c,c+3*t,e)
                assert sum(g)+3==n==sum(h)+3
                assert deck_from_gaps(g)==deck_from_gaps(h)
                assert g!=h
                param_pairs.add((n,g,h))
    assert sum(1 for q in param_pairs if q[0]==n)==pair_count(n)

# Certificate coefficients and generating-function coefficient identity.
for row in cert['coefficients_0_through_50']:
    n=row['n']
    total=math.comb(n,3) if n>=3 else 0
    p=pair_count(n)
    assert row['weight_three_words']==total
    assert row['paired_classes']==p
    assert row['D_3_3']==total-p

# The collision series is z^7/((1-z)^2(1-z^2)(1-z^4)); coefficient by direct convolution.
def collision_gf_coeff(n):
    s=0
    # z^7 * z^i*z^j*z^(2c)*z^(4q), i,j,c,q>=0
    for q in range((n-7)//4+1 if n>=7 else 0):
        rem=n-7-4*q
        for c in range(rem//2+1):
            r=rem-2*c
            s += r+1
    return s
for n in range(51):
    assert collision_gf_coeff(n)==pair_count(n)

print(f'VERIFY_OK direct_n=3..12 census_n=3..35 words={checked_words} max_class={max_class} gf_n=0..50 D_3_3_7={34} D_3_3_30={math.comb(30,3)-pair_count(30)}')
