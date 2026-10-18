#!/usr/bin/env python3
"""Exhaustive check of distinct descendants for one length-two tandem-or-palindrome duplication."""
import itertools
from collections import Counter
from fractions import Fraction


def descendant_sets(w):
    n = len(w)
    td = [w[:i + 2] + w[i:i + 2] + w[i + 2:] for i in range(n - 1)]
    pd = [w[:i + 2] + w[i:i + 2][::-1] + w[i + 2:] for i in range(n - 1)]
    return td, pd


def formula(w):
    n = len(w)
    return (1
            + sum(w[i] != w[i + 2] for i in range(n - 2))
            + sum(w[i] != w[i + 1] for i in range(n - 1))
            - sum(w[i] == w[i + 3] and w[i + 1] == w[i + 2]
                  and w[i] != w[i + 1] for i in range(n - 3)))


def binary_best_difference(d):
    if not any(d):
        return False
    begin = 0
    while begin < len(d):
        if d[begin]:
            begin += 1
            continue
        end = begin
        while end < len(d) and not d[end]:
            end += 1
        length = end - begin
        if begin == 0 or end == len(d):
            if length != 1:
                return False
        elif length not in (1, 2):
            return False
        begin = end
    return True


def tribonacci_binary_best_counts(nmax):
    # G(z) = z (1+z)^2/(1-z-z^2-z^3).
    mmax = nmax - 1
    a = [0] * (mmax + 1)
    for m in range(1, mmax + 1):
        a[m] = (a[m - 1] if m >= 1 else 0) + (a[m - 2] if m >= 2 else 0) + (a[m - 3] if m >= 3 else 0)
        a[m] += {1: 1, 2: 2, 3: 1}.get(m, 0)
    return [2 * a[n - 1] for n in range(2, nmax + 1)]


def main():
    limits = {2: 12, 3: 9, 4: 7, 5: 6}
    total_words = 0
    total_site_collisions = 0
    for q, max_n in limits.items():
        for n in range(2, max_n + 1):
            mx = -1
            mx_count = 0
            tally = 0
            for w in itertools.product(range(q), repeat=n):
                td, pd = descendant_sets(w)
                actual = len(set(td + pd))
                assert actual == formula(w), (q, w, actual, formula(w))
                # Exact collision type: nonconstant P_i matches some T_j iff abba at site i.
                for i in range(n - 1):
                    if w[i] != w[i + 1]:
                        actual_cross = {j for j, v in enumerate(td) if v == pd[i]}
                        expected_cross = (i <= n - 4 and w[i] == w[i + 3]
                                          and w[i + 1] == w[i + 2])
                        assert bool(actual_cross) == expected_cross, (q, w, i, actual_cross)
                        # No nonconstant PAL value equals another PAL value.
                        assert all(pd[i] != pd[j] for j in range(n - 1) if j != i), (q, w, i)
                        total_site_collisions += 1
                if q == 2:
                    d = tuple(w[i] != w[i + 1] for i in range(n - 1))
                    assert (actual == n) == binary_best_difference(d), (w, actual, d)
                mx = max(mx, actual)
                mx_count += int(actual == (n if q == 2 else 2*n - 2))
                tally += actual
                total_words += 1
            exp_max = n if q == 2 else 2*n - 2
            assert mx == exp_max, (q, n, mx, exp_max)
            exp_mxc = (tribonacci_binary_best_counts(n)[-1] if q == 2 else q*(q-1)*(q-2)**(n-2))
            assert mx_count == exp_mxc, (q, n, mx_count, exp_mxc)
            # For random independent coordinates, P(abba with a!=b)=(q-1)/q^3.
            expected_mean = (Fraction(1,1)
                + Fraction((n-2+n-1)*(q-1),q)
                - Fraction(max(0,n-3)*(q-1),q**3))
            assert Fraction(tally, q**n) == expected_mean, (q, n, tally, expected_mean)
    assert tribonacci_binary_best_counts(11) == [2, 6, 10, 18, 34, 62, 114, 210, 386, 710]
    print('MIXED_PAL_TANDEM_LENGTH2_PASS q=2..5 nmax=12,9,7,6 words=%d nonconstant_pal_sites=%d' % (total_words, total_site_collisions))

if __name__ == '__main__':
    main()
