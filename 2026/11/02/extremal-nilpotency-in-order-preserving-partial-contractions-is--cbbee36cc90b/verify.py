#!/usr/bin/env python3
"""Exhaustive and arithmetic verification of extremal-index partial contractions.

Python 3 standard library only; run ``python3 verify.py``.
"""
from itertools import combinations


def partitions_by_parts(nmax):
    """Euler coin-change DP: counts partitions by size and exact number of parts."""
    p = [[0]*(nmax+1) for _ in range(nmax+1)]
    p[0][0] = 1
    for m in range(1, nmax+1):
        for total in range(m, nmax+1):
            for k in range(1, nmax+1):
                p[total][k] += p[total-m][k-1]
    return p


def formula(n, k, part):
    if k == 0:
        return 0  # the empty map is intentionally excluded
    return 2*sum((n-m)*part[m][k] for m in range(k, n))


def index_by_actual_composition(domain, image):
    """Index of a partial map, using direct iteration, independent of gap classification."""
    base = dict(zip(domain, image))
    power = base
    exponent = 1
    while power:
        power = {x:base[y] for x, y in power.items() if y in base}
        exponent += 1
        if exponent > len(domain)+2:
            return None  # not nilpotent
    return exponent


def exhaustive(n):
    stats = [0]*(n+1)
    for k in range(1, n+1):
        subsets = list(combinations(range(1,n+1),k))
        for domain in subsets:
            for image in subsets:
                if any(image[i+1]-image[i] > domain[i+1]-domain[i]
                       for i in range(k-1)):
                    continue
                if index_by_actual_composition(domain, image) == k+1:
                    stats[k] += 1
    return stats


def series_via_euler_product(maxn):
    """Coefficients of 2z(1-z)^(-2)(Euler partition product minus 1)."""
    p = [0]*(maxn+1)
    p[0] = 1
    for part_size in range(1,maxn+1):
        for total in range(part_size,maxn+1):
            p[total] += p[total-part_size]
    return [2*sum((n-m)*p[m] for m in range(1,n)) for n in range(maxn+1)]


def main():
    max_n = 12
    part = partitions_by_parts(max_n)
    predicted = series_via_euler_product(max_n)
    for n in range(max_n+1):
        raw = exhaustive(n)
        formal = [formula(n,k,part) for k in range(n+1)]
        assert raw == formal, (n, raw, formal)
        assert sum(raw) == predicted[n], (n,raw,predicted[n])
        if n>=2:
            assert raw[n-1] == 2
        if n>=1:
            assert raw[n] == 0
    print('VERIFY_OK: exhaustive every partial injection contraction n=0..12;')
    print('           independently computed nilpotency by iteration;')
    print('           coefficients agree with partition-product formula.')
    for n in (4,8,12):
        print('n=',n,'rank_profile=',exhaustive(n),'total=',predicted[n])


if __name__ == '__main__':
    main()
