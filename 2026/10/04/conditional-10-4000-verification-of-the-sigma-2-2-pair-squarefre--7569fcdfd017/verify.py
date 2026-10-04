#!/usr/bin/env python3
# Exact verification of the finite squarefreeness certificates.

PAIRS = [
    (3, 13),
    (13, 61),
    (22419767768701, 107419560853453),
]
FACTORS = {
    3: [13],
    13: [3, 61],
    61: [3, 13, 97],
    22419767768701: [3, 7, 199, 1119712369, 107419560853453],
    107419560853453: [3, 7, 24508477928503, 22419767768701],
}

# Deterministic strong Miller--Rabin bases for unsigned 64-bit integers.
BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

def is_prime_64(n):
    if n < 2:
        return False
    small = (2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in BASES_64:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True

# Reconstruct the quasisolution recurrence through the large prime pair.
t = [None, 1, 1]
while len(t) <= 23:
    num = t[-1]*t[-1] + t[-1] + 1
    assert num % t[-2] == 0
    t.append(num // t[-2])
assert (t[3],t[4]) == PAIRS[0]
assert (t[4],t[5]) == PAIRS[1]
assert (t[22],t[23]) == PAIRS[2]

# Check pair divisibility.
for p,q in PAIRS:
    assert (p*p+p+1) % q == 0
    assert (q*q+q+1) % p == 0

# Check complete squarefree factorizations and prime certificates.
for x, fac in FACTORS.items():
    assert len(fac) == len(set(fac))
    prod = 1
    for r in fac:
        assert r < 2**64
        assert is_prime_64(r), (x, r)
        prod *= r
    assert prod == x*x+x+1, (x, prod, x*x+x+1)

print('VERIFY_OK')
