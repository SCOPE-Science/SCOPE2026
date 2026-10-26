#!/usr/bin/env python3
"""Finite exact checks for the Bernoulli SJR/SSJR coverage theorem.

All profiles have equal probability at p=1/2. Definitions are direct
support-set formulations of Strong and Semi-Strong Justified Representation.
"""
from itertools import combinations
from collections import Counter
from math import comb, ceil
from fractions import Fraction


def analyze_profile(ballots, m, k):
    n=len(ballots)
    supporters=[sum(((b >> c)&1) << i for i,b in enumerate(ballots)) for c in range(m)]
    cohesive={c for c in range(m) if supporters[c].bit_count()*k>=n}
    r=len(cohesive)
    target=Fraction(min(k,r),r) if r else Fraction(1)
    strong_best=semi_best=Fraction(0)
    strong_feas=semi_feas=False
    universal_separation=True
    for elected in combinations(range(m),k):
        W=set(elected)
        covered=0
        for d in W:
            covered |= supporters[d]
        # Universal noncoverability event: every c not elected has a
        # witness approving c and none of the elected candidates.
        if any((supporters[c] & ~covered)==0 for c in range(m) if c not in W):
            universal_separation=False
        strong_hits=sum(any(supporters[c] & ~supporters[d] == 0 for d in W) for c in cohesive)
        semi_hits=sum(supporters[c] & ~covered == 0 for c in cohesive)
        strong_score=Fraction(strong_hits,r) if r else Fraction(1)
        semi_score=Fraction(semi_hits,r) if r else Fraction(1)
        strong_best=max(strong_best,strong_score)
        semi_best=max(semi_best,semi_score)
        strong_feas |= strong_hits==r
        semi_feas |= semi_hits==r
    assert strong_feas <= semi_feas
    assert (r<=k) <= strong_feas
    assert target <= strong_best <= semi_best
    if universal_separation:
        assert strong_best==semi_best==target
        assert strong_feas==semi_feas==(r<=k)
    return (r, universal_separation, strong_feas, semi_feas, strong_best, semi_best)


def exhaustive(n,m,k):
    total=1<<(n*m)
    stats=Counter()
    diffs=[]
    for bits in range(total):
        ballots=tuple((bits>>(i*m))&((1<<m)-1) for i in range(n))
        r,sep,sf,ss,bs,bt=analyze_profile(ballots,m,k)
        stats['E']+=sep
        stats['SJR']+=sf
        stats['SSJR']+=ss
        stats['R_le_k']+=r<=k
        stats['sep_opt_correct']+=sep and bs==bt==(Fraction(min(r,k),r) if r else 1)
        if sf != (r<=k) or ss!=(r<=k):diffs.append(bits)
    q=Fraction(sum(comb(n,j) for j in range((n+k-1)//k,n+1)),2**n)
    base=sum(Fraction(comb(m,j))*q**j*(1-q)**(m-j) for j in range(k+1))
    d=Fraction(m*comb(m-1,k))*(1-Fraction(1,2)*(1-Fraction(1,2))**k)**n
    obs_sjr=Fraction(stats['SJR'],total)
    obs_ssjr=Fraction(stats['SSJR'],total)
    assert 0<=obs_sjr-base<=d
    assert 0<=obs_ssjr-base<=d
    assert Fraction(total-stats['E'],total)<=d
    print(f'n={n} m={m} k={k} profiles={total} P(R<=k)={base} '
          f'P(SJR)={obs_sjr} P(SSJR)={obs_ssjr} '
          f'P(separation)={Fraction(stats["E"],total)} '
          f'bound={d} errors={len(diffs)}')


if __name__=='__main__':
    for n,m,k in [(2,3,2),(3,3,2),(3,4,2),(4,4,2),(3,5,2)]:
        exhaustive(n,m,k)
    print('ALL FINITE ENUMERATION ASSERTIONS PASSED')
