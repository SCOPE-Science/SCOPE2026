#!/usr/bin/env python3
"""Independent finite tests for modular Fibonacci-like first-zero statistics.

Standard library only. This finite replay corroborates, rather than proves,
the general modular theorem.
"""
from collections import Counter
from math import gcd


def phi(n):
    return sum(gcd(j,n)==1 for j in range(n))


def rank(n):
    if n == 1:
        return 1
    a,b = 0,1
    for j in range(1,6*n*n+1):
        a,b = b,(a+b)%n
        if a % n == 0:
            return j
    raise AssertionError(('rank bound',n))


def first_zero(a,b,n):
    seen = set()
    j = 0
    while (a,b) not in seen:
        if a == 0:
            return j
        seen.add((a,b))
        a,b = b,(a+b)%n
        j += 1
    return None


def run(limit=90):
    pairs = 0
    histogram_cells = 0
    ranks = {d:rank(d) for d in range(1,limit+1)}
    for m in range(1,limit+1):
        actual = Counter()
        strata = {}
        for a in range(m):
            for b in range(m):
                j = first_zero(a,b,m)
                actual[j] += 1
                d = m // gcd(a,b,m)
                if j is not None:
                    strata[d,j] = strata.get((d,j),0) + 1
                pairs += 1
        divs = [d for d in range(1,m+1) if m % d == 0]
        zmax=max(ranks[d] for d in divs)
        expected = Counter({j:sum(phi(d) for d in divs if ranks[d] > j) for j in range(zmax)})
        expected[None]=m*m-sum(phi(d)*ranks[d] for d in divs)
        assert actual == expected, ('hist',m,actual,expected)
        for d in divs:
            for j in range(ranks[d]):
                assert strata.get((d,j),0)==phi(d),('stratum',m,d,j,strata.get((d,j),0))
                histogram_cells += 1
        # Verify ordinary first-hit expectation and total against independent count.
        assert sum(j*actual[j] for j in actual if j is not None) == sum(phi(d)*ranks[d]*(ranks[d]-1)//2 for d in divs)
        assert sum(c for j,c in actual.items() if j is not None)==sum(phi(d)*ranks[d] for d in divs)
    # OEIS A232656's published first sixteen entries.
    published=[1,4,9,16,21,36,49,40,81,84,101,96,85,196,189,136]
    from_formula=[sum(phi(d)*ranks[d] for d in range(1,m+1) if m%d==0) for m in range(1,len(published)+1)]
    assert from_formula == published, ('OEIS',from_formula,published)
    print('VERIFY_OK: %d moduli (1..%d); %d independently iterated initial pairs; %d exact gcd-stratum/time cells; 16 published OEIS total counts' % (limit,limit,pairs,histogram_cells))


if __name__=='__main__':
    run()
