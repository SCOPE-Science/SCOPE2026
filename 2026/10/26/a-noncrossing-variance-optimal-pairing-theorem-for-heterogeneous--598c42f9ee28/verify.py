"""Exact-rational checks for pairwise Dorfman workload-variance matching.

Run with Python 3.9+ and no third-party packages.
"""
import itertools
import json
from fractions import Fraction
from functools import lru_cache


def pairings(v):
    if not v:
        yield ()
        return
    a, *tail = v
    for k, b in enumerate(tail):
        for rem in pairings(tail[:k] + tail[k+1:]):
            yield ((a,b),) + rem


def f(q):
    return q*(1-q)


def weight(x, matching):
    return sum((f(x[i]*x[j]) for i,j in matching), Fraction(0))


def noncross(matching):
    for (a,b),(c,d) in itertools.combinations(matching, 2):
        a,b=sorted((a,b));c,d=sorted((c,d))
        if a<c<b<d or c<a<d<b:
            return False
    return True


def dynamic(x):
    n=len(x)
    @lru_cache(None)
    def dp(i,j):
        if i>j:
            return Fraction(0), ()
        assert (j-i+1)%2==0
        cand=[]
        for k in range(i+1,j+1,2):
            left, ml=dp(i+1,k-1)
            right,mr=dp(k+1,j)
            cand.append((left+right+f(x[i]*x[k]), ((i,k),)+ml+mr))
        return min(cand,key=lambda a:a[0])
    return dp(0,n-1)


def moments_by_status(x,matching):
    n=len(x)
    expected=Fraction(0);second=Fraction(0)
    for status in itertools.product((0,1),repeat=n):
        pr=Fraction(1)
        for i,positive in enumerate(status):
            pr*=1-x[i] if positive else x[i]
        t=n//2+2*sum(status[i] or status[j] for i,j in matching)
        expected+=pr*t
        second+=pr*t*t
    return expected,second-expected*expected


def main():
    count=0; four=0;patterns=0;workload=0;sampled=0
    grid=[Fraction(i,10) for i in range(1,10)]
    for a,b,c,d in itertools.combinations(grid,4):
        # Coordinates are increasing: d>=c>=b>=a.
        pd=f(c*d)+f(a*b)
        pc=f(b*d)+f(a*c)
        pn=f(a*d)+f(b*c)
        assert min(pd,pn)<=pc
        assert (pd-pc)==(d-a)*(c-b)*(1-(d+a)*(c+b))
        assert (pc-pn)==(d-c)*(b-a)*(1-(d+c)*(b+a))
        four+=1
    for n in (4,6,8):
        all_pairs=list(pairings(list(range(n))))
        for x in itertools.combinations(grid,n):
            all_cost=[weight(x,m) for m in all_pairs]
            optimum=min(all_cost)
            rec,rec_pairs=dynamic(x)
            assert rec==optimum and noncross(rec_pairs)
            count+=1
            if n==6:
                for m,v in zip(all_pairs,all_cost):
                    ex,var=moments_by_status(x,m)
                    assert var==4*v
                    assert ex==n//2+2*sum(1-x[i]*x[j] for i,j in m)
                    workload+=1
        patterns+=len(all_pairs)
    # The smallest six-distinct-risk example with an intermediate optimum.
    x=tuple(Fraction(i,7) for i in range(1,7))
    allm=list(pairings(list(range(6))))
    c=[weight(x,m) for m in allm]
    opt=min(c)
    wins=[m for m,v in zip(allm,c) if v==opt]
    assert wins==[((0,3),(1,2),(4,5))]
    assert opt==Fraction(144,343)
    assert weight(x,((0,1),(2,3),(4,5)))==Fraction(1108,2401)
    assert weight(x,((0,5),(1,4),(2,3)))==Fraction(156,343)
    # Ten-individual deterministic synthetic profiles, checked against all 945 matchings.
    all10=list(pairings(list(range(10))))
    for shift in range(15):
        nums=sorted(((11*i+7*shift+3*i*i)%100+1) for i in range(10))
        vals=tuple(Fraction(j,101) for j in nums)
        dpm, pm=dynamic(vals)
        assert dpm==min(weight(vals,m) for m in all10)
        assert noncross(pm)
        sampled+=1
    print(json.dumps({
        'four_point_exact_checks':four,
        'complete_risk_profiles_sizes_4_6_8':count,
        'total_distinct_matching_topologies_examined':patterns,
        'complete_six_individual_moment_enumerations':workload,
        'ten_individual_full_matching_profiles':sampled,
        'six_individual_unique_optimum_pairs_0_based':[[0,3],[1,2],[4,5]],
        'six_individual_optimum_sum_f':'144/343',
        'six_individual_adjacent_sum_f':'1108/2401',
        'six_individual_opposite_sum_f':'156/343',
        'result':'all_checks_passed'
    },sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
