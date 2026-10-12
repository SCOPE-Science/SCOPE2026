#!/usr/bin/env python3
"""Exact-arithmetic checks of the level-13 four-term recurrence and 2-adic congruence."""
from fractions import Fraction
from math import comb

N = 350
s = [1]
for n in range(N):
    numerator = 6 * (2*n+1) * (3*n*n+3*n+1) * s[n]
    if n >= 1:
        numerator += 4*n * (148*n*n+27) * s[n-1]
    if n >= 2:
        numerator += 24 * (6*n-5) * (6*n-1) * (2*n-1) * s[n-2]
    denom = (n+1)**3
    assert numerator % denom == 0, ('recurrence_integrality', n)
    s.append(numerator//denom)

reference = [1, 6, 182, 5148, 173862, 6266676,
             237979196, 9366227832, 378768328198,
             15643121895492, 657035290739412]
assert s[:len(reference)] == reference, 'source_initial_terms'

for n in range(1, N+1):
    v2 = (s[n] & -s[n]).bit_length() - 1
    popcount = n.bit_count()
    assert v2 == popcount, ('valuation', n, v2, popcount)
    catalan = comb(2*n-2, n-1) // n
    leading = 2 * ((-1)**(n-1)) * (3**n) * catalan
    assert (s[n] - leading) % (1 << (popcount+2)) == 0, ('mod4_congruence', n)

# Independent rational coefficient check of Z^2 for the first seven powers of X.
z = [Fraction(s[k], 4**k) for k in range(7)]
f = [sum(z[k]*z[n-k] for k in range(n+1)) for n in range(7)]
assert f == list(map(Fraction, [1, 3, 25, 195, 1729, 16107, 156481])), ('square_coefficients', f)

# The leading binomial coefficient has exact valuation s_2(n).
for n in range(1, N+1):
    c = 2*((-1)**(n-1))*(comb(2*n-2, n-1)//n)
    assert ((abs(c)&-abs(c)).bit_length()-1) == n.bit_count()

print('VERIFY_OK')
print(f'checked_recurrence_indices=0..{N-1}')
print(f'checked_2_adic_valuations=1..{N}')
print(f'checked_sharp_mod4_congruences=1..{N}')
print('checked_square_coefficients=0..6_exact_rational')
print('checked_catalan_leading_terms=1..350')
print('finite_computations_supplement_unrestricted_proof')
