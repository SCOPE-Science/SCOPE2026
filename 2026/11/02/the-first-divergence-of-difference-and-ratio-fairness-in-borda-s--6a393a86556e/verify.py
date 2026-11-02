#!/usr/bin/env python3
"""Exact finite certificate for Borda utility-gap comparisons in stable marriage."""
from itertools import permutations, product
from fractions import Fraction

WITNESS_MEN = ((2,0,3,1),(2,0,1,3),(3,2,1,0),(3,1,0,2))
WITNESS_WOMEN = ((3,2,0,1),(0,3,2,1),(3,2,1,0),(0,1,2,3))


def stable_matching_stats(men, women):
    n = len(men)
    assert len(women) == n
    rank_m = [tuple(row.index(w) for w in range(n)) for row in men]
    rank_w = [tuple(row.index(m) for m in range(n)) for row in women]
    result = []
    for pi in permutations(range(n)):
        inv = [None] * n
        for m, w in enumerate(pi):
            inv[w] = m
        blocked = False
        for m in range(n):
            for w in range(n):
                if rank_m[m][w] < rank_m[m][pi[m]] and rank_w[w][m] < rank_w[w][inv[w]]:
                    blocked = True
        if blocked:
            continue
        ranks = [rank_m[m][pi[m]] + 1 for m in range(n)] + [rank_w[w][inv[w]] + 1 for w in range(n)]
        hi = max(ranks)
        lo = min(ranks)
        gap = hi - lo
        ratio = Fraction(n + 1 - lo, n + 1 - hi)
        result.append((pi, gap, ratio, tuple(sorted(ranks))))
    assert result, 'The stable matching set must be nonempty'
    return result


def main():
    totals = {}
    for n in (1, 2, 3):
        orders = tuple(permutations(range(n)))
        profile_count = 0
        stable_count = 0
        uniform_second = 0
        for men in product(orders, repeat=n):
            for women in product(orders, repeat=n):
                v = stable_matching_stats(men, women)
                profile_count += 1
                stable_count += len(v)
                for _, gap, ratio, ranks in v:
                    if n == 3 and ranks[0] != 1:
                        assert ranks == (2,) * 6, (men,women,ranks)
                        uniform_second += 1
                # The entire weak preorder must agree, not just minimizers.
                for s in v:
                    for t in v:
                        assert (s[1] > t[1]) - (s[1] < t[1]) == (s[2] > t[2]) - (s[2] < t[2])
        assert profile_count == (len(orders) ** (2*n))
        totals[n] = (profile_count,stable_count,uniform_second)
    # Literal deterministic certificate, including exclusion of every other matching.
    w = stable_matching_stats(WITNESS_MEN, WITNESS_WOMEN)
    assert [(a[0],a[1],a[2]) for a in w] == [
        ((0,2,3,1),2,Fraction(2,1)),
        ((0,3,2,1),2,Fraction(3,1))], w
    assert set(a[0] for a in w if a[1] == min(x[1] for x in w)) == {(0,2,3,1),(0,3,2,1)}
    assert set(a[0] for a in w if a[2] == min(x[2] for x in w)) == {(0,2,3,1)}
    print('VERIFY_OK exact_small_profiles='+str(totals)+' witness_stable_matchings='+str(len(w))+' difference_optima=2 ratio_optima=1')

if __name__ == '__main__': main()
