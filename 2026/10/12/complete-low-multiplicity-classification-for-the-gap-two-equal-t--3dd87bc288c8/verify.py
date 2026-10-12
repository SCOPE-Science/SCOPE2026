#!/usr/bin/env python3
"""Finite regression checks for the low-multiplicity equal-totient classification."""

LIMIT = 1_000_000

def build_spf(n):
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    i = 2
    while i * i <= n:
        if spf[i] == i:
            j = i * i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1
    return spf

def factor(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p, a))
    return out

def omega(n, spf):
    return sum(a for _, a in factor(n, spf))

def phi(n, spf):
    ans = n
    for p, _ in factor(n, spf):
        ans = ans // p * (p - 1)
    return ans

def params_to_primes(A, B):
    nums = (
        A * B - A - B + 3,
        A * B + A - B + 1,
        A * B - A + B + 1,
        A * B + A + B + 3,
    )
    assert all(x % 2 == 0 for x in nums)
    return tuple(x // 2 for x in nums)

def invert(p, q, r, s):
    d = q - p
    e = s - r
    assert e > d >= 0
    assert (e - d) % 2 == 0 and (e + d) % 2 == 0
    return (e - d) // 2, (e + d) // 2

# Pure algebra regression on a parameter grid.
for A in range(3, 202, 2):
    for B in range(A + 2, 252, 2):
        r, p, q, s = params_to_primes(A, B)
        assert r + s == p + q + 2
        assert r * s == p * q + 2
        assert p - r == A - 1
        assert q - r == B - 1
        assert invert(p, q, r, s) == (A, B)

spf = build_spf(LIMIT + 2)
hits = []
parameter_hits = []

for n in range(1, LIMIT + 1):
    if omega(n, spf) > 2 or omega(n + 2, spf) > 2:
        continue
    if phi(n, spf) != phi(n + 2, spf):
        continue
    hits.append(n)
    if n in (4, 7):
        continue

    f1 = factor(n, spf)
    f2 = factor(n + 2, spf)
    assert len(f1) == 2 and all(a == 1 for _, a in f1)
    assert len(f2) == 2 and all(a == 1 for _, a in f2)

    p, q = [x for x, _ in f1]
    r, s = [x for x, _ in f2]
    assert p < q and r < s
    A, B = invert(p, q, r, s)
    assert A >= 3 and A < B and A % 2 == B % 2 == 1
    rr, pp, qq, ss = params_to_primes(A, B)
    assert (rr, pp, qq, ss) == (r, p, q, s)
    parameter_hits.append((n, A, B))

expected = [4, 7, 6497, 12317, 133787, 181427, 404471, 439097, 485237]
assert hits == expected

print(
    "VERIFY_OK "
    f"limit={LIMIT} "
    f"hits={','.join(map(str, hits))} "
    "parameters="
    + ";".join(f"{n}:{A},{B}" for n, A, B in parameter_hits)
)
