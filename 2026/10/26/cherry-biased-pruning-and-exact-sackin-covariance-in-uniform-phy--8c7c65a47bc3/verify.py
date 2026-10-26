"""Exact checks for the cherry/Sackin Palm identity in uniform rooted binary trees.

Only Python's standard library is required. Exhaustive checks are finite illustrations;
all-size statements follow from the separate combinatorial and algebraic proofs.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


@lru_cache(maxsize=None)
def plane_trees(n):
    if n == 1:
        return (None,)
    return tuple((a, b) for j in range(1, n)
                 for a in plane_trees(j) for b in plane_trees(n - j))


def tree_stats(t):
    if t is None or isinstance(t, int):
        return (0, 0, 1)
    c1, s1, a = tree_stats(t[0])
    c2, s2, b = tree_stats(t[1])
    n = a + b
    return c1 + c2 + int(n == 2), s1 + s2 + n, n


def leaf_depths(t, depth=0):
    if t is None or isinstance(t, int):
        return (depth,)
    return leaf_depths(t[0], depth + 1) + leaf_depths(t[1], depth + 1)


@lru_cache(maxsize=None)
def labeled_trees(labels):
    if len(labels) == 1:
        return (labels[0],)
    anchor, rest = labels[0], labels[1:]
    output = []
    for size in range(1, len(labels)):
        for subset in combinations(rest, size - 1):
            left = (anchor,) + subset
            remaining = set(left)
            right = tuple(x for x in labels if x not in remaining)
            for u in labeled_trees(left):
                for v in labeled_trees(right):
                    output.append((u, v))
    return tuple(output)


def model_q(n):
    return Fraction(4 ** (n - 1), comb(2 * n - 2, n - 1))


def model_cov(n):
    q = model_q(n)
    return Fraction(n, 4 * (2 * n - 3)) * (4 * (n - 1) - n * q)



def check_plane_joint():
    rows, histogram_entries = 0, 0
    for n in range(2, 10):
        ts = plane_trees(n)
        assert len(ts) == comb(2 * n - 2, n - 1) // n
        sample = [tree_stats(t) for t in ts]
        N = len(sample)
        sumc = sum(c for c, _, _ in sample)
        sums = sum(s for _, s, _ in sample)
        sumcs = sum(c * s for c, s, _ in sample)
        assert Fraction(sumc, N) == Fraction(n * (n - 1), 2 * (2 * n - 3))
        assert Fraction(sums, N) == n * (model_q(n) - 1)
        covariance = Fraction(sumcs, N) - Fraction(sumc * sums, N * N)
        assert covariance == model_cov(n), (n, covariance, model_cov(n))
        weight = Counter()
        for c, s, _ in sample:
            weight[s] += c
        contracted = Counter()
        old = plane_trees(n - 1)
        for t in old:
            s = tree_stats(t)[1]
            for d in leaf_depths(t):
                contracted[s + d + 2] += 1
        target_factor = Fraction(n * (n - 1), 2 * (2 * n - 3))
        for val in set(weight) | set(contracted):
            lhs = Fraction(weight[val], N)
            rhs = target_factor * Fraction(contracted[val], len(old) * (n - 1))
            assert lhs == rhs, (n, val, lhs, rhs)
            histogram_entries += 1
        rows += 1
    return rows, histogram_entries


def check_labeled():
    count = 0
    for n in range(2, 8):
        ts = labeled_trees(tuple(range(n)))
        expected_count = 1
        for odd in range(1, 2 * n - 2, 2):
            expected_count *= odd
        assert len(ts) == expected_count, (n, len(ts), expected_count)
        C, S, CS = 0, 0, 0
        for t in ts:
            c, s, leaves = tree_stats(t)
            assert leaves == n
            C, S, CS = C + c, S + s, CS + c * s
        N = len(ts)
        assert Fraction(C, N) == Fraction(n * (n - 1), 2 * (2 * n - 3))
        assert Fraction(S, N) == n * (model_q(n) - 1)
        assert Fraction(CS, N) - Fraction(C * S, N * N) == model_cov(n)
        count += N
    return count


def check_algebra():
    catalan = [0] * 202
    total = [0] * 202
    catalan[1] = 1
    for n in range(2, 202):
        catalan[n] = sum(catalan[j] * catalan[n - j]
                         for j in range(1, n))
        total[n] = n * catalan[n] + 2 * sum(catalan[j] * total[n - j]
                                           for j in range(1, n))
        assert total[n] == 4 ** (n - 1) - comb(2 * n - 2, n - 1)
        assert catalan[n] == comb(2 * n - 2, n - 1) // n
        a = Fraction(n * model_q(n), n - 1)
        if n in (2, 3):
            assert a == 4 and model_cov(n) == 0
        else:
            assert a > 4 and model_cov(n) < 0
        if n >= 3:
            next_a = Fraction((n + 1) * model_q(n + 1), n)
            assert next_a / a == Fraction(2 * (n * n - 1), n * (2 * n - 1))
    return 200


if __name__ == "__main__":
    plane_rows, palm_bins = check_plane_joint()
    labeled_count = check_labeled()
    algebra_cases = check_algebra()
    print(f"PASS: {plane_rows} exhaustive plane-tree sizes (2..9), "
          f"{palm_bins} Palm-histogram bins; {labeled_count} exhaustive "
          f"labeled trees (2..7), {algebra_cases} exact algebra recurrences.")
