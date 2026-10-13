"""Exact symbolic verification of a four-population, two-trial selection identity.

Requires only Python 3 standard library. All coefficient arithmetic uses Fraction.
The tie-breaking calculation independently enumerates the 24 strict rankings.
"""
from fractions import Fraction
from itertools import product, permutations
from math import comb

ZERO = {}

def C(c):
    c = Fraction(c)
    return {(0, 0): c} if c else {}

def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
        if not out[k]:
            del out[k]
    return out

def neg(a):
    return {k: -v for k, v in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, Fraction(0)) + v * w
    return {k: v for k, v in out.items() if v}

def power(a, n):
    out = C(1)
    for _ in range(n):
        out = mul(out, a)
    return out

def scale(a, c):
    return mul(a, C(c))

def evaluate(a, delta, shift):
    delta, shift = Fraction(delta), Fraction(shift)
    return sum((v * delta**i * shift**j for (i, j), v in a.items()), Fraction(0))

def weights(x):
    return [power(sub(C(1), x), 2),
            scale(mul(x, sub(C(1), x)), 2), power(x, 2)]

D = {(1, 0): Fraction(1)}
H = {(0, 1): Fraction(1)}
p = add(scale(sub(C(1), D), Fraction(1, 2)), H)
q = add(scale(add(C(1), D), Fraction(1, 2)), H)
lo, hi = weights(p), weights(q)

rankings = tuple(permutations(range(4)))

def fair_success_probability(scores):
    wins = 0
    for order in rankings:
        placement = {index: order.index(index) for index in range(4)}
        selected = sorted(range(4), key=lambda index: (-scores[index], placement[index]))[:2]
        wins += set(selected) == {0, 1}
    return Fraction(wins, 24)

computed = C(0)
number_nonzero = 0
for g1, g2, l1, l2 in product(range(3), repeat=4):
    chance = fair_success_probability((g1, g2, l1, l2))
    if not chance:
        continue
    number_nonzero += 1
    law = mul(mul(hi[g1], hi[g2]), mul(lo[l1], lo[l2]))
    computed = add(computed, scale(law, chance))

central = scale(mul(power(add(C(1), D), 4),
                    add(add(sub(power(D, 3), scale(power(D, 2), 4)),
                            scale(D, -7)), C(16))), Fraction(1, 96))
# bracket = 29+64d+38d^2-3d^4-(84-12d^2)h^2-16h^4
bracket = add(add(add(C(29), scale(D, 64)),
                  sub(scale(power(D, 2), 38), scale(power(D, 4), 3))),
              add(neg(mul(sub(C(84), scale(power(D, 2), 12)), power(H, 2))),
                  scale(power(H, 4), -16)))
expected = add(central, scale(mul(mul(D, power(H, 2)), bracket), Fraction(1, 24)))
assert computed == expected, 'Exact coefficient identity failed'
assert len(computed) > 0 and number_nonzero > 0
assert evaluate(computed, 0, 0) == Fraction(1, 6)
assert evaluate(computed, 1, 0) == Fraction(1)
for dd in [Fraction(1, 10), Fraction(2, 5), Fraction(3, 4)]:
    for z in [Fraction(0), (1-dd)/2, -(1-dd)/2, (1-dd)/4]:
        assert evaluate(computed, dd, z) >= evaluate(central, dd, 0)
print('PASS: independent 24-ranking/81-count enumeration; full polynomial identity; boundary tests')
print('nonzero count configurations:', number_nonzero)
print('nonzero monomials:', len(computed))
