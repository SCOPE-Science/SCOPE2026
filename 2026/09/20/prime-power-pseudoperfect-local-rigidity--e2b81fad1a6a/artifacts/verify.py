#!/usr/bin/env python3
from fractions import Fraction
import math

LIMIT = 100_000

def spf_table(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

SPF = spf_table(LIMIT)

def factorint(n):
    f = {}
    while n > 1:
        p = SPF[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f

def H(f):
    n = math.prod(p**a for p, a in f.items())
    ans = Fraction(1, n)
    for p, a in f.items():
        ans += sum((Fraction(1, p**j) for j in range(1, a + 1)), Fraction())
    return ans

def local_congruences(f):
    n = math.prod(p**a for p, a in f.items())
    return all((n // (p**a) - (p - 1)) % (p**a) == 0 for p, a in f.items())

checked = 0
mismatches = []
ppp = []
for n in range(2, LIMIT + 1):
    f = factorint(n)
    if len(f) <= 4:
        checked += 1
        eq = (H(f) == 1)
        lc = local_congruences(f)
        if eq:
            ppp.append(n)
        if eq != lc:
            mismatches.append(n)

family = []
for c in range(1, 13):
    n = 6 * 7**c
    val = Fraction(1, 2) + Fraction(1, 3)
    val += sum((Fraction(1, 7**j) for j in range(1, c + 1)), Fraction())
    val += Fraction(1, n)
    assert val == 1
    family.append(n)

print(f"limit={LIMIT}")
print(f"omega_le_4_checked={checked}")
print(f"criterion_mismatches={len(mismatches)}")
print("ppp_prefix=" + ",".join(map(str, ppp[:30])))
print("family_c_1_to_12=" + ",".join(map(str, family)))
