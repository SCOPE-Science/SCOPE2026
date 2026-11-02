#!/usr/bin/env python3
"""Exact finite checks for root-degree/leaf dependence in plane recursive trees.

Uses only Python's standard library.  These are diagnostics, not a substitute
for the arbitrary-size coefficient and recurrence proofs.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def wallis(n):
    return Fraction(4 ** (n - 1), comb(2*n - 2, n - 1))


def predicted(n, r):
    assert n >= 3 and 1 <= r <= n - 1
    m = n - 1
    return Fraction(2*m + r, 3) - Fraction(2*(r+1)*(m-r), 3*(2*m-r-1))


def update(dist, n):
    """Counts after growing a size-n tree by every distinct insertion gap."""
    out = defaultdict(int)
    for (r,l), c in dist.items():
        root = r+1
        leaf = l
        other = 2*n-1-root-leaf
        assert other >= 0
        out[(r+1,l+1)] += c*root
        out[(r,l)] += c*leaf
        if other: out[(r,l+1)] += c*other
    return dict(out)


def explicit(n):
    """Independently enumerate labeled ordered increasing trees up to n=8.

    Each parent and ordered child-list assignment is produced by inserting
    the largest label at every available gap. State is a tuple of child lists.
    """
    curr = {((2,), ()): 1}
    for size in range(2, n):
        nxt = {}
        for tr in curr:
            for v, children in enumerate(tr):
                for slot in range(len(children)+1):
                    new = list(tr)
                    new[v] = children[:slot] + (size+1,) + children[slot:]
                    new.append(())
                    key = tuple(new)
                    assert key not in nxt
                    nxt[key] = 1
        curr = nxt
    d = defaultdict(int)
    for tr in curr:
        root_degree = len(tr[0])
        leaves = sum(not xs for xs in tr)
        d[(root_degree,leaves)] += 1
    return dict(d)


def test():
    tests = 0
    d = {(1,1): 1}
    for n in range(2, 61):
        total = sum(d.values())
        expected_total = 1
        for odd in range(1,2*n-2,2):
            expected_total *= odd
        assert total == expected_total
        tests += 1
        if n <= 8:
            assert d == explicit(n), n
            tests += 1
        if n >= 3:
            W = wallis(n)
            root_mean = Fraction(sum(r*c for (r,l),c in d.items()), total)
            leaf_mean = Fraction(sum(l*c for (r,l),c in d.items()), total)
            root_second = Fraction(sum(r*r*c for (r,l),c in d.items()), total)
            leaf_second = Fraction(sum(l*l*c for (r,l),c in d.items()), total)
            mixed = Fraction(sum(r*l*c for (r,l),c in d.items()), total)
            assert root_mean == W-1
            assert leaf_mean == Fraction(2*n-1,3)
            assert root_second-root_mean**2 == 4*n-2-W-W*W
            assert leaf_second-leaf_mean**2 == Fraction(2*n*(n-2),9*(2*n-3))
            assert mixed-root_mean*leaf_mean == (W-2)/3
            tests += 5
            for r in range(1,n):
                subset = {l:c for (rr,l),c in d.items() if rr == r}
                assert subset
                cond = Fraction(sum(l*c for l,c in subset.items()), sum(subset.values()))
                assert cond == predicted(n,r), (n,r,cond,predicted(n,r))
                m=n-1
                bias = cond-leaf_mean
                threshold_formula = Fraction((r+1)**2-4*m,3*(2*m-r-1))
                assert bias == threshold_formula
                assert (bias>0)-(bias<0) == ((r+1)**2>4*m)-((r+1)**2<4*m)
                tests += 3
            for r in range(1,n-1):
                m=n-1
                delta = predicted(n,r+1)-predicted(n,r)
                explicit_delta = Fraction((m-r)*(4*r+2)+(r-1)*(3*r+2), 3*(2*m-r-1)*(2*m-r-2))
                assert delta == explicit_delta and delta > 0
                tests += 1
        d = update(d,n)
    return tests

if __name__ == '__main__':
    print('VERIFICATION_OK exact assertions=',test())
