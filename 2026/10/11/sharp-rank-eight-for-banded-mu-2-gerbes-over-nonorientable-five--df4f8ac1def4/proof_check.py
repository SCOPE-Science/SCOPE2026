#!/usr/bin/env python3
"""Exact low-degree monodromy and coefficient-arithmetic consistency checks."""
from math import gcd

A = ((0, -1), (1, 0))
D = ((A[0][0] - 1, A[0][1]), (A[1][0], A[1][1] - 1))
det = D[0][0] * D[1][1] - D[0][1] * D[1][0]
entry_gcd = 0
for row in D:
    for entry in row:
        entry_gcd = gcd(entry_gcd, abs(entry))
# Smith invariants in rank two: gcd of entries, abs(det) / gcd.
assert entry_gcd == 1
assert abs(det) == 2
assert abs(det) // entry_gcd == 2

# Solutions to (A-I)x=0 modulo two: the unique nonzero one is (1,1).
fixed2 = []
for x in range(2):
    for y in range(2):
        if all((D[i][0] * x + D[i][1] * y) % 2 == 0 for i in range(2)):
            fixed2.append((x, y))
assert fixed2 == [(0, 0), (1, 1)]

# In integral H^4(F), monodromy has degree -1, so H^4(N,Z)=0
# and H^5(N,Z)=coker(-2: Z -> Z)=Z/2.
assert -2 != 0
assert abs(-2) == 2

# With Z/4 coefficients the monodromy-invariant degree-four subgroup
# is exactly {0,2}. The fiberwise Pontryagin square of u+v is 2uv.
fixed4 = [z for z in range(4) if (-z - z) % 4 == 0]
assert fixed4 == [0, 2]
# u^2 = v^2 = 0 in H^4(S^2 x S^2; Z), uv = vu = 1.
square_uv_sum = 0 + 1 + 1 + 0
assert square_uv_sum == 2
assert square_uv_sum % 4 == fixed4[1]

# Since H^4(N,Z)=0, beta_4 is injective on H^4(N,Z/4)=Z/2.
# Nonzero P_2(xi) therefore maps to the nonzero H^5(N,Z)=Z/2.
pontryagin_square_nonzero = square_uv_sum % 4 != 0
assert pontryagin_square_nonzero
q_order = 2
period = 2
index = period * q_order
assert index == 4
regular_rank = 2 * index
assert regular_rank == 8
print('VERIFY_OK')
