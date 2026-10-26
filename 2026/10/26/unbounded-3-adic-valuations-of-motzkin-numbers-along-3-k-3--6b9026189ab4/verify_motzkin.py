#!/usr/bin/env python3
"""Integer-arithmetic finite corroboration for a Motzkin prime-power theorem."""
from math import comb


def v3(n):
    assert n > 0
    s = 0
    while n % 3 == 0:
        s += 1
        n //= 3
    return s


def carries3(a, b):
    carry = 0
    count = 0
    while a or b or carry:
        da, db = a % 3, b % 3
        carry = (da + db + carry) // 3
        count += carry
        a //= 3
        b //= 3
    return count


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def check():
    a, b = 1, 1
    indexes = {3 ** k - 3: k for k in range(2, 8)}
    assert (a, b) == (1, 1)
    for n in range(2, max(indexes) + 1):
        numerator = (2 * n + 1) * b + 3 * (n - 1) * a
        assert numerator % (n + 2) == 0
        a, b = b, numerator // (n + 2)
        if n in indexes:
            k = indexes[n]
            assert b % (3 ** k) == (-3 ** (k - 1)) % (3 ** k)
            assert v3(b) == k - 1
    for k in range(2, 9):
        N = 3 ** k
        assert 4 * (2 * N - 1) * (2 * N - 3) * catalan(N - 2) == N * comb(2 * N, N)
        assert v3(catalan(N - 2)) == k - 1
        for j in range(1, k):
            s = N - j - 2
            assert v3(catalan(s)) == carries3(s, s) - v3(s + 1)
            assert v3(catalan(s)) >= k - j
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
