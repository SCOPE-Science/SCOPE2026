"""Reproducible exact rational checks for gamma allocation fairness.
Python 3 standard library suffices for the checks.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial


def compositions(n, total, minimum=1):
    if n == 1:
        if total >= minimum:
            yield (total,)
        return
    for i in range(minimum, total-minimum*(n-1)+1):
        for t in compositions(n-1,total-i,minimum):
            yield (i,)+t


def exact_range_ratio_probability(shapes, ratio):
    """Independent Gamma(integer shape, 1) bundle totals, exact rational R."""
    if min(shapes) <= 0:
        return Q(0)
    n = len(shapes)
    R = Q(ratio)
    assert R > 1
    total = Q(0)
    for i in range(n):
        others = [j for j in range(n) if j != i]
        for mask in range(1 << (n-1)):
            T = {others[p] for p in range(n-1) if mask >> p & 1}
            coefficient = Q((-1)**len(T),factorial(shapes[i]-1))
            rate = Q(n)+(R-1)*len(T)
            for indices in product(*(range(shapes[j]) for j in others)):
                powers = dict(zip(others,indices))
                degree = sum(indices)
                monomial = R**sum(powers[j] for j in T)
                denominator = 1
                for p in indices:
                    denominator *= factorial(p)
                total += coefficient * factorial(shapes[i]-1+degree) * monomial / (denominator*rate**(shapes[i]+degree))
    return total


def asymptotic_coefficient(shapes):
    # Coefficient of epsilon^(n-1) for Gamma(integer shapes, 1).
    n = len(shapes)
    total = sum(shapes)
    out = Q(factorial(total-1),n**(total-1))
    for a in shapes:
        out /= factorial(a-1)
    return out


def run():
    nprofiles = 0
    ncomparisons = 0
    strict_pairs = 0
    for n in range(2, 6):
        for m in range(n, 11):
            q,r=divmod(m,n)
            balanced = tuple(sorted((q,)*(n-r)+(q+1,)*r))
            shapes_set = sorted(set(tuple(sorted(t)) for t in compositions(n,m)))
            for R in [Q(3,2),Q(2),Q(3)]:
                reference = exact_range_ratio_probability(balanced,R)
                for a in shapes_set:
                    p=exact_range_ratio_probability(a,R)
                    assert p <= reference, (n,m,R,a,p,reference)
                    if a != balanced:
                        assert p < reference, (n,m,R,a,p,reference)
                        strict_pairs+=1
                    ncomparisons+=1
                nprofiles+=len(shapes_set)
            cb=asymptotic_coefficient(balanced)
            for a in shapes_set:
                c=asymptotic_coefficient(a)
                assert c <= cb
                if a!=balanced:
                    assert c < cb
    # Independent n=2 expression via the incomplete-beta/binomial-tail identity.
    for a in range(1,7):
        for b in range(1,7):
            for R in [Q(3,2),Q(2),Q(3)]:
                upper=R/(1+R); lower=1/(1+R)
                t=a+b-1
                beta_cdf=lambda z:sum((Q(__import__('math').comb(t,j))*z**j*(1-z)**(t-j) for j in range(a,t+1)),Q(0))
                p=beta_cdf(upper)-beta_cdf(lower)
                assert p == exact_range_ratio_probability((a,b),R),(a,b,R,p)
    # With m=n=2 independent Exp(1) items, the fair ratio event has
    # probability epsilon/(2+epsilon) exactly.
    for epsilon in [Q(1,2),Q(1),Q(2),Q(4)]:
        assert exact_range_ratio_probability((1,1),1+epsilon)==epsilon/(2+epsilon)
    print(f'VERIFY_OK exact_profile_comparisons={ncomparisons} strict_comparisons={strict_pairs} beta_reductions={6*6*3} small_tolerance_coefficients=checked')

if __name__=='__main__':
    run()
