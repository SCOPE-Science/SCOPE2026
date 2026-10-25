#!/usr/bin/env python3
"""Exact arithmetic checks for the characteristic-five example in RESULT.md."""
from math import comb, gcd

p = 5

def add_poly(a, b, p):
    out = dict(a)
    for e, c in b.items():
        out[e] = (out.get(e, 0) + c) % p
        if out[e] == 0:
            del out[e]
    return out

def shift_power(a, n, p):
    """Coefficients of (a+u)^n over F_p, keyed by exponent of u."""
    return {j: (comb(n, j) * pow(a, n-j, p)) % p
            for j in range(n+1)
            if (comb(n, j) * pow(a, n-j, p)) % p != 0}

def semigroup_gap_count(a, b):
    assert gcd(a, b) == 1
    conductor = (a-1)*(b-1)
    represented = {i*a + j*b for i in range(conductor//a + 2)
                   for j in range(conductor//b + 2)
                   if i*a + j*b < conductor}
    return sum(n not in represented for n in range(conductor))

# h(t)=t^5+t^2+t. Its derivative is 2t+1 in characteristic five.
assert (2*2 + 1) % p == 0
assert (pow(2, 5, p) + pow(2, 2, p) + 2) % p == 3
# The derivative has no other root, and h(2) != 0; f(1,0)=1,
# so the degree-five binary form has five distinct roots.
assert (pow(2, 5, p) + 2*2 + 2) % p != 0

# Expansion at t=2: h(2+u)=3+u^2+u^5.
expansion = add_poly(add_poly(shift_power(2, 5, p),
                              shift_power(2, 2, p), p),
                     shift_power(2, 1, p), p)
assert expansion == {0: 3, 2: 1, 5: 1}, expansion

# At infinity, g(s)=f(1,s)=1+s^3+s^4; g'(s)=s^2(3+4s).
assert (3 + 4*0) % p == 3
assert (3 + 4*3) % p == 0
assert semigroup_gap_count(2, 5) == 2
assert semigroup_gap_count(3, 5) == 4
assert (2-1) + (3-1) == p-2
assert (p-1)*(p-2)//2 == 6
assert 2 + 4 == 6
print("VERIFY_OK: squarefree quintic; critical orders 2,3; delta sum 6")
