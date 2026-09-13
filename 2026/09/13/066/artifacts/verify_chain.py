"""Self-contained verifier for lane-1764 certificate (no external libraries needed).

Checks:
 1. W0 = floor(X0^0.53) via exact integer inequalities: W0^100 <= X0^53 < (W0+1)^100.
 2. The 10 chain integers are prime (trial division by all primes <= 1000005, generated
    by a simple sieve inside this script; since each candidate n <= 1000009163347
    < (1000005)^2 = 1000010000025 (hence also < 1000003*1000033 = 1000036000099),
    trial division up to 1000005 is a complete primality proof).
 3. Each chain pair has gap <= 80.
 4. Chain covering inequalities: b_0 <= X0; each next b <= a_prev + W0 + 1;
    a_last + W0 >= X0 + L. Together with x^theta >= W0 for x >= X0 this proves that
    every [x - x^0.53, x], X0 <= x <= X0+L, contains a prime pair with gap <= 80.

Usage: python3 verify_chain.py
"""
import json, math

X0 = 10**12; L = 10**7; W0 = 2290867; C = 80
CHAIN = [(999999999961,999999999989),(1000002290813,1000002290821),
         (1000004581663,1000004581673),(1000006872517,1000006872523),
         (1000009163341,1000009163347)]

# 1. W0 certificate
assert pow(W0,100) <= pow(X0,53), "W0^100 <= X0^53 failed"
assert pow(W0+1,100) > pow(X0,53), "(W0+1)^100 > X0^53 failed"
print("W0 = floor(X0^0.53) certified: OK")

# 2. primality by trial division (self-contained base sieve)
lim = 1000005
sv = bytearray(b'\x01')*(lim+1); sv[0]=sv[1]=0
for i in range(2,int(lim**0.5)+1):
    if sv[i]:
        sv[i*i:lim+1:i] = bytes(len(range(i*i,lim+1,i)))
base = [i for i in range(2,lim+1) if sv[i]]
def is_prime(n):
    for p in base:
        if p*p > n:
            return True
        if n % p == 0:
            return n == p
    return True
for a,b in CHAIN:
    assert b-a <= C and b-a >= 1
    assert is_prime(a), f"{a} composite!"
    assert is_prime(b), f"{b} composite!"
print("all 10 chain integers prime, all gaps<=80: OK")

# 3. covering
assert CHAIN[0][1] <= X0
F = CHAIN[0][0]+W0
for a,b in CHAIN[1:]:
    assert b <= F+1, (a,b,F)
    F = a+W0
assert F >= X0+L, (F, X0+L)
print(f"chain covers [X0,X0+L] (final reach {F} >= {X0+L}): OK")

# 4. monotonicity lemma (exact): for x>=X0, x^theta>=W0 since x^53>=X0^53>=W0^100
print("monotonicity lemma: x>=X0 -> x^0.53>=W0 (exact integer comparison): OK")
print("CERTIFICATE VALID: target claim is TRUE.")
