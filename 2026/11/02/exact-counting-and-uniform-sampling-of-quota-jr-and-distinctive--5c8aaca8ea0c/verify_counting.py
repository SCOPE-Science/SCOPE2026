#!/usr/bin/env python3
"""Exact count and random sampling of quota-JR committees for interval approvals.

The input is a candidate order of positions 1..m; ballots are inclusive
integer intervals (left,right), or empty ballots represented by (1,0).
"""
from __future__ import annotations
import itertools
import math
import random


def is_qjr(m, ballots, q, committee):
    """Directly check every candidate's uncovered-support count."""
    chosen = set(committee)
    for candidate in range(1,m+1):
        uncovered = 0
        for lo,hi in ballots:
            if lo <= candidate <= hi and not any(lo <= w <= hi for w in chosen):
                uncovered += 1
        if uncovered >= q:
            return False
    return True


def gap_table(m,ballots,q):
    assert m >= 1 and q >= 1
    for lo,hi in ballots:
        assert 1 <= lo <= m+1 and 0 <= hi <= m and (lo <= hi or (lo,hi)==(1,0))
    good = [[False]*(m+2) for _ in range(m+2)]
    for a in range(0,m+1):
        for b in range(a+1,m+2):
            diff = [0]*(m+3)
            for lo,hi in ballots:
                if a < lo <= hi < b:
                    diff[lo] += 1
                    diff[hi+1] -= 1
            now = 0
            good[a][b] = True
            for c in range(a+1,b):
                now += diff[c]
                if now >= q:
                    good[a][b] = False
                    break
    return good


def exact_counts(m,ballots,q,eligible,k):
    """Counts valid committees using a gap-DAG, returns count and suffix DP."""
    assert 1 <= k <= m and 1 <= q
    E = sorted(set(eligible))
    assert all(1 <= e <= m for e in E)
    good = gap_table(m,ballots,q)
    suffix = [[0]*(m+2) for _ in range(k+1)]
    for a in [0]+E:
        suffix[0][a]=int(good[a][m+1])
    for t in range(1,k+1):
        for a in [0]+E:
            suffix[t][a]=sum(suffix[t-1][b] for b in E if b>a and good[a][b])
    return suffix[k][0],suffix,good,E


def sample_uniform(m,ballots,q,eligible,k,rng):
    count,suffix,good,E = exact_counts(m,ballots,q,eligible,k)
    if not count:
        raise ValueError('No valid committees')
    a=0; out=[]
    for remaining in range(k,0,-1):
        num=rng.randrange(suffix[remaining][a]); current=0
        for b in E:
            if b <= a or not good[a][b]:
                continue
            w=suffix[remaining-1][b]
            if num < current + w:
                out.append(b);a=b;break
            current+=w
        else:
            raise AssertionError('DP sampler has no transition')
    assert good[a][m+1]
    return tuple(out)


def brute_count(m,ballots,q,eligible,k):
    E=sorted(set(eligible))
    return sum(is_qjr(m,ballots,q,W) for W in itertools.combinations(E,k))


def test_exhaustive():
    checked=0
    for m in range(1,6):
        intervals=[(l,r) for l in range(1,m+1) for r in range(l,m+1)]
        for n in range(1,4):
            for ballots in itertools.product(intervals,repeat=n):
                for k in range(1,m+1):
                    q=(n+k-1)//k
                    support=[sum(l<=c<=r for l,r in ballots) for c in range(1,m+1)]
                    E=[c for c in range(1,m+1) if support[c-1]==q]
                    dp,_,_,_=exact_counts(m,ballots,q,E,k)
                    br=brute_count(m,ballots,q,E,k)
                    if dp!=br: raise AssertionError((m,n,ballots,k,q,E,dp,br))
                    checked+=1
    return checked


def test_random(seed=0, trials=12000):
    rng=random.Random(seed)
    for trial in range(trials):
        m=rng.randint(1,9)
        n=rng.randint(1,12)
        intervals=[(l,r) for l in range(1,m+1) for r in range(l,m+1)]
        ballots=[rng.choice(intervals+[(1,0)]) for _ in range(n)]
        k=rng.randint(1,m)
        q=rng.randint(1,n+1)
        E=[c for c in range(1,m+1) if rng.randrange(2)]
        dp,_,_,_=exact_counts(m,ballots,q,E,k)
        br=brute_count(m,ballots,q,E,k)
        if dp!=br:raise AssertionError((m,n,ballots,k,q,E,dp,br))
        if dp:
            draw=sample_uniform(m,ballots,q,E,k,rng)
            assert draw in itertools.combinations(sorted(E),k) and is_qjr(m,ballots,q,draw)
    return trials


def get_example():
    rng=random.Random(42)
    for _ in range(100000):
        m=6;n=8;k=3;q=(n+k-1)//k
        ballots=[(rng.randint(1,m),rng.randint(1,m)) for i in range(n)]
        ballots=[(min(a,b),max(a,b)) for a,b in ballots]
        support=[sum(l<=c<=r for l,r in ballots) for c in range(1,m+1)]
        E=[c for c in range(1,m+1) if support[c-1]==q]
        if len(E)<k+1:continue
        dp,_,_,_=exact_counts(m,ballots,q,E,k)
        choices=math.comb(len(E),k)
        if 1<dp<choices:
            return {'m':m,'n':n,'k':k,'q':q,'ballots':ballots,'support':support,'eligible':E,'accepted':dp,'total_candidate_subsets':choices,
                    'committees':[W for W in itertools.combinations(E,k) if is_qjr(m,ballots,q,W)]}
    return None

if __name__=='__main__':
    print('exhaustive_DR_profiles',test_exhaustive())
    print('random_general_profiles',test_random())
    print('example',get_example())
