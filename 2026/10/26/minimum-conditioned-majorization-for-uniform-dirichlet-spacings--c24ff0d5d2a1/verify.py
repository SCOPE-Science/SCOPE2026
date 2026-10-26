"""Exact arithmetic checks for uniform-simplex minimum-conditioned majorization corollaries.
Pure Python 3 standard library; no external data or packages.
"""
from fractions import Fraction as Q
from math import comb


def harmonic(n, power=1):
    return sum((Q(1, k**power) for k in range(1, n+1)), Q(0))


def positive_power(x, power):
    return max(x, Q(0)) ** power


def conditional_max_cdf(n, a, b):
    if n < 3:
        return Q(int(b >= 1-a))
    if b < a:
        return Q(0)
    x = (b-a)/(1-n*a)
    return sum(((-1)**j * comb(n-1,j) * positive_power(1-j*x, n-2)
                for j in range(n)), Q(0))


def joint_min_ge_and_max_le(n, a, b):
    return sum(((-1)**j * comb(n,j) * positive_power(1-n*a-j*(b-a), n-1)
                for j in range(n+1)), Q(0))


def joint_derivative_neg(n, a, b):
    # Away from kinks, minus d/da P(min>=a, max<=b).
    return sum(((-1)**j * comb(n,j) * (n-1) * (n-j) * positive_power(1-n*a-j*(b-a), n-2)
                for j in range(n+1)), Q(0))


for n in range(2, 30):
    hn = harmonic(n)
    hm = harmonic(n-1)
    emin = Q(1, n*n)
    emax = hn/n
    vmin = Q(n-1, n**4*(n+1))
    cov_conditional = (1-Q(n)*hm/(n-1))*vmin
    cov_formula = (1-hn)/Q(n**3*(n+1))
    cross_from_exponentials = (2+n*hm)/Q(n**3*(n+1))
    assert cov_conditional == cov_formula
    assert cross_from_exponentials-emin*emax == cov_formula
    assert cov_formula < 0
    assert emin + Q(0) < Q(1,n)
    assert (n*harmonic(n,2)-hn*hn)>0
print('PASS exact covariance identities and strict sign for n=2,...,29')

checks=0
for n in range(3, 9):
    for a in [Q(0),Q(1,5*n),Q(1,3*n)]:
        for delta in [Q(1,7*n),Q(2,5*n),Q(3,4*n), Q(5,4*n)]:
            b=a+delta
            # Skip derivative exactly at a knot (a new summand switches on/off).
            if any(1-n*a-j*(b-a)==0 for j in range(n+1)):
                continue
            f=n*(n-1)*positive_power(1-n*a,n-2)
            assert joint_derivative_neg(n,a,b)==f*conditional_max_cdf(n,a,b), (n,a,b)
            assert Q(0) <= conditional_max_cdf(n,a,b) <= Q(1), (n,a,b)
            checks+=1
print(f'PASS {checks} rational conditional-CDF / independent joint-volume derivative checks')
print('PASS: exact rational checks are finite; the general theorem follows from the displayed analytic disintegration and affine majorization proof, not these tests.')
