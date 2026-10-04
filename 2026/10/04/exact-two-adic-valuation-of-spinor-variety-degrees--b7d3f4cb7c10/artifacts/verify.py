from math import factorial
from functools import lru_cache

def degree_product(n):
    M = n * (n + 1) // 2
    num = factorial(M)
    for a in range(2, n):
        num *= factorial(a)
    den = 1
    for a in range(2, n + 1):
        den *= factorial(2 * a - 1)
    assert num % den == 0
    return num // den

def v2(x):
    assert x > 0
    r = 0
    while x % 2 == 0:
        x //= 2
        r += 1
    return r

def s2(x):
    return x.bit_count()

def removable(lam):
    out = []
    L = list(lam)
    for i, x in enumerate(L):
        y = x - 1
        if y == 0:
            if i == len(L) - 1:
                out.append(tuple(L[:-1]))
            continue
        prev = L[i - 1] if i else 10**9
        nxt = L[i + 1] if i + 1 < len(L) else 0
        if prev > y > nxt:
            K = L.copy()
            K[i] = y
            out.append(tuple(K))
    return out

@lru_cache(None)
def chain_count(lam):
    if not lam:
        return 1
    return sum(chain_count(mu) for mu in removable(lam))

chain_checks = 0
for n in range(1, 16):
    rho = tuple(range(n, 0, -1))
    assert chain_count(rho) == degree_product(n)
    chain_checks += 1

valuation_checks = 0
for n in range(1, 201):
    M = n * (n + 1) // 2
    d = degree_product(n)
    assert v2(d) == n - s2(M)
    assert (d % 2 == 1) == (n in (1, 2))
    assert (d % 4 == 2) == (n in (3, 5))
    valuation_checks += 1

assert degree_product(3) == 2
assert degree_product(4) == 12
assert degree_product(5) == 286
assert degree_product(6) == 33592

print('VERIFY_OK', chain_checks, valuation_checks)
