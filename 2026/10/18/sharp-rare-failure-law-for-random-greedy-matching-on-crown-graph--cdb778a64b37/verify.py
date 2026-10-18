"""Exact rational verification of a greedy matching law on crown graphs.

No external dependencies; run with Python 3.10 or later.
The analytic asymptotic theorem is proved separately, not inferred from computations.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial

@lru_cache(None)
def failure_reduced(r, c):
    assert 1 <= r and 0 <= c <= r
    if r == 1:
        return Fraction(c, 1)
    d = r * r - c
    counts = ((c * (c - 1), c - 2),
              (2 * c * (r - c), c - 1),
              ((r - c) ** 2, c))
    return sum((Fraction(mult, d) * failure_reduced(r - 1, nxt)
                for mult, nxt in counts if mult), Fraction(0))

@lru_cache(None)
def failure_labeled(a, b):
    assert a.bit_count() == b.bit_count()
    if not a:
        return Fraction(0)
    available = [(i, j)
                 for i in range(a.bit_length()) if (a >> i) & 1
                 for j in range(b.bit_length()) if (b >> j) & 1 and i != j]
    if not available:
        assert a.bit_count() == 1
        return Fraction(1)
    return sum((failure_labeled(a ^ (1 << i), b ^ (1 << j))
                for i, j in available), Fraction(0)) / len(available)

def brute_edge_permutations(n):
    edge_list = [(i, j) for i in range(n) for j in range(n) if i != j]
    bad = 0
    count = 0
    for order in permutations(edge_list):
        used_left, used_right, selected = set(), set(), 0
        for i, j in order:
            if i not in used_left and j not in used_right:
                used_left.add(i)
                used_right.add(j)
                selected += 1
        bad += selected != n
        count += 1
    assert count == factorial(len(edge_list))
    return Fraction(bad, count)

def validate():
    rows = []
    for n in range(2, 8):
        q = failure_reduced(n, n)
        q_labeled = failure_labeled((1 << n) - 1, (1 << n) - 1)
        assert q == q_labeled, (n, q, q_labeled)
        rows.append((n, str(q)))
    assert brute_edge_permutations(2) == failure_reduced(2, 2)
    assert brute_edge_permutations(3) == failure_reduced(3, 3)
    print('Independent labeled-state exact enumerations: n=2,...,7 PASS')
    print('Independent complete edge-permutation enumerations: n=2,3 PASS')
    print('failure probabilities n=2,...,7:', rows)

    # Check the conditional drift and factorial-moment identities
    # exactly for all admissible integer states through 30.
    for r in range(2, 31):
        for c in range(r + 1):
            d = Fraction(r*r-c)
            transitions = [(c*(c-1),c-2), (2*c*(r-c),c-1),((r-c)**2,c)]
            trans = [(Fraction(mult, 1)/d,nxt) for mult,nxt in transitions if mult]
            assert sum((weight for weight, _ in trans),Fraction(0)) == 1
            v_old = Fraction(2*c,r*(r+1))
            v_new = sum((weight*Fraction(2*nxt,r*(r-1)) for weight,nxt in trans),Fraction(0))
            negative = -Fraction(4*c*(c-1),r*(r-1)*(r+1)*(r*r-c))
            assert v_new-v_old == negative
            moment = sum((weight*nxt*(nxt-1) for weight,nxt in trans),Fraction(0))
            predicted = Fraction(c*(c-1))*(1-Fraction(4*r-6,r*r-c))
            assert moment == predicted
    print('Statewise supermartingale and factorial-moment identities: r=2,...,30 PASS')
    q100 = failure_reduced(100,100)
    print('n=100 failure probability (12 digits):', f'{float(q100):.12f}')
    print('Asymptotic theorem: established analytically, not inferred from finite checks')
    print('No finite numerical check is used to certify that limit.')

if __name__ == '__main__':
    validate()
