"""Exact checks of first-level preimage rigidity and square-failure densities."""
from math import gcd


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def active_factors(h):
    ans = []
    for p in range(2, h + 1):
        if h % p or not prime(p):
            continue
        a = 0
        v = h
        while v % p == 0:
            a += 1
            v //= p
        if p == 2 or p % 20 in (13, 17):
            ans.append((p, a, 1 if p == 2 else 2))
        else:
            assert p % 4 == 3, (h, p)
    return ans


def late_zero(p, t):
    seen = set()
    z = t
    for n in range(p + 2):
        if z in seen:
            return False
        seen.add(z)
        if z == 0:
            return n >= 2
        z = None if z is None or z == 0 else (z + pow(z, -1, p)) % p
        if z is None:
            return False
    raise AssertionError('Orbit did not close')


active_primes = [2] + [p for p in range(3, 501) if prime(p) and p % 20 in (13, 17)]
for p in active_primes:
    assert all(not late_zero(p, e) for e in range(p))
    first = sum((e * e + 1) % p == 0 for e in range(p))
    assert first == (1 if p == 2 else 2)

checks = []
for h in (1, 3, 13, 17, 26, 39, 169, 221):
    facts = active_factors(h)
    period = 1
    no_bad = 1
    for p, a, r in facts:
        m = p ** (a + 1)
        period *= m
        no_bad *= m - r
    observed_bad = 0
    for x0 in range(1, period + 1):
        g = gcd(x0, h)
        u, v = x0 // g, h // g
        first_bad = gcd(h, u*u + v*v) > 1
        observed_bad += first_bad
        # Modular homogeneous iteration avoids integer blowup.
        u, v = u % h, v % h
        for j in range(1, 8):
            u, v = (u*u + v*v) % h, (u*v) % h
            if j >= 2:
                assert gcd(u, h) == 1, (h, x0, j)
    assert observed_bad == period - no_bad, (h, observed_bad, period, no_bad)
    checks.append((h, period, no_bad, observed_bad))

assert (221, 48841, 47929, 912) in checks
assert (26, 676, 501, 175) in checks
print('CERTIFICATE_OK checked_active_primes=', len(active_primes))
for h, mod, no_bad, one_bad in checks:
    print('h=%d period=%d zero_failures=%d one_failure=%d' % (h, mod, no_bad, one_bad))
