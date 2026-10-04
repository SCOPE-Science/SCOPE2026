#!/usr/bin/env python3
import math

LIMIT = 1_000_000

# Smallest-prime-factor sieve.
spf = list(range(LIMIT + 1))
for p in range(2, int(LIMIT ** 0.5) + 1):
    if spf[p] == p:
        for n in range(p * p, LIMIT + 1, p):
            if spf[n] == n:
                spf[n] = p

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def direct_arithmetic_squarefree(n):
    fac = factor(n)
    if any(e != 1 for _, e in fac):
        return None
    tau = 1
    sigma = 1
    for p, _ in fac:
        tau *= 2
        sigma *= p + 1
    return sigma % tau == 0

def structural_squarefree(n):
    fac = factor(n)
    if any(e != 1 for _, e in fac):
        return None
    if n % 2 == 1:
        return True
    return any(p % 4 == 3 for p, _ in fac)

squarefree = 0
exceptions = 0
checkpoint_counts = {10_000: 0, 100_000: 0, 1_000_000: 0}
for n in range(1, LIMIT + 1):
    structural = structural_squarefree(n)
    if structural is None:
        continue
    squarefree += 1
    direct = direct_arithmetic_squarefree(n)
    if direct != structural:
        raise AssertionError((n, direct, structural))
    if not structural:
        exceptions += 1
    for x in checkpoint_counts:
        if n == x:
            checkpoint_counts[x] = exceptions

# The loop only updates a checkpoint when n itself is square-free, so recompute exact
# prefix counts in one pass over the already available criterion.
for x in list(checkpoint_counts):
    checkpoint_counts[x] = sum(
        1 for n in range(1, x + 1) if structural_squarefree(n) is False
    )

# Truncated Euler product for the Landau-Ramanujan constant.
is_prime = bytearray(b'\x01') * (LIMIT + 1)
is_prime[:2] = b'\x00\x00'
for p in range(2, int(LIMIT ** 0.5) + 1):
    if is_prime[p]:
        is_prime[p * p:LIMIT + 1:p] = b'\x00' * (((LIMIT - p * p) // p) + 1)
P3 = 1.0
for p in range(3, LIMIT + 1, 2):
    if is_prime[p] and p % 4 == 3:
        P3 *= 1.0 - 1.0 / (p * p)
K_lr = 1.0 / math.sqrt(2.0 * P3)
coefficient = 2.0 * K_lr / (math.pi ** 2)

for x in sorted(checkpoint_counts):
    e = checkpoint_counts[x]
    normalized = e * math.sqrt(math.log(x)) / x
    print(f"CHECK x={x} exceptions={e} normalized={normalized:.9f}")

assert squarefree == 607_926
assert exceptions == 42_186
assert abs(coefficient - 0.15486409) < 2e-8
print(
    f"VERIFY_OK limit={LIMIT} squarefree={squarefree} "
    f"exceptions={exceptions} coefficient≈{coefficient:.8f}"
)
