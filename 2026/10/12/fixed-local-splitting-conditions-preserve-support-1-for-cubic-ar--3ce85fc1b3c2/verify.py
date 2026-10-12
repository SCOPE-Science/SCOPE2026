from fractions import Fraction
from math import sqrt

sigmas = [Fraction(1,2), Fraction(3,4), Fraction(9,10), Fraction(99,100)]
for s in sigmas:
    avg_mult = Fraction(1,1)/s - Fraction(1,2)
    nonvan = Fraction(1,1) - avg_mult/Fraction(2,1)
    expected = Fraction(5,4) - Fraction(1,1)/(2*s)
    assert nonvan == expected
    assert nonvan < Fraction(3,4)

# Exact identity for the fixed-prime Euler tail is elementary; numerically
# corroborate it for representative primes and a long truncation.
for p in [2,3,5,7,11,101]:
    r = p**-0.5
    partial = sum(r**e for e in range(1,500))
    closed = 1/(sqrt(p)-1)
    assert abs(partial-closed) < 1e-12

print('VERIFY_OK sigma_cases=4 limit_nonvanishing=0.750000 fixed_prime_geometric_bound=1')
