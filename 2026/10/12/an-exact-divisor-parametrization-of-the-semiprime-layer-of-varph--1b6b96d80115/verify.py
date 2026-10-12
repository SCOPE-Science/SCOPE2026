#!/usr/bin/env python3
from math import isqrt, gcd

LIMIT = 2_000_000

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p * p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    x = n
    out = []
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out.append((p, e))
    return out

def phi_from_factor(fac):
    ans = 1
    for p, e in fac:
        ans *= p ** (e - 1) * (p - 1)
    return ans

omega2_checked = 0
square_checks = 0
even_semiprime_checks = 0
odd_pair_checks = 0
hits = []

for n in range(2, LIMIT + 1):
    fac = factor(n)
    if sum(e for _, e in fac) != 2:
        continue
    omega2_checked += 1
    ph = phi_from_factor(fac)
    direct = ((n * n - 1) % ph == 0)

    if len(fac) == 1:
        p, e = fac[0]
        assert e == 2
        predicted = False
        square_checks += 1
    else:
        (p, ep), (q, eq) = fac
        assert ep == eq == 1 and p < q
        if p == 2:
            predicted = False
            even_semiprime_checks += 1
        else:
            odd_pair_checks += 1
            u = (p - 1) // 2
            v = (q - 1) // 2
            g = gcd(u, v)
            a = u // g
            b = v // g
            assert gcd(a, b) == 1 and a < b

            numerator = g * (a + b) + 1
            normalized = (a + b) % g == 0 and numerator % (a * b) == 0
            predicted = normalized

            if normalized:
                h = numerator // (a * b)
                assert h > 0
                assert (h * a - g) * (h * b - g) == g * g + h
                assert h <= (3 * g + 1) // 2
                assert q <= (p * p + 1) // 2

                r = h * a - g
                s = h * b - g
                assert 0 < r < s
                assert r * s == g * g + h
                assert (r + g) % h == 0 and (s + g) % h == 0
                aa = (r + g) // h
                bb = (s + g) // h
                assert (aa, bb) == (a, b)
                assert (a + b) % g == 0

    assert direct == predicted, (n, fac, ph, direct, predicted)
    if direct:
        hits.append(n)

expected_prefix = [15, 35, 65, 91, 377, 559, 2059, 12851]
assert hits[:len(expected_prefix)] == expected_prefix, hits[:12]

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"omega2_checked={omega2_checked}",
    f"square_checks={square_checks}",
    f"even_semiprime_checks={even_semiprime_checks}",
    f"odd_pair_checks={odd_pair_checks}",
    f"hits={len(hits)}",
    f"first_hits={hits[:12]}",
)
