from math import factorial

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

def multiplicities(lam):
    out = {}
    for x in lam:
        out[x] = out.get(x, 0) + 1
    return out

def vp(n, p):
    v = 0
    while n % p == 0 and n:
        v += 1
        n //= p
    return v

def s_p(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s

def prime_list(N):
    out = []
    for x in range(2, N+1):
        if all(x % q for q in range(2, int(x**0.5)+1)):
            out.append(x)
    return out

def degree_primal(lam):
    m = multiplicities(lam)
    d = len(lam)
    num = factorial(d)
    for e in m.values():
        num //= factorial(e)
    for j, e in m.items():
        num *= j ** e
    return num

def degree_dual(lam):
    assert 1 not in lam
    m = multiplicities(lam)
    d = len(lam)
    num = factorial(d+1)
    for e in m.values():
        num //= factorial(e)
    for j, e in m.items():
        num *= (j-1) ** e
    return num

primes = prime_list(29)
primal_checks = dual_checks = 0

for n in range(1, 29):
    for lam in partitions(n):
        m = multiplicities(lam)
        d = len(lam)
        deg = degree_primal(lam)
        for p in primes:
            pred = (sum(s_p(e,p) for e in m.values()) - s_p(d,p)) // (p-1)
            pred += sum(e * vp(j,p) for j,e in m.items())
            assert vp(deg,p) == pred, (lam,p,deg,vp(deg,p),pred)

            carry_free = (sum(s_p(e,p) for e in m.values()) == s_p(d,p))
            local_units = all(j % p for j in m)
            assert (deg % p != 0) == (carry_free and local_units)
            primal_checks += 1

        if 1 not in lam:
            ddeg = degree_dual(lam)
            shifted = tuple(x-1 for x in lam)
            assert ddeg == (d+1) * degree_primal(shifted)
            for p in primes:
                pred = vp(d+1,p)
                pred += (sum(s_p(e,p) for e in m.values()) - s_p(d,p)) // (p-1)
                pred += sum(e * vp(j-1,p) for j,e in m.items())
                assert vp(ddeg,p) == pred, (lam,p,ddeg,vp(ddeg,p),pred)

                carry_free = (sum(s_p(e,p) for e in m.values()) == s_p(d,p))
                local_units = all((j-1) % p for j in m)
                expected_unit = ((d+1) % p != 0) and carry_free and local_units
                assert (ddeg % p != 0) == expected_unit
                dual_checks += 1

# Published software-normalization example.
lam = (6,4,3,3,2)
assert degree_primal(lam) == 25920
assert degree_dual(lam) == 21600

print("VERIFY_OK", primal_checks, dual_checks)
