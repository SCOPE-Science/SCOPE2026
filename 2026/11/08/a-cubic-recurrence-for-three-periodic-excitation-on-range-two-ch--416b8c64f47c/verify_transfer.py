#!/usr/bin/env python3
"""Exact finite transfer certificate for 3-period Greenberg-Hastings states on path squares."""
from itertools import product

S = list(product(range(3), repeat=4))
index = {s: k for k, s in enumerate(S)}
assert len(S) == 81

def has_successor(x, neighbors):
    return (x + 1) % 3 in neighbors

left = [int(has_successor(a, (b, c)) and has_successor(b, (a, c, d)))
        for a, b, c, d in S]
right = [int(has_successor(c, (a, b, d)) and has_successor(d, (b, c)))
         for a, b, c, d in S]
edges = [[index[(b, c, d, e)] for e in range(3)
          if has_successor(c, (a, b, d, e))] for a, b, c, d in S]

def matvec(v):
    return [sum(v[j] for j in edges[i]) for i in range(81)]

R1 = matvec(right)
R2 = matvec(R1)
R3 = matvec(R2)
assert all(R3[i] == 3 * R2[i] - 2 * R1[i] + 2 * right[i]
           for i in range(81)), "Exact cubic transfer relation failed"
print('EXACT_MATRIX_IDENTITY: (M^3-3M^2+2M-2I)r=0, all 81 entries')
print('27 representative 4-step terminal profiles (a=0):')
for i, (a, b, c, d) in enumerate(S):
    if a == 0:
        print(f'{b}{c}{d}: {right[i]},{R1[i]},{R2[i]},{R3[i]}')

r = right
counts = {3: 6}
for n in range(4, 41):
    counts[n] = sum(u*v for u,v in zip(left,r))
    if n >= 6:
        assert counts[n] == 3*counts[n-1]-2*counts[n-2]+2*counts[n-3]
    r = matvec(r)
assert [counts[n] for n in range(3, 12)] == [6,18,42,102,258,654,1650,4158,10482]
print('TRANSFER_COUNTS_n3_to_n12:', [counts[n] for n in range(3, 13)])
print('RECURRENCE_VERIFIED: n=6..40')
print('PASS')
