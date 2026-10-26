#!/usr/bin/env python3
"""Exact rational certificate for the three-species sampling-effort example."""
from fractions import Fraction
import json

def expected_singletons(n, probabilities):
    assert n>=1 and sum(probabilities)==1
    return n*sum((p*(1-p)**(n-1) for p in probabilities),Fraction(0))

def main():
    probabilities=[Fraction(9899,10000),Fraction(100,10000),Fraction(1,10000)]
    checked={n:expected_singletons(n, probabilities) for n in [1,2,3,99,100,101,102,103,104,999,1000,1001,9998,9999,10000,10001]}
    peaks=[1,102,9999]
    assert checked[1]>checked[2]
    assert all(checked[n]>checked[n-1] and checked[n]>checked[n+1] for n in peaks[1:])
    assert checked[100]>checked[2]
    assert checked[100]>checked[1000]
    assert checked[9999]>checked[1000]
    assert checked[9999]>checked[10000]
    output={'probabilities':['9899/10000','1/100','1/10000'],
            'strict_local_maxima_verified':[1,102,9999],
            'checked_sample_sizes':sorted(checked),
            'inequalities':{'s1>s2':True,'s102>s101':True,'s102>s103':True,
                            's9999>s9998':True,'s9999>s10000':True,
                            's100>s2':True,'s100>s1000':True,'s9999>s1000':True},
            'analytic_upper_bound_needed_for_exhaustiveness':True,
            'method':'exact integer rational arithmetic, no floating point'}
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
