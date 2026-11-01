#!/usr/bin/env python3
"""Exact finite checks for sliding min/max and path-variation constants.

Only finite cases are checked. General statements require the analytic proof.
"""
from fractions import Fraction as Q
from itertools import permutations
from random import Random


def window_selector(values, radius, use_min=True):
    n = len(values)
    chooser = min if use_min else max
    return tuple(chooser(range(max(0, i-radius), min(n, i+radius+1)),
                         key=lambda j: values[j]) for i in range(n))


def morph(values, radius, use_min=True):
    p = window_selector(values, radius, use_min)
    return tuple(values[j] for j in p)


def variations(values, weights):
    return sum((Q(w) * abs(values[i+1] - values[i]) for i,w in enumerate(weights)), Q(0))


def expected_pairs(n, radius):
    return {(i,k) for i in range(n-1) for k in range(n-1)
            if (i >= radius or i+radius+1 < n)
            and max(0, i-radius) <= k <= min(n-2, i+radius)}


def construct(n, r, i, k):
    f = [10+j for j in range(n)]
    if i >= r:
        f[i-r] = 0
        f[k+1] = 1
    else:
        f[i+r+1] = 0
        f[k] = 1
    return tuple(Q(x) for x in f)


def predicted_norm(n, r, w):
    pairs=expected_pairs(n,r)
    return max((Q(w[i],w[k]) for i,k in pairs), default=Q(0))


def main():
    rng=Random(72359)
    profile_count=0; selector_checks=0; exact_witnesses=0
    ratio_tests=0; weight_cases=0
    for n in range(2,9):
        for r in range(0,n):
            expected=expected_pairs(n,r)
            got=set()
            for p_values in permutations(range(n)):
                p=window_selector(p_values,r,True)
                assert all(p[i]<=p[i+1] for i in range(n-1))
                for i in range(n-1):
                    for k in range(p[i],p[i+1]):
                        got.add((i,k))
                selector_checks+=1
            assert expected == got, (n,r,got-expected,expected-got)
            profile_count+=1
            for i,k in expected:
                f=construct(n,r,i,k)
                h=tuple(Q(j>k) for j in range(n))
                eps=Q(1,100)
                for use_min in [True,False]:
                    sign=1 if use_min else -1
                    ff=tuple(sign*x for x in f)
                    f2=tuple(ff[j]+eps*h[j] for j in range(n))
                    p=window_selector(ff,r,use_min)
                    assert p[i]<=k<p[i+1]
                    for w in [[1]*(n-1),list(range(1,n)),list(range(n-1,0,-1))]:
                        y1=morph(ff,r,use_min)
                        y2=morph(f2,r,use_min)
                        lhs=variations(tuple(y2[j]-y1[j] for j in range(n)),w)
                        rhs=variations(tuple(f2[j]-ff[j] for j in range(n)),w)
                        assert lhs * w[k] == rhs * w[i], (n,r,i,k,w,lhs,rhs)
                        exact_witnesses+=1
            for w in ([1]*(n-1),list(range(1,n)),list(range(n-1,0,-1)),
                      [rng.randrange(1,9) for _ in range(n-1)]):
                L=predicted_norm(n,r,w)
                assert L>=0
                weight_cases+=1
                for _ in range(15):
                    f=tuple(Q(rng.randrange(-8,9)) for _ in range(n))
                    g=tuple(Q(rng.randrange(-8,9)) for _ in range(n))
                    for use_min in (True,False):
                        d=tuple(a-b for a,b in zip(morph(f,r,use_min),morph(g,r,use_min)))
                        h=tuple(a-b for a,b in zip(f,g))
                        assert variations(d,w)<=L*variations(h,w), (n,r,w,L)
                        ratio_tests+=1
                if r == n-1:
                    assert L == 0
                elif r>0:
                    a=set(range(0,n-r-1))|set(range(r,n-1))
                    c=[w[i] for i in sorted(a)]
                    classification=(len(set(c))==1 and all(w[k]>=c[0] for k in range(n-1)))
                    assert (L<=1)==classification,(n,r,w,L)
    print('PASS: window/radius profiles',profile_count)
    print('PASS: exhaustive generic selectors',selector_checks)
    print('PASS: exact local sharpness witnesses',exact_witnesses)
    print('PASS: positive weight profiles',weight_cases)
    print('PASS: direct exact-rational two-input comparisons',ratio_tests)
    print('All finite tests are corroborative, not a universal proof.')

if __name__=='__main__':main()
