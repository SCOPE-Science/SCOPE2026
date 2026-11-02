"""Reproducible checks for circular palindrome counts in binary run words.

The theorem in RESULT.md is proved mathematically; this program gives
finite, definition-level tests and independent enumeration controls.
Run: python3 verify_circular_four_run.py
"""
from itertools import product
from collections import Counter
from random import Random


def direct_palindromes(word):
    n = len(word)
    doubled = word + word
    out = set()
    for start in range(n):
        for length in range(1, n + 1):
            z = doubled[start:start + length]
            if z == z[::-1]:
                out.add(z)
    return out


def center_palindromes(word):
    n = len(word)
    doubled = word + word
    out = set()
    for center_twice in range(4 * n - 1):
        left = center_twice // 2
        right = left + center_twice % 2
        while left >= 0 and right < 2 * n and doubled[left] == doubled[right]:
            if left < n and right - left + 1 <= n:
                out.add(doubled[left:right + 1])
            left -= 1
            right += 1
    return out


def count4(a, b, c, d):
    n = a + b + c + d
    if a != c and b != d:
        return n + min(a, c) + min(b, d)
    if a == c and b != d:
        return n + a + b // 2 + d // 2
    if a != c and b == d:
        return n + b + a // 2 + c // 2
    return n + a // 2 + b // 2


def count2(a, b):
    return a + b + a // 2 + b // 2


def equality4(a, b, c, d):
    n = a + b + c + d
    if n < 5:
        return False
    return ((a == c and b != d and not (b % 2 and d % 2)) or
            (b == d and a != c and not (a % 2 and c % 2)))


def expected_maximizers(n):
    if n % 2:
        m = (n - 1) // 2
        return 2 * m * (m - 1)
    m = n // 2
    return (m - 1) * (m - 2) - 2 * ((m - 1) // 2)


def runs4(n):
    for a in range(1, n - 2):
        for b in range(1, n - a - 1):
            for c in range(1, n - a - b):
                yield a, b, c, n - a - b - c


def main():
    direct_calls = 0
    for n in range(2, 30):
        for a in range(1, n):
            w = '0' * a + '1' * (n - a)
            p1 = direct_palindromes(w)
            p2 = center_palindromes(w)
            assert p1 == p2
            assert len(p1) == count2(a, n - a)
            direct_calls += 1

    for n in range(4, 19):
        observed = Counter()
        best = 0
        for a, b, c, d in runs4(n):
            w = '0' * a + '1' * b + '0' * c + '1' * d
            p1 = direct_palindromes(w)
            p2 = center_palindromes(w)
            assert p1 == p2, (a, b, c, d)
            got = len(p1)
            assert got == count4(a, b, c, d), (a, b, c, d, got)
            observed[got] += 1
            best = max(best, got)
            direct_calls += 1
        expected_best = 4 if n == 4 else 8 if n == 6 else (3 * n) // 2
        assert best == expected_best, (n, best, expected_best)
        assert observed[best] == (1 if n == 4 else 8 if n == 6 else expected_maximizers(n)), (n, observed[best])

    # A larger symbolic census tests the equality classification and counts.
    symbolic_calls = 0
    for n in range(7, 80):
        num = 0
        for a, b, c, d in runs4(n):
            got = count4(a, b, c, d)
            assert got <= (3 * n) // 2
            eq = got == (3 * n) // 2
            assert eq == equality4(a, b, c, d), (n, a, b, c, d)
            num += eq
            symbolic_calls += 1
        assert num == expected_maximizers(n), (n, num)

    # Additional distant parameters are checked from the original definition.
    rng = Random(20261028)
    for _ in range(350):
        a, b, c, d = (rng.randint(1, 50) for _ in range(4))
        w = '0' * a + '1' * b + '0' * c + '1' * d
        assert len(center_palindromes(w)) == count4(a, b, c, d)
        direct_calls += 1

    # Simpson's six-run family, independently checked at finite sizes.
    for t in range(2, 22):
        w = '0' * (2 * t) + '1' + '0' * (2 * t - 1) + '1' + '0' * (2 * t - 2) + '1'
        assert len(w) == 6 * t
        assert len(direct_palindromes(w)) == 10 * t - 2
        direct_calls += 1

    print(f'VERIFY_OK direct_definition_instances={direct_calls} symbolic_compositions={symbolic_calls} six_run_cases=20')


if __name__ == '__main__':
    main()
