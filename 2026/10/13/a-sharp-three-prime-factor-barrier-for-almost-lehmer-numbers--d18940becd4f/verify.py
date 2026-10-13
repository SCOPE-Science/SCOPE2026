from math import gcd, isqrt

LIMIT = 5000

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]

def squarefree(n):
    d = 2
    while d*d <= n:
        if n % (d*d) == 0:
            return False
        d += 1
    return True

def almost_semiprime(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    d = phi // gcd(phi, n-1)
    return squarefree(d) and (n-1) % d == 0

P = [p for p in primes_upto(LIMIT) if p % 2]
pairs = 0
bad = []
for i,p in enumerate(P):
    for q in P[i+1:]:
        pairs += 1
        if almost_semiprime(p,q):
            bad.append((p,q))
if bad:
    raise SystemExit(f'FAIL semiprime counterexamples={bad[:5]}')

n = 1729
phi = (7-1)*(13-1)*(19-1)
d = phi // gcd(phi,n-1)
assert d == 3
assert squarefree(d) and (n-1) % d == 0
assert (3*(n-1)) % phi == 0
print(f'VERIFY_OK semiprime_pairs={pairs} max_prime={LIMIT} sharp_witness={n} denominator={d}')
