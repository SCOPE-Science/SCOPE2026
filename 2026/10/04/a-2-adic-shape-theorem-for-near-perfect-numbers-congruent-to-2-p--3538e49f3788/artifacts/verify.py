#!/usr/bin/env python3
from math import isqrt

BOUND = 2_000_000
sigma = [0] * (BOUND + 1)
for d in range(1, BOUND + 1):
    for n in range(d, BOUND + 1, d):
        sigma[n] += d

def factor_odd(m):
    out = []
    p = 3
    while p * p <= m:
        if m % p == 0:
            a = 0
            while m % p == 0:
                m //= p
                a += 1
            out.append((p, a))
        p += 2
    if m > 1:
        out.append((m, 1))
    return out

near = 0
target = []
for n in range(2, BOUND + 1):
    d = sigma[n] - 2 * n
    if not (0 < d < n and n % d == 0):
        continue
    near += 1
    if n % 4 != 2:
        continue
    m = n // 2
    fac = factor_odd(m)
    odd_exp = [(p, a) for p, a in fac if a % 2]
    is_square = not odd_exp
    assert (d % 2 == 1) == is_square, (n, d, fac)
    if is_square:
        pass
    else:
        assert d % 4 == 2, (n, d, fac)
        assert len(odd_exp) == 1, (n, d, fac)
        p, a = odd_exp[0]
        assert p % 4 == 1 and a % 4 == 1, (n, d, fac)
    target.append(n)

assert target == [18, 234, 650], target
print(f"VERIFY_OK bound={BOUND} nearperfect={near} target={len(target)} target_values=" + ",".join(map(str,target)))
