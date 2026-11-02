#!/usr/bin/env python3
"""Finite exact checks for regular-graph edge-coupon coverage.

Run with Python 3 standard library. These checks verify finite identities,
not asymptotic statements or historical originality.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import exp, factorial, log

CHECKS = 0


def assert_equal(a, b, context):
    global CHECKS
    CHECKS += 1
    assert a == b, (context, a, b)


def assert_close(a, b, tol, context):
    global CHECKS
    CHECKS += 1
    assert abs(a-b) <= tol, (context, a, b, tol)


def cycle(n, offset=0):
    return [(offset+i, offset+(i+1)%n) for i in range(n)]


def complete(n):
    return list(combinations(range(n), 2))


def distributions(n, edges, numerator):
    """Exact probability law for q=numerator/3 that an edge is untouched.

    Numerator=1 denotes q=1/2 instead, to exercise a second grid.
    """
    qden = 2 if numerator == 1 else 3
    qnum = 1 if numerator == 1 else 2
    m = len(edges)
    incident = [0]*n
    degrees = [0]*n
    for j, (u, v) in enumerate(edges):
        assert 0 <= u < n and 0 <= v < n and u != v
        incident[u] |= 1 << j
        incident[v] |= 1 << j
        degrees[u] += 1
        degrees[v] += 1
    d = degrees[0]
    assert d >= 1 and all(x == d for x in degrees)
    assert len({tuple(sorted(e)) for e in edges}) == m
    assert n*d == 2*m
    counts = [0]*(n+1)
    for status in range(1 << m):
        untouched = status.bit_count()
        weight = qnum**untouched * (qden-qnum)**(m-untouched)
        unseen = sum((status & inc) == inc for inc in incident)
        counts[unseen] += weight
    law = tuple(Fraction(count, qden**m) for count in counts)
    assert_equal(sum(law), Fraction(1), (n, d, 'mass'))
    q = Fraction(qnum, qden)
    p = q**d
    mean = sum(k*law[k] for k in range(n+1))
    second = sum(k*k*law[k] for k in range(n+1))
    variance = second-mean*mean
    assert_equal(mean, n*p, (n,d,q,'mean'))
    assert_equal(variance, n*p*(1-p)+n*d*p*p*(1/q-1), (n,d,q,'variance'))
    factorial_second = sum(k*(k-1)*law[k] for k in range(n+1))
    assert_equal(factorial_second,n*(n-1)*p*p+n*d*p*p*(1/q-1),(n,d,q,'factorial-second'))
    if d == 1:
        assert n % 2 == 0
        for k in range(n+1):
            wanted = (Fraction(comb(n//2,k//2))*q**(k//2)*(1-q)**(n//2-k//2)
                      if k % 2 == 0 else Fraction(0))
            assert_equal(law[k], wanted,(n,d,q,k,'matching-law'))
    lam = float(n*p)
    pois = [exp(-lam)*lam**k/factorial(k) for k in range(n+1)]
    tv = (sum(abs(float(law[k])-pois[k]) for k in range(n+1))
          +max(0,1-sum(pois)))/2
    bound=(1-exp(-lam))*float(p)*(1+d*(1/float(q)-1))
    assert_close(min(tv,bound),tv,1e-11,(n,d,q,'size-bias-TV'))
    return law


def comb(n,k):
    if 0 <= k <= n:
        return factorial(n)//(factorial(k)*factorial(n-k))
    return 0


def independent_discrete_check(n,edges,steps):
    """Compare inclusion-exclusion and covered-subset dynamic programming."""
    m=len(edges)
    masks=[(1<<u)|(1<<v) for u,v in edges]
    full=(1<<n)-1
    dp={0:Fraction(1)}
    for t in range(steps+1):
        inc_exc=Fraction(0)
        for unseen in range(1<<n):
            incident=sum(bool(edge_mask&unseen) for edge_mask in masks)
            term=Fraction(m-incident,m)**t
            inc_exc += (-1 if unseen.bit_count()%2 else 1)*term
        assert_equal(dp.get(full,Fraction(0)),inc_exc,(n,len(edges),t,'discrete-CDF'))
        next_dp=defaultdict(Fraction)
        for cover,p in dp.items():
            for mask in masks:
                next_dp[cover|mask] += p/m
        dp=next_dp


def main():
    examples=[
        ('triangle',3,cycle(3)),
        ('square',4,cycle(4)),
        ('complete4',4,complete(4)),
        ('pentagon',5,cycle(5)),
        ('complete5',5,complete(5)),
        ('hexagon',6,cycle(6)),
        ('two-triangles',6,cycle(3,0)+cycle(3,3)),
        ('K33',6,[(u,v) for u in range(3) for v in range(3,6)]),
        ('prism',6,cycle(3)+cycle(3,3)+[(i,i+3) for i in range(3)]),
        ('complete6',6,complete(6)),
        ('three-disjoint-edges',6,[(0,1),(2,3),(4,5)]),
        ('octagon',8,cycle(8)),
        ('two-squares',8,cycle(4)+cycle(4,4)),
        ('two-K4',8,complete(4)+[(u+4,v+4) for u,v in complete(4)]),
    ]
    laws={}
    for name,n,edges in examples:
        for numerator in (1,2):
            laws[(name,numerator)]=distributions(n,edges,numerator)
        if n <= 6 and len(edges)<=9:
            independent_discrete_check(n,edges,9)
    assert_equal(laws['hexagon',1][:],laws['two-triangles',1][:],
                 'same degree n but different full distribution') if False else None
    assert_equal(laws['hexagon',1] != laws['two-triangles',1],True,
                 'topology-dependent finite law')
    for L in (0.1,0.5,1,3,8,15):
        values=[d*(exp(L/d)-1) for d in range(2,51)]
        for i in range(len(values)-1):
            assert_equal(values[i]>values[i+1],True,('degree-monotonic',L,i+2))
    for n in (100,1000,10000,100000):
        for x in (-2.,0.,2.):
            if log(n)+x<=0:
                continue
            p=exp(-x)/n
            for d in (2,3,5,min(n-1,10),n-1):
                if d>=n:
                    continue
                exact=p*(1+d*(exp((log(n)+x)/d)-1))
                upper=p*(2*exp((log(n)+x)/2)-1)
                assert_equal(exact<=upper+1e-12,True,('uniform-bound',n,d,x))
    print('PASS', CHECKS, 'independent exact-rational assertions and checks')
    print('finite law differs for C6 versus 2C3 while their first two moments agree')
    print('Poisson coupling bound checked at q=1/2 and q=2/3')

if __name__=='__main__':
    main()
