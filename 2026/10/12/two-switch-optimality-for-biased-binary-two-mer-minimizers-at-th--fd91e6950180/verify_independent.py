#!/usr/bin/env python3
"""Independent boundary-event enumeration for Bernoulli binary two-mer minimizers.
Standard-library cross-check; uses endpoint replacement, not two argmin positions.
"""
from itertools import product, permutations
from fractions import Fraction

ranks = tuple(permutations(('00','01','10','11')))
A = ('01','00','10','11')
B = ('11','01','00','10')

def profile(ordered, w):
    order = {mer:j for j,mer in enumerate(ordered)}
    result = [0]*(w+3)
    for x in product('01', repeat=w+2):
        s=''.join(x)
        mers = [s[i:i+2] for i in range(w+1)]
        old = min(range(w), key=lambda j:(order[mers[j]],j))
        # A changed minimizer is charged iff the old choice departs at the
        # left boundary, or the newly arriving mer outranks the old choice.
        charged = old == 0 or order[mers[-1]] < order[mers[old]]
        if charged: result[s.count('1')] += 1
    return tuple(result)

def value(coef,p):
    m=len(coef)-1
    return sum(c*p**r*(1-p)**(m-r) for r,c in enumerate(coef))

for w in range(2,10):
    profiles={ordered:profile(ordered,w) for ordered in ranks}
    assert sum(profiles[A])>0
    for p in (Fraction(1,10),Fraction(1,4),Fraction(3,10),Fraction(2,5),Fraction(49,100)):
        optimum=min(value(coef,p) for coef in profiles.values())
        expect=min(value(profiles[A],p),value(profiles[B],p)) if w==9 else value(profiles[A],p)
        assert optimum == expect,(w,p,optimum,expect)
    print('independent endpoint enumeration w',w,'PASS')
assert profile(A,9)==(1,2,10,37,85,127,127,85,37,11,3,1)
assert profile(B,9)==(1,2,11,38,77,109,131,126,84,36,9,1)
assert value(profile(B,9),Fraction(3,10)) < value(profile(A,9),Fraction(3,10))
assert value(profile(A,9),Fraction(2,5)) < value(profile(B,9),Fraction(2,5))
print('INDEPENDENT_REPLAY_PASSED')
