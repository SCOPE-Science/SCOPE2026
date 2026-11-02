#!/usr/bin/env python3
"""Exact-rational checks of the complete-bipartite random-majority formulas.

No external dependencies are required. These finite checks supplement, rather
than establish, the proofs valid for all positive part sizes.
"""
from fractions import Fraction
from math import comb


def tie_prob(n):
    return Fraction(comb(n, n // 2), 2**n) if n % 2 == 0 else Fraction(0)


def pure_prob(n):
    return Fraction(2, 2**n)


def sign(k, n):
    return (k > n - k) - (k < n - k)


def law(a, b, i, j):
    qa, qb = tie_prob(a), tie_prob(b)
    ua, ub = pure_prob(a), pure_prob(b)
    denom = 1 - qa * qb
    x = (2 + qb - ub - qb * ua - qa * qb) / denom
    y = (2 + qa - ua - qa * ub - qa * qb) / denom
    z = (2 + qa + qb - qa * qb - qa * ub - qb * ua - ua * ub) / denom
    if i in (0, a) and j in (0, b):
        e = Fraction(0)
    else:
        sa, sb = sign(i, a), sign(j, b)
        if sa == 0 and sb == 0:
            e = z
        elif sa == 0:
            e = x
        elif sb == 0:
            e = y
        else:
            e = Fraction(1)
    fa = Fraction(1) if sign(i, a) > 0 else Fraction(0) if sign(i, a) < 0 else Fraction(1, 2)
    fb = Fraction(1) if sign(j, b) > 0 else Fraction(0) if sign(j, b) < 0 else Fraction(1, 2)
    return (e, fa * fb, (1-fa) * (1-fb), fa * (1-fb) + (1-fa) * fb)


def next_side(n, opposite_count, opposite_size):
    if opposite_count > opposite_size - opposite_count:
        return ((n, Fraction(1)),)
    if opposite_count < opposite_size - opposite_count:
        return ((0, Fraction(1)),)
    return tuple((k, Fraction(comb(n, k), 2**n)) for k in range(n + 1))


def check_bellman():
    cases = 0
    state_checks = 0
    transition_checks = 0
    for a in range(1, 13):
        for b in range(1, 13):
            cases += 1
            for i in range(a + 1):
                for j in range(b + 1):
                    ans = law(a, b, i, j)
                    assert ans[1] + ans[2] + ans[3] == 1
                    is_recurrent = (i in (0, a)) and (j in (0, b))
                    if is_recurrent:
                        assert ans[0] == 0
                        continue
                    total = [Fraction(0)] * 4
                    for ni, pi in next_side(a, j, b):
                        for nj, pj in next_side(b, i, a):
                            transition_checks += 1
                            lp = law(a, b, ni, nj)
                            for k in range(4):
                                total[k] += pi * pj * lp[k]
                    assert ans[0] == 1 + total[0], (a,b,i,j,'time',ans,total)
                    assert ans[1:] == tuple(total[1:]), (a,b,i,j,'outcomes',ans,total)
                    state_checks += 1
    return cases, state_checks, transition_checks


def expected_both_ties(a,b):
    qa,qb=tie_prob(a),tie_prob(b)
    ua,ub=pure_prob(a),pure_prob(b)
    return (2+qa+qb-qa*qb-qa*ub-qb*ua-ua*ub)/(1-qa*qb)


def no_pure_upper(qa,qb):
    return (2+qa+qb-qa*qb)/(1-qa*qb)


def check_sharp_bound():
    target = Fraction(79,27)
    assert no_pure_upper(tie_prob(4),tie_prob(8)) < target
    assert no_pure_upper(tie_prob(2),tie_prob(14)) < target
    finite = {}
    for a,b in [(2,2),(2,4),(2,6),(2,8),(2,10),(2,12),(4,4),(4,6),(6,6)]:
        finite[(a,b)]=expected_both_ties(a,b)
        assert finite[(a,b)] <= target
    assert [pair for pair,value in finite.items() if value == target] == [(2,6)]
    for k in range(1,40):
        assert tie_prob(2*k+2) < tie_prob(2*k)
    return finite


def main():
    cases,states,transitions = check_bellman()
    finite = check_sharp_bound()
    print('PASS: exact Bellman and absorbing-class equations')
    print('graphs:',cases,'transient count states:',states,'transitions checked:',transitions)
    print('sharp expected stabilization time:',expected_both_ties(2,6))
    print('finite boundary cases:', ', '.join(f'{p}:{v}' for p,v in finite.items()))
    print('Finite comparisons complement the analytical monotonic upper-envelope proof.')

if __name__ == '__main__':
    main()
