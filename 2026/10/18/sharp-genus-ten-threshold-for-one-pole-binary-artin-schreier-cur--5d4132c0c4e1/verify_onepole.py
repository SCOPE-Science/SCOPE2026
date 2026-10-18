#!/usr/bin/env python3
"""Finite-field certificates for the degree-six point obstruction (standard library)."""
MOD = 0b1000011  # t^6+t+1 irreducible over F2

def mul(a, b):
    out = 0
    while b:
        if b & 1: out ^= a
        a <<= 1
        if a & 64: a ^= MOD
        b >>= 1
    return out

def power(a, n):
    res = 1
    while n:
        if n & 1: res = mul(res, a)
        a = mul(a, a)
        n >>= 1
    return res

def trace(a, n=6):
    s = 0
    for _ in range(n):
        s ^= a
        a = mul(a, a)
    assert s in (0, 1)
    return s

def frob_orbit(a):
    out = []
    while a not in out:
        out.append(a)
        a = mul(a, a)
    return out

# Verify the chosen field has 64 elements and the defining sextic is irreducible.
assert all(len(frob_orbit(a)) == 6 for a in [2])
assert power(2, 63) == 1 and all(power(2, 63//d) != 1 for d in (3, 7))
closed = [(len(frob_orbit(a)), a) for a in range(64)
          if a == min(frob_orbit(a))]
D3 = [a for d, a in closed if d == 3]
D6 = [a for d, a in closed if d == 6]
assert D3 == [14, 15], D3
assert D6 == [2, 3, 6, 7, 32, 33, 34, 40, 41], D6

# Dual certificate: these seven degree-6 base places define a linear functional
# that annihilates every monomial x^j for 0 <= j <= 20.
seven = [3, 6, 7, 32, 33, 34, 40]
assert all(a in D6 for a in seven)
assert [sum(trace(power(a, j)) for a in seven) % 2
        for j in range(22)] == [0] * 21 + [1]

# At degree 21, f = x^21 + x^7 has trace one at all degree-six
# places and trace zero at both degree-three places.
def f(a): return power(a, 21) ^ power(a, 7)
assert [trace(f(a)) for a in D6] == [1] * 9
assert [trace(f(a)) for a in D3] == [0] * 2

N = {}
for n in (1, 2, 3, 6):
    elems = [a for a in range(64) if power(a, 2**n) == a]
    assert len(elems) == 2**n
    N[n] = 1 + 2 * sum(trace(f(a), n) == 0 for a in elems)
assert N == {1: 5, 2: 5, 3: 17, 6: 17}, N
assert (N[6] - N[3] - N[2] + N[1]) // 6 == 0
print('PASS: degree-6 representatives', D6)
print('PASS: dual certificate', seven, 'annihilates degrees 0..20')
print('PASS: genus-10 witness y^2+y=x^21+x^7')
print('PASS: point counts', N, 'closed degree-six count 0')
