#!/usr/bin/env python3
"""Exact finite check for the iterated unitary-sigma multiplier-four result."""

from sympy import factorint, primerange

def usigma(n: int) -> int:
    out = 1
    for p, e in factorint(n).items():
        out *= p**e + 1
    return int(out)

def usigma2(n: int) -> int:
    return usigma(usigma(n))

solutions = []
checked = 0
for a in range(1, 17):
    for p in primerange(3, 500):
        for b in range(1, 8):
            n = (2**a) * (int(p)**b)
            checked += 1
            if usigma2(n) == 4*n:
                solutions.append((a, int(p), b, n))

assert solutions == [(1, 3, 2, 18)]
assert usigma(18) == 30
assert usigma(30) == 72

print(f"checked_triples={checked}")
print(f"solutions={solutions}")
print(f"usigma(18)={usigma(18)}")
print(f"usigma(usigma(18))={usigma2(18)}")
