"""Exact finite cross-checks for unit/double cumulative-envy theorem.

No third-party dependencies. Run: python verify.py
This verifies bounded finite instances; the accompanying proof covers all lengths.
"""
from functools import lru_cache
from itertools import product


def fixed_optimal(seq):
    n = len(seq)
    @lru_cache(None)
    def solve(t, d):
        if t == n:
            return 0
        val = seq[t]
        x, y = abs(d - val), d + val
        return min(x + solve(t + 1, x), y + solve(t + 1, y))
    return solve(0, 0)


def greedy_cost(seq):
    d = cost = 0
    for val in seq:
        d = abs(d - val)
        cost += d
    return cost


def free_optimal(a, b):
    @lru_cache(None)
    def solve(aa, bb, d):
        if aa == bb == 0:
            return 0
        ans = 10 ** 10
        for val, avail in ((1, aa), (2, bb)):
            if avail:
                for next_d in (abs(d - val), d + val):
                    ans = min(ans, next_d + solve(aa - (val == 1), bb - (val == 2), next_d))
        return ans
    return solve(a, b, 0)


def free_formula(a, b):
    return b + (a + 1) // 2 + (a == 0 and b % 2 == 1)


def main():
    count = 0
    for m in range(15):
        for seq in product((1, 2), repeat=m):
            g = greedy_cost(seq)
            opt = fixed_optimal(seq)
            assert g == opt, (seq, g, opt)
            count += 1
    free_count = 0
    for a in range(17):
        for b in range(17):
            formula = free_formula(a, b)
            opt = free_optimal(a, b)
            assert opt == formula, (a, b, opt, formula)
            free_count += 1
    failing = (1, 1, 3, 1)
    assert greedy_cost(failing) == 6
    assert fixed_optimal(failing) == 4
    assert all(greedy_cost(s) == fixed_optimal(s)
               for m in range(4)
               for s in product((1, 3), repeat=m))
    print(f'VERIFY_OK fixed_words={count} free_count_pairs={free_count} '
          'sharp_fixed_counterexample=(1,1,3,1)')


if __name__ == '__main__':
    main()
