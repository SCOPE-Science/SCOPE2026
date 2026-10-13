#!/usr/bin/env python3

LIMIT = 50000
KMAX = 10

spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i

def factorization(n):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p,a))
    return out

def omega(n):
    return sum(a for _,a in factorization(n))

def tau_from_fac(fac):
    t = 1
    for _,a in fac:
        t *= a + 1
    return t

def sigma_k_from_fac(fac,k):
    s = 1
    for p,a in fac:
        x = p**k
        s *= (x**(a+1) - 1)//(x-1)
    return s

hits = []
tested = 0
for n in range(2, LIMIT + 1):
    fac = factorization(n)
    if sum(a for _,a in fac) > 2:
        continue
    for k in range(1, KMAX + 1):
        tested += 1
        sig = sigma_k_from_fac(fac,k)
        num = (n**k) * tau_from_fac(fac)
        if num % sig == 0:
            hits.append((k,n))

assert hits == [(1,6)], hits

h2 = []
for x in range(2,20):
    for y in range(x,20):
        if (x-1)*(y-1) == 2:
            h2.append((x,y))
assert h2 == [(2,3)]

h3 = []
for x in range(2,30):
    for y in range(x,30):
        if (x-3)*(y-3) == 12:
            h3.append((x,y))
assert h3 == [(4,15),(5,9),(6,7)]

print(
    "VERIFY_OK",
    f"range=2..{LIMIT}",
    f"k=1..{KMAX}",
    f"tested={tested}",
    f"hits={hits}",
    f"H2={h2}",
    f"H3={h3}",
)
