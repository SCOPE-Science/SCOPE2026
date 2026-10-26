"""Reproducible arithmetic checks for the product-multiple cutoff theorem."""
from math import gcd


def primitive_t(a, b, k):
    """Primitive nonnegative solution iff some 0<=t<=k has gcd one."""
    assert a >= 2 and b >= 2 and gcd(a, b) == 1
    return [t for t in range(k + 1) if gcd(b * (k-t), a * t) == 1]


def factorizations(n):
    fac = []
    for p in range(2, n + 1):
        if n % p == 0 and all(p % d for d in range(2, int(p**0.5) + 1)):
            fac.append(p)
    return fac


def exact_criterion(a, b, k, t):
    return gcd(k, t) == gcd(a, k-t) == gcd(b, t) == 1


def check():
    tests = 0
    for a in range(2, 121):
        for b in range(2, 121):
            if gcd(a, b) != 1:
                continue
            for k in range(2, 16):
                ts = primitive_t(a, b, k)
                assert ts, (a, b, k)
                for t in range(k + 1):
                    assert (t in ts) == exact_criterion(a, b, k, t)
                tests += 1
    a, b, k = 273, 55, 16
    assert gcd(a,b) == 1 and a*b*k == 240240
    assert not primitive_t(a,b,k)
    # A direct, independent enumeration of all coefficient solutions.
    raw = []
    for y in range((a*b*k)//b + 1):
        x, rem = divmod(a*b*k - b*y, a)
        if rem == 0 and x >= 0:
            raw.append((x,y))
    expected = [(b*(k-t),a*t) for t in range(k+1)]
    assert set(raw) == set(expected) and len(raw) == k+1
    assert all(gcd(x,y)>1 for x,y in raw)
    for m in range(1, 101):
        if gcd(m, 273) == 1:
            assert not primitive_t(273,55*m,16)
    print('VERIFY_OK', tests, 'all-coefficient witness', len(raw))

if __name__ == '__main__':
    check()
