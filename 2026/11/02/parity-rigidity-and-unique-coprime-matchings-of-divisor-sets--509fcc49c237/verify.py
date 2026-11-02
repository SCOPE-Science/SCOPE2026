"""Independent finite checks for the coprime-divisor matching uniqueness theorem."""
from itertools import permutations
from math import gcd


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def prime_support(n):
    p = 2
    ans = []
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return tuple(ans)


def is_squarefree(n):
    for p in prime_support(n):
        if n % (p * p) == 0:
            return False
    return True


def predicted_unique(n, target):
    ps = prime_support(n)
    return is_squarefree(n) and len({tuple(p for p in ps if y % p == 0) for y in target}) == len(divisors(n))


def predicted_ap(n, a, b):
    if n == 1:
        return True
    ps = prime_support(n)
    if n in ps:
        p = n
        return (a % p == 0) != ((a + b) % p == 0)
    if n == 6:
        return (a % 3 == 0 and b % 2 != 0 and b % 3 != 0)
    return False


def count_by_dp(n, target):
    d = divisors(n)
    N = len(d)
    assert len(target) == N and len(set(target)) == N
    dp = {0: 1}
    for x in d:
        nx = {}
        opts = [j for j, y in enumerate(target) if gcd(x, y) == 1]
        for mask, count in dp.items():
            for j in opts:
                if not (mask & (1 << j)):
                    k = mask | (1 << j)
                    nx[k] = nx.get(k, 0) + count
        dp = nx
    return dp.get((1 << N) - 1, 0)


def count_brute(n, target):
    return sum(all(gcd(x, target[j]) == 1 for x, j in zip(divisors(n), perm))
               for perm in permutations(range(len(target))))


def run():
    checked = 0
    odd_cases = 0
    unique_cases = 0
    total_zero = 0
    sample_six = []
    for n in range(1, 181):
        N = len(divisors(n))
        if N > 12:
            continue
        for a in range(1, 15):
            for b in range(1, 6):
                target = tuple(a + b*j for j in range(N))
                c = count_by_dp(n, target)
                pred = predicted_unique(n, target)
                assert (c % 2 == 1) == pred, (n, a, b, c, pred)
                assert (c == 1) == pred, (n, a, b, c, pred)
                assert pred == predicted_ap(n, a, b), (n, a, b)
                checked += 1
                odd_cases += c % 2
                unique_cases += (c == 1)
                total_zero += (c == 0)
                if n == 6 and pred:
                    sample_six.append((a, b, c))
                if n <= 14 and N <= 6 and a <= 3 and b <= 2:
                    assert count_brute(n, target) == c, (n, a, b)
    # Arbitrary non-progression targets: one for each possible prime support.
    for n in (6, 30, 210):
        target = divisors(n)  # all support patterns distinct
        assert predicted_unique(n, target)
        assert count_by_dp(n, target) == 1
    # Non-squarefree and repeated support: involution makes count even.
    for n, target in [(12, (1, 2, 3, 4, 5, 6)), (6, (1, 2, 4, 8)), (30, (1, 2, 3, 4, 6, 8, 9, 12))]:
        assert not predicted_unique(n, target)
        assert count_by_dp(n, target) % 2 == 0
    assert sample_six
    print('VERIFY_OK cases=%d odd=%d unique=%d zero=%d six_examples=%d arbitrary_sets=6 independent_brute=yes' % (checked, odd_cases, unique_cases, total_zero, len(sample_six)))
    print('SIX_EXAMPLES_FIRST', sample_six[:8])


if __name__ == '__main__':
    run()
