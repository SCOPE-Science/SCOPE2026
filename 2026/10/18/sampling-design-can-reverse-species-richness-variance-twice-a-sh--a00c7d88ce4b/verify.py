#!/usr/bin/env python3
"""Reproduce exact finite-census richness-variance comparisons.

Run: python verify.py --write-certificate (to regenerate the certificate),
     python verify.py (to compare with the certificate shipped alongside).
Only the Python standard library is used.
"""
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path


def partitions(n, bound=None):
    if n == 0:
        yield ()
        return
    if bound is None:
        bound = n
    for x in range(min(bound, n), 0, -1):
        for tail in partitions(n - x, x):
            yield (x,) + tail


def miss(a, n, m, replacement):
    if replacement:
        return Fraction(n - a, n) ** m
    if n - a < m:
        return Fraction(0)
    return Fraction(comb(n - a, m), comb(n, m))


def variance_moments(profile, m, replacement):
    """Indicator first/second-moment formula, exact rational arithmetic."""
    n = sum(profile)
    absent = [miss(x, n, m, replacement) for x in profile]
    result = sum((q * (1 - q) for q in absent), Fraction())
    for i, ai in enumerate(profile):
        for j in range(i + 1, len(profile)):
            result += 2 * (miss(ai + profile[j], n, m, replacement) - absent[i] * absent[j])
    return result


def variance_direct(profile, m, replacement):
    """Independent exhaustive elementary-outcome count; no moment formula."""
    labels = tuple(i for i, abundance in enumerate(profile) for _ in range(abundance))
    n = len(labels)
    if replacement:
        outcomes = itertools.product(range(n), repeat=m)
        denominator = n ** m
    else:
        outcomes = itertools.combinations(range(n), m)
        denominator = comb(n, m)
    counts = Counter(len(set(labels[i] for i in seq)) for seq in outcomes)
    assert sum(counts.values()) == denominator
    mean = Fraction(sum(x * count for x, count in counts.items()), denominator)
    return Fraction(sum(x*x * count for x, count in counts.items()), denominator) - mean*mean


def sign(value):
    return '+' if value > 0 else '-' if value < 0 else '0'


def changes(signs):
    nz = ''.join(c for c in signs if c != '0')
    return sum(x != y for x, y in zip(nz, nz[1:]))


def frac(x):
    return f'{x.numerator}/{x.denominator}'


def family_difference_2(t):
    return Fraction(-(5*t-1)*(3*t*t-2*t+1), 81*t*t*(3*t-1)**2)


def family_poly_3(t):
    return (8343*t**7-24426*t**6+21591*t**5-5657*t**4-1152*t**3
            +757*t*t-108*t+4)


def family_difference_3(t):
    return Fraction(family_poly_3(t),729*t**4*(3*t-2)**2*(3*t-1)**2)


def family_poly_3_shifted(u):
    return (8343*u**7+92376*u**6+429291*u**5+1080733*u**4
            +1581152*u**3+1329613*u*u+583224*u+98640)


def main():
    records = []
    total_checks = 0
    distributions = {}
    for n in range(1, 7):
        distribution = Counter()
        for profile in partitions(n):
            diffs = []
            for m in range(1, n+1):
                fixed = variance_moments(profile,m,False)
                iid = variance_moments(profile,m,True)
                direct_fixed = variance_direct(profile,m,False)
                direct_iid = variance_direct(profile,m,True)
                assert (fixed,iid) == (direct_fixed,direct_iid), (profile,m)
                total_checks += 2
                if m >= 2:
                    diffs.append(fixed-iid)
            signature=''.join(sign(x) for x in diffs)
            reversal_count=changes(signature)
            distribution[reversal_count]+=1
            records.append({'n':n,'abundances':list(profile),'depths':list(range(2,n+1)),
                            'variance_difference':[frac(x) for x in diffs],
                            'signs':signature,'nonzero_sign_changes':reversal_count})
        distributions[str(n)]={str(k):distribution.get(k,0) for k in range(3)}
    assert sum(v['2'] for v in distributions.values()) == 1
    winners=[x for x in records if x['nonzero_sign_changes'] >= 2]
    assert len(winners)==1 and winners[0]['n']==6 and winners[0]['abundances']==[4,1,1]
    assert winners[0]['variance_difference'][:3]==['-1/100','137/6480','-15211/233280']
    for t in range(2,10):
        profile=(2*t,)+(1,)*t
        assert variance_moments(profile,2,False)-variance_moments(profile,2,True)==family_difference_2(t)
        assert variance_moments(profile,3,False)-variance_moments(profile,3,True)==family_difference_3(t)
        assert family_difference_2(t) < 0 < family_difference_3(t)
        assert family_poly_3(t)==family_poly_3_shifted(t-2)
        assert variance_moments(profile,3*t,False)==0
        assert variance_moments(profile,3*t,True)>0
    cert = {'model':'exact species-richness variance under two sampling designs',
            'definition':'difference = variance(uniform sample of distinct labeled individuals) minus variance(iid draws from same labeled population)',
            'full_finite_domain':'every nonincreasing positive integer partition of each n=1,...,6 and each sampling depth m=1,...,n',
            'independent_method':'explicit labeled subset/ordered draw enumeration compared to absence-indicator second moments',
            'profiles':records,'distributions_by_n':distributions,
            'checked_rational_moment_pairs':total_checks,
            'unbounded_family':'abundances (2t,1 repeated t times), t>=2; exact formulas at depths 2 and 3 and strict negative difference at depth 3t'}
    payload=(json.dumps(cert,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode('utf-8')
    target=Path(__file__).with_name('census_certificate.json')
    if args.write_certificate:
        target.write_bytes(payload)
        print('Wrote certificate:',len(payload),'bytes')
    else:
        assert target.read_bytes()==payload,'certificate regeneration mismatch'
        print('PASS: exact independent moment and outcome enumeration, all',total_checks,'variance pairs')
        print('PASS: all 29 partitions of totals 1..6, exactly one two-switch profile')
        print('PASS: analytic family formulas tested for t=2..9 and positivity-shift identity')
        print('PASS: embedded certificate exactly reproduced')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-certificate',action='store_true')
    args=parser.parse_args()
    main()
