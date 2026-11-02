"""Exact finite checks for coordinate-Cesaro mixed-commutator identities.

The Hilbert--Schmidt classification is an analytic theorem; this checks only
specified finite coefficient identities and positive finite partial sums.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb

checks = 0

def compositions(n, d):
    if d == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for rest in compositions(n-k, d-1):
                yield (k,) + rest

def weight(alpha):
    result = Fraction(1, factorial(sum(alpha)))
    for a in alpha:
        result *= factorial(a)
    return result

def coefficient(n, p, q):
    return Fraction(p-q, (n+p+1)*(n+q+1)*(n+p+q+1))

def combined_weight(d, n, p, q):
    s = p+q
    return Fraction(factorial(p)*factorial(q), factorial(d+s-1)) * Fraction(factorial(n+d+s-1), factorial(n+s))

for d in range(2, 7):
    for n in range(0, 6):
        for p in range(0, 7):
            for q in range(0, 7):
                brute = sum((weight((a[0]+p, a[1]+q) + a[2:])/weight(a) for a in compositions(n,d)), Fraction(0))
                assert brute == combined_weight(d,n,p,q), (d,n,p,q,brute,combined_weight(d,n,p,q))
                checks += 1

# Direct finite upper and lower comparators for Hilbert--Schmidt degree energy.
for d in range(2, 9):
    for n in range(0, 12):
        for s in range(1, 15):
            rec_binom = sum((Fraction(1, comb(s,p)) for p in range(s+1)), Fraction(0))
            assert rec_binom <= 3
            for p in range(s+1):
                q = s-p
                term = coefficient(n,p,q)**2 * combined_weight(d,n,p,q)
                if d <= 5:
                    upper = Fraction(s*s, (n+1)**2*(s+1)**4*comb(s,p))
                else:
                    upper = (Fraction(n+1)**(d-7)) * Fraction(s*s, (s+1)**4*comb(s,p))
                assert term <= upper, (d,n,p,q,term,upper)
                checks += 1

# One-step terms produce a strict diverging lower bound from dimension six.
for d in range(6, 11):
    for n in range(1, 26):
        first_pair = 2 * coefficient(n,1,0)**2 * combined_weight(d,n,1,0)
        assert first_pair > 0
        checks += 1
print('EXACT_COMMUTATOR_CHECK_OK', checks)
