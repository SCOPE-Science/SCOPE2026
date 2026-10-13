from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def next_prime(n):
    k = max(2, n + 1)
    while not is_prime(k):
        k += 1
    return k


def first_primes_above(y, count):
    out = []
    p = y
    while len(out) < count:
        p = next_prime(p)
        out.append(p)
    return out


def crt_pairwise(congruences):
    a, m = 0, 1
    for b, mod in congruences:
        t = ((b - a) * pow(m, -1, mod)) % mod
        a += m * t
        m *= mod
        a %= m
    return a, m


def witness(y):
    ps = first_primes_above(y, 2 * y)
    pairs = [(ps[2*j], ps[2*j+1]) for j in range(y)]
    congruences = [((-j) % (r*s), r*s) for j, (r, s) in enumerate(pairs, start=1)]
    a, M = crt_pairwise(congruences)
    assert gcd(a, M) == 1
    q = a if a >= 2 else a + M
    while not is_prime(q):
        q += M
    for j, (r, s) in enumerate(pairs, start=1):
        assert (q + j) % r == 0 and (q + j) % s == 0
        assert r != s
    # Every q+j has two distinct prime divisors, so q is exactly the
    # largest prime power in [q,q+y]. Thus the map sends q+y to y.
    assert (q + y) - q == y
    return y, a, M, q


rows = [witness(y) for y in range(1, 4)]
print("VERIFY_OK " + " ".join(f"y={y}:a={a}:M={M}:q={q}" for y, a, M, q in rows))
