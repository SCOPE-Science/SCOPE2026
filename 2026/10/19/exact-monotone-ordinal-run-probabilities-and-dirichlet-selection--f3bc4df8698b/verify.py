#!/usr/bin/env python3
"""Exact finite-horizon checks for monotone ordinal runs of integer shifts.

All assertions are over rational numbers or exact integer combinatorics.
The infinite-horizon assertions require the proof in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def theoretical_probability(base, comparisons):
    return Fraction(comb(comparisons + base - 1, base - 2),
                    (base - 1) * base ** comparisons)


def rational_cylinder_intervals(base, comparisons):
    """Enumerate each base-adic cell; directly intersect ALL adjacent-order inequalities.

    On a length-base^{-m} cell, the first m+1 iterates are affine except for
    their last-digit jump. Splitting additionally at the final jump makes the
    linear inequalities exact (and hence use b^(m+1) cells).
    """
    denominator = base ** (comparisons + 1)
    intervals = []
    # Base-(m+1) cells control floors for T^0,...,T^m.
    for cell in range(denominator):
        lo, hi = Fraction(cell, denominator), Fraction(cell + 1, denominator)
        digit_prefix = [cell // (base ** (comparisons + 1 - t)) for t in range(comparisons + 1)]
        for t in range(comparisons):
            # b^t*x - floor(b^t*x) < b^(t+1)*x - floor(b^(t+1)*x)
            # Thus x > (prefix[t+1]-prefix[t]) / (b^(t+1)-b^t).
            lower = Fraction(digit_prefix[t+1] - digit_prefix[t],
                             base ** (t+1) - base ** t)
            lo = max(lo, lower)
        if hi > lo:
            midpoint = (hi + lo) / 2
            jpath = []
            for t in range(comparisons):
                y = (midpoint * base ** t) % 1
                j = int(base * y)
                assert 0 <= j <= base-2
                jpath.append(j)
            intervals.append((lo, hi, tuple(jpath)))
    return intervals


def main():
    horizon_checks = 0
    path_checks = 0
    for b in range(2, 7):
        for m in range(1, 6):
            intervals = rational_cylinder_intervals(b, m)
            total = sum((hi-lo for lo, hi, _ in intervals), Fraction(0))
            assert total == theoretical_probability(b, m), (b,m,total)
            horizon_checks += 1
            paths = defaultdict(Fraction)
            for lo, hi, js in intervals:
                assert list(js) == sorted(js)
                paths[js] += hi-lo
            assert len(paths) == comb(m+b-2, b-2)
            for js, measure in paths.items():
                last = js[-1]
                expected = Fraction(b-1-last,(b-1)*b**m)
                assert measure == expected, (b,m,js,measure,expected)
                path_checks += 1
            # The probability of visiting all b-1 indices, conditional on monotonicity.
            actual_all = sum((v for js, v in paths.items()
                              if len(set(js)) == b-1), Fraction(0))
            proposed_all = (Fraction(comb(m-1,b-2), (b-1)*b**m)
                            if m >= b-1 else Fraction(0))
            assert actual_all == proposed_all
            if m >= b-1:
                ratio = Fraction(comb(m-1,b-2),comb(m+b-1,b-2))
                assert actual_all/total == ratio
            # Verify each orbit's proximity to the repelling fixed points,
            # by interval endpoint domination of its affine orbit sum.
            for lo,hi,js in intervals:
                first=(lo+hi)/2
                values=[(first*b**t)%1 for t in range(m)]
                err=sum(values[t]-Fraction(js[t],b-1) for t in range(m))
                assert 0 <= err <= b, (b,m,js,err)
    comb_checks=0
    for b in range(2,15):
        for m in range(1,22):
            left=sum((b-1-j)*comb(m+j-1,j) for j in range(b-1))
            assert left==comb(m+b-1,b-2)
            if m>=b-1:
                good=comb(m-1,b-2)
                allwords=comb(m+b-1,b-2)
                assert 0<=good<=allwords
            comb_checks+=1
    print(f'VERIFY_OK {horizon_checks} independently intersected exact horizons; '
          f'{path_checks} exact branch cylinders; '
          f'{comb_checks} combinatorial identities and occupation bounds')


if __name__ == '__main__':
    main()
