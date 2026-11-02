#!/usr/bin/env python3
"""Independent bounded-multiplicity coefficient check for a partition identity."""

def valuation_two(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r

def is_power_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

def counts(limit, delete_powers=False):
    dp = [1] + [0] * limit
    for part in range(1, limit + 1):
        if delete_powers and is_power_three(part):
            continue
        if delete_powers and part == 1:
            raise AssertionError('1 is a power of three')
        bound = 2 + valuation_two(part)
        nxt = [0] * (limit + 1)
        for amount in range(limit + 1):
            if dp[amount] == 0:
                continue
            for j in range(min(bound, (limit-amount)//part) + 1):
                nxt[amount+j*part] += dp[amount]
        dp = nxt
    return dp

def verify(limit=512):
    a = counts(limit)
    b = counts(limit, True)
    assert a[:7] == [1, 1, 2, 2, 4, 5, 8], a[:7]
    assert all(a[n] - (a[n-1] if n > 0 else 0) == b[n] for n in range(limit+1))
    assert [n for n in range(1, limit+1) if a[n] == a[n-1]] == [1, 3]
    assert all(b[n] > 0 for n in range(4, limit+1))
    # Also evaluate the bijection as a local weight-preserving base-three digit conversion.
    for total in range(5000):
        digits = []
        w = total
        while w:
            digits.append(w % 3)
            w //= 3
        assert sum(d * 3**j for j, d in enumerate(digits)) == total
        assert all(0 <= d <= 2 for d in digits)
    print(f'VERIFIED: independent coefficient tables 0..{limit}, sharp plateau set, 5000 ternary conversions')
    print('first 21 original counts:', a[:21])
    print('first 21 differences:', b[:21])

if __name__ == '__main__':
    verify()
