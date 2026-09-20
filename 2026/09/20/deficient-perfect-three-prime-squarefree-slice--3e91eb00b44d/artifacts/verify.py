from math import isqrt

MAX_PARAM_A = 12
MAX_BRUTE_A = 7

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = isqrt(n)
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True

def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        old = ds[:]
        mul = 1
        for _ in range(e):
            mul *= p
            ds += [x * mul for x in old]
    return sorted(ds)

def direct_deficiency(a, p, q):
    m = (1 << (a + 1)) - 1
    return p * q - m * (p + q + 1)

def parametrized(a):
    m = (1 << (a + 1)) - 1
    ans = set()
    for e in range(a + 1):
        A = m * (m + 1) + (1 << e)
        for s in divisors(A):
            if s * s >= A:
                continue
            p = m + s
            q = m + A // s
            if is_prime(p) and is_prime(q) and p < q:
                d = 1 << e
                assert direct_deficiency(a, p, q) == d
                ans.add((p, q, d))

        B = (1 << (a + 1)) + (1 << e)
        for s in divisors(B):
            k = B // s
            if k < 2:
                continue
            p = m + s
            q = k * p - 1
            if is_prime(p) and is_prime(q) and p < q:
                d = (1 << e) * p
                assert direct_deficiency(a, p, q) == d
                ans.add((p, q, d))
    return ans

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]

def brute(a):
    m = (1 << (a + 1)) - 1
    Amax = m * (m + 1) + (1 << a)
    Bmax = (1 << (a + 1)) + (1 << a)
    p_bound = m + max(isqrt(Amax) + 1, Bmax // 2)
    q_bound = 15 * (1 << (2 * a))
    ps = [p for p in primes_upto(q_bound) if p > m and p <= p_bound and p % 2]
    qs = [q for q in primes_upto(q_bound) if q % 2]
    ans = set()
    for p in ps:
        for q in qs:
            if q <= p:
                continue
            d = direct_deficiency(a, p, q)
            if d <= 0:
                continue
            n = (1 << a) * p * q
            if n % d == 0:
                ans.add((p, q, d))
    return ans

print('Parametrized counts for a=1..%d:' % MAX_PARAM_A)
all_count = 0
for a in range(1, MAX_PARAM_A + 1):
    vals = parametrized(a)
    all_count += len(vals)
    print(a, len(vals))
print('total', all_count)

print('Brute-force cross-check for a=1..%d:' % MAX_BRUTE_A)
for a in range(1, MAX_BRUTE_A + 1):
    x = parametrized(a)
    y = brute(a)
    print(a, len(x), len(y), 'OK' if x == y else 'MISMATCH')
    assert x == y

print('First solutions by a:')
for a in range(1, 7):
    vals = sorted(parametrized(a), key=lambda t: (1 << a) * t[0] * t[1])
    print(a, [((1 << a) * p * q, p, q, d) for p, q, d in vals])
