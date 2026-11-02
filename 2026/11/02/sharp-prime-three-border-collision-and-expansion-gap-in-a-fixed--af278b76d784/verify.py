"""Exact symbolic and finite rational tests for the four-branch map's three-cycle census.

Run with Python 3 and SymPy. The universal classification is proved in RESULT.md;
finite tests here check algebra and guard against branch-endpoint mistakes.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as sp

r, s = sp.symbols('r s', positive=True)
D = r*s**2-1
x = r*(s**2-s+1)/D
y = sp.factor(s*(x-1))
z = sp.factor(s*(y+1))
K = r*(s-1)-1
assert sp.simplify(r*(z-1)-x) == 0
for val, expected in [
    (1-x, K/D), (-y, s*K/D), (s-z, s**2*K/D),
    (y+1, (r*s+s-1)/D), (z-1, (s**2-s+1)/D),
]:
    assert sp.simplify(val-expected) == 0


def evaluate(value, rr, ss):
    if -ss <= value <= -1:
        return 0, rr*(value+1)
    if -1 < value < 0:
        return 1, ss*(value+1)
    if 0 <= value < 1:
        return 2, ss*(value-1)
    if 1 <= value <= ss:
        return 3, rr*(value-1)
    raise ValueError('state outside invariant interval')


def enumerate_prime_three(rr, ss):
    """Exhaustively solve 64 affine itinerary equations at rational test parameters."""
    branches = [(rr,rr), (ss,ss), (ss,-ss), (rr,-rr)]
    cycles = set()
    verified_words = 0
    for word in product(range(4), repeat=3):
        A, B = Q(1), Q(0)
        for i in word:
            a, b = branches[i]
            A, B = a*A, a*B+b
        if A == 1:
            assert B != 0, 'possible continuum requires separate handling'
            continue
        point = B/(1-A)
        states, state, admissible = [], point, True
        for expected_branch in word:
            if state < -ss or state > ss:
                admissible = False
                break
            actual_branch, next_state = evaluate(state,rr,ss)
            if actual_branch != expected_branch:
                admissible = False
                break
            states.append(state)
            state = next_state
        if admissible and state == point:
            assert len(set(states)) == 3, 'no fixed point allowed'
            cycles.add(tuple(sorted(states)))
            verified_words += 1
    assert verified_words == 3*len(cycles)
    return cycles

samples = [(Q(1,2),Q(2)),(Q(1,2),Q(3)),(Q(4,5),Q(5)),
           (Q(1,5),Q(4)),(Q(1,4),Q(6)),(Q(9,10),Q(11,5)),
           (Q(3,4),Q(7,3)),(Q(1,10),Q(100)),(Q(4,5),Q(9,4)),
           (Q(1,3),Q(4)),(Q(1,3),Q(7,2)),(Q(1,3),Q(5))]
for rr, ss in samples:
    k = rr*(ss-1)
    expected = 0 if k < 1 else 1 if k == 1 else 2
    cycles = enumerate_prime_three(rr, ss)
    assert len(cycles) == expected, (rr,ss,expected,cycles)
    if k > 1:
        xx = Q(rr*(ss**2-ss+1), rr*ss**2-1)
        yy,zz = ss*(xx-1),ss*(ss*(xx-1)+1)
        assert tuple(sorted([xx,yy,zz])) in cycles
        assert tuple(sorted([-xx,-yy,-zz])) in cycles
        assert rr*ss**2 > 1
    if k == 1:
        assert tuple(sorted([Q(0),-ss,Q(-1)])) in cycles
print(f'PASS: 5 symbolic identities and {len(samples)*64} rational itinerary trials across {len(samples)} parameter choices')
