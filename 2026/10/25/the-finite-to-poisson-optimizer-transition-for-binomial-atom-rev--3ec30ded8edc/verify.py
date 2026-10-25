"""Exact-integer certificates for the binomial zero-to-r crossover.
Run with Python 3 standard library: python3 verify.py.
The analytical infinite-domain proof is recorded in RESULT.md.
"""
from math import comb, factorial
from fractions import Fraction

SCALE = 10**40
OPTIMAL_N = {4: 4, 5: 7, 6: 10, 7: 15, 8: 25, 9: 51, 10: 294}


def integer_root_floor(z, r):
    """The unique integer L with L**r <= z < (L+1)**r."""
    assert z >= 0 and r >= 1
    hi = 1 << ((z.bit_length() + r - 1) // r)
    lo = 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**r <= z:
            lo = mid
        else:
            hi = mid
    assert lo**r <= z < (lo+1)**r
    return lo


def scaled_root_floor(n, r):
    return integer_root_floor(comb(n, r) * SCALE**r, r)


def certify_threshold_less(a, b, r):
    """Prove a/(1+C(a,r)**(1/r)) < b/(1+C(b,r)**(1/r))."""
    la = scaled_root_floor(a, r)
    lb = scaled_root_floor(b, r)
    # Exact rational bounds: F(a) <= a*S/(S+la),
    # whereas F(b) > b*S/(S+lb+1).
    margin = b*(SCALE+la) - a*(SCALE+lb+1)
    assert margin > 0, (r, a, b, margin)
    return margin


def verify_binomial_ratio(n, r, p):
    """Check mass(r)/mass(0)=comb(n,r)*(p/(1-p))**r."""
    q = 1-p
    pr = Fraction(comb(n,r),1) * p**r * q**(n-r)
    p0 = q**n
    assert pr/p0 == comb(n,r)*(p/q)**r


def main():
    for r in range(1,11):
        assert 2**r * factorial(r) > (r-1)**r
    assert 10**11 > 2**11 * factorial(11)
    print('Factorial sign transition at r=11: PASS')
    for r, n in OPTIMAL_N.items():
        if n > r:
            certify_threshold_less(n, n-1, r)
        certify_threshold_less(n, n+1, r)
        print('Certified unique optimal trial count:', r, n)
    for n in range(1,19):
        for r in range(1,n+1):
            for p in (Fraction(1,7),Fraction(2,5),Fraction(3,4)):
                verify_binomial_ratio(n, r, p)
    print('Exact binomial ratio identities and all comparisons: PASS')

if __name__ == '__main__':
    main()
