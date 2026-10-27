#!/usr/bin/env python3
"""Independent exact checks for binary weight-three scattered-deck classification."""
from collections import defaultdict
from itertools import combinations
from math import comb

def words(n):
    for i,j,k in combinations(range(n), 3):
        yield ''.join('1' if t in (i,j,k) else '0' for t in range(n))

def deck_dp(word, k):
    # DP counts scattered subsequences; no gap formula is used.
    d={'': 1}
    for letter in word:
        nxt=d.copy()
        for sub, count in d.items():
            if len(sub)<k:
                nxt[sub+letter]=nxt.get(sub+letter,0)+count
        d=nxt
    return tuple(d.get(format(v,f'0{k}b'),0) for v in range(2**k))

def gap(w):
    z=w.split('1')
    assert len(z)==4
    return tuple(map(len,z))

def word_for(a,b,c,d):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d

def partner(w):
    a,b,c,d=gap(w)
    if b==c or (b-c)%3:
        return None
    s=(b-c)//3
    p=(a+s,c,b,d-s)
    return word_for(*p) if min(p)>=0 else None

def collision_pairs_gf_coefficient(n):
    count=0
    # P_n coefficient z^7/((1-z)^2(1-z^2)(1-z^4))
    for s in range(1,(n-3)//4+1):
        for c in range((n-3-4*s)//2+1):
            r=n-3-4*s-2*c
            count+=r+1
    return count

def check_all():
    examples=[]
    inspected=0
    observed=[]
    for n in range(3,35):
        groups=defaultdict(list)
        for word in words(n):
            groups[deck_dp(word,3)].append(word)
            inspected+=1
        hist=defaultdict(int)
        for cls in groups.values():
            hist[len(cls)]+=1
            assert len(cls)<=2,(n,cls)
            for word in cls:
                expect=partner(word)
                assert (len(cls)==2)==(expect is not None),(n,cls,word,expect)
                if expect is not None:
                    assert expect in cls, (n,cls,word,expect)
        P=collision_pairs_gf_coefficient(n)
        assert hist[2]==P,(n,hist,P)
        assert hist[1]==comb(n,3)-2*P,(n,hist,P)
        assert len(groups)==comb(n,3)-P
        if n<=12:
            examples.append((n,comb(n,3),P,len(groups),dict(hist)))
        observed.append((n,P))
    print('checked exact 3-deck fibers on',inspected,'source words for lengths 3..34')
    print('initial distributions:', examples)
    # Separate exact 4-deck check: ensure no colliding pair remains colliding at length four.
    four_checks=0
    for n in range(7,25):
        for word in words(n):
            mate=partner(word)
            if mate is not None:
                assert deck_dp(word,4)!=deck_dp(mate,4)
                four_checks+=1
    print('verified 4-deck separation for',four_checks,'directed collision cases')
    # Independent direct subsequence enumeration on modest cases.
    total=0
    for n in range(3,12):
        for w in words(n):
            explicit=defaultdict(int)
            for inds in combinations(range(n),3):
                explicit[''.join(w[i] for i in inds)]+=1
            assert tuple(explicit[format(v,'03b')] for v in range(8))==deck_dp(w,3)
            total+=1
    print('independent explicit triple enumerations:',total)
    # Check quasi-polynomial coefficients for all n>=3 in tested range.
    for n,P in observed:
        m,r=divmod(n,4)
        formulas=[m*(m-1)*(4*m-5)//3,
                  2*m*(m-1)*(2*m-1)//3,
                  m*(m-1)*(4*m+1)//3,
                  m*(2*m-1)*(2*m+1)//3]
        assert P==formulas[r], (n,P,formulas[r])
    print('verified all four quasi-polynomial branches through n=34')
    print('VERIFIED_OK')

if __name__=='__main__':check_all()
