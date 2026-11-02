#!/usr/bin/env python3
"""Exact finite-state checks for the reset-to-root biclique cover-time decomposition.

All checks are self-contained and use integer/rational arithmetic.  These
finite tests are not a proof of the asymptotic limit in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, exp, log


def direct_probabilities(a, b, r, horizon):
    """Distribution over current vertex and visited masks, by exact transitions."""
    g = 1-r
    law = {(0, 1, 0): Fraction(1)}
    output = []
    for t in range(horizon+1):
        both = sum((p for (v,ma,mb),p in law.items() if ma==(1<<a)-1 and mb==(1<<b)-1),Fraction(0))
        done_a = sum((p for (v,ma,mb),p in law.items() if ma==(1<<a)-1),Fraction(0))
        done_b = sum((p for (v,ma,mb),p in law.items() if mb==(1<<b)-1),Fraction(0))
        output.append((done_a,done_b,both))
        nxt=defaultdict(Fraction)
        for (v,ma,mb),p in law.items():
            nxt[(0,ma,mb)] += p*r
            if v<a:
                for w in range(b):
                    nxt[(a+w,ma,mb|(1<<w))] += p*g/b
            else:
                for w in range(a):
                    nxt[(w,ma|(1<<w),mb)] += p*g/a
        assert sum(nxt.values())==1
        law=nxt
    return output


def coupon_finished(m, size, unobserved_types):
    """Coupon occupancy inclusion-exclusion; only unobserved_types are required."""
    return sum(((-1)**j * comb(unobserved_types,j) *
                (Fraction(size-j,size)**m) for j in range(unobserved_types+1)), Fraction(0))


def count_probabilities(a,b,r,horizon):
    """Exact two-state Markov-modulated coupon-count decomposition."""
    g=1-r
    law={('A',0,0):Fraction(1)}
    result=[]
    for t in range(horizon+1):
        fa=fb=both=Fraction(0)
        for (side,ma,mb),p in law.items():
            ca=coupon_finished(ma,a,a-1)
            cb=coupon_finished(mb,b,b)
            fa+=p*ca; fb+=p*cb; both+=p*ca*cb
        result.append((fa,fb,both))
        nxt=defaultdict(Fraction)
        for (side,ma,mb),p in law.items():
            if side=='A':
                nxt[('A',ma,mb)] +=p*r
                nxt[('B',ma,mb+1)] +=p*g
            else:
                nxt[('A',ma,mb)] +=p*r
                nxt[('A',ma+1,mb)] +=p*g
        assert sum(nxt.values())==1
        law=nxt
    return result


def stationary_rates_check(r):
    g=1-r
    pi_a=1/(1+g); pi_b=g/(1+g)
    assert pi_a*(1-g)+pi_b == pi_a
    assert pi_a*g == pi_b
    return pi_a*g,pi_b*g


def main():
    assertions=0
    for r in (Fraction(1,4),Fraction(1,2),Fraction(2,3)):
        eta_b,eta_a=stationary_rates_check(r)
        assert eta_a == (1-r)**2/(2-r)
        assert eta_b == (1-r)/(2-r)
        assertions += 4
        for a in (1,2,3,4):
            for b in (1,2,3,4):
                d=direct_probabilities(a,b,r,8)
                c=count_probabilities(a,b,r,8)
                for step,(x,y) in enumerate(zip(d,c)):
                    assert x==y,(r,a,b,step,x,y)
                    assertions+=3
    # Deterministic conditional missing-type asymptotics, not an infinite proof.
    g=Fraction(3,4); n=200_000
    for x in (-1.,0.,1.):
        a=round(float(g)*n)
        t=(2-float(1-g))/float(g)*n*(log(n)+x)
        visits_b=float(g)/(1+float(g))*t
        visits_a=float(g)**2/(1+float(g))*t
        exp_missing_b=n*exp(visits_b*log(1-1/n))
        exp_missing_a=(a-1)*exp(visits_a*log(1-1/a))
        assert abs(exp_missing_b-exp(-x))<1e-3
        assert abs(exp_missing_a-float(g)*exp(-x))<1e-3
        assertions+=2
    print(f"PASS {assertions} exact/evaluated assertions; finite-state checks rational-exact")

if __name__=='__main__': main()
