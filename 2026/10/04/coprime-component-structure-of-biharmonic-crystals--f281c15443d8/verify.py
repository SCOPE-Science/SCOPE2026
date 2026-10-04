#!/usr/bin/env python3
from math import gcd

def recurrence_pairs():
    checked = 0
    for w in range(3, 101):
        u = [0, 1]
        for k in range(1, 18):
            u.append((w - 2) * u[-1] - u[-2] + 2)
        for n in range(3, 19):
            x, y = u[n], u[n-1]
            assert (x + y - 1) ** 2 == w * x * y
            if x <= 1 or y <= 1:
                continue
            a, b = 2 * x - 1, 2 * y - 1
            assert a > 1 and b > 1 and a % 2 == 1 and b % 2 == 1
            assert gcd(a, b) == 1
            assert gcd(a + 1, b + 1) == 2
            checked += 1
    return checked

def direct_pairs():
    found = 0
    for a in range(3, 1202, 2):
        for b in range(a, 1202, 2):
            den = (a + 1) * (b + 1)
            num = (a + b) ** 2
            if num % den == 0:
                found += 1
                assert gcd(a, b) == 1
                assert gcd(a + 1, b + 1) == 2
    return found

if __name__ == "__main__":
    r = recurrence_pairs()
    d = direct_pairs()
    print(f"VERIFY_OK recurrence_pairs={r} direct_crystal_pairs={d}")
