#!/usr/bin/env python3
"""Integer verification of the finite transition certificate and sharp witness.
The universal mathematical argument is in RESULT.md.
"""
from itertools import product

POTENTIAL = (
    (0, 0, 0, 4),
    (4, 0, 3, 6),
    (10, 4, 0, 4),
    (13, 6, 3, 0),
    (10, 4, 0, 0),
    (3, 0, 0, 0),
)

def potential(g, diff):
    return POTENTIAL[abs(diff)][g] if abs(diff) < 6 else 0

def test_transition_certificate():
    tests = 0
    for g in range(4):
        for d in range(-8, 9):
            for value in (1, 2, 3):
                for direction in (-1, 1):
                    gn = abs(g-value)
                    dn = d + direction*value
                    assert 3*gn-5*abs(dn)+potential(gn,dn) <= potential(g,d), (g,d,value,direction)
                    tests += 1
    # For |d| >= 9, |d'| >= 6, both potentials vanish,
    # and 3g'-5|d'| <= 9-30 < 0 analytically.
    assert potential(0,0) == 0
    assert all(x >= 0 for row in POTENTIAL for x in row)
    return tests

def optimum_by_independent_dynamic_program(values):
    costs = {0:0}
    for value in values:
        new = {}
        for signed_delta, accumulated in costs.items():
            for sign in (-1, 1):
                d = signed_delta + sign*value
                c = accumulated + abs(d)
                if d not in new or c < new[d]: new[d] = c
        costs = new
    return min(costs.values())

def greedy_by_loads(values):
    a=b=0
    total=0
    for v in values:
        if a <= b: a += v
        else: b += v
        total += abs(a-b)
    return total

def test_exhaustive():
    total=0
    for length in range(1,10):
        for seq in product((1,2,3), repeat=length):
            G=greedy_by_loads(seq)
            O=optimum_by_independent_dynamic_program(seq)
            assert 3*G <= 5*O,(seq,G,O)
            total+=1
    return total

def test_sharp_family():
    for r in range(0,501):
        seq=(1,1,3,1)+(2,3,1)*r
        assert greedy_by_loads(seq)==6+5*r
        # Explicit signed allocation (-1,-1,+1,-1) then (+1,-1,+1) per block
        signs=(-1,-1,1,-1)+(1,-1,1)*r
        balance=0
        total=0
        for value,sign in zip(seq,signs):
            balance+=sign*value
            total+=abs(balance)
        assert total==4+3*r
    return 501

if __name__=='__main__':
    print('Finite transition certificate checks:',test_transition_certificate())
    print('Complete independent DP sequences:',test_exhaustive())
    print('Sharp witness instances:',test_sharp_family())
    print('PASS')
