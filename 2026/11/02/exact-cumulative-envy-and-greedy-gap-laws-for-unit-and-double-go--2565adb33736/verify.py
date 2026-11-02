"""Exact finite cross-checks for two-agent temporal envy, item weights 1 and 2.

No third-party dependencies; run with Python >=3.9.
"""
from functools import lru_cache

@lru_cache(None)
def exact(a, b, difference):
    if a == b == 0:
        return 0
    possible = []
    for size, count in ((1, a), (2, b)):
        if count:
            for sign in (-1, 1):
                nxt = difference + sign * size
                possible.append(abs(nxt) + exact(a - (size == 1), b - (size == 2), nxt))
    return min(possible)


def expected_optimum(a, b):
    return (a + 1) // 2 + b if a else 2 * ((b + 1) // 2)


def greedy(a, b):
    difference = 0
    score = 0
    for size in [1] * a + [2] * b:
        difference = abs(difference - size)
        score += difference
    return score


def expected_greedy(a, b):
    if a % 2:
        return (a + 1) // 2 + b
    return a // 2 + 2 * ((b + 1) // 2)


def main():
    checks = 0
    for a in range(23):
        for b in range(23):
            observed = exact(a, b, 0)
            assert observed == expected_optimum(a, b), (a, b, observed)
            assert greedy(a, b) == expected_greedy(a, b), (a, b)
            difference = greedy(a, b) - observed
            assert difference == int(a >= 2 and a % 2 == 0 and b % 2 == 1)
            checks += 1
    print('VERIFY_OK exact_count_pairs=', checks, 'max_a=max_b=22')

if __name__ == '__main__':
    main()
