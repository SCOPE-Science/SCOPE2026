#!/usr/bin/env python3
"""Exact standard-library checks for even-window Fibonacci/Lucas cubic GCD laws."""
from math import gcd


def fibonacci(n):
    if n < 0:
        return (1 if (-n) % 2 else -1) * fibonacci(-n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    if n < 0:
        return (1 if (-n) % 2 == 0 else -1) * lucas(-n)
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sign(z):
    return 1 if z % 2 == 0 else -1


def B(t, z):
    return t * (lucas(3*z) + lucas(3*z-3)) - 12 * sign(z) * (lucas(z-1) - lucas(z))


def C(t, z):
    return t * (fibonacci(3*z) + fibonacci(3*z-3)) + 12 * sign(z) * (fibonacci(z-1) - fibonacci(z))


assert [B(0, z) for z in range(4)] == [36, 12, 24, -12]
assert [B(1, z) - B(0, z) for z in range(4)] == [-2, 6, 22, 94]
assert [C(0, z) for z in range(4)] == [12, 12, 0, 12]
assert [C(1, z) - C(0, z) for z in range(4)] == [2, 2, 10, 42]
for t in range(-100, 101):
    assert gcd(*(B(t,z) for z in range(4))) == 2*gcd(t-18, 30)
    assert gcd(*(C(t,z) for z in range(4))) == 2*gcd(t+6, 30)
    for W in (B,C):
        for z in range(-9,10):
            assert W(t,z+4) == 3*W(t,z+3)+6*W(t,z+2)-3*W(t,z+1)-W(t,z)
print('PASS: four-value integer templates, exact GCD reductions, invertible fourth-order recurrence')

for m in range(1,81):
    fm, lm = fibonacci(m), lucas(m)
    base = (fm if m%2==0 else lm)
    expected_f = (base * (3 if m%4==0 else 1)) // (2 if m%3==0 else 1)
    expected_l = expected_f * (5 if m%2==0 else 1)
    assert expected_f == (fm*gcd(fm*fm-3,6)//2 if m%2==0 else lm*gcd(lm*lm-15,6)//2)
    assert expected_l == (5*fm*gcd(fm*fm-3,6)//2 if m%2==0 else lm*gcd(lm*lm-15,6)//2)
    for tag, seq, wanted in [('F',fibonacci,expected_f),('L',lucas,expected_l)]:
        vals = []
        for n in range(8):
            val=sum(seq(n+j)**3 for j in range(1,2*m+1))
            vals.append(val)
            z=n+m+1
            if tag=='F' and m%2==0: lhs,rhs=20*val,fm*B(5*fm*fm+3,z)
            elif tag=='F': lhs,rhs=20*val,lm*C(lm*lm+3,z)
            elif m%2==0: lhs,rhs=4*val,5*fm*C(5*fm*fm+3,z)
            else: lhs,rhs=4*val,lm*B(lm*lm+3,z)
            assert lhs==rhs, (tag,m,n)
        assert gcd(*vals[:4])==wanted, (tag,m)
        assert all(val%wanted==0 for val in vals)
print('PASS: all four exact summation identities and direct GCDs, lengths 2..160 and starts 0..7')
