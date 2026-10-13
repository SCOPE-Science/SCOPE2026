#!/usr/bin/env python3
"""Exact finite certificates for reciprocal-square divisor sums on cube-free integers.

The infinite-prime argument is mathematical (Nagura's theorem), not a
finite check; this script checks its seven small-prime base cases and
the rational comparisons in the nine-interval reduction.
"""
from fractions import Fraction as Q

F = lambda p: 1 + Q(1, p * p) + Q(1, p ** 4)

WITNESSES = {
    5: (7, 11, 13, 17, 19),
    7: (11, 13, 17, 19),
    11: (13, 17),
    13: (17, 19),
    17: (19, 23),
    19: (23, 29),
    23: (29, 31),
}
for p, ps in WITNESSES.items():
    product = Q(1)
    for q in ps:
        assert q > p
        assert all(q % d for d in range(2, int(q ** .5) + 1))
        product *= F(q)
    assert product > 1 + Q(1, p * p), (p, product)

# Archimedes' bounds 223/71 < pi < 22/7.
pi_lo, pi_hi = Q(223, 71), Q(22, 7)
T_coeff = Q(9720, 91)
T_lo, T_hi = T_coeff / pi_hi ** 4, T_coeff / pi_lo ** 4
assert T_lo > Q(200, 189)
assert T_hi < Q(10, 9)
assert Q(120) / pi_lo ** 4 < Q(5, 4)

f2 = (Q(1), Q(5, 4), Q(21, 16))
f3 = (Q(1), Q(10, 9), Q(91, 81))
c = [(f2[a] * f3[b], a, b) for a in range(3) for b in range(3)]
c.sort()
expected = [
    (Q(1), 0, 0), (Q(10, 9), 0, 1),
    (Q(91, 81), 0, 2), (Q(5, 4), 1, 0),
    (Q(21, 16), 2, 0), (Q(25, 18), 1, 1),
    (Q(455, 324), 1, 2), (Q(35, 24), 2, 1),
    (Q(1911, 1296), 2, 2),
]
assert c == expected

# Two connected blocks beyond isolated (0,0), by exact overlaps.
assert c[2][0] / c[1][0] < T_lo
for i in range(4, 9):
    assert c[i][0] / c[i-1][0] < T_lo
assert max(c[i][0] / c[i-1][0] for i in range(4, 9)) == Q(200, 189)
# Gaps after the 1st and 3rd interval, respectively.
assert T_hi < c[1][0]
assert c[2][0] * T_hi < c[3][0]
assert c[2][0] * T_coeff == Q(120)
assert c[8][0] * T_coeff == Q(315, 2)

# The cube-free conditional probabilities for the three components.
p2 = (Q(4, 7), Q(2, 7), Q(1, 7))
p3 = (Q(9, 13), Q(3, 13), Q(1, 13))
weights = (
    p2[0] * p3[0],
    p2[0] * (p3[1] + p3[2]),
    (p2[1] + p2[2]) * sum(p3),
)
assert weights == (Q(36, 91), Q(16, 91), Q(39, 91))
assert sum(weights) == 1

# A finite illustration, not used to prove the infinite result.
N = 100000
obs = [0, 0, 0]
total = 0
for n in range(1, N+1):
    m = n
    fac = {}
    p = 2
    while p*p <= m:
        if m % p == 0:
            a = 0
            while m % p == 0:
                m //= p
                a += 1
            fac[p] = a
        p = 3 if p == 2 else p+2
    if m > 1:
        fac[m] = fac.get(m, 0)+1
    if max(fac.values(), default=0) > 2:
        continue
    total += 1
    a, b = fac.get(2, 0), fac.get(3, 0)
    k = 0 if a == b == 0 else 1 if a == 0 else 2
    obs[k] += 1
print('EXACT_CERTIFICATE_OK',
      'finite_prime_witnesses=7',
      'local_intervals=9',
      'components=3',
      'conditional_weights=36/91,16/91,39/91',
      f'illustrative_cube_free_to_{N}={total}',
      f'illustrative_counts={obs}')
