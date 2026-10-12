#!/usr/bin/env python3
"""Exact rational checks for a two-habitat founder viability optimization theorem.
No third-party modules required; this is supplemental finite verification."""
from fractions import Fraction as Q


def success(n, p, r, m, f):
    """n founders of each sex; m males and f females placed at site 1."""
    t = 1-p
    a = (1-t**m)*(1-t**f)
    b = (1-t**(n-m))*(1-t**(n-f))
    return 1-(1-r*a)*(1-r*b)


def check():
    total = 0
    for n in range(1, 13):
        for p in (Q(1, 7), Q(2, 5), Q(3, 4), Q(9, 10)):
            for r in (Q(1, 5), Q(3, 5), Q(9, 10), Q(1)):
                outcomes = [(success(n, p, r, m, f), m, f)
                            for m in range(n+1) for f in range(n+1)]
                best = max(z[0] for z in outcomes)
                k = n//2
                candidates = [success(n, p, r, 0, 0),success(n, p, r, k, k)]
                assert best == max(candidates), ('bang-bang',n,p,r)
                # Strictness: every maximizer is either a paired concentration
                # or a paired, nearest-equal split (plus exchange of sites).
                allowed = {(0,0),(n,n),(k,k),(n-k,n-k)}
                for prob,m,f in outcomes:
                    if prob == best:
                        assert (m,f) in allowed,(n,p,r,m,f)
                t = 1-p
                a = (1-t**k)**2
                b = (1-t**(n-k))**2
                c = (1-t**n)**2
                delta = success(n,p,r,k,k)-success(n,p,r,0,0)
                assert delta == r*(a+b-c-r*a*b)
                if n % 2 == 0 and n >= 2:
                    z = t**k
                    assert delta == r*(1-z)**2*(2-(1+z)**2-r*(1-z)**2)
                total += len(outcomes)
    # Explicit four-founder transition at r=1/2, p=2/5 vs 9/10
    assert success(2,Q(2,5),Q(1,2),0,0) > success(2,Q(2,5),Q(1,2),1,1)
    assert success(2,Q(9,10),Q(1,2),1,1) > success(2,Q(9,10),Q(1,2),0,0)
    print('VERIFY_OK exact_profiles=',total,'population_sizes=1..12','parameter_pairs=16','special_transition=1')

if __name__ == '__main__':
    check()
