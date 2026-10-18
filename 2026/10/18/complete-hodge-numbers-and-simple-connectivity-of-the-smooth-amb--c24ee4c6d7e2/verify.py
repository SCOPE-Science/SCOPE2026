#!/usr/bin/env python3
"""Exact integer checks of a Hodge-number formula; not a proof of the topological theorems."""
from math import comb

h = {(p, q): (comb(4, p) * comb(4, q) if (p-q) % 3 == 0 else 0)
             + (81 if p == q and p in (1,2,3) else 0)
     for p in range(5) for q in range(5)}
for p in range(5):
    for q in range(5):
        assert h[p,q] == h[q,p]
        assert h[p,q] == h[4-p,4-q]

expected_nonzero = {(0,0):1,(4,4):1,(0,3):4,(3,0):4,(1,4):4,(4,1):4,
                    (1,1):97,(3,3):97,(2,2):117}
assert {k:v for k,v in h.items() if v} == expected_nonzero
b = [sum(h[p,q] for p in range(5) for q in range(5) if p+q == k)
     for k in range(9)]
assert b == [1,0,97,8,117,8,97,0,1]
assert sum((-1)**k * value for k,value in enumerate(b)) == 297
assert sum((-1)**q * h[p,q] for p in range(5) for q in range(5)) == -75
assert sum((-1)**q * h[0,q] for q in range(5)) == -3
assert (243 + 2 * 324) // 3 == 297
assert 243 + 2 * 324 == 3 * 297
print('VERIFY_OK')
