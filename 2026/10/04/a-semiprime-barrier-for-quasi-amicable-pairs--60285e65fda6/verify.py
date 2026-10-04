#!/usr/bin/env python3
LIMIT = 2_000_000

spf = list(range(LIMIT + 1))
if LIMIT >= 1:
    spf[1] = 1
for p in range(2, int(LIMIT**0.5) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f

def omega_big(n):
    return sum(factor(n).values())

def sigma(n):
    ans = 1
    for p,a in factor(n).items():
        ans *= (p**(a+1)-1)//(p-1)
    return ans

def L(n):
    return sigma(n) - n - 1

low = 0
positive_mates = 0
low_mates = 0
cycles = []
for n in range(2, LIMIT + 1):
    if omega_big(n) <= 2:
        low += 1
        m = L(n)
        if m > 0:
            positive_mates += 1
            assert m <= n, (n, m)
            if m >= 2 and omega_big(m) <= 2:
                low_mates += 1
                if L(m) == n and m != n:
                    cycles.append((n,m))

assert cycles == [], cycles
print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"omega_le_2={low}",
    f"positive_mates={positive_mates}",
    f"omega_le_2_mates={low_mates}",
    "cycles=0",
)
