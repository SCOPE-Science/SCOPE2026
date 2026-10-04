#!/usr/bin/env python3
from math import isqrt

LIMIT = 20000

def factorint(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def jordan(n, s):
    if n == 1:
        return 1
    ans = 1
    for p, e in factorint(n).items():
        ans *= p ** (s * (e - 1)) * (p ** s - 1)
    return ans

def F(n, a, b, s):
    return n ** a * jordan(n, s) ** b

def is_powerful(n):
    return all(e >= 2 for e in factorint(n).values())

def main():
    powerful = [n for n in range(1, LIMIT + 1) if is_powerful(n)]

    cases = 0
    for s in range(3, 7):
        for b in range(1, 4):
            for a in range(1, s * b):
                seen = {}
                for n in powerful:
                    value = F(n, a, b, s)
                    assert value not in seen, (a, b, s, seen[value], n)
                    seen[value] = n
                cases += 1

    m = 2 ** 2 * 37 * 191
    n = 2 * 3 ** 2 * 5 * 11 * 29
    assert m == 28268
    assert n == 28710
    assert jordan(m, 3) == jordan(n, 3)
    assert any(e == 1 for e in factorint(m).values())
    assert any(e == 1 for e in factorint(n).values())

    print("VERIFY_OK")
    print("powerful_limit=" + str(LIMIT))
    print("powerful_count=" + str(len(powerful)))
    print("open_range_parameter_cases=" + str(cases))
    print("fu_j3_collision_replayed=true")

if __name__ == "__main__":
    main()
