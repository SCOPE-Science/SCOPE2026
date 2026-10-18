#!/usr/bin/env python3
"""Exact-integer reproducibility checks for Fibonacci cubic window gcds.
Finite testing supplements, but does not substitute for, the infinite proof.
"""
from math import gcd

def fib_table(n):
    out = [0, 1]
    while len(out) <= n:
        out.append(out[-1] + out[-2])
    return out

def predicted(k, f):
    assert k >= 2 and k % 2 == 0
    m = k // 2
    Lm = f[m - 1] + f[m + 1]
    H = f[m] if k % 4 == 0 else Lm
    numerator = H * (3 if k % 8 == 0 else 1)
    denominator = 2 if k % 6 == 0 else 1
    assert numerator % denominator == 0
    return numerator // denominator

def test():
    f = fib_table(750)
    count = 0
    for k in range(2, 401, 2):
        u, v = f[k+1], f[k+2]
        h = gcd(u - 1, v - 1)
        A = gcd(u**3 - 1, v**3 - 1)
        H = f[k//2] if k % 4 == 0 else f[k//2-1] + f[k//2+1]
        assert h == H, (k, h, H)
        assert A == h * (3 if k % 8 == 0 else 1), k
        assert u*u + u*v - v*v == 1, k
        S0 = sum(f[i]**3 for i in range(1, k + 1))
        assert 2*S0 == -3*u**3 + 3*u*v*v - v**3 + 1, k
        assert gcd(A, S0) == predicted(k, f), k
        actual = 0
        S = S0
        for n in range(31):
            actual = gcd(actual, S)
            S += f[n+k+1]**3 - f[n+1]**3
        assert actual == predicted(k, f), (k, actual, predicted(k, f))
        for n in range(1, 32):
            assert (f[n+k]**3 - f[n]**3) % A == 0, (k, n)
            count += 1
    assert sum(f[i]**3 for i in range(1, 7)) == 674
    assert gcd(f[7]**3-1, f[8]**3-1) == 4
    assert predicted(6, f) == 2
    assert gcd(f[9]**3-1, f[10]**3-1) == 9
    assert predicted(8, f) == 9
    print(f"PASS: {200} even lengths 2..400, {count} exact shift-difference checks, 6200 window-gcd updates, two published-conjecture counterexamples")
    for k in (6, 8, 12, 16, 24, 30, 40):
        print(f"k={k}: exact gcd={predicted(k, f)}")
if __name__ == '__main__':
    test()
