#!/usr/bin/env python3
"""Exact finite arithmetic checks for a three-sign random-walk theorem."""
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations, product
from math import factorial

# Derived by two elementary polynomial integrations:
# t = 4*integral_0^1 [(b(1-b)^4)/3 + (1-b)^5/4] db.
# Here integral b(1-b)^4 = 1/30 and integral (1-b)^5 = 1/6.
t = 4*(Q(1,3)*Q(1,30)+Q(1,4)*Q(1,6))
assert t == Q(19,90)


def table(t):
    assert 0 <= t < Q(1,3)
    return {'+++':Q(5,16),'++-':Q(1,16),
            '+-+':Q(1,16)-t/8,'+--':Q(1,16)+t/8,
            '-++':Q(1,16)+t/8,'-+-':Q(1,16)-t/8,
            '--+':Q(1,16),'---':Q(5,16)}

expected = table(t)
assert sum(expected.values()) == 1
assert all(v > 0 for v in expected.values())
assert {word:expected[word] for word in expected} == {
    '+++':Q(225,720),'++-':Q(45,720),'+-+':Q(26,720),
    '+--':Q(64,720),'-++':Q(64,720),'-+-':Q(26,720),
    '--+':Q(45,720),'---':Q(225,720)}

observed = Counter()
for p in permutations(range(6)):
    walk = 0
    sign_word = ''
    for j in range(5):
        walk += 1 if p[j] < p[j+1] else -1
        if j % 2 == 0:
            assert walk != 0
            sign_word += '+' if walk > 0 else '-'
    observed[sign_word] += 1
assert sum(observed.values()) == factorial(6)
assert all(Q(observed[w], factorial(6)) == expected[w] for w in expected)

simple_counts = Counter()
for steps in product((-1,1), repeat=5):
    walk = 0
    word = ''
    for j,increment in enumerate(steps):
        walk += increment
        if j % 2 == 0:
            assert walk != 0
            word += '+' if walk > 0 else '-'
    simple_counts[word] += 1
simple_table = {w:Q(simple_counts[w],32) for w in expected}
assert simple_table == table(Q(1,4))
total_variation = sum((abs(expected[w]-simple_table[w]) for w in expected),Q(0))/2
assert total_variation == Q(7,720)

# Both sign triple laws induce the universal three-step arcsine count law.
for tab in (expected, simple_table):
    occupation_counts = [sum((v for w,v in tab.items() if w.count('+')==k),Q(0))
                         for k in range(4)]
    assert occupation_counts == [Q(5,16), Q(3,16), Q(3,16), Q(5,16)]

# Check the symmetry, normalization and linear feasible family at rational parameters.
for q in (Q(0),Q(1,20),Q(1,6),Q(19,90),Q(1,4),Q(1,3)-Q(1,1000)):
    tab=table(q)
    assert sum(tab.values())==1
    assert tab['+++']==tab['---'] and tab['++-']==tab['--+']
    assert tab['+-+']==tab['-+-'] and tab['+--']==tab['-++']
print('PASS: triangular dominance 19/90; 720 permutation cases; 32 walk cases; TV 7/720; 6 family checks')
