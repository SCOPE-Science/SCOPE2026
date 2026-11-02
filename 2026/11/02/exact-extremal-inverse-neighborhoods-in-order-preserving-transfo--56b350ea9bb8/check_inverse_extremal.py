"""Exact verification for inverse neighborhoods of isotone full transformations.

Run with Python 3.9+: python check_inverse_extremal.py
Only standard-library integer arithmetic is used.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb


def compose(f, g):
    """Return f after g, using zero-based coordinate maps."""
    return tuple(f[t] for t in g)


def direct_inverse_degree(f, maps):
    out = 0
    for g in maps:
        fg = compose(f, g)
        gf = compose(g, f)
        if compose(fg, f) == f and compose(gf, g) == g:
            out += 1
    return out


def block_gap_degree(f):
    blocks = []
    image = []
    for a in f:
        if not image or a != image[-1]:
            image.append(a)
            blocks.append(1)
        else:
            blocks[-1] += 1
    ans = 1
    for length in blocks:
        ans *= length
    for left, right in zip(image, image[1:]):
        ans *= right - left
    return ans


def balanced_product(total, parts):
    a, r = divmod(total, parts)
    return pow(a, parts - r) * pow(a + 1, r)


def rank_bound(n, rank):
    if rank == 1:
        return n
    return balanced_product(n, rank) * balanced_product(n - 1, rank - 1)


def closed_max(n):
    if n <= 2:
        return n
    if n == 3:
        return 4
    m, r = divmod(n, 3)
    if r == 0:
        return 16 * pow(3, 2 * m - 3)
    if r == 1:
        return 4 * pow(3, 2 * m - 1)
    return 8 * pow(3, 2 * m - 1)


def max_count(n):
    if n <= 2:
        return n
    if n == 3:
        return 2
    m, r = divmod(n, 3)
    if r == 0:
        return (comb(m - 1, 2) if m >= 3 else 0) + m * comb(m + 1, 3)
    if r == 1:
        return comb(m + 1, 2)
    return m * (m + 1)


def fixed_rank_extremizers(n, rank):
    if rank == 1:
        return n
    q, a = divmod(n, rank)
    qprime, b = divmod(n - 1, rank - 1)
    return comb(rank, a) * comb(rank - 1, b)


def run():
    for n in range(1, 7):
        maps = list(combinations_with_replacement(range(n), n))
        counts = Counter()
        pair_count_by_rank = Counter()
        for f in maps:
            x = direct_inverse_degree(f, maps)
            y = block_gap_degree(f)
            assert x == y, (n, f, x, y)
            counts[x] += 1
            pair_count_by_rank[len(set(f))] += x
        for r in range(1, n + 1):
            expected_pairs = comb(n + r - 1, 2 * r - 1) ** 2
            assert pair_count_by_rank[r] == expected_pairs, (n, r, pair_count_by_rank[r], expected_pairs)
        observed_max = max(counts)
        assert observed_max == closed_max(n)
        assert counts[observed_max] == max_count(n)
        assert sum(counts.values()) == comb(2 * n - 1, n)
        print("DIRECT", n, len(maps), observed_max, counts[observed_max])
    for n in range(2, 501):
        vals = [rank_bound(n, k) for k in range(1, n + 1)]
        best = max(vals)
        assert best == closed_max(n), (n, best, closed_max(n))
        maximizers = [k for k, v in enumerate(vals, start=1) if v == best]
        cnt = sum(fixed_rank_extremizers(n, k) for k in maximizers)
        assert cnt == max_count(n), (n, cnt, max_count(n), maximizers)
        if n >= 7:
            m, r = divmod(n, 3)
            expected_ranks = ([m + 1] if m == 2 else [m, m + 1]) if r == 0 else [m + 1]
            assert maximizers == expected_ranks, (n, maximizers, expected_ranks)
    print("FORMULA", "all dimensions 2..500 rank bounds and maximizer counts agree")
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
