#!/usr/bin/env python3
"""Independent exhaustive and queue-path checks of a bivariate rank formula."""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb, factorial


def exact_formula(n, d, r):
    if d == r == 0:
        return 1
    if d < 1 or r < 1 or r > d or n - d - r < 0:
        return 0
    return (factorial(n) * comb(d-1, r-1) //
            (factorial(d+1) * factorial(r) * factorial(n-d-r)))


def exhaustive(n):
    tab = Counter()
    for d in range(n + 1):
        for domain in combinations(range(1, n + 1), d):
            D = set(domain)
            for images in combinations_with_replacement(range(1, n+1), d):
                if any(y < x for x, y in zip(domain, images)):
                    continue
                if any(y in D for y in images):
                    continue
                tab[d, len(set(images))] += 1
    return tab


def queue_paths(n):
    # State (outstanding source count, domain count, distinct target count).
    states = Counter({(0, 0, 0): 1})
    for _ in range(n):
        nxt = Counter()
        for (q,d,r), ways in states.items():
            nxt[(q,d,r)] += ways       # unused position
            nxt[(q+1,d+1,r)] += ways   # new domain/source
            for k in range(1,q+1): # new image/target consumes k earliest sources
                nxt[(q-k,d,r+1)] += ways
        states = nxt
    return Counter({(d,r):ways for (q,d,r),ways in states.items() if q == 0})


def catalan(n):
    return comb(2*n,n)//(n+1)


def narayana(n,d):
    return comb(n,d)*comb(n,d+1)//n if 0 <= d < n else 0


if __name__ == '__main__':
    for n in range(1,11):
        actual = exhaustive(n)
        queue = queue_paths(n)
        for d in range(n+1):
            for r in range(n+1):
                want = exact_formula(n,d,r)
                assert actual[d,r] == want, (n,d,r,'exhaustive',actual[d,r],want)
                assert queue[d,r] == want, (n,d,r,'queue',queue[d,r],want)
            assert sum(actual[d,r] for r in range(n+1)) == (narayana(n,d) if d<n else 0), (n,d,'Narayana')
        assert sum(actual.values()) == catalan(n)
        print('n',n,'square_zero',sum(actual.values()),'domain/image nonzero profiles',sum(v>0 for v in actual.values()))
    # Analytic closed formula and Narayana marginal for larger sizes.
    for n in range(11,101):
        assert sum(exact_formula(n,d,r) for d in range(n+1) for r in range(n+1)) == catalan(n)
        for d in range(n):
            assert sum(exact_formula(n,d,r) for r in range(n+1)) == narayana(n,d)
    print('VERIFY_OK_SQUARE_ZERO_POE_BIVARIATE_TREE')
