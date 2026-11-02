#!/usr/bin/env python3
"""Exact subset-DP checks for Nash welfare in symmetric friendship cycles.

Uses direct agent utilities for arbitrary coalitions, independently of
connected-arc reductions, to check small instances against the arc DP.
All numerical comparisons of finite optima use Python exact integers.
"""
from functools import lru_cache
from math import log, sqrt


def direct_opt(n):
    whole=(1 << n)-1
    weight=[0]*(whole+1)
    for mask in range(1,whole+1):
        product=1
        for i in range(n):
            if not ((mask>>i)&1):
                continue
            u=0
            for j in range(n):
                if i==j or not ((mask>>j)&1):
                    continue
                u += n if (i-j)%n in (1,n-1) else -1
            if u < 0:
                product=0
                break
            product*=u
        weight[mask]=product

    @lru_cache(None)
    def dp(mask):
        if mask==0:
            return 1
        lo=mask & -mask
        sub=mask
        best=0
        while sub:
            if sub & lo and weight[sub]:
                score=weight[sub]*dp(mask^sub)
                if score>best:
                    best=score
            sub=(sub-1)&mask
        return best
    return dp(whole)


def arc_opt(n):
    block={s:(n+2-s)**2*(2*n+3-s)**(s-2) for s in range(2,n)}
    dp=[0]*(n+1)
    dp[0]=1
    for t in range(1,n+1):
        dp[t]=max((dp[t-s]*block[s] for s in range(2,min(t,n-1)+1)), default=0)
    return max((n+3)**n,dp[n]),dp[n]


def main():
    # Directly considers ALL set partitions with no connectivity assumptions.
    expected_proper={
        4:256,5:4000,6:90000,7:2129400,8:65610000,
        9:2088124416,10:81663349824,11:3269493248000,
        12:154922431942656,
    }
    for n in range(4,13):
        exact=direct_opt(n)
        by_arcs,proper=arc_opt(n)
        assert proper==expected_proper[n],(n,proper)
        assert exact==by_arcs,(n,exact,by_arcs)
        grand=(n+3)**n
        assert (proper>grand)==(n>=12),(n,proper,grand)
    # Every even balanced split past threshold has a rigorous monotonic proof;
    # these further finite cases serve only as regression checks.
    for n in range(12,201):
        a=n//2; b=n-a
        p=lambda s:(n+2-s)**2*(2*n+3-s)**(s-2)
        assert p(a)*p(b)>(n+3)**n,n
    # Compare the full arc optimum against its proven leading asymptotics.
    for n in (100,400,1600,6400):
        # Avoid huge integer optimization: construct q nearly equal blocks.
        s0=2*sqrt(n*log(2))
        q=max(2,round(n/s0))
        sizes=[n//q+(1 if i<n%q else 0) for i in range(q)]
        avg=sum(2*log(n+2-s)+(s-2)*log(2*n+3-s) for s in sizes)/n
        loss=log(2*n)-avg
        predicted=2*sqrt(log(2)/n)
        assert abs(loss-predicted)<10/n,(n,loss,predicted)
    print('VERIFY_OK exact_all_partition_n=4..12 balanced_breakup_n=12..200 asymptotic_n=100,400,1600,6400')

if __name__=='__main__':
    main()
