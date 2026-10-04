import math


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(n ** 0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b"\x00" * (((n - q*q) // q) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def r_p(k, p):
    r = 1
    power = p
    while power <= k:
        r += 1
        power *= p
    return r


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


k_cases = 0
valuation_pairs = 0
deficiency_cases = 0
for k in range(2, 121):
    ps = primes_upto(k)
    rs = {p: r_p(k, p) for p in ps}
    M = math.prod(p ** rs[p] for p in ps)
    C = math.comb(M + k - 1, k)
    for p in ps:
        got = valuation(C, p)
        want = rs[p] - valuation(k, p)
        assert got == want, (k, p, got, want)
        assert got >= 1
        valuation_pairs += 1

    smooth_offsets = []
    for i in range(k):
        y = M + i
        for p in ps:
            while y % p == 0:
                y //= p
        if y == 1:
            smooth_offsets.append(i)
    assert smooth_offsets == [0], (k, smooth_offsets)
    deficiency_cases += 1
    k_cases += 1

print(f"VERIFY_OK k_cases={k_cases} valuation_pairs={valuation_pairs} deficiency_cases={deficiency_cases}")
