"""Independent bounded arithmetic replay after checking the analytic reductions."""
from math import isqrt

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def valuation(x, p):
    count = 0
    while x % p == 0:
        count += 1
        x //= p
    return count

def divisor_sum(a):
    return sum(128**j for j in range(a))

assert 5**15 > divisor_sum(5)
assert 3**17 * 127 >= 2**28
assert 3**19 > sum(2**(4*j) for j in range(7))
assert 3**23 > sum(2**(5*j) for j in range(7))
for v, beta, last_lambda, count, maximum in [(2,12,4,8,1),(3,8,25,62,1),(4,16,4,33,2)]:
    cases = []
    for lam in range(2, last_lambda + 1):
        for q in range(1, 3 * 2**(v-1), 2):
            p = q * 2**lam - 1
            if not prime(p) or p == 7:
                continue
            for alpha in range(2, lam + v + 1):
                if p < 3 * 2**(alpha-1) - 1:
                    cases.append((alpha, p, valuation(divisor_sum(alpha), p)))
    assert len(cases) == count
    assert max(c[2] for c in cases) == maximum < beta - 1
    print(v, beta, len(cases), max(c[2] for c in cases))
constants = {1:[43,127],2:[127],3:[14197],4:[7],5:[29,2129]}
for t, primes in constants.items():
    c = sum(4**i * t**(6-i) for i in range(7))
    assert all(prime(p) for p in primes)
    while c % 2 == 0:
        c //= 2
    for p in primes:
        while c % p == 0:
            c //= p
        if p not in (7,127):
            assert (p+1) % t or ((p+1)//t) & (((p+1)//t)-1)
    assert c == 1
print('VERIFY_OK: bounded cases and beta-four factor exclusions')
