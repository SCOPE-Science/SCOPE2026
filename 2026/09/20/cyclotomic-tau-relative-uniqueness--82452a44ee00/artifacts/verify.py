from math import isqrt

N = 1_000_000
CASES = [(3,1),(3,2),(3,3),(7,1),(7,2),(11,1),(19,1)]


def divisor_counts(limit):
    spf = list(range(limit + 1))
    spf[1] = 1
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    tau = [1] * (limit + 1)
    tau[0] = 0
    for n in range(2, limit + 1):
        p = spf[n]
        m = n
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        tau[n] = tau[m] * (e + 1)
    return tau


def phi_2pk_mod(n, p, k, modulus):
    """Return Phi_{2 p^k}(n) modulo modulus for odd prime p."""
    if modulus == 1:
        return 0
    y = pow(n, p ** (k - 1), modulus)
    value = 0
    for j in range(p):
        value = (value * y + (1 if j % 2 == 0 else -1)) % modulus
    return value


tau = divisor_counts(N)
print(f"range=2..{N}")
for p, k in CASES:
    hits = [n for n in range(2, N + 1) if phi_2pk_mod(n, p, k, tau[n]) == 0]
    print(f"p={p} k={k} nontrivial_hits={len(hits)} first_hits={hits[:5]}")
