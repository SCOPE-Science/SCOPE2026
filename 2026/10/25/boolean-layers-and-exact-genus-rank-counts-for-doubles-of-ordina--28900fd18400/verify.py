"""Independent finite verification of fixed ordinary quotient genus-rank formulas.
No external packages; Python 3.9+.
"""
from collections import Counter
from itertools import combinations
from math import comb


def in_semigroup(n, m, b, B):
    if n == 0:
        return True
    if n % 2 == 0:
        return n >= 2*m
    return n == b or n in B or n >= b + 2*m


def brute_closure(generators, bound):
    reached = [False] * (bound+1)
    reached[0] = True
    for n in range(1, bound+1):
        reached[n] = any(g <= n and reached[n-g] for g in generators)
    return reached


def parameter_checks():
    checked=0
    observed=Counter()
    for m in range(2, 9):
        b0=m+(m%2==0)
        for b in range(b0, b0+22, 2):
            for mask in range(1<<(m-1)):
                B={b+2*j for j in range(1,m) if mask & (1<<(j-1))}
                generators=list(range(2*m,4*m,2))+[b]+sorted(B)
                bound=max(300,b+4*m+10)
                closure=brute_closure(generators,bound)
                for n in range(bound+1):
                    assert closure[n] == in_semigroup(n,m,b,B),(m,b,mask,n)
                gaps=[n for n in range(bound+1) if not closure[n]]
                genus=len(gaps)
                relmin=[u for u in range(1,b+2*m,2) if closure[u] and not any(closure[u-e] for e in range(2*m,min(u,4*m)+1,2))]
                assert relmin==[b]+sorted(B),(m,b,mask,relmin)
                assert genus == 2*m-2 + (b-1)//2 - len(B),(m,b,mask,genus)
                rank=len(relmin)
                observed[m,genus,rank]+=1
                checked+=1
    print('PARAMETER_CASES_OK',checked)
    return observed


def brute_census():
    total=0
    for m in (2,3,4,5):
        cutoff=2*m+17
        if cutoff%2==0: cutoff+=1
        odds=list(range(1,cutoff,2))
        # All odd numbers >= cutoff are included, independently of low odd choices.
        for mask in range(1<<len(odds)):
            chosen={x for j,x in enumerate(odds) if mask>>j&1}
            if not chosen: b=cutoff
            else: b=min(chosen)
            if b+2*m>cutoff: continue # no assertion about unexamined tail windows
            def member(n):
                return n==0 or (n%2==0 and n>=2*m) or (n%2==1 and (n>=cutoff or n in chosen))
            if not all(not (member(x) and member(y)) or member(x+y)
                       for x in range(1,cutoff+2*m)
                       for y in range(1,cutoff+2*m) if x+y < 2*cutoff+4*m):
                continue
            B={x for x in chosen if b<x<b+2*m}
            assert chosen==({b}|B|{x for x in odds if x>=b+2*m}),(m,cutoff,b,chosen,B)
            assert b%2 and b>=m
            total+=1
        print('BRUTE_FIBER_SLICE_OK',m,cutoff)
    print('BRUTE_CASES_OK',total)


def exact_rank_census():
    for m in range(2, 9):
        b0=m+(m%2==0)
        g0=m-1+(b0-1)//2
        # Aggregate by explicit independent enumeration of window choices and b values.
        for g in range(g0,g0+15):
            for r in range(1,m+1):
                count=0
                for h in range(0,g-g0+1):
                    b=b0+2*h
                    for mask in range(1<<(m-1)):
                        size=mask.bit_count()
                        if r == size+1 and g == 2*m-2+(b-1)//2-size:
                            count+=1
                expect=comb(m-1,r-1) if g>=g0+m-r else 0
                assert count==expect,(m,g,r,count,expect)
    print('JOINT_CENSUS_OK')


if __name__=='__main__':
    parameter_checks()
    brute_census()
    exact_rank_census()
    print('VERIFY_OK')
