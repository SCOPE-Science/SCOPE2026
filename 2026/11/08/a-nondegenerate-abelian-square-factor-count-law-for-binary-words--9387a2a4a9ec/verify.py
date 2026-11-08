#!/usr/bin/env python3
"""Independent finite checks for distinct Abelian squares in two-one binary words."""
from collections import defaultdict
from math import comb
from random import Random


def formula(a, b, c):
    zeros = max(a, b, c) // 2
    two = 0
    for u in range(a + 1):
        for v in range(c + 1):
            if abs(u - v) <= b and (u + b + v) % 2 == 0:
                two += 1
    return zeros, two


def actual(a, b, c):
    w = '0' * a + '1' + '0' * b + '1' + '0' * c
    factors = set()
    for start in range(len(w)):
        for stop in range(start + 2, len(w) + 1, 2):
            mid = (start + stop) // 2
            left, right = w[start:mid], w[mid:stop]
            if left.count('1') == right.count('1'):
                factors.add(w[start:stop])
    return sum('1' not in f for f in factors), sum('1' in f for f in factors)


def grouped_count(n):
    total = 0
    mean_sum = 0
    for a in range(n-1):
        for b in range(n-1-a):
            c = n-2-a-b
            z, t = formula(a, b, c)
            rz, rt = actual(a, b, c)
            assert (z, t) == (rz, rt), (a, b, c, z, t, rz, rt)
            total += t
            mean_sum += z + t
    m = n // 2
    closed = m*(m+1)*(m*m+m+1)//6 if n % 2 == 0 else m*(m+1)*(m+1)*(m+2)//6
    assert total == sum(k*k*(n - 2*k + 1) for k in range(1, n//2 + 1)), n
    assert total == closed, (n, total, closed)
    return total, mean_sum


def main():
    number = 0
    for n in range(2, 34):
        grouped_count(n)
        number += comb(n, 2)
    rng = Random(44221)
    for _ in range(2500):
        n = rng.randint(35, 125)
        p, q = sorted(rng.sample(range(n), 2))
        a, b, c = p, q-p-1, n-q-1
        assert formula(a, b, c) == actual(a, b, c)
    # Exact discrete strip-counting identity used in the proof.
    for a in range(11):
        for b in range(11):
            for c in range(11):
                by_d = 0
                for d in range(-b, b+1):
                    if (d-b) % 2: continue
                    lo=max(0,d)
                    hi=min(a,c+d)
                    by_d += max(0, hi-lo+1)
                assert by_d == formula(a,b,c)[1], (a,b,c)
    print(f'VERIFY_OK: {number} complete exhaustive words, 2500 random long words; all exact length-class totals n=2..33; 1331 difference-strip checks')


if __name__ == '__main__':
    main()
