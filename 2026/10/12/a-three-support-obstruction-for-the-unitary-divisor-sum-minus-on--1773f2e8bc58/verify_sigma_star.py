#!/usr/bin/env python3
def factor(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1))
    return out

def sigma_star_from_factorization(factors):
    s = 1
    for p, e in factors:
        s *= p ** e + 1
    return s

LIMIT = 200000
checked = 0
hits = []
for n in range(2, LIMIT + 1):
    fs = factor(n)
    if len(fs) <= 3:
        checked += 1
        ss = sigma_star_from_factorization(fs)
        if (ss + 1) % n == 0:
            hits.append((n, (ss + 1) // n, len(fs)))

assert hits == [(2, 2, 1)], hits
print("VERIFY_OK limit=%d checked=%d hits=%s" % (LIMIT, checked, hits))
