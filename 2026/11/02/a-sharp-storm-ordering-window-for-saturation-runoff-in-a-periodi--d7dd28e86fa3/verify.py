"""Exact-arithmetic checks for three-stage periodic storage and overflow.

No external packages are required. These finite checks supplement the proof;
they do not certify its universal quantifiers.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement


def cap(u, x, q, C):
    return min(C, q * x + u)


def periodic_storage_and_spill(inputs, q, C):
    """Independent closed-form solution of the fixed point of a capped affine composition."""
    n = len(inputs)
    weighted_sum = F(0)
    limits = []
    for k in range(n):
        limits.append(weighted_sum + q**k * C)
        weighted_sum += q**k * inputs[n - 1 - k]
    end_state = min(*limits, weighted_sum / (1 - q**n))
    start = end_state
    storage_sum = F(0)
    spill = F(0)
    for u in inputs:
        overflow = max(F(0), q * end_state + u - C)
        spill += overflow
        end_state = cap(u, end_state, q, C)
        storage_sum += end_state
    assert end_state == start
    assert spill == sum(inputs) - (1-q) * storage_sum
    return spill


def analytical_values(a, b, c, q, C):
    U = a + b + c
    A = cap(a, C, q, C)
    B = cap(b, A, q, C)
    D = cap(c, A, q, C)
    E = cap(b, C, q, C)
    Fv = cap(a, E, q, C)
    asc = max(F(0), U - (1-q) * (C + A + B))
    rev = max(F(0), U - (1-q) * (C + A + D),
              U - (1-q) * (C + E + Fv))
    return asc, rev


def run():
    total = 0
    strict = 0
    qs = (F(1,5), F(1,3), F(1,2), F(2,3), F(4,5))
    amounts = [F(k,4) for k in range(9)]
    capacities = [F(k,4) for k in range(1,21)]
    for a, b, c in combinations_with_replacement(amounts, 3):
        for q in qs:
            for C in capacities:
                direct_asc = periodic_storage_and_spill((a,b,c),q,C)
                direct_rev = periodic_storage_and_spill((a,c,b),q,C)
                formula_asc, formula_rev = analytical_values(a,b,c,q,C)
                assert direct_asc == formula_asc
                assert direct_rev == formula_rev
                assert direct_asc >= direct_rev
                low = (b + q*a)/(1 - q*q)
                high = (c + q*b + q*q*a)/(1 - q**3)
                exact_strict = (a < b < c and low < C < high)
                assert (direct_asc > direct_rev) == exact_strict
                strict += exact_strict
                total += 1

    q, C = F(1,2), F(2)
    a,b,c = F(1,4), F(1), F(3,2)
    aa=periodic_storage_and_spill((a,b,c),q,C)
    rr=periodic_storage_and_spill((a,c,b),q,C)
    assert aa == F(5,16) and rr == F(1,8) and aa-rr == F(3,16)
    print(f"PASS: {total} exact triples x parameters; {strict} strict cases; rational witness {aa} vs {rr}")


if __name__ == '__main__':
    run()
