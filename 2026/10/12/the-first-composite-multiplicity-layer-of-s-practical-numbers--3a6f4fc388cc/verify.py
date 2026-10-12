from math import isqrt

LIMIT = 1_000_000

# Smallest-prime-factor sieve.
spf = [0] * (LIMIT + 1)
for i in range(2, LIMIT + 1):
    if spf[i] == 0:
        spf[i] = i
        if i <= isqrt(LIMIT):
            for j in range(i * i, LIMIT + 1, i):
                if spf[j] == 0:
                    spf[j] = i


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


def aliquot_weights_from_factors(fac):
    # Build (d, sigma(d)) for every divisor d of n from the known factorization.
    pairs = [(1, 1)]
    for p, e in fac:
        old = pairs
        pairs = []
        pp = 1
        geom = 1
        for a in range(e + 1):
            for d, sig in old:
                pairs.append((d * pp, sig * geom))
            pp *= p
            geom += pp
    return sorted(sig - d for d, sig in pairs if sig - d > 0)


def complete(weights):
    total = 0
    for w in weights:
        if w > total + 1:
            return False
        total += w
    return True


def spractical_from_factors(fac):
    return complete(aliquot_weights_from_factors(fac))

low = []
for n in range(4, LIMIT + 1):
    fac = factor(n)
    omega_big = sum(e for _, e in fac)
    if omega_big > 4:
        continue
    # Composite exactly when Omega(n) >= 2.
    if omega_big >= 2 and spractical_from_factors(fac):
        low.append(n)

assert low == [60], low
weights60 = aliquot_weights_from_factors(factor(60))
assert weights60 == [1, 1, 1, 3, 6, 8, 9, 16, 22, 42, 108]
assert complete(weights60)

# Exact small candidate failures used in the symbolic case split.
failed = [12, 24, 36, 84, 90, 100, 126, 198]
assert all(not spractical_from_factors(factor(n)) for n in failed)

print(
    "VERIFY_OK "
    f"limit={LIMIT} "
    "omega_le4_composite_s_practical=60 "
    "s60_weights=" + ",".join(map(str, weights60))
)
