"""Exact, standard-library-only checks for a five-plant conservation example."""
from fractions import Fraction
from itertools import product
from collections import Counter

POLLINATORS = ('A', 'B', 'F1', 'F2', 'F3', 'F4', 'F5')
PLANTS = {
    'P1': ('A',),
    'P2': ('B', 'F1'),
    'P3': ('B', 'F2'),
    'P4': ('A', 'F1', 'F2', 'F3', 'F4', 'F5'),
    'P5': ('A', 'F1', 'F2', 'F3', 'F4', 'F5'),
}

def gain_poly(target):
    out = Counter()
    for neighbors in PLANTS.values():
        if target in neighbors:
            out[len(neighbors) - 1] += 1
    return {degree: count for degree, count in out.items() if count}

def polynomial_value(poly, q):
    return sum(Fraction(v) * q**k for k,v in poly.items())

def exact_expected_count(q, guaranteed=None):
    remaining = tuple(x for x in POLLINATORS if x != guaranteed)
    result = Fraction(0)
    for bits in product((0, 1), repeat=len(remaining)):
        alive = {guaranteed} if guaranteed is not None else set()
        weight = Fraction(1)
        for name, bit in zip(remaining, bits):
            if bit:
                alive.add(name)
                weight *= 1-q
            else:
                weight *= q
        result += weight*sum(bool(alive.intersection(neigh)) for neigh in PLANTS.values())
    return result

A = gain_poly('A')
B = gain_poly('B')
assert A == {0:1, 5:2}, A
assert B == {1:2}, B
for f in ('F1','F2'):
    assert gain_poly(f) == {1:1, 5:2}
for f in ('F3','F4','F5'):
    assert gain_poly(f) == {5:2}

for q in (Fraction(1,4), Fraction(3,4), Fraction(9,10)):
    baseline = exact_expected_count(q)
    scores = {}
    for target in POLLINATORS:
        rescued = exact_expected_count(q, guaranteed=target) - baseline
        expected = polynomial_value(gain_poly(target),q)
        assert rescued == q*expected, (q,target,rescued,expected)
        scores[target] = rescued/q
    f = scores['A']-scores['B']
    assert f == 1-2*q+2*q**5
    assert (f>0)==(q != Fraction(3,4))
    winner=max(scores,key=scores.get)
    assert winner==('B' if q==Fraction(3,4) else 'A'),(q,winner,scores)
    print('q=',q,'normalized_gains=',scores,'A-B=',f,'winner=',winner)
assert (1-2*Fraction(3,4)+2*Fraction(3,4)**5)==-Fraction(13,512)
# Analytical uniqueness: derivative -2+10q^4 has exactly one zero on (0,1).
# Endpoints f(0)=f(1)=1, while f(3/4)=-13/512: exactly two internal zeros.
print('All seven symbolic gain identities and 3 x 7 exact enumeration checks passed.')
