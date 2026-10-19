#!/usr/bin/env python3
"""Exact finite consistency checks for quartic integer-spectrum witnesses."""
from math import gcd
from functools import reduce


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def rem(a, monic):
    v = a[:]
    while len(v) >= len(monic):
        v = trim(v)
        if len(v) < len(monic):
            break
        coef = v[-1]
        off = len(v) - len(monic)
        for j, q in enumerate(monic):
            v[off+j] -= coef*q
        trim(v)
    return v


def power_remainder(n, poly):
    value = [1]
    x = [0, 1]
    while n:
        if n & 1:
            value = rem(mul(value, x), poly)
        x = rem(mul(x, x), poly)
        n >>= 1
    return value


def phi(m):
    return sum(gcd(j,m) == 1 for j in range(1,m+1))


f2 = [ -2,0,1 ]
f3 = [4,-2,1]
f4 = [2,-2,1]
f6 = [3,-3,1]
f5 = [16,8,4,2,1]
f8 = [2,0,2,0,1]
f10 = [25,-25,15,-5,1]
f12 = [3,0,-3,0,1]
scalar = [ -2, 1 ]
witness = {
    1: [scalar, scalar, scalar, scalar],
    2: [f2,scalar,scalar],
    3: [f3,scalar,scalar],
    4: [f4,scalar,scalar],
    5: [f5],
    6: [f6,scalar,scalar],
    8: [f8],
    10: [f10],
    12: [f12],
}
count = 0
for expected, blocks in witness.items():
    assert sum(len(p)-1 for p in blocks) == 4
    count += 1
    exponent = next(k for k in range(1,121) if all(len(power_remainder(k,p))==1 for p in blocks))
    assert exponent == expected, (expected, exponent)
    count += 1
    assert 120 % expected == 0
    count += 1
    assert all(len(power_remainder(120,p)) == 1 for p in blocks)
    count += 1
assert power_remainder(5,f5) == [32]
assert power_remainder(8,f8) == [-4]
assert power_remainder(10,f10) == [3125]
assert power_remainder(12,f12) == [-27]
count += 4
lcm = reduce(lambda x,y:x*y//gcd(x,y), witness)
assert lcm == 120
count += 1
for d, targets in [
    (2, {3,4,6}),
    (4, {5,8,10,12}),
    (6, {7,9,14,18}),
    (8, {15,16,20,24,30}),
]:
    got = {m for m in range(1,201) if phi(m) == d}
    assert got == targets, (d, got)
    count += 1
assert {m for m in (15,16,20,24,30) if m % 4 == 0} == {16,20,24}
count += 1
print(f"PASS: {count} exact finite assertions; witness indices {sorted(witness)}; sharp lcm {lcm}")
