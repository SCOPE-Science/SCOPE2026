"""Exact finite Bernoulli-run covariance checks (Python 3, standard library)."""
from fractions import Fraction
from itertools import product
from math import sqrt


def measured_covariance(n, k, p):
    q = 1 - p
    e_r = Fraction(0)
    e_t = Fraction(0)
    e_rt = Fraction(0)
    for word in product((0, 1), repeat=n):
        one_count = sum(word)
        weight = p**one_count * q**(n-one_count)
        lengths = []
        current = 0
        for x in word:
            if x:
                current += 1
            elif current:
                lengths.append(current)
                current = 0
        if current:
            lengths.append(current)
        r = len(lengths)
        t = sum(length >= k for length in lengths)
        e_r += weight * r
        e_t += weight * t
        e_rt += weight * r * t
    return e_rt - e_r*e_t


def covariance_formula(n, k, p):
    q = 1-p
    if n == k:
        return p**k*q*(1-(k-1)*p)
    s = n-k
    h = (s+1)-((k+2)*s+k-1)*p+((k+2)*s-2)*p*p
    return p**k*q*h


def roots(n, k):
    assert n > k >= 2
    s=n-k
    a=(k+2)*s-2
    b=(k+2)*s+k-1
    c=s+1
    disc=b*b-4*a*c
    assert disc>=0
    return ((b-sqrt(disc))/(2*a), (b+sqrt(disc))/(2*a))


def run():
    exact_checks=0
    for n in range(2,13):
        for k in range(2,n+1):
            for p in (Fraction(1,7),Fraction(2,5),Fraction(3,4)):
                a=measured_covariance(n,k,p)
                b=covariance_formula(n,k,p)
                assert a == b, (n,k,p,a,b)
                exact_checks += 1
    phase_checks = 0
    for k in range(2,40):
        for n in range(k+1,k+80):
            low,high=roots(n,k)
            assert 0<low<=0.5+1e-11 and high>0.5-1e-11
            if n>2*k:
                assert 0.5-1e-10 < high < 1+1e-10
            elif n==2*k:
                assert abs(high-1)<1e-8
            else:
                assert high > 1-1e-10
            phase_checks += 1
    for k in range(3,40):
        n=100000+k
        low,high=roots(n,k)
        limit_low=(1-sqrt(1-4/(k+2)))/2
        limit_high=(1+sqrt(1-4/(k+2)))/2
        assert abs(low-limit_low)<0.001 and abs(high-limit_high)<0.001
    print(f'PASS: {exact_checks} exhaustive exact-rational covariance checks')
    print(f'PASS: {phase_checks} numerical root-placement and finite-size classification checks')
    print('PASS: 37 large-n limiting-root comparisons')


if __name__=='__main__':
    run()
