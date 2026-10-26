"""Independent finite checks for cyclic binary reverse-complement subsequences.

Run: python verify.py. The proof for all run lengths is in RESULT.md.
"""
from itertools import product
from math import ceil


def longest_antipal(word):
    """Independent interval DP on a *linear* rotation, using endpoints only."""
    n = len(word)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for gap in range(1, n):
        for left in range(n - gap):
            right = left + gap
            best = max(dp[left + 1][right], dp[left][right - 1])
            if word[left] != word[right]:
                best = max(best, 2 + (dp[left + 1][right - 1] if gap > 1 else 0))
            dp[left][right] = best
    return dp[0][n - 1]


def cyclic_dp(a, b, c, d):
    word = '0' * a + '1' * b + '0' * c + '1' * d
    return max(longest_antipal(word[p:] + word[:p]) for p in range(len(word)))


def formula(a, b, c, d):
    two = max(min(a + c, b), min(a + c, d),
              min(b + d, a), min(b + d, c))
    four = max(min(a, d) + min(b, c),
               min(a, b) + min(c, d))
    return 2 * max(two, four)


def brute_subsets(a, b, c, d):
    """Independent embedding via all masks for n <= 12."""
    word = '0' * a + '1' * b + '0' * c + '1' * d
    n = len(word)
    best = 0
    for p in range(n):
        rot = word[p:] + word[:p]
        for mask in range(1, 1 << n):
            size = mask.bit_count()
            if size <= best or size % 2:
                continue
            subseq = ''.join(rot[i] for i in range(n) if mask & (1 << i))
            if all(subseq[i] != subseq[size - 1 - i] for i in range(size // 2)):
                best = size
    return best


def main():
    count = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        exact = cyclic_dp(a, b, c, d)
        target = formula(a, b, c, d)
        assert exact == target, (a, b, c, d, exact, target)
        count += 1
    brute_count = 0
    for n in range(4, 13):
        for a in range(1, n - 2):
            for b in range(1, n - a - 1):
                for c in range(1, n - a - b):
                    d = n - a - b - c
                    assert brute_subsets(a, b, c, d) == formula(a, b, c, d)
                    brute_count += 1
    for s in range(2, 51):
        m = min(formula(a, b, s - a, s - b)
                for a in range(1, s) for b in range(1, s))
        target = 2 * ((3 * s + 3) // 4)
        assert m == target, (s, m, target)
        if s >= 4:
            q, r = divmod(s, 4)
            a, b, c, d = q, 2*q + r // 2, 3*q + r, 2*q + (r + 1) // 2
        else:
            a, b, c, d = 1, 1, s - 1, s - 1
        assert (a + c == s and b + d == s)
        assert formula(a, b, c, d) == target, (s, a, b, c, d)
    print('VERIFY_OK dp_quadruples=%s independent_masks=%s balanced_s=2..50' % (count, brute_count))


if __name__ == '__main__':
    main()
