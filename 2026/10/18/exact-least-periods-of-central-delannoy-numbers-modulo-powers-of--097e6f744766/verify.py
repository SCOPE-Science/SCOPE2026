#!/usr/bin/env python3
"""Exact arithmetic sanity checks for central Delannoy periods."""
from math import comb

def Dmod(n, r):
    m = 1 << r
    return sum(((1 << k) * comb(n, k) ** 2) for k in range(min(n + 1, r))) % m

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

def expected(r):
    return (1, 2, 4, 4)[r - 1] if r <= 4 else 1 << (r - 2)

for r in range(1, 13):
    h = expected(r)
    for n in range(min(2*h, 1400)):
        assert Dmod(n+h, r) == Dmod(n, r), (r, n, 'period')
    if h > 1:
        witness = 0 if r <= 4 else 1
        assert Dmod(witness+h//2, r) != Dmod(witness, r), (r, 'half-period')
for s in range(2, 13):
    for j in range(1, (1 << s) + 1):
        assert v2(comb(1 << s, j)) == s-v2(j)
for t in range(3, 10):
    h = 1 << t
    for k in range(2, h+2):
        assert v2(comb(h+1, k)) == t-v2(k*(k-1))
        assert k - 2*v2(k*(k-1)) >= 0
    assert v2(Dmod(h+1, t+5)-Dmod(1, t+5) if Dmod(h+1, t+5)>Dmod(1, t+5) else Dmod(h+1,t+5)-Dmod(1,t+5)+(1<<(t+5))) == t+2
print('VERIFY_OK: periods r=1..12; shift-binomial valuations s=2..12; sharpness t=3..9')
