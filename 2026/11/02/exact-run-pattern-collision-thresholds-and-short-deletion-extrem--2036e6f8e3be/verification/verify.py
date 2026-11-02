"""Reproduce finite checks of run-pattern injectivity and a deletion-sphere extremum.

Python 3.10+; standard library only. This is not an infinite-proof certificate.
"""
from itertools import combinations, product
from math import comb


def runs(word):
    ans = []
    for ch in word:
        if ans and ans[-1][0] == ch:
            a, size = ans[-1]
            ans[-1] = (a, size + 1)
        else:
            ans.append((ch, 1))
    return ans


def pattern_count(lengths, deletions):
    dp = [1] + [0] * deletions
    for size in lengths:
        nxt = [0] * (deletions + 1)
        for j in range(deletions + 1):
            nxt[j] = sum(dp[j - h] for h in range(min(size, j) + 1))
        dp = nxt
    return dp[deletions]


def ball_count(word, deletions):
    n = len(word)
    return len({tuple(word[j] for j in I)
                for I in combinations(range(n), n - deletions)})


def first_collision_threshold(profile):
    if not any(profile[i][0] == profile[j][0]
               for i in range(len(profile)) for j in range(i + 1, len(profile))):
        return float('inf')
    return min(1 + sum(profile[h][1] for h in range(i + 1, j))
               for i in range(len(profile)) for j in range(i + 1, len(profile))
               if profile[i][0] == profile[j][0])


def balanced_bound(n, r, t):
    a, s = divmod(n, r)
    return pattern_count([a + 1] * s + [a] * (r - s), t)


def verify():
    checks = 0
    # Every t, including t beyond the alphabet size, tests the exact onset theorem.
    for q in (2, 3, 4):
        for n in range(1, 8 if q == 4 else 9):
            for word in product(range(q), repeat=n):
                p = runs(word)
                boundary = first_collision_threshold(p)
                sizes = [h for _, h in p]
                for t in range(1, n):
                    actual = ball_count(word, t)
                    upper = pattern_count(sizes, t)
                    assert (actual == upper) == (t < boundary), (q, word, t, upper, actual, boundary)
                    checks += 1
    print('run-pattern threshold cases:', checks)

    # Exhaust all eligible words: the bound is attained for each run count.
    trials = 0
    maxima = 0
    for q in (2, 3, 4):
        for n in range(2, 9):
            for t in range(1, min(q, n)):
                observed = {}
                for w in product(range(q), repeat=n):
                    r = len(runs(w))
                    observed[r] = max(observed.get(r, 0), ball_count(w, t))
                    trials += 1
                for r, got in observed.items():
                    want = balanced_bound(n, r, t)
                    assert got == want, (q, n, t, r, got, want)
                    maxima += 1
    print('maximum sphere word-tests:', trials, 'parameter rows:', maxima)
    # At alphabet size t the uniform statement fails already for n=r=t+1.
    for t in range(2, 9):
        q = t
        n = r = t + 1
        assert comb(r, t) == t + 1 > q
    print('sharp alphabet threshold examples:', 7)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    verify()
