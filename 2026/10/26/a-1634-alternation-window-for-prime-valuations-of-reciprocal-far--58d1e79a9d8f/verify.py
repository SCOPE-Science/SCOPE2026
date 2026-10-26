"""Exact, reproducible arithmetic certificate for Farey valuation sign windows."""
from fractions import Fraction
from math import gcd

def phi_sieve(n):
    a = list(range(n + 1))
    for p in range(2, n + 1):
        if a[p] == p:
            for k in range(p, n + 1, p):
                a[k] -= a[k] // p
    a[1] = 1
    return a

def certify_window():
    phi = phi_sieve(820)
    a = 0
    s = Fraction(0)
    min_c = None
    min_gap = None
    first_failure = None
    for m in range(1, 821):
        a += phi[m]
        s += Fraction(phi[m], m)
        c = 2*a - m*s
        if 3 <= m <= 819:
            min_c = c if min_c is None else min(min_c, c)
            min_gap = phi[m]-c if min_gap is None else min(min_gap, phi[m]-c)
            assert Fraction(6, 5) <= c <= phi[m]-Fraction(1, 2), m
        if m >= 3 and not 0 < c < phi[m] and first_failure is None:
            first_failure = m
        if m == 820:
            assert -9 < c < -8
    assert min_c == Fraction(6, 5), min_c
    assert min_gap == Fraction(1, 2), min_gap
    assert first_failure == 820, first_failure
    return min_c, min_gap, c

def valuation(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e

def farey_exponent_bruteforce(n, p):
    r = 0
    for d in range(1, n+1):
        for a in range(1, d+1):
            if gcd(a,d) == 1:
                r += valuation(d, p) - valuation(a, p)
    return r

def farey_exponent_count(n, p):
    # Algebraically independent of the transfer approximation: count all
    # p-adic numerator and denominator contributions by coprime pairs.
    r = 0
    for d in range(1,n+1):
        if d % p == 0:
            r += valuation(d,p) * sum(gcd(a,d)==1 for a in range(1,d+1))
        for a in range(p,d+1,p):
            if gcd(a,d)==1:
                r -= valuation(a,p)
    return r

def confirm_error_bound():
    phi = phi_sieve(30)
    for p in (11,13,17,19):
        for m in range(3, min(p,10)):
            a=sum(phi[1:m+1]); s=sum((Fraction(phi[j],j) for j in range(1,m+1)),Fraction(0)); c=2*a-m*s
            direct=farey_exponent_count(m*p,p)
            assert abs(direct-p*c) <= m*m,(p,m,direct,p*c)
            assert direct-farey_exponent_count(m*p-1,p)==(p-1)*phi[m]
            if p<=13:
                assert direct == farey_exponent_bruteforce(m*p,p)
    return True

if __name__=='__main__':
    mn,mg,c = certify_window()
    assert confirm_error_bound()
    print('CERTIFICATE_OK', 'm=3..819', 'min_C',str(mn),'min_phi_minus_C',str(mg),'first_failure=820','C_820_between=-9,-8','direct_count_samples=26')
