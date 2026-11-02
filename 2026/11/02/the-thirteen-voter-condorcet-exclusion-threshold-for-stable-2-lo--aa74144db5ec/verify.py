#!/usr/bin/env python3
"""Exact check of the three-alternative stable-two-lottery Condorcet boundary.

The finite enumeration supplements the symbolic inequalities in RESULT.md.
Run with Python 3 standard library only: python verify.py
"""

from fractions import Fraction
from itertools import permutations
from math import comb

CANDIDATES = ('A', 'B', 'C')
ORDERS = tuple(permutations(CANDIDATES))

def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def payoffs(orders_with_counts, lottery):
    total = sum(weight for _, weight in orders_with_counts)
    values = {}
    for attacker in CANDIDATES:
        numerator = Fraction(0)
        z = lottery[attacker]
        for order, multiplicity in orders_with_counts:
            below = sum((lottery[c] for c in order[order.index(attacker) + 1:]), Fraction(0))
            numerator += multiplicity * (below * below + below * z + z * z / 3)
        values[attacker] = numerator / total
    return values


# Exact finite boundary for *all* anonymous preference profiles with <=13 voters.
# A represents an arbitrary named strict Condorcet winner; relabeling covers B,C.
lines = []
for n in range(1, 14):
    condorcet_count = 0
    positive_bc_count = 0
    excluded_winners = []
    for counts in compositions(n, 6):
        ab = sum(c for order, c in zip(ORDERS, counts) if order.index('A') < order.index('B'))
        ac = sum(c for order, c in zip(ORDERS, counts) if order.index('A') < order.index('C'))
        if 2 * ab <= n or 2 * ac <= n:
            continue
        condorcet_count += 1
        u = sum(c for order, c in zip(ORDERS, counts) if order.index('B') < order.index('C'))
        x_num = 3 * u - n
        if not (0 < x_num < n):
            continue
        positive_bc_count += 1
        t = sum(c for order, c in zip(ORDERS, counts) if order[0] == 'A')
        b_middle = counts[ORDERS.index(('B', 'A', 'C'))]
        c_middle = counts[ORDERS.index(('C', 'A', 'B'))]
        numerator = t*n*n + b_middle*(n-x_num)**2 + c_middle*x_num**2
        if 3*numerator <= n**3:
            excluded_winners.append((counts, Fraction(x_num, n), Fraction(numerator, n**3)))
    assert condorcet_count > 0
    assert len(excluded_winners) == (2 if n == 13 else 0), (n,excluded_winners)
    lines.append((n,condorcet_count,positive_bc_count,len(excluded_winners)))
    if n == 13:
        # Both witnesses have one top-A voter, 6 B>A>C, 6 C>A>B,
        # with B/C order switched within the single A-first ballot.
        for counts,x,h in excluded_winners:
            assert sorted(counts) == [0,0,0,1,6,6]
            assert h == Fraction(703, 2197)
            assert x in (Fraction(5,13), Fraction(8,13))
print('n, anonymous Condorcet-A profiles, interior B/C stationary pairs (before A inequality), A-excluding equilibria')
for row in lines:
    print(*row,sep=',')

# Exact witness, with 1 A>C>B ballot, 6 B>A>C ballots, 6 C>A>B ballots.
witness = [(('A','C','B'),1),(('B','A','C'),6),(('C','A','B'),6)]
d = {'A':Fraction(0), 'B':Fraction(5,13), 'C':Fraction(8,13)}
assert (sum(c for o,c in witness if o.index('A') < o.index('B')),
        sum(c for o,c in witness if o.index('A') < o.index('C'))) == (7,7)
p = payoffs(witness,d)
assert p == {'A': Fraction(703,2197), 'B': Fraction(1,3), 'C': Fraction(1,3)}
assert p['A'] < Fraction(1,3)

# Identity: weighted payoffs of candidate copies average to 1/3.
# Verify over the small exact rational simplex for every ballot order.
for denom in range(1,11):
    for a_num in range(denom+1):
        for b_num in range(denom-a_num+1):
            c_num=denom-a_num-b_num
            ell={'A':Fraction(a_num,denom),'B':Fraction(b_num,denom),'C':Fraction(c_num,denom)}
            for order in ORDERS:
                h=payoffs([(order,1)],ell)
                assert sum(ell[c]*h[c] for c in CANDIDATES) == Fraction(1,3)

# 2026 reference's symmetric exclusion construction: n=18, support (0,1/2,1/2).
reference18 = [(('A','B','C'),1),(('A','C','B'),1),
               (('B','A','C'),8),(('C','A','B'),8)]
assert payoffs(reference18,{'A':Fraction(0),'B':Fraction(1,2),'C':Fraction(1,2)}) == {
    'A':Fraction(1,3),'B':Fraction(1,3),'C':Fraction(1,3)}
print('Witness: n=13, strict Condorcet wins 7-6 twice; H_A=703/2197, H_B=H_C=1/3.')
print('Unique 13-voter exclusion is compatible with the prior n=18 symmetric construction.')
print('All exact checks passed.')
