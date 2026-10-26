#!/usr/bin/env python3
"""Independent finite checks for a periodic binary lunar divisor formula."""
from functools import lru_cache

@lru_cache(None)
def compositions(b, m):
    if m == 0:
        return 1
    if m < 0:
        return 0
    return sum(compositions(b, m-j) for j in range(1, min(m, b)+1))

def predicted(n):
    return sum((compositions(b, n-b) + compositions(b, n-b)**2)
               for b in range(1, n+1))

def lunar_divisor_count(t):
    N = t.bit_length()
    total = 0
    for a in range(N):
        b = N-1-a
        if not ((t >> a) & 1):
            continue
        if a == 0 or b == 0:
            total += 1
            continue
        allowed = [i for i in range(1, a) if (t >> i) & 1]
        for code in range(1 << len(allowed)):
            A = (1 << a) | 1
            for i, j in enumerate(allowed):
                if (code >> i) & 1:
                    A |= 1 << j
            # Canonical maximal admissible cofactor: its OR-product
            # covers the target iff any cofactor covers the target.
            B = sum(1 << j for j in range(b+1) if ((A << j) & ~t) == 0)
            if not (B & (1 << b)):
                continue
            value = 0
            x = A
            while x:
                bit = x & -x
                value |= B << (bit.bit_length()-1)
                x -= bit
            total += value == t
    return total

def main():
    expected = (2,4,6,12,24,62,160)
    assert tuple(predicted(n) for n in range(1,8)) == expected
    checks = 0
    for n in range(1,7):
        for h in range(3,7):
            if n*h > 24:
                continue
            target = 3 * sum(1 << (h*j) for j in range(n))
            assert lunar_divisor_count(target) == predicted(n), (h,n)
            checks += 1
    assert lunar_divisor_count(15) == 5
    assert predicted(2) == 4
    print(f'VERIFY_OK: {checks} independent gap/length cases; h=2 boundary; seven formula values')

if __name__ == '__main__':
    main()
