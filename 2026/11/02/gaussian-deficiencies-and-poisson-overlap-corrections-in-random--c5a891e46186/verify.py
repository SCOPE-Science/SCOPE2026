#!/usr/bin/env python3
"""Independent exact finite checks of random-product rank and collision counts.
All finite computations use integer arithmetic; this is not an infinite proof.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
from math import factorial, comb, lgamma, exp, sqrt


def enumerate_partial_injections(n):
    for r in range(n + 1):
        for dom in combinations(range(n), r):
            for image in permutations(range(n), r):
                f = [-1] * n
                for i, j in zip(dom, image): f[i] = j
                yield tuple(f)


def compose(f, g):
    return tuple(-1 if j < 0 or g[j] < 0 else g[j] for j in f)


def direct_hist(n, m):
    maps = list(enumerate_partial_injections(n))
    hist = defaultdict(int)
    for tup in product(maps, repeat=m):
        f = tup[0]
        s = n - sum(x >= 0 for x in f)
        c = 0
        for g in tup[1:]:
            d = n - sum(x >= 0 for x in g)
            fg = compose(f, g)
            ns = n - sum(x >= 0 for x in fg)
            c += s + d - ns
            f, s = fg, ns
        hist[(s, c)] += 1
    return dict(hist)


def exact_hist(n, m):
    fact = factorial(n)
    weight = {d: comb(n, d) * fact // factorial(d) for d in range(n + 1)}
    hist = {(d, 0): w for d, w in weight.items()}
    for j in range(2, m + 1):
        nxt = defaultdict(int)
        for (s, c), times in hist.items():
            for d in range(n + 1):
                for h in range(max(0, s + d - n), min(s, d) + 1):
                    ways = (fact // factorial(d)) * comb(s, h) * comb(n - s, d - h)
                    nxt[(s + d - h, c + h)] += times * ways
        hist = dict(nxt)
    return hist


def mean_deficiency(n):
    l=[lgamma(n+1)-lgamma(n-d+1)-2*lgamma(d+1) for d in range(n+1)]
    xmax=max(l)
    w=[exp(x-xmax) for x in l]
    total=sum(w)
    return sum(d*wd for d,wd in enumerate(w))/total


def test():
    cases = [(1,2),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)]
    for n,m in cases:
        direct = direct_hist(n,m)
        exact = exact_hist(n,m)
        assert direct == exact, (n,m,{k:(direct.get(k),exact.get(k)) for k in set(direct)|set(exact) if direct.get(k)!=exact.get(k)})
        R=sum(comb(n,r)**2 * factorial(r) for r in range(n+1))
        assert sum(exact.values())==R**m
        # The expected product defect obeys the exact multiplicative recurrence.
        numerator=sum(s*c for (s,b),c in exact.items())
        dsum=sum((n-r)*comb(n,r)**2*factorial(r) for r in range(n+1))
        mu_num=dsum
        # Cross-multiply the exact expectation identity, using integers only.
        assert numerator * n**(m-1) == (n*R)**m - (n*R-mu_num)**m
        print('EXACT_OK',n,m,'tuples',R**m,'states',len(exact),'mean_deficit',float(numerator/(R**m)))
    for n in [100,400,1000]:
        mu=mean_deficiency(n)
        print('LAGUERRE_MEAN',n,round(mu,8),'minus_sqrt',round(mu-sqrt(n),8))
    print('VERIFY_OK',len(cases),'exhaustive direct-composition cases')

if __name__=='__main__': test()
