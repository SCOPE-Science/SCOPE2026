#!/usr/bin/env python3
"""Finite exact cross-checks for the coupon-collection singleton theorem.
No finite test is used as a proof of the all-parameter inequalities.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def associated_stirling(max_n):
    a = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    a[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            a[n][k] = k * a[n-1][k] + ((n-1)*a[n-2][k-1] if n >= 2 else 0)
    return a


def dynamic_joint(q, limit):
    # Number of length-r words by occupied box count and singleton count.
    states = {(0,0): 1}
    result = {}
    for t in range(1, limit+1):
        result[t] = {s+1: v for (used,s),v in states.items() if used == q-1}
        nxt = defaultdict(int)
        for (used,s),v in states.items():
            if used < q:
                nxt[(used+1,s+1)] += v*(q-used)
            if s:
                nxt[(used,s-1)] += v*s
            if used > s:
                nxt[(used,s)] += v*(used-s)
        states = dict(nxt)
    return result


def formula(q,t,s,assoc):
    if not (1 <= s <= q and t>=q):
        return 0
    return factorial(q)*comb(t-1,s-1)*assoc[t-s][q-s]


def main():
    assertions=0
    assoc=associated_stirling(400)
    for q in range(2,10):
        lim=55
        joint=dynamic_joint(q,lim)
        for t in range(q,lim+1):
            for s in range(1,q+1):
                assert joint[t].get(s,0)==formula(q,t,s,assoc)
                assertions+=1
        # Reverse total positivity of order 2 for all row/column pairs.
        for t in range(q,lim+1):
            for u in range(t+1,lim+1):
                for s in range(1,q+1):
                    for r in range(s+1,q+1):
                        assert joint[t].get(s,0)*joint[u].get(r,0) <= joint[t].get(r,0)*joint[u].get(s,0)
                        assertions+=1
    # Direct full word enumeration, independent of both associated Stirling formula and dynamic states.
    for q in range(2,5):
        joint=dynamic_joint(q,8)
        for t in range(q,9):
            raw=defaultdict(int)
            for word in product(range(q),repeat=t):
                if len(set(word[:-1]))!=q-1 or len(set(word))!=q:
                    continue
                s=sum(word.count(i)==1 for i in range(q))
                raw[s]+=1
            assert dict(raw)==joint[t]
            assertions+=1
    # Convergent independent sum of moments, compared with analytic harmonic result.
    for q in range(2,8):
        joint=dynamic_joint(q,280)
        ET=Fraction(0);ES=Fraction(0);ETS=Fraction(0)
        for t,counts in joint.items():
            for s,n in counts.items():
                p=Fraction(n,q**t)
                ET+=t*p;ES+=s*p;ETS+=t*s*p
        H=sum((Fraction(1,j) for j in range(1,q+1)),Fraction(0))
        H2=sum((Fraction(1,j*j) for j in range(1,q+1)),Fraction(0))
        # Truncation errors are exponentially small; use a strict tolerance.
        assert abs(float(ETS-ET*ES-q*(H2-H))) < 1e-13
        assert abs(float(ES-H))<1e-13
        assert abs(float(ET-q*H))<1e-13
        assertions+=3
    print('PASS exact assertions:',assertions)
    print('Coverage: q=2..9, t<=55; exhaustive q<=4, t<=8; moment check q<=7, t<=280.')
    print('The infinite theorem is proved analytically, not by these finite checks.')

if __name__=='__main__':
    main()
