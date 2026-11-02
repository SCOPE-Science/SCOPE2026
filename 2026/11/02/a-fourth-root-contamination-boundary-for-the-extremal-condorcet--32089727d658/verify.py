#!/usr/bin/env python3
"""Exact finite checks for cyclic/impartial Condorcet mixtures; standard library only."""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial


def winner(orders):
    n = len(orders[0])
    ranks = []
    for order in orders:
        positions = [0] * n
        for pos, candidate in enumerate(order):
            positions[candidate] = pos
        ranks.append(positions)
    for candidate in range(n):
        if all(sum(r[candidate] < r[other] for r in ranks) >= 2
               for other in range(n) if other != candidate):
            return candidate
    return None


def q_finite(n):
    """Impartial three-voter winner probability by three disjoint upper sets."""
    N = n - 1
    total = F(0)
    for a in range(n):
        for b in range(n-a):
            p_disjoint = F(comb(N-a, b), comb(N, b))
            for c in range(n-a-b):
                total += p_disjoint * F(comb(N-a-b, c), comb(N, c))
    return total / n**2


def a_formula(n):
    return F(3*n-2, n*n)


def b_formula(n):
    return (2*sum((F(1, j) for j in range(1, n+1)), F(0)) - 1)/n


def p_formula(n, e):
    a, b, q = a_formula(n), b_formula(n), q_finite(n)
    return (1-e)**3*a + 3*e*(1-e)**2*b + e**2*(3-2*e)*q


def check_strata(n):
    all_orders = list(permutations(range(n)))
    ident = all_orders[0]
    rotations = [ident[j:]+ident[:j] for j in range(n)]
    a = F(sum(winner((ident, x, y)) is not None
              for x in rotations for y in rotations), n*n)
    b = F(sum(winner((ident, x, y)) is not None
              for x in rotations for y in all_orders), n*factorial(n))
    q = F(sum(winner((ident, x, y)) is not None
              for x in all_orders for y in all_orders), factorial(n)**2)
    assert a == a_formula(n), (n, 'cyclic', a, a_formula(n))
    assert b == b_formula(n), (n, 'one impartial', b, b_formula(n))
    assert q == q_finite(n), (n, 'two impartial', q, q_finite(n))
    return a,b,q


def check_direct_mixture(n,e):
    all_orders = list(permutations(range(n)))
    ident = all_orders[0]
    rotations = {ident[j:]+ident[:j] for j in range(n)}
    weights = {p: F(e, factorial(n)) + (F(1)-e)*F(p in rotations,n)
               for p in all_orders}
    assert sum(weights.values(), F(0)) == 1
    total = F(0)
    for x in all_orders:
        for y in all_orders:
            for z in all_orders:
                if winner((x,y,z)) is not None:
                    total += weights[x] * weights[y] * weights[z]
    assert total == p_formula(n,e), (n,e,total,p_formula(n,e))
    return total


def main():
    comparisons = 0
    for n in range(2,7):
        a,b,q = check_strata(n)
        assert a<=b<=q
        comparisons += 3
        print(f'n={n}: cyclic={a}, mixed-one={b}, impartial={q}')
    for n in (2,3,4):
        for e in (F(0),F(1,4),F(1,2),F(1)):
            v=check_direct_mixture(n,e)
            comparisons += 1
            print(f'  direct mixture n={n}, epsilon={e}, exact={v}')
    for n in range(3,101):
        assert b_formula(n)>a_formula(n)
        comparisons += 1
    print(f'PASS: {comparisons} exact independent probability identities or inequalities')

if __name__ == '__main__':
    main()
