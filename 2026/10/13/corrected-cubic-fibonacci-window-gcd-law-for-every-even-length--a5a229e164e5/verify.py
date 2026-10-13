"""Exact-integer spot checks for the even-window Fibonacci cube gcd theorem.
Finite checks supplement, and do not certify, the unrestricted proof.
"""
from math import gcd

KMAX = 600
WINDOWS = 25
F = [0, 1]
for _ in range(KMAX + WINDOWS + 5):
    F.append(F[-1] + F[-2])

case_count = 0
window_count = 0
bad = []
for k in range(2, KMAX + 1, 2):
    a, v, u = F[k], F[k+1], F[k+2]
    m = gcd(v**3 - 1, u**3 - 1)
    assert v*v - a*v - a*a == 1
    assert m == gcd(u - 1, 3*(v - 1))
    assert (u - 1) % m == 0
    delta = v - 1
    assert (3*delta) % m == 0
    assert (delta*delta) % m == 0
    subtotal = sum(F[i]**3 for i in range(1, k+1))
    assert 4*subtotal == v**3 + a**3 - 3*(v-a) + 2
    expected = m // 2 if k % 6 == 0 else m
    assert m % 2 == (0 if k % 6 == 0 else 1)
    exact = 0
    s = subtotal
    for n in range(WINDOWS):
        exact = gcd(exact, s)
        assert (F[n+k+1]**3 - F[n+1]**3) % m == 0
        window_count += 1
        s += F[n+k+1]**3 - F[n+1]**3
    if exact != expected: bad.append((k, exact, expected))
    assert gcd(m, subtotal) == expected
    if k % 6 == 0:
        def nu2(x): return (x & -x).bit_length()-1
        t = nu2(m)
        assert t >= 2
        assert nu2(a) == t+1
        assert nu2(subtotal) == t-1
    case_count += 1
assert not bad, bad
print('VERIFY_OK')
print(f'even_k_2_to_{KMAX}={case_count}_PASS')
print(f'first_{WINDOWS}_windows={window_count}_gcd_checks_PASS')
print('norm_cubic_difference_gcd_and_summation_identities=PASS')
print('2_adic_exact_half_factor_for_multiples_of_6=PASS')
print('finite_checks_supplement_unrestricted_symbolic_proof')
