#!/usr/bin/env python3
"""Finite exact checks of the Lucas-rank distribution theorem.

The recurrence is evaluated directly at every parameter of each indicated
prime-power ring. This checker does not replace the infinite proof.
"""
from collections import Counter


def totient(d):
    n, result = d, d
    v = 2
    while v * v <= n:
        if n % v == 0:
            result -= result // v
            while n % v == 0:
                n //= v
        v += 1
    if n > 1:
        result -= result // n
    return result


def first_zero(s, q):
    before, current = 0, 1
    for n in range(1, q + 2):
        if current % q == 0:
            return n
        before, current = current, (s * current - before) % q
    raise AssertionError("Rank not found within the proven bound")


def predicted(p, k):
    q = p ** k
    minus = (p - 1) * p ** (k - 1) // 2
    plus = (p + 1) * p ** (k - 1) // 2
    answer = Counter()
    for d in range(1, q + 2):
        dprime = d
        while dprime % p == 0:
            dprime //= p
        if dprime > 1:
            count = int(minus % d == 0) + int(plus % d == 0)
            if count:
                answer[d] += count * totient(d)
    if p == 3:
        answer[3] += 2
        for a in range(2, k + 1):
            answer[3 ** a] += 4 * 3 ** (a - 2)
    else:
        answer[q] += 2 * p ** (k - 1)
    return answer


def main():
    rings = 0
    parameters = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 31]:
        for k in range(1, 7):
            q = p ** k
            if q > 1300:
                continue
            actual = Counter(first_zero(s, q) for s in range(q))
            expected = predicted(p, k)
            assert actual == expected, (p, k, actual, expected)
            assert sum(expected.values()) == q
            assert all(1 < d <= q + 1 for d in actual)
            rings += 1
            parameters += q
    assert predicted(3, 2) == Counter({2: 1, 3: 2, 6: 2, 9: 4})
    assert predicted(7, 2) == Counter({2: 1, 3: 2, 4: 2, 14: 6, 21: 12, 28: 12, 49: 14})
    print(f"VERIFY_OK rings={rings} parameters={parameters}")


if __name__ == '__main__':
    main()
