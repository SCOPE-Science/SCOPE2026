"""Exact-arithmetic verification of a Jacobsthal quotient gcd factorization.

No external packages; finite checks supplement, and do not prove, the theorem.
"""
from math import gcd


def jac(n):
    assert isinstance(n, int) and n >= 0
    return ((1 << n) - (-1 if n & 1 else 1)) // 3


def data(n):
    assert n >= 1 and n % 3 != 0
    z = 1 << n
    sign = -1 if n & 1 else 1
    c = z*z + sign*z + 1
    e = z**6 + sign*z**3 + 1
    f = z**18 + sign*z**9 + 1
    assert c % 3 == 0 and f % 3 == 0 and e % 57 == 0
    a,b,h = c // 3, f // 3, e // 57
    assert gcd(a,b) == 1
    return a,b,h


# Algebraic polynomial identities, evaluated at exact powers of two.
for n in range(1,501):
    z = 1 << n
    sign = -1 if n & 1 else 1
    c = z*z + sign*z + 1
    e = z**6 + sign*z**3 + 1
    f = z**18 + sign*z**9 + 1
    assert jac(3*n) == jac(n)*c
    assert jac(9*n) == jac(3*n)*e
    assert jac(27*n) == jac(9*n)*f
    assert (f-3) % c == 0

# Directly compute BOTH original rational quotients and their alleged gcd.
checks = 0
for n in range(1,401):
    if n % 3 == 0:
        continue
    u,v,h = data(n)
    a_den = jac(9)*jac(n)
    b_den = jac(9)*jac(3*n)
    assert jac(9*n) % a_den == 0
    assert jac(27*n) % b_den == 0
    a = jac(9*n)//a_den
    b = jac(27*n)//b_den
    assert a == h*u
    assert b == h*v
    assert gcd(a,b) == h
    assert (a == h) == (n == 1)
    checks += 1

assert jac(9) == 171
assert pow(11,3,19) == 1 and 11 % 19 != 1
assert (11*11+11+1) % 19 == 0
print('VERIFY_OK')
print('jacobsthal_triple_factorization_indices=500')
print('full_original_quotient_and_exact_gcd_indices=' + str(checks))
print('coprime_reduced_factors=' + str(checks))
print('mod_19_order_three_test=PASS')
print('unrestricted_proof_is_symbolic_not_from_finite_tests=TRUE')
