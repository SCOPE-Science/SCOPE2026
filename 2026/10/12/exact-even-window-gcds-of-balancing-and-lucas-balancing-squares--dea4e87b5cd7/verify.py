#!/usr/bin/env python3
"""Finite exact-integer tests of the even-window balancing-square GCD formulas.
Run: python3 verify.py. These tests do not replace the universal proof.
"""
from math import gcd

K_MAX = 250
N_MAX = 80
L = K_MAX + N_MAX + 3
P = [0, 1]
Q = [1, 1]
for _ in range(2 * L):
    P.append(2 * P[-1] + P[-2])
    Q.append(2 * Q[-1] + Q[-2])
B = [P[2*n] // 2 for n in range(L)]
C = [Q[2*n] for n in range(L)]
assert all(2*B[n] == P[2*n] and C[n]**2 == 8*B[n]**2 + 1 for n in range(L))

def vp(n, p):
    z = 0
    while n and n % p == 0:
        n //= p
        z += 1
    return z

window_checks = 0
for k in range(2, K_MAX + 1, 2):
    g = gcd(k, B[k])
    assert g % 2 == 0 and gcd(k, P[2*k]) == g
    # Test the exact 2-adic units without using nonintegral quotients.
    power_two = k & -k
    odd_k = k // power_two
    u_mod_16 = ((P[2*k] // (2*power_two)) * pow(odd_k, -1, 16)) % 16
    assert u_mod_16 == 3 and C[k] % 16 == 1
    assert vp(B[k], 2) == vp(k, 2)
    assert vp(B[k], 3) == vp(k, 3) + 1
    A_b = A_c = empirical_b = empirical_c = 0
    for n in range(1, N_MAX + 1):
        if n == 1:
            A_b = sum(B[j]**2 for j in range(1, k+1))
            A_c = sum(C[j]**2 for j in range(1, k+1))
        else:
            A_b += B[n+k-1]**2-B[n-1]**2
            A_c += C[n+k-1]**2-C[n-1]**2
        assert A_c == 8*A_b + k
        empirical_b = gcd(empirical_b, A_b)
        empirical_c = gcd(empirical_c, A_c)
        window_checks += 2
    assert empirical_b == g//2 and empirical_c == g, (k, g, empirical_b, empirical_c)

print('VERIFY_OK')
print('even_window_lengths=2,4,...,250')
print('starting_indices=1..80')
print(f'exact_window_sums_compared={window_checks}')
print('both_even_window_gcd_formulas=PASS')
print('2_adic_Pell_units_and_square_identity=PASS')
print('3_adic_Pell_valuation=PASS')
print('finite_tests_supplement_unrestricted_proof')
