#!/usr/bin/env python3
"""Independent exact checks for the Catalan law of Dyck subsequence universality.
No third-party packages are needed. Finite checks support, but do not prove,
the unrestricted all-length theorem stated in RESULT.md.
"""
from collections import Counter, defaultdict
from math import comb
from fractions import Fraction


def greedy_index(word):
    seen = 0
    arches = 0
    for c in word:
        seen |= 1 << c
        if seen == 3:
            arches += 1
            seen = 0
    return arches


def enumerate_dyck(n):
    word = []
    def rec(zeros, ones):
        if zeros == n and ones == n:
            yield tuple(word)
            return
        if zeros < n:
            word.append(0)
            yield from rec(zeros + 1, ones)
            word.pop()
        if ones < zeros:
            word.append(1)
            yield from rec(zeros, ones + 1)
            word.pop()
    yield from rec(0, 0)


def catalan(m):
    return comb(2*m, m) // (m + 1)


def algebraic_coefficient(n, k):
    """[t^n u^k] C(t*u*(1-t*u)/(1-t)), as a finite integer sum."""
    if n == 0:
        return int(k == 0)
    if k <= 0 or k > n:
        return 0
    d = n - k
    return sum(((-1) ** (k - j)) * catalan(j) * comb(j, k - j)
               * comb(j + d - 1, d)
               for j in range((k + 1) // 2, k + 1))


def independent_arch_transfer(max_k, max_d):
    """Counts paths of greedy arches by number of arches and positive-height ascent."""
    counts = {(0, 0): 1}  # (upward increments, current height)
    rows = []
    for k in range(max_k + 1):
        rows.append([sum(v for (d, h), v in counts.items() if d == target)
                     for target in range(max_d + 1)])
        next_counts = defaultdict(int)
        for (d, h), v in counts.items():
            next_counts[(d, h)] += (1 if h == 0 else 2) * v
            for s in range(1, max_d - d + 1):
                next_counts[(d + s, h + s)] += v
            for s in range(1, h):
                next_counts[(d, h - s)] += v
        counts = next_counts
    return rows


def main():
    checks = 0
    for n in range(0, 13):
        actual = Counter(greedy_index(w) for w in enumerate_dyck(n))
        assert sum(actual.values()) == catalan(n), (n, actual)
        for k in range(n + 1):
            assert actual[k] == algebraic_coefficient(n, k), (
                'direct Dyck vs algebraic', n, k, actual[k], algebraic_coefficient(n, k))
            checks += 1
    rows = independent_arch_transfer(18, 8)
    for k, row in enumerate(rows):
        for d, count in enumerate(row):
            assert count == algebraic_coefficient(k + d, k), (
                'arch graph vs algebraic', k, d, count, algebraic_coefficient(k + d, k))
            checks += 1
    for n in range(2, 65):
        assert algebraic_coefficient(n, n - 1) == 2**(n - 1) - 1
        checks += 1
    for n in range(4, 65):
        assert algebraic_coefficient(n, n - 2) == (comb(n, 2) - 1) * 2**(n - 4)
        checks += 1
    # Derivatives of 4*u*u*r*r-(4*u+1)*r+1=0 at u=1, r=1/4.
    r = Fraction(1, 4)
    fp_r = 8*r - 5
    fp_u = 8*r*r - 4*r
    r1 = -fp_u / fp_r
    r2 = -(8*r*r + 2*(16*r-4)*r1 + 8*r1*r1) / fp_r
    mean_slope = -r1 / r
    variance_slope = - (r1 / r + r2 / r - (r1 / r)**2)
    assert (r1, r2, mean_slope, variance_slope) == (
        Fraction(-1, 6), Fraction(13, 54), Fraction(2, 3), Fraction(4, 27))
    checks += 4
    print('VERIFY_OK', 'assertions=', checks,
          'direct_Dyck_words=', sum(catalan(n) for n in range(13)),
          'transfer_cells=', len(rows)*len(rows[0]),
          'mean_slope=', str(mean_slope), 'variance_slope=', str(variance_slope))

if __name__ == '__main__':
    main()
