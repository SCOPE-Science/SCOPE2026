#!/usr/bin/env python3
"""Exact tests for root-split/cherry second moments in the Yule model."""
from collections import Counter
from fractions import Fraction as Q
from math import factorial


def cherry_pmf(max_n):
    law = {1: {0: Q(1)}, 2: {1: Q(1)}}
    for n in range(2, max_n):
        next_law = {}
        for c, p in law[n].items():
            next_law[c] = next_law.get(c, Q(0)) + p * Q(2 * c, n)
            next_law[c + 1] = next_law.get(c + 1, Q(0)) + p * Q(n - 2 * c, n)
        assert sum(next_law.values()) == 1
        law[n + 1] = next_law
    return law


def moments(law):
    mean = sum(Q(c) * p for c, p in law.items())
    second = sum(Q(c*c) * p for c, p in law.items())
    return mean, second


def deviations(n, k):
    j = min(k, n-k)
    a = {1: Q(-1, 3), 2: Q(1, 3)}.get(j, Q(0))
    b = {1: Q(-10*n+3,45), 2: Q(10*n+1,45),
         3: Q(-6,45),4: Q(2,45)}.get(j,Q(0))
    return a, b


def sizes_cherries(tree):
    if tree is None:
        return 1, 0
    ls, lc = sizes_cherries(tree[0])
    rs, rc = sizes_cherries(tree[1])
    return ls + rs, lc + rc + (ls == 1 and rs == 1)


def split_leaf(tree, index):
    if tree is None:
        assert index == 0
        return (None, None)
    left_count = sizes_cherries(tree[0])[0]
    if index < left_count:
        return (split_leaf(tree[0], index), tree[1])
    return (tree[0], split_leaf(tree[1], index - left_count))


def test_histories():
    histories = [(None, None)]
    assertions = 0
    for n in range(2, 9):
        assert len(histories) == factorial(n-1)
        cells = Counter()
        for tree in histories:
            k = sizes_cherries(tree[0])[0]
            c = sizes_cherries(tree)[1]
            cells[k, c] += 1
        for k in range(1, n):
            total = sum(v for (j, c), v in cells.items() if j == k)
            assert total == len(histories) // (n - 1)
            assertions += 1
        if n < 8:
            histories = [split_leaf(tree, i) for tree in histories for i in range(n)]
    return assertions


def main():
    laws = cherry_pmf(65)
    assertions = 0
    for n in range(10, 66):
        mu = Q(n, 3)
        second = Q(n*n, 9) + Q(2*n, 45)
        assert moments(laws[n]) == (mu, second)
        for k in range(1, n):
            klaw, rlaw = laws[k], laws[n-k]
            cmu = sum(Q(a+b)*p*q for a,p in klaw.items() for b,q in rlaw.items())
            csecond = sum(Q((a+b)**2)*p*q for a,p in klaw.items() for b,q in rlaw.items())
            da, db = deviations(n, k)
            assert cmu == mu + da, ('mean',n,k,cmu,da)
            assert csecond == second + db, ('second',n,k,csecond,db)
            assertions += 2
        event_mean = Q(1,4) * sum(mu + deviations(n, k)[0] for k in (1,2,n-2,n-1))
        event_second = Q(1,4) * sum(second + deviations(n,k)[1] for k in (1,2,n-2,n-1))
        assert event_mean == mu
        assert event_second - event_mean**2 == Q(2*(n+1),45)
        assertions += 2
    assertions += test_histories()
    print('PASS:',assertions,'exact moment/history assertions, n=10..65 and independent Yule histories n<=8')

if __name__ == '__main__':
    main()
