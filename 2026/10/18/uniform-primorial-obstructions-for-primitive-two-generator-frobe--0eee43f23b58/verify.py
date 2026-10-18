"""Exact finite checks for a CRT obstruction in primitive two-generator representations."""
import math
import random


def primes(n):
    ps = []
    candidate = 2
    while len(ps) < n:
        if all(candidate % p for p in ps if p*p <= candidate):
            ps.append(candidate)
        candidate += 1
    return ps


def crt(congruences):
    """Return the representative in [1, product moduli]."""
    x, modulus = 0, 1
    for p, r in congruences:
        offset = ((r-x) * pow(modulus, -1, p)) % p
        x += modulus * offset
        modulus *= p
    assert 0 <= x < modulus
    return x or modulus


def witness(a,b,k):
    assert math.gcd(a,b) == 1 and k >= 2
    ps = primes(k - 1)
    M = math.prod(ps)
    assert min(a,b) > M
    c = crt([(p,t*b) for t,p in enumerate(ps, 1)])
    d = crt([(p,(k-t)*a) for t,p in enumerate(ps, 1)])
    n = k*a*b - a*c - b*d
    assert 1 <= c <= M < b and 1 <= d <= M < a
    assert n >= k*a*b-M*(a+b) and n > 0
    assert n % M == 0
    for t,p in enumerate(ps,1):
        x,y = t*b-c,(k-t)*a-d
        assert x>=0 and y>=0
        assert a*x+b*y == n
        assert x % p == 0 and y % p == 0
        assert math.gcd(x,y)>1
    return n, M, c, d


def independent_brute(a,b,n):
    """Enumerate every possible nonnegative representation independently."""
    representations = []
    for y in range(n//b+1):
        remaining = n-b*y
        if remaining % a == 0:
            x=remaining//a
            representations.append((x,y,math.gcd(x,y)))
    assert representations
    assert all(g>1 for x,y,g in representations)
    return len(representations)

rng = random.Random(20261015)
crt_cases=0
exhaustive_cases=0
representations=0
for k in range(2,8):
    M = math.prod(primes(k-1))
    cases=[(M+1,M+2),(M+2,M+3),(M+1,2*M+1)]
    cases += [(M+rng.randrange(1,500),M+rng.randrange(1,500)) for _ in range(120)]
    for a,b in cases:
        if math.gcd(a,b)>1: continue
        n,mm,c,d=witness(a,b,k)
        crt_cases +=1
        if k<=6 and exhaustive_cases < 150:
            representations += independent_brute(a,b,n)
            exhaustive_cases+=1
for a,b in [(413,415),(413,414),(412,413),(500,1001),(10000,10001)]:
    assert math.gcd(a,b)==1
    n,mm,_,_=witness(a,b,5)
    assert mm==210
    assert n >= 4*(a*b-a-b)
print(f'VERIFY_OK crt_cases={crt_cases} independent_exhaustive_cases={exhaustive_cases} nonprimitive_representations={representations} threshold_pairs=5')
