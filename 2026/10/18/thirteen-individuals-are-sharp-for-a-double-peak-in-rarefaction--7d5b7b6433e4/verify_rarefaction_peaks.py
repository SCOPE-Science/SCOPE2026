"""Exact certificate for a sharp nonunimodal rarefaction-richness variance boundary.

Python 3 standard library only. All counts, moments and comparisons are exact.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb
from collections import defaultdict

@lru_cache(None)
def profiles(total, least=1):
    """All nondecreasing positive-integer partitions of total, once each."""
    if total == 0:
        return ((),)
    return tuple((first,) + rest
                 for first in range(least, total+1)
                 for rest in profiles(total-first, first))

def variance_formula(profile, m):
    total = sum(profile)
    base = comb(total, m)
    absent = [Fraction(comb(total-a, m), base) if m<=total-a else Fraction(0)
              for a in profile]
    result = sum((u*(1-u) for u in absent), Fraction(0))
    for i in range(len(profile)):
        for j in range(i+1, len(profile)):
            remaining = total-profile[i]-profile[j]
            both_absent = Fraction(comb(remaining, m), base) if m<=remaining else Fraction(0)
            result += 2*(both_absent-absent[i]*absent[j])
    return result

def distribution_dp(profile):
    """Independent distribution enumeration by multivariate hypergeometric convolution."""
    states = {(0,0):1}
    for abundance in profile:
        new = defaultdict(int)
        for (drawn, distinct), count in states.items():
            for k in range(abundance+1):
                new[(drawn+k, distinct+(k>0))] += count*comb(abundance,k)
        states = dict(new)
    return states

def variance_dp(states, total, m):
    n = comb(total,m)
    assert sum(weight for (taken,_),weight in states.items() if taken==m)==n
    s1 = sum(k*weight for (taken,k),weight in states.items() if taken==m)
    s2 = sum(k*k*weight for (taken,k),weight in states.items() if taken==m)
    return Fraction(s2,n)-Fraction(s1,n)**2

def maxima(curve):
    return tuple(m for m in range(2,len(curve)) if curve[m-2] < curve[m-1] > curve[m])

def run():
    partition_numbers = (3,5,7,11,15,22,30,42,56,77,101)
    witness = (1,6,6)
    witnesses = []
    total_profiles = 0
    for total, expected in zip(range(3,14), partition_numbers):
        ps=profiles(total)
        assert len(ps)==expected, (total, len(ps), expected)
        hits=[]
        for profile in ps:
            dp=distribution_dp(profile)
            curve=[]
            for m in range(1,total+1):
                val=variance_formula(profile,m)
                assert val==variance_dp(dp,total,m), (profile,m,val)
                curve.append(val)
            peaks=maxima(curve)
            if len(peaks)>=2:
                hits.append((profile,peaks))
        total_profiles += len(ps)
        if total<13:
            assert not hits, (total,hits)
        else:
            assert hits==[(witness,(3,6))], hits
            witnesses=hits
        print('N=%d, profiles=%d, at-least-two-strict-peaks=%d' % (total,len(ps),len(hits)))
    assert total_profiles==369, total_profiles
    curve = tuple(variance_formula(witness,m) for m in range(1,14))
    assert maxima(curve)==(3,6)
    assert curve[1]<curve[2]>curve[3] and curve[4]<curve[5]>curve[6]
    print('verified profiles:',total_profiles)
    print('witness:', witness)
    print('variance sequence:',[str(v) for v in curve])
    print('success: exact formula, independent convolution, sharpness and uniqueness')

if __name__=='__main__':
    run()
