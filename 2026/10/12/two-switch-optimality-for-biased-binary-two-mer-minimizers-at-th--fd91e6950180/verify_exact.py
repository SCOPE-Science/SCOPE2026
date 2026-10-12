#!/usr/bin/env python3
"""Exact integer proof checks for weighted binary two-mer minimizer order regimes.
Only Python standard library. No external datasets or solver required.
"""
from itertools import permutations
from math import comb
from fractions import Fraction

A = (1, 0, 2, 3)                 # 01,00,10,11
A2 = (1, 0, 3, 2)                # 01,00,11,10
B = (3, 1, 0, 2)                 # 11,01,00,10
C = (3, 1, 2, 0)                 # competitor dominated by B
ORDERS = tuple(permutations(range(4)))

def counts(order, w):
    m = w + 2
    rank = {k: j for j, k in enumerate(order)}
    c = [0] * (m + 1)
    for word in range(1 << m):
        bits = [(word >> i) & 1 for i in range(m)]
        mer = [2 * bits[i] + bits[i + 1] for i in range(w + 1)]
        i = min(range(w), key=lambda j: (rank[mer[j]], j))
        j = min(range(1, w + 1), key=lambda t: (rank[mer[t]], t))
        if i != j:
            c[sum(bits)] += 1
    return tuple(c)

def shift_q(left, right, m):
    """Coefficients of (1+2u)^m [d_left(u/(1+2u))-d_right(...)]."""
    return [sum((left[r] - right[r]) * comb(m - r, j - r)
                for r in range(j + 1)) for j in range(m + 1)]

def bernstein_to_power(coef):
    m = len(coef) - 1
    return [sum(coef[r] * comb(m-r, j-r) * (-1)**(j-r)
                for r in range(j + 1)) for j in range(m + 1)]

def polynomial_at(coeff, x):
    return sum(Fraction(a) * x**i for i, a in enumerate(coeff))

all_ties = {}
for w in range(2, 10):
    m = w + 2
    all_counts = {o: counts(o, w) for o in ORDERS}
    ca, cb = all_counts[A], all_counts[B]
    ties = []
    excluded = {B, C} if w == 9 else set()
    for order in ORDERS:
        if order in excluded:
            continue
        q = shift_q(all_counts[order], ca, m)
        assert min(q) >= 0, ('nonnegative-coefficient certificate failed', w, order, q)
        if not any(q):
            ties.append(order)
    all_ties[w] = tuple(ties)
    assert A in ties and A2 in ties
    assert len(ties) == (4 if w == 2 else 2), (w, ties)
    if w == 9:
        assert all(x >= 0 for x in shift_q(all_counts[C], cb, m))
        difference = bernstein_to_power(tuple(x-y for x,y in zip(ca, cb)))
        h = [1,-7,13,-5,9,-16,15,-5,1]
        # d_A-d_B = p^2(p-1)H(p).
        expected = [0,0] + [-h[0]] + [h[i-1]-h[i] for i in range(1,len(h))] + [h[-1]]
        assert difference == expected, (difference, expected)
        # d_C-d_B = p(1-p)^10.
        actual_cb = bernstein_to_power(tuple(x-y for x,y in zip(all_counts[C],cb)))
        assert actual_cb == [0]+[comb(10,j-1)*(-1)**(j-1) for j in range(1,12)]
        assert ca == (1,2,10,37,85,127,127,85,37,11,3,1)
        assert cb == (1,2,11,38,77,109,131,126,84,36,9,1)
        # Positive-halfline Descartes bound after p=u/(1+2u).
        transform = [sum(h[i] * comb(8-i, j-i) * 2**(j-i) for i in range(j+1)) for j in range(9)]
        assert transform == [1,9,27,11,-101,-192,-57,135,99]
        signs = [1 if x > 0 else -1 for x in transform if x]
        assert sum(signs[j]!=signs[j-1] for j in range(1,len(signs))) == 2
        # At least two distinct roots; Descartes shows exactly two on (0,1/2).
        for lo, hi in ((Fraction(257,1000),Fraction(258,1000)),
                       (Fraction(346,1000),Fraction(347,1000))):
            assert polynomial_at(h,lo)>0 if lo<Fraction(3,10) else polynomial_at(h,lo)<0
            assert polynomial_at(h,hi)<0 if lo<Fraction(3,10) else polynomial_at(h,hi)>0
        # Independence of the (non-optimal) C order near transition.
        assert shift_q(all_counts[C], cb, m) != [0] * (m+1)
        print('w=9 A/B Bernstein vectors:',ca,cb)
        print('w=9 H(u/(1+2u)) transformed signs:',transform)
        print('w=9 Q(C-B) min:', min(shift_q(all_counts[C],cb,m)))
    print('w=%d all-order exact polynomial certificate PASS; exact A ties %d' % (w,len(ties)))

# Boundary p=1/2 by uniform integer sums, and symmetry for p>1/2.
cv={o: sum(counts(o,9)) for o in ORDERS}
lo=min(cv.values()); best=tuple(o for o in ORDERS if cv[o]==lo)
assert lo == 526 and len(best) == 8
for o in ORDERS:
    compliment=tuple(3-v for v in o)
    v=counts(o,9); t=counts(compliment,9)
    assert all(v[r]==t[len(v)-1-r] for r in range(len(v)))
print('p=1/2: min charged 526/2048, exactly 8 orders')
print('ALL_EXACT_CHECKS_PASSED')
