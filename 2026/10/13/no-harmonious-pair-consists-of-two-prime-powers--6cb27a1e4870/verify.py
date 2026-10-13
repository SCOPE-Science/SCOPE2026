#!/usr/bin/env python3
from fractions import Fraction

def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        ok = True
        d = 2
        while d*d <= x:
            if x % d == 0:
                ok = False
                break
            d += 1
        if ok:
            out.append(x)
    return out

def sigma_prime_power(p, a):
    return (p**(a+1) - 1) // (p - 1)

ps = primes_upto(97)
tested = 0
for p in ps:
    for q in ps:
        for a in range(1, 9):
            A = sigma_prime_power(p, a)
            for b in range(1, 9):
                B = sigma_prime_power(q, b)
                lhs = Fraction(p**a, A) + Fraction(q**b, B)
                assert lhs != 1, (p, a, q, b)
                tested += 1

# Independent algebraic identity check on arbitrary sample parameters:
# AB - p^a B - q^b A = UV - p^a q^b.
for p in ps[:10]:
    for q in ps[:10]:
        for a in range(1, 6):
            for b in range(1, 6):
                pa, qb = p**a, q**b
                A, B = sigma_prime_power(p, a), sigma_prime_power(q, b)
                U, V = A-pa, B-qb
                assert A*B - pa*B - qb*A == U*V - pa*qb

# Final size contradiction for distinct primes and a>=2.
for p in ps:
    for q in ps:
        if p == q:
            continue
        for a in range(2, 9):
            left = (p-1)*(q-1)*p**(a-1)
            right = p**(a-1)-1
            assert left > right

print("VERIFY_OK", f"primes={len(ps)}", f"ordered_cases={tested}", "exponents=1..8", "algebra=passed", "size=passed")
