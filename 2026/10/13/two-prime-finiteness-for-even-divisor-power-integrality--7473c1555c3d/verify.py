"""Exact finite reproducibility checks for the divisor-power two-support theorem.

The unconditional infinite statements are proved in RESULT.md, not by
exhaustive computation. Python standard library only.
"""
from math import isqrt


def factor(n):
    d, result = 2, {}
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def all_two_support(k):
    assert k >= 2 and k % 2 == 0
    answers = []
    for a in range(1, 2 * k):
        s = (2 ** (k * (a + 1)) - 1) // (2 ** k - 1)
        for p, e in factor(s).items():
            assert p > 2
            for b in range(1, e + 1):
                if (b + 1) % (2 ** a) == 0:
                    assert s % p ** b == 0
                    n = 2 ** a * p ** b
                    sigma = sum(2 ** (k * j) for j in range(a + 1)) * sum(p ** (k * j) for j in range(b + 1))
                    assert sigma % n == 0
                    answers.append((a, p, b, n))
    return sorted(answers)


def direct_check(k, top=10000):
    solution_set = []
    for n in range(2, top + 1, 2):
        f = factor(n)
        if len(f) != 2 or f.get(2, 0) < 1:
            continue
        sigma = 1
        for p, e in f.items():
            sigma *= sum(p ** (k * j) for j in range(e + 1))
        if sigma % n == 0:
            solution_set.append(n)
    return solution_set


def main():
    assert all_two_support(2) == [(1, 5, 1, 10)]
    assert all_two_support(4) == [(1, 17, 1, 34)]
    assert direct_check(2) == [10]
    assert direct_check(4) == [34]
    for k in range(2, 32, 2):
        for a in range(2 * k, 2 * k + 8):
            assert 2 ** a - 1 >= k * (a + 1)
    for p in (3, 5, 7, 11, 17, 31):
        for k in range(2, 14, 2):
            for b in range(1, 64):
                v2_sum = sum(p ** (k * j) for j in range(b + 1))
                v = 0
                while v2_sum % 2 == 0:
                    v2_sum //= 2
                    v += 1
                t, w = b + 1, 0
                while t % 2 == 0:
                    t //= 2
                    w += 1
                assert v == w
    print('EXACT_CERTIFICATE_OK k2=[10] k4=[34] brute_ceiling=10000 valuation_checks=2268 bound_layers=120')


if __name__ == '__main__':
    main()
