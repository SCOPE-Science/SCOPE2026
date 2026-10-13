"""Exact independent checks for binomial-GCD prime-power layers.

Proof of the infinite asymptotic rests on the prime number theorem,
not on the finite checks below.
"""
import math


def prime_list(limit):
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00' * (((limit - p*p)//p) + 1)
    return [p for p in range(2, limit+1) if sieve[p]]


def layers_by_prime_power(X, primes=None):
    if primes is None:
        primes = prime_list(math.isqrt(X))
    counts = {}
    for p in primes:
        a = 2
        power = p*p
        while power <= X:
            cap = min(power, X // power)
            counts[a] = counts.get(a, 0) + cap - cap//p
            power *= p
            a += 1
    return counts


def trial_factor(n):
    result = []
    m = n
    for p in range(2, math.isqrt(m)+1):
        if m%p==0:
            a=0
            while m%p==0:
                m//=p
                a+=1
            result.append((p,a))
    if m>1:
        result.append((m,1))
    return result


def qualifying(n):
    factors = trial_factor(n)
    powers = [(p**a,p,a) for p,a in factors]
    # Direct source criterion from the exact components.
    nontrivial = any(A*A >= n for A,p,a in powers)
    no_large_prime = max(p for p,a in factors)**2 <= n
    layers = [a for A,p,a in powers if A*A >= n]
    assert len(layers) <= 1
    return (nontrivial and no_large_prime), (layers[0] if nontrivial and no_large_prime else None)


def direct_gcd(n):
    k = n-1
    out = 0
    for q in range(2, n+1):
        out = math.gcd(out, math.comb(q*k, k))
        if out == 1:
            break
    return out

# The direct binomial definition agrees with Guo et al.'s structural
# criterion, without needing their implementation.
for n in range(3, 151):
    g = direct_gcd(n)
    P = max(p**a for p,a in trial_factor(n))
    assert (g > 1) == (P*P >= n), (n, g, P)
    eligible, a = qualifying(n)
    if eligible:
        assert a is not None and a >= 2

# Independent census by trial factorization against the prime-power sum.
for X in [10, 100, 1000, 10000, 20000]:
    direct = {}
    for n in range(3, X+1):
        ok, a = qualifying(n)
        if ok:
            direct[a] = direct.get(a, 0) + 1
    exact = layers_by_prime_power(X)
    assert direct == exact, (X, direct, exact)

# Large integer-only computations: no floating-point use in counts.
checks = {}
for X in [10**6, 10**9, 10**12]:
    counts = layers_by_prime_power(X)
    checks[X] = (sum(counts.values()), counts.get(2, 0), counts.get(3,0))

assert checks[10**6] == (15198, 9117, 2080), checks[10**6]
assert checks[10**9] == (1640126, 1252863, 174315), checks[10**9]
assert checks[10**12] == (201954460, 176088644, 14699180), checks[10**12]

print('VERIFY_OK direct_gcd_n=3..150 brute_census_X=10,100,1000,10000,20000')
for X,(total,a2,a3) in checks.items():
    print(f'EXACT X={X} E={total} E2={a2} E3={a3}')
