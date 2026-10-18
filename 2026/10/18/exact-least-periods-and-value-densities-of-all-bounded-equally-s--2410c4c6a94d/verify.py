#!/usr/bin/env python3
"""Reproduce exact finite checks for shifted Fibonacci gcd periods and densities.
Only the Python standard library is needed. General results follow from the proof.
"""
from fractions import Fraction
from math import gcd, lcm


def divisors(n):
    out = []
    for d in range(1, n + 1):
        if d * d > n:
            break
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def mobius(n):
    if n == 1:
        return 1
    ans = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            ans = -ans
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans = -ans
    return ans


def totient(n):
    out = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            out -= out // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out -= out // n
    return out


def local_progression(d, a):
    """Return (c, L, z, h, u) or None for the event d | G_a(n)."""
    if d == 1:
        return (0, 1, 1, 1, 1)
    prev, cur = 0, 1
    for z in range(1, 6 * d + 6):
        prev, cur = cur, (prev + cur) % d
        if prev % d == 0:
            break
    else:
        raise AssertionError(('rank not found', d))
    u = cur % d
    assert gcd(u, d) == 1
    h, power = 1, u
    while power != 1:
        power = (power * u) % d
        h += 1
        assert h <= 4
    assert pow(u, 2, d) == ((-1) ** z) % d
    power = 1
    for j in range(h):
        if power == (-a) % d:
            return ((1 + j * z) % (z * h), z * h, z, h, u)
        power = power * u % d
    return None


def check(a):
    nbound = a**4 - 1
    ds = divisors(nbound)
    events = {d: local_progression(d, a) for d in ds}
    assert events[1][1] == 1
    period = 1
    for evt in events.values():
        if evt is not None:
            period = lcm(period, evt[1])
    assert period < 6000
    # Independent successive Fibonacci recurrence: no reliance on event formula.
    f, fnext = 1, 1
    observed = []
    for n in range(1, period + 1):
        actual = gcd(f + a, fnext + a)
        # f and fnext are only maintained modulo nbound, sufficient for gcd | nbound.
        actual = gcd(nbound, actual)
        from_events = sum(totient(d) for d, evt in events.items()
                          if evt is not None and n % evt[1] == evt[0])
        assert actual == from_events, (a, n, actual, from_events)
        for d, evt in events.items():
            detected = (actual % d == 0)
            predicted = (evt is not None and n % evt[1] == evt[0])
            assert detected == predicted, (a, d, n)
        observed.append(actual)
        f, fnext = fnext, (f + fnext) % nbound
    assert all(observed[n] == observed[(n + period) % period]
               for n in range(period))
    # Every proper divisor of P fails as a period: exact minimality on the full P-cycle.
    for shorter in divisors(period):
        if shorter == period:
            continue
        assert any(observed[n] != observed[(n + shorter) % period]
                   for n in range(period)), (a, shorter)
    actual_count = {d: observed.count(d) for d in ds}
    assert sum(actual_count.values()) == period
    for q in ds:
        density = sum((Fraction(mobius(d // q), evt[1])
                       for d, evt in events.items()
                       if d % q == 0 and evt is not None), Fraction())
        assert density == Fraction(actual_count[q], period), (a, q, density, actual_count[q])
    assert sum(actual_count.values()) == period
    return period, {d: cnt for d, cnt in actual_count.items() if cnt}


def main():
    total = 0
    for magnitude in range(2, 13):
        for a in (magnitude, -magnitude):
            p, histogram = check(a)
            print(f'a={a:+d}; N={a**4-1}; least_period={p}; '
                  f'distinct_values={len(histogram)}; counts={histogram}')
            total += 1
    print(f'VERIFY_OK: {total} signed shifts, complete least-period and density replay')


if __name__ == '__main__':
    main()
