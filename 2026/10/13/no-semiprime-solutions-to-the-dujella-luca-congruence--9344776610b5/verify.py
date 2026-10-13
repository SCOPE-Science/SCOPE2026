#!/usr/bin/env python3
LIMIT = 2_000_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def phi_sigma_from_factor(fac):
    phi = 1
    sig = 1
    for p, e in fac:
        phi *= p ** (e - 1) * (p - 1)
        sig *= (p ** (e + 1) - 1) // (p - 1)
    return phi, sig

spf = spf_table(LIMIT)
omega = [0] * (LIMIT + 1)
for n in range(2, LIMIT + 1):
    omega[n] = omega[n // spf[n]] + 1

composite_hits = []
semiprime_hits = []
low_checked = 0
prime_hits = 0

for n in range(1, LIMIT + 1):
    if omega[n] > 2:
        continue
    low_checked += 1
    fac = factor(n, spf)
    phi, sig = phi_sigma_from_factor(fac)
    ok = (n * phi - 2) % sig == 0
    is_prime = len(fac) == 1 and fac[0][1] == 1
    if is_prime:
        assert ok
        prime_hits += 1
    elif n == 1:
        assert ok
    elif ok:
        composite_hits.append(n)
        if len(fac) == 2 and all(e == 1 for _, e in fac):
            semiprime_hits.append(n)

assert composite_hits == [9], composite_hits
assert semiprime_hits == [], semiprime_hits

# Finite checks of the algebraic reductions.
primes = [p for p in range(2, 5000) if spf[p] == p]
square_checks = 0
for p in primes:
    D = p * p + p + 1
    lhs = (p * p) * (p * (p - 1)) - 2
    assert (lhs % D == 0) == ((p - 3) % D == 0)
    square_checks += 1

pair_checks = 0
for i, p in enumerate(primes[:120]):
    for q in primes[i + 1:i + 20]:
        if p == 2:
            rem = (2 * q * (q - 1) - 2) % (q + 1)
            assert rem == 2 % (q + 1)
        else:
            A = p * q * (p - 1) * (q - 1) - 2
            assert A % (q + 1) == (2 * (p * p - p - 1)) % (q + 1)
            assert A % (p + 1) == (2 * (q * q - q - 1)) % (p + 1)
        pair_checks += 1

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"low_omega_checked={low_checked}",
    f"prime_hits={prime_hits}",
    f"composite_hits={composite_hits}",
    f"semiprime_hits={semiprime_hits}",
    f"square_checks={square_checks}",
    f"pair_checks={pair_checks}",
)
