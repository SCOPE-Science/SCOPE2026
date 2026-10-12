#!/usr/bin/env python3
from math import isqrt

R = 113322
c = 797
p = 157

def sieve(n):
    a = bytearray(b"\x01") * (n + 1)
    a[:2] = b"\x00\x00"
    for q in range(2, isqrt(n) + 1):
        if a[q]:
            a[q*q:n+1:q] = b"\x00" * (((n - q*q)//q) + 1)
    return a

R1 = R * p
c1 = c * p - R
assert R1 == 17791554
assert c1 == 11807

q_lo = R1 // c1 + 1
q_hi = (3 * R1) // c1
assert (q_lo, q_hi) == (1507, 4520)

# The largest possible r occurs at the smallest admissible prime q.
# A small preliminary sieve through a safe global ceiling covers q, r, and s
# once an integral candidate is produced.
prime = sieve(1_200_000)

q_count = 0
r_count = 0
integral_candidates = []
solutions = []

for q in range(q_lo, q_hi + 1):
    if not prime[q]:
        continue
    q_count += 1
    c2 = c1 * q - R1
    R2 = R1 * q
    assert c2 > 0

    # From s > r > q and c2*r*s - R2*(r+s)=1:
    # R2/c2 < r <= 2*R2/c2.
    r_lo = max(q + 1, R2 // c2 + 1)
    r_hi = (2 * R2) // c2
    assert r_hi < len(prime)

    for r in range(r_lo, r_hi + 1):
        if not prime[r]:
            continue
        r_count += 1
        den = c2 * r - R2
        num = R2 * r + 1
        assert den > 0
        if num % den:
            continue
        s = num // den
        integral_candidates.append((q, r, s))
        if s > r and s < len(prime) and prime[s]:
            solutions.append((q, r, s))

assert q_count == 375
assert r_count == 242779
assert integral_candidates == [(1979, 10093, 16879)]
assert solutions == [(1979, 10093, 16879)]

q, r, s = solutions[0]
B = p*q*r*s
partial = q*r*s + p*r*s + p*q*s + p*q*r
assert B == 52931284472141
assert c*B - R*partial == 1

print(
    "VERIFY_OK "
    "q_primes=375 r_primes=242779 integral_candidates=1 "
    "solution=157*1979*10093*16879 "
    "filling_identity=yes"
)
