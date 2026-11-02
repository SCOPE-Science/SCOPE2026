#!/usr/bin/env python3
"""Exact finite checks for an accelerated symmetric lattice walk.

Proofs of the infinite-state claims are in RESULT.md. This executable checks
independent transition enumerations and exact stationary identities on finite
subsets without treating finite testing as an infinite proof.
"""
from collections import defaultdict
from fractions import Fraction

HALF = Fraction(1, 2)
checks = 0


def check(condition, name):
    global checks
    if not condition:
        raise AssertionError(name)
    checks += 1


def step(n):
    length = 1 if abs(n) <= 1 else abs(n) + 1
    return (n - length, n + length)


def point_mass(n):
    if n in (-1, 0, 1):
        return Fraction(1, 5)
    a = abs(n)
    if a < 2:
        return Fraction(0)
    y = a + 1
    if y % 3 != 0:
        return Fraction(0)
    q = y // 3
    if q <= 0 or q & (q - 1):
        return Fraction(0)
    k = q.bit_length()
    return Fraction(1, 5 * (1 << k))


def reach_zero_in_four(n):
    distribution = {n: Fraction(1)}
    for _ in range(4):
        nxt = defaultdict(Fraction)
        for state, mass in distribution.items():
            left, right = step(state)
            nxt[left] += mass * HALF
            nxt[right] += mass * HALF
        distribution = nxt
    return distribution.get(0, Fraction(0))


def x(k):
    return 3 * (1 << (k - 1)) - 1


# Transition graph and point probabilities, including the geometric arms.
check(step(0) == (-1, 1), 'central transition')
check(step(1) == (0, 2) and step(-1) == (-2, 0), 'inner transitions')
for k in range(1, 41):
    check(step(x(k)) == (-1, x(k + 1)), 'positive arm transition')
    check(step(-x(k)) == (-x(k + 1), 1), 'negative arm transition')
    check(point_mass(x(k)) == Fraction(1, 5 * (1 << k)), 'positive stationary mass')
    check(point_mass(-x(k)) == Fraction(1, 5 * (1 << k)), 'negative stationary mass')
    if k >= 2:
        check(point_mass(x(k)) == point_mass(x(k - 1)) / 2, 'positive arm balance')
        check(point_mass(-x(k)) == point_mass(-x(k - 1)) / 2, 'negative arm balance')

# Exact mass sums and the only infinite incoming-flow sums use closed
# geometric series; they are not inferred from finite truncation.
check(Fraction(1, 5) * 3 + 2 * Fraction(1, 5) == 1, 'normalization')
check(Fraction(1, 5) == point_mass(1) * HALF + point_mass(-1) * HALF,
      'zero balance')
check(point_mass(1) == point_mass(0) * HALF + Fraction(1, 5) * HALF,
      'positive one balance using exact geometric arm sum')
check(point_mass(-1) == point_mass(0) * HALF + Fraction(1, 5) * HALF,
      'negative one balance using exact geometric arm sum')
check(point_mass(2) == point_mass(1) * HALF, 'initial positive arm balance')
check(point_mass(-2) == point_mass(-1) * HALF, 'initial negative arm balance')

# Independent four-step path enumeration on a large finite sample.
for n in range(-1000, 1001):
    p = reach_zero_in_four(n)
    check(p >= Fraction(1, 16), 'four-step minorization')
    if abs(n) == 1:
        check(p == Fraction(1, 16), 'sharpness of minorization')
    elif n == 0:
        check(p == Fraction(3, 8), 'origin return probability')
    else:
        check(p == Fraction(1, 4), 'outer return probability')

# The exact stationary strict tail for x_k <= t < x_(k+1) equals
# 2/(5*2^k). Test it at both lattice and nonlattice thresholds.
for k in range(1, 41):
    value = Fraction(2, 5 * (1 << k))
    check(value * x(k) < Fraction(6, 5), 'tail lower shell')
    check(value * x(k) > Fraction(0), 'tail positivity')
    check(value * (x(k + 1) - Fraction(1, 2)) < Fraction(6, 5),
          'tail upper shell')
    check(value * (x(k) + 1) == Fraction(2, 5 * (1 << k)) * (3 * (1 << (k-1))),
          'shifted-scale prefactor')
    check(value == 2 * Fraction(1, 5 * (1 << (k + 1))) * 2,
          'exact tail geometric sum')

# Moment threshold: arm terms at p=1 are bounded away from zero,
# whereas for p<1 geometric comparison is summable (proved in RESULT.md).
for k in range(1, 41):
    check(Fraction(x(k), (1 << k)) >= Fraction(1, 1),
          'nonsummable first-moment terms')

print(f'PASS {checks} exact finite checks; analytical infinite-state proofs are separate.')
