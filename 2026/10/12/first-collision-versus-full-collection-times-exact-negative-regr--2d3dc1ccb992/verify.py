"""Reproduce exact collision/cover moments and asymptotic estimates.
Python >=3.9; only standard library. The exact check enumerates all n^n length-n prefixes.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt, pi


def harmonic(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction())


def formula(n):
    assert n >= 2
    s = Fraction(1)
    surv = [s]
    for j in range(1, n + 1):
        s *= Fraction(n-j+1, n)
        surv.append(s)
    cov = -sum((surv[j] * sum((Fraction(k, n-k) for k in range(1, j)), Fraction())
                for j in range(2, n + 1)), Fraction())
    probs = [Fraction(0)] * (n+2)
    for b in range(2, n+1):
        probs[b] = surv[b-1] * Fraction(b-1, n)
    probs[n+1] = surv[n]
    hm = harmonic(n)
    conditional = [Fraction(0)] * (n+2)
    for b in range(2, n+1):
        conditional[b] = Fraction(b) + n * harmonic(n-b+1)
    conditional[n+1] = Fraction(n)
    e_b = sum((probs[b]*b for b in range(2,n+2)), Fraction())
    e_t = n*hm
    e_bt = sum((probs[b]*b*conditional[b] for b in range(2,n+2)), Fraction())
    assert e_bt-e_b*e_t == cov
    return probs, conditional, cov


def enumerate_prefixes(n):
    # After n draws, B is known (n+1 when all initial draws are distinct).
    # The remaining mean full-cover time is n*H_(missing coupon count).
    e_b = e_t = e_bt = Fraction()
    count_by_b = [0] * (n + 2)
    conditional_tsum = [Fraction()] * (n + 2)
    for seq in product(range(n), repeat=n):
        seen = set()
        first_collision = None
        covered_at = None
        for i, a in enumerate(seq, start=1):
            if a in seen and first_collision is None:
                first_collision = i
            seen.add(a)
            if len(seen) == n and covered_at is None:
                covered_at = i
        b = first_collision if first_collision is not None else n + 1
        t_conditional = Fraction(covered_at) if covered_at is not None else Fraction(n) + n*harmonic(n-len(seen))
        count_by_b[b] += 1
        conditional_tsum[b] += t_conditional
        e_b += b
        e_t += t_conditional
        e_bt += b*t_conditional
    denominator = n**n
    probs, cond, cov = formula(n)
    assert e_b/denominator == sum((b*probs[b] for b in range(2,n+2)), Fraction())
    assert e_t/denominator == n * harmonic(n)
    assert e_bt/denominator - e_b*e_t/(denominator**2) == cov
    for b in range(2,n+2):
        assert Fraction(count_by_b[b],denominator) == probs[b]
        assert conditional_tsum[b]/count_by_b[b] == cond[b]
    return denominator, n-1


def numeric_cov(n):
    p = 1.0
    inner = 0.0
    acc = 0.0
    for j in range(1,n+1):
        p *= (n-j+1)/n
        if j >= 2:
            inner += (j-1)/(n-j+1)
            acc += p*inner
    return -acc

if __name__ == '__main__':
    totals = 0
    comparisons = 0
    for n in range(2,8):
        prefixes, cond_cases = enumerate_prefixes(n)
        totals += prefixes
        comparisons += (3+2*cond_cases)
    print('EXACT_OK', 'enumerated_prefixes',totals,'independent_checks',comparisons)
    print('small exact covariance values:', [(n,str(formula(n)[2])) for n in range(2,8)])
    limit = -sqrt(pi/8)
    print('limit target',limit)
    for n in (100, 500, 2000, 10000, 40000):
        scaled = numeric_cov(n)/sqrt(n)
        print('n',n,'scaled',format(scaled,'.9f'),'absolute_error',format(abs(scaled-limit),'.6g'))
    assert abs(numeric_cov(40000)/sqrt(40000) - limit) < 0.001
    print('VERIFY_OK')
