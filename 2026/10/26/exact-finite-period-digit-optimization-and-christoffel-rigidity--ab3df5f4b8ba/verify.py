#!/usr/bin/env python3
"""Exact integer checks for rational extremal words and one quadratic irrational example."""
from itertools import combinations, product
from math import gcd, isqrt


def upper_word(p, q):
    return tuple(((j + 1) * p + q - 1) // q - (j * p + q - 1) // q for j in range(q))


def max_rotation(w):
    q = len(w)
    return max(w[j:] + w[:j] for j in range(q))


def all_rotations(w):
    q = len(w)
    return {w[j:] + w[:j] for j in range(q)}


def golden_ceiling(k):
    if not k:
        return 0
    # floor(k*(sqrt(5)-1)/2), no floating-point computation.
    floor_alpha = (isqrt(5*k*k)-k)//2
    return floor_alpha+1


def golden_prefix(length):
    return tuple(golden_ceiling(j+1) - golden_ceiling(j) for j in range(length))


def accepted_up_to(w, upper):
    q = len(w)
    for start in range(q):
        for j, ai in enumerate(upper):
            b = w[(start+j)%q]
            if b != ai:
                if b > ai:
                    return False
                break
    return True


def proximity_golden(p, q):
    # p/q < alpha < p/q+1/q^2 via positive-rational square comparison.
    from fractions import Fraction
    lower = Fraction(2*p+q, q)
    upper = Fraction(2*p*q+q*q+2, q*q)
    return lower*lower < 5 and 5 < upper*upper


def run():
    extremal = 0
    for q in range(2, 14):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            mech = upper_word(p, q)
            assert mech == max_rotation(mech), (p, q, mech)
            rot = all_rotations(mech)
            for pos in combinations(range(q), p):
                w = tuple(1 if k in pos else 0 for k in range(q))
                m = max_rotation(w)
                assert m >= mech, (p, q, w)
                assert (m == mech) == (w in rot), (p, q, w)
                extremal += 1
    target = golden_prefix(260)
    fixed_words = 0
    near = []
    for q in range(1, 14):
        p = golden_ceiling(q)-1
        accepted = []
        for w in product((0, 1), repeat=q):
            if accepted_up_to(w, target):
                accepted.append(w)
                fixed_words += 1
        top = [w for w in accepted if sum(w) == p]
        assert len(top) >= 1 and all(sum(w) <= p for w in accepted), (q, p)
        if q >= 2 and 1 <= p < q and gcd(p, q) == 1 and proximity_golden(p, q):
            assert len(top) == q and set(top) == all_rotations(upper_word(p, q)), (q, p)
            near.append(q)
    assert near == [2, 5, 13], near
    print(f'VERIFY_OK Lyndon_extremal_cases={extremal} golden_periods=1..13 accepted_words={fixed_words} rigid_q={near}')

if __name__ == '__main__':
    run()
