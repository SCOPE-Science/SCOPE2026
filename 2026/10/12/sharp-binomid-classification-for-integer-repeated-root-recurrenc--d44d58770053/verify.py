"""Exact finite checks for generalized binomial coefficients of integer repeated-root recurrences.

Runs on Python >=3.9, standard library only. No finite test establishes infinitude.
"""
from fractions import Fraction
from math import gcd, comb


def is_prime(p):
    if p < 2:
        return False
    k = 2
    while k*k <= p:
        if p % k == 0:
            return False
        k += 1
    return True


def first_witness(a, c, d):
    """A prime and central index satisfying the proof's interval conditions."""
    g = gcd(abs(c), abs(d))
    eps = 1 if c > 0 else -1
    A, B = eps*c//g, eps*d//g
    assert A >= 1 and B != 0 and gcd(A, B) == 1
    for p in range(max(11, 4*abs(B)+4*A+11), 20000):
        if not is_prime(p) or a % p == 0 or (p-B) % A:
            continue
        k = (p-B)//A
        if k < 1:
            continue
        denominator = [A*j+B for j in range(1, k+1)]
        numerator = [A*j+B for j in range(k+1, 2*k+1)]
        if sum(z % p == 0 for z in denominator) != 1:
            continue
        if any(z % p == 0 for z in numerator):
            continue
        return p, k
    raise AssertionError(('no finite witness in search range', a,c,d))


def sequence(a, x0, x1, n):
    c, d = x1-a*x0, a*x0
    return (c*n+d)*a**(n-1)


def fbinom(a, x0, x1, n, k):
    out = Fraction(1)
    for j in range(1, k+1):
        out *= Fraction(sequence(a, x0, x1, n-k+j),
                        sequence(a, x0, x1, j))
    return out


def valid(a, x0, x1):
    c,d=x1-a*x0,a*x0
    return x1!=0 and (c==0 or not (-d % c == 0 and -d//c >= 1))


positive_checks = 0
negative_checks = 0
exact_witness_checks = 0
finite_nonzero_cases = 0
for a in (-4,-3,-2,-1,1,2,3,4):
    for x0 in range(-5,6):
        for x1 in range(-5,6):
            if not valid(a,x0,x1):
                continue
            finite_nonzero_cases += 1
            c,d=x1-a*x0,a*x0
            if c==0 or d==0:
                for n in range(1,17):
                    for k in range(n+1):
                        actual=fbinom(a,x0,x1,n,k)
                        expected=a**(k*(n-k))*(comb(n,k) if d==0 else 1)
                        assert actual == expected,(a,x0,x1,n,k)
                        positive_checks += 1
            else:
                p,k=first_witness(a,c,d)
                assert all(sequence(a,x0,x1,j)!=0 for j in range(1,2*k+1))
                negative_checks += 1
                if k<=35:
                    actual=fbinom(a,x0,x1,2*k,k)
                    assert actual.denominator % p == 0,(a,x0,x1,p,k,actual)
                    exact_witness_checks += 1

assert positive_checks>1000 and negative_checks>100
print('VERIFY_OK')
print('integer_recurrence_parameter_cases=',finite_nonzero_cases,sep='')
print('positive_class_binomial_coefficients=',positive_checks,sep='')
print('negative_class_prime_witness_checks=',negative_checks,sep='')
print('exact_fraction_witnesses_at_small_indices=',exact_witness_checks,sep='')
print('finite_checks_do_not_prove_dirichlet_or_unrestricted_theorem')
