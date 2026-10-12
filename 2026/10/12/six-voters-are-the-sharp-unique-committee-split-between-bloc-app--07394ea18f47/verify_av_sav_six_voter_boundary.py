#!/usr/bin/env python3
from itertools import product, permutations
from fractions import Fraction
from math import factorial
from collections import Counter

BALLOTS = (1,2,4,3,5,6,7)  # A,B,C,AB,AC,BC,ABC

def scores(profile):
    av = [0,0,0]
    sav = [Fraction(0),Fraction(0),Fraction(0)]
    for mask in profile:
        k = mask.bit_count()
        for c in range(3):
            if mask & (1 << c):
                av[c] += 1
                sav[c] += Fraction(1,k)
    return tuple(av), tuple(sav)

def unique_committee(score):
    # committee size 2 among 3 candidates: unique committee iff unique loser
    lo = min(score)
    losers = [i for i,x in enumerate(score) if x == lo]
    if len(losers) != 1:
        return None
    loser = losers[0]
    return tuple(i for i in range(3) if i != loser)

def eval_profile(profile):
    av,sav = scores(profile)
    return av,sav,unique_committee(av),unique_committee(sav)

def weak_compositions(n,k,prefix=()):
    if k == 1:
        yield prefix + (n,)
        return
    for x in range(n+1):
        yield from weak_compositions(n-x,k-1,prefix+(x,))

def anonymous_eval(counts):
    profile=[]
    for cnt,b in zip(counts,BALLOTS):
        profile.extend([b]*cnt)
    return eval_profile(tuple(profile))

def multinomial(counts):
    n=sum(counts)
    z=factorial(n)
    for x in counts:
        z//=factorial(x)
    return z

def permute_mask(mask,p):
    out=0
    for c in range(3):
        if mask & (1<<c):
            out |= 1 << p[c]
    return out

def permute_counts(counts,p):
    out=[0]*7
    index={b:i for i,b in enumerate(BALLOTS)}
    for cnt,b in zip(counts,BALLOTS):
        out[index[permute_mask(b,p)]] = cnt
    return tuple(out)

# Full labeled enumeration through the boundary.
expected_both = {1:3,2:27,3:201,4:1467,5:10398,6:75051}
expected_conf = {1:0,2:0,3:0,4:0,5:0,6:360}
for n in range(1,7):
    both=conf=0
    for profile in product(BALLOTS, repeat=n):
        _,_,avc,savc = eval_profile(profile)
        if avc is not None and savc is not None:
            both += 1
            if avc != savc:
                conf += 1
    assert both == expected_both[n], (n,both)
    assert conf == expected_conf[n], (n,conf)

# Independent anonymous enumeration at n=6.
conf_anon=[]
weighted=0
for counts in weak_compositions(6,7):
    _,_,avc,savc = anonymous_eval(counts)
    if avc is not None and savc is not None and avc != savc:
        conf_anon.append(counts)
        weighted += multinomial(counts)

assert len(conf_anon) == 6
assert weighted == 360

rep=(0,1,2,3,0,0,0)  # B + 2C + 3AB
orbit={permute_counts(rep,p) for p in permutations(range(3))}
assert len(orbit) == 6
assert set(conf_anon) == orbit

rep_av,rep_sav,rep_avc,rep_savc = anonymous_eval(rep)
assert rep_av == (3,4,2)
assert rep_sav == (Fraction(3,2),Fraction(5,2),Fraction(2,1))
assert rep_avc == (0,1)
assert rep_savc == (1,2)
assert multinomial(rep) == 60

# Direct arithmetic lower-bound conditions in the oriented conflict
# AV elects AB while SAV elects BC. Exhaustively confirm every oriented
# conflict through n=6 obeys the derived inequalities.
for n in range(1,7):
    for counts in weak_compositions(n,7):
        a,b,c,ab,ac,bc,abc=counts
        av,sav,avc,savc=anonymous_eval(counts)
        if avc==(0,1) and savc==(1,2):
            d=c-a
            e=ab-bc
            assert d >= 2
            assert e >= d+1
            if n == 6:
                assert counts == rep

print("VERIFY_OK")
print("labeled_both_unique", expected_both)
print("labeled_conflicts", expected_conf)
print("anonymous_conflicts_n6", len(conf_anon))
print("representative_counts_A_B_C_AB_AC_BC_ABC", rep)
print("representative_AV_scores", rep_av)
print("representative_SAV_scores", [str(x) for x in rep_sav])
print("representative_labeled_multiplicity", multinomial(rep))
print("candidate_orbit_size", len(orbit))
