"""Exact finite checks for Mallows cycle-count/inversion covariance reversal.

This script uses Python's standard library, and enumerates permutations only
for consistency checks at small sizes. The general theorem has an analytic proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial


def cycles(p):
    visited = set()
    count = 0
    for i in range(len(p)):
        if i not in visited:
            count += 1
            j = i
            while j not in visited:
                visited.add(j)
                j = p[j]
    return count


def inversion_count(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i+1, len(p)))


def enumerate_coefficients(n):
    total = n*(n-1)//2
    z = [0]*(total+1)
    g = [0]*(total+1)
    for p in permutations(range(n)):
        k = inversion_count(p)
        z[k] += 1
        g[k] += cycles(p)
    return z, g


def check(n):
    z, g = enumerate_coefficients(n)
    N = n*(n-1)//2
    assert sum(z) == factorial(n)
    assert z[0] == z[N] == 1
    assert z[1] == z[N-1] == n-1
    assert g[0] == n
    c_reverse = (n+1)//2
    assert g[N] == c_reverse
    assert g[1] - n*z[1] == -(n-1)
    a = (n-1) if n%2 else (n-3)
    assert g[N-1]-c_reverse*z[N-1] == -a
    expected_mean = sum(Fraction(1,k) for k in range(1,n+1))
    mean_cycles = Fraction(sum(g),factorial(n))
    assert expected_mean == mean_cycles
    mean_inv = Fraction(sum(i*z[i] for i in range(N+1)), factorial(n))
    mixed = Fraction(sum(i*g[i] for i in range(N+1)), factorial(n))
    cov = mixed - mean_cycles*mean_inv
    assert cov == -Fraction(2*n-1,12)
    print(f'n={n} perms={factorial(n)} near_zero_coeff={-(n-1)} '
          f'near_infty_coeff={-a} covariance_at_q1={cov}')


def check_three():
    z, g = enumerate_coefficients(3)
    assert z == [1,2,2,1]
    assert g == [3,4,2,2]
    # The derivative numerator G'Z-GZ' is 2q^4-7q^2-8q-2.
    deriv = [0]*(len(z)*2-1)
    for i, gi in enumerate(g):
        for j, zj in enumerate(z):
            if i:
                deriv[i+j-1] += i*gi*zj
            if j:
                deriv[i+j-1] -= j*zj*gi
    while deriv and deriv[-1] == 0:
        deriv.pop()
    assert deriv == [-2,-8,-7,0,2]
    # Unique positive root follows analytically from Descartes' sign rule.
    assert sum((a>0) != (b>0) for a,b in zip(
        [x for x in deriv[::-1] if x], [x for x in deriv[::-1] if x][1:])) == 1
    print('n=3 derivative numerator verified: 2*q**4 - 7*q**2 - 8*q - 2')


if __name__ == '__main__':
    for n in range(2,9):
        check(n)
    check_three()
    print('CHECK_OK: exact finite consistency checks; general proof is analytic')
