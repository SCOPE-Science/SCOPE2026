"""Exact finite checks of the cycle graph-state cut-rank generating function.

Only Python's standard library is needed. Run with:
    python3 verify_cycle_entanglement.py

For each size, two different calculations are compared: dynamic polynomial
transfer (the claimed formula) and exhaustive GF(2) cut-matrix elimination.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, log2


def rank_over_f2(rows):
    pivots = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def direct_cut_rank(n, mask):
    selected = [i for i in range(n) if (mask >> i) & 1]
    outside = [i for i in range(n) if not ((mask >> i) & 1)]
    cols = {i: j for j, i in enumerate(outside)}
    rows = []
    for i in selected:
        row = 0
        for neighbor in ((i - 1) % n, (i + 1) % n):
            if neighbor in cols:
                row ^= 1 << cols[neighbor]
        rows.append(row)
    return rank_over_f2(rows)


def transfer_polynomial(n):
    # State (current bit, parity of preceding run of crossing edges).
    states = ((0, 0), (0, 1), (1, 0), (1, 1))
    polynomial = Counter()
    for start in states:
        dp = {(start, 0, 0): 1}
        for _ in range(n):
            next_dp = defaultdict(int)
            for (state, z_degree, t_degree), count in dp.items():
                bit, parity = state
                for next_bit in (0, 1):
                    if bit == next_bit:
                        next_parity, rank_increment = 0, 0
                    else:
                        next_parity, rank_increment = 1 - parity, 1 - parity
                    key = ((next_bit, next_parity),
                           z_degree + bit, t_degree + rank_increment)
                    next_dp[key] += count
            dp = next_dp
        for (end, k, h), count in dp.items():
            if end == start:
                polynomial[(k, h)] += count
    if n % 2 == 0:
        m = n // 2
        polynomial[(m, m - 1)] += 2
        polynomial[(m, m)] -= 4
    return Counter({term: count for term, count in polynomial.items() if count})


def exhaustive_polynomial(n):
    counts = Counter()
    for mask in range(1 << n):
        counts[(mask.bit_count(), direct_cut_rank(n, mask))] += 1
    return counts


def expected_unconditioned_mean(n):
    if n % 2:
        return Fraction(n, 3) * (1 - Fraction(2, 1 << n))
    return Fraction(n, 3) - Fraction(n + 6, 3 * (1 << n))


def main():
    for n in range(3, 16):
        by_transfer = transfer_polynomial(n)
        by_elimination = exhaustive_polynomial(n)
        assert by_transfer == by_elimination, (n, by_transfer - by_elimination,
                                               by_elimination - by_transfer)
        assert sum(by_transfer.values()) == 1 << n
        for k in range(n + 1):
            assert sum(count for (size, h), count in by_transfer.items()
                       if size == k) == comb(n, k)
            for h in range(n // 2 + 1):
                assert by_transfer.get((k, h), 0) == by_transfer.get((n - k, h), 0)
        mean = Fraction(sum(h * count for (k, h), count in by_transfer.items()), 1 << n)
        assert mean == expected_unconditioned_mean(n), (n, mean)
        if n == 12:
            histogram = {h: by_transfer[(6, h)] for h in range(7)
                         if by_transfer[(6, h)]}
            assert histogram == {2: 12, 3: 96, 4: 306, 5: 386, 6: 124}
            entropy = -sum((count / 924) * log2(count / 924)
                           for count in histogram.values())
            assert abs(entropy - 1.8637129063345772) < 1e-12
    print("VERIFY_OK: cycles n=3..15; every subset size and rank; "
          "C12 balanced histogram (12,96,306,386,124).")

if __name__ == "__main__":
    main()
