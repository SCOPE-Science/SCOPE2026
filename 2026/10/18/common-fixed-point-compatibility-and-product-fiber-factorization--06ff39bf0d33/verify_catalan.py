#!/usr/bin/env python3
"""Exact finite checks of commuting order-preserving regressive retractions."""
from collections import Counter
from itertools import combinations
from math import comb, prod


def compose(a, b):
    return tuple(a[t-1] for t in b)


def retractions(n):
    ans = []
    for mask in range(1 << (n-1)):
        fixed = {1} | {j for j in range(2, n+1) if mask & (1 << (j-2))}
        f = tuple(max(j for j in fixed if j <= i) for i in range(1, n+1))
        ans.append((fixed, f))
    return ans


def predicted(n):
    # c[n,k] = [z^(n-k)] (1-z)^(-k)(1-2z)^(-k)
    return {k: sum(comb(k+j-1, j) * comb(n-j-1, n-k-j)
                   * 2**(n-k-j) for j in range(n-k+1)) for k in range(1, n+1)}


def direct(n):
    ans = Counter()
    product_fibers = Counter()
    es = retractions(n)
    for F, e in es:
        for G, f in es:
            if compose(e, f) == compose(f, e):
                ans[len(set(compose(e, f)))] += 1
                product_fibers[tuple(sorted(F & G))] += 1
                # independent combinatorial characterization test
                common = sorted(F & G)
                bounds = common + [n+1]
                assert all(not ((F-G) & set(range(left+1, right)) and
                                (G-F) & set(range(left+1, right)))
                           for left, right in zip(bounds[:-1], bounds[1:]))
            else:
                common = sorted(F & G)
                bounds = common + [n+1]
                assert any((F-G) & set(range(left+1, right)) and
                           (G-F) & set(range(left+1, right))
                           for left, right in zip(bounds[:-1], bounds[1:]))
    for H, mult in product_fibers.items():
        gaps = [b-a-1 for a,b in zip(H, H[1:])] + [n-H[-1]]
        assert mult == prod(2**(length+1)-1 for length in gaps), (n,H,mult,gaps)
    assert len(product_fibers) == 2**(n-1)
    return dict(ans)


def all_catalan_maps(n):
    def rec(part):
        if len(part) == n:
            yield tuple(part)
            return
        hi = len(part) + 1
        lo = part[-1] if part else 1
        for value in range(lo, hi + 1):
            yield from rec(part+[value])
    return set(rec([]))


def run():
    for n in range(1, 11):
        counts = direct(n)
        assert counts == predicted(n), (n, counts, predicted(n))
        assert sum(counts.values()) == (1 if n==1 else 4*sum(predicted(n-1).values()) - (0 if n==2 else 2*sum(predicted(n-2).values())))
        if n <= 8:
            raw = all_catalan_maps(n)
            idem = {f for f in raw if compose(f, f) == f}
            assert idem == {f for _, f in retractions(n)}
            assert len(raw) == comb(2*n, n)//(n+1)
        print(n, len(retractions(n)), sum(counts.values()), ','.join(str(counts[k]) for k in range(1, n+1)))
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
