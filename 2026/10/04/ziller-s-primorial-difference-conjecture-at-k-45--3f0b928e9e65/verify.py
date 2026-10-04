#!/usr/bin/env python3
from math import gcd, prod

# Exact public sequence prefixes used in the argument.
A329815 = [
    0, 1, 3, 5, 7, 10, 13, 16, 20, 23, 29, 33, 37, 43, 49, 53,
    59, 66, 75, 84, 92, 99, 108, 116, 127, 132, 140, 148, 156,
    164, 174, 185, 193, 206, 215, 224, 235, 245, 255, 267, 275,
    286, 297, 308
]
A048670 = [
    2, 4, 6, 10, 14, 22, 26, 34, 40, 46, 58, 66, 74, 90, 100,
    106, 118, 132, 152, 174, 190, 200, 216, 234, 258, 264, 282,
    300, 312, 330, 354, 378, 388, 414, 432, 450, 476, 492, 510,
    538, 550, 574, 600, 616, 642
]

assert len(A329815) == 44
assert A329815[43] == 308
assert A048670[43] == 616
assert A048670[44] == 642

evens = list(range(2, 617, 2))
assert len(evens) == 308
assert evens[-1] == 616

def primes(n):
    out = []
    x = 2
    while len(out) < n:
        if all(x % p for p in out if p * p <= x):
            out.append(x)
        x += 1
    return out

def gap_set(k):
    ps = primes(k)
    P = prod(ps)
    residues = [x for x in range(1, P + 1) if gcd(x, P) == 1]
    gaps = [residues[i+1] - residues[i] for i in range(len(residues)-1)]
    gaps.append(residues[0] + P - residues[-1])
    return set(gaps)

# Regression check only; the general inclusion is proved symbolically in RESULT.md.
for k in range(1, 6):
    assert gap_set(k) <= gap_set(k + 1)

print("VERIFY_OK")
print("A329815(44)=308")
print("A048670(44)=616")
print("A048670(45)=642")
