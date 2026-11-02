"""Independent truth-table test for the nine-element Heyting example."""
from itertools import product

# Three incomparable minimal points 0,1,2, all below the apex 3.
ideals = [frozenset(s) for k in range(4) for s in __import__('itertools').combinations(range(3), k)]
ideals.append(frozenset(range(4)))
all_points = frozenset(range(4))
assert len(ideals) == 9

def meet(a, b):
    return a & b

def join(a, b):
    return a | b

def implication(a, b):
    return max((c for c in ideals if meet(c, a) <= b), key=len)

a = frozenset({0, 1})
neg = implication(a, frozenset())
mat = {b for b in ideals if implication(a, b) == join(neg, b)}
expected = {frozenset(), frozenset({0}), frozenset({1}), frozenset({2}),
            frozenset({0,2}), frozenset({1,2}), all_points}
assert mat == expected, (mat, expected)
assert frozenset({0}) | frozenset({1}) not in mat

def internal_join(x, y):
    return min((z for z in mat if x <= z and y <= z), key=len)

x, y, z = frozenset({2}), frozenset({0}), frozenset({1})
assert meet(x, internal_join(y,z)) == x
assert internal_join(meet(x,y), meet(x,z)) == frozenset()
print('NINE_ELEMENT_NON_DISTRIBUTIVE_MATERIALIZER_PASS H=9 M=7')
