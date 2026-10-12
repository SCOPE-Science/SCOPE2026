#!/usr/bin/env python3
"""Exact finite checks for skew idempotent pairs in full transformation monoids."""
import itertools
import math
from collections import Counter


def predicted(n):
    d = Counter()
    for r in range(1, n + 1):
        for s in range(1, n + 1):
            for t in range(max(0, r + s - n), min(r, s) + 1):
                placements = (math.comb(n, s) * math.comb(s, t)
                              * math.comb(n - s, r - t) * (r*s)**(n-r-s+t))
                inner = 0
                for k in range(max(1, t), min(r, s) + 1):
                    inner += (math.comb(s-t, k-t)
                              * (math.factorial(r-t)//math.factorial(r-k))
                              * k**(r-k) * (r**(s-k)-k**(s-k)))
                d[r, s] += placements * inner
    return d


def idempotents(n):
    for r in range(1, n + 1):
        for image in itertools.combinations(range(n), r):
            other = [a for a in range(n) if a not in image]
            for values in itertools.product(image, repeat=n-r):
                f = list(range(n))
                for a, b in zip(other, values):
                    f[a] = b
                yield tuple(f), r


def compose(a, b):
    return tuple(a[j] for j in b)


def observed(n):
    transformations = list(idempotents(n))
    counts = Counter()
    for e, r in transformations:
        for f, s in transformations:
            ef, fe = compose(e, f), compose(f, e)
            if compose(fe, fe) == fe and compose(ef, ef) != ef:
                counts[r, s] += 1
    return counts, len(transformations)


def main():
    totals = {1:0, 2:0, 3:6, 4:204, 5:5900, 6:190410}
    idem_totals = {1:1, 2:3, 3:10, 4:41, 5:196, 6:1057}
    for n in range(1, 7):
        actual, idem_count = observed(n)
        want = predicted(n)
        assert actual == want, (n, actual, want)
        assert idem_count == idem_totals[n]
        assert sum(actual.values()) == totals[n]
        if n >= 3:
            assert actual[2, 2] == (n*(n-1)*(n-2)*(n+1)//4) * 4**(n-3)
        print('n=%d idempotents=%d skew=%d OK' % (n, idem_count, sum(actual.values())))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
