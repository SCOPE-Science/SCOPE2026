#!/usr/bin/env python3
"""Exact arithmetic reproducibility for odd-window cubic sums of Fibonacci/Lucas terms."""
from math import gcd

def sequence(n, lucas):
    x, y = (2, 1) if lucas else (0, 1)
    z = [x, y]
    for _ in range(n - 1):
        x, y = y, x + y
        z.append(y)
    return z

def check():
    for lucas in (False, True):
        a = sequence(1205, lucas)
        for i in range(1000):
            q = [a[i+j] ** 3 for j in range(5)]
            assert q[4] - 3*q[3] - 6*q[2] + 3*q[1] + q[0] == 0
        for k in range(1, 203, 2):
            s = [sum(a[n+j] ** 3 for j in range(1, k+1)) for n in range(20)]
            g = 0
            for v in s:
                g = gcd(g, v)
            expected = 2 if k % 6 == 3 else 1
            assert g == expected, (lucas, k, g, expected)
            d = 0
            for t in range(1, 12):
                d = gcd(d, a[t+k]**3 - a[t]**3)
            assert d == expected, (lucas,k,d)
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 31, 43):
            for k in range(1, 81, 2):
                assert any((a[t+k]**3-a[t]**3) % p != 0 for t in range(1, 5)), (lucas,p,k)
    print('PASS: 1000 fourth-order recurrence instances per family; 202 odd-window lengths across both families; modular witnesses for 10 odd primes and 40 window lengths each.')

if __name__ == '__main__':
    check()
