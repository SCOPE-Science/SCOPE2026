#!/usr/bin/env python3
from fractions import Fraction

# Exact partition maxima used for Omega <= 4.
low = {
    (4,): Fraction(31,16),
    (3,1): Fraction(15,8)*Fraction(4,3),
    (2,2): Fraction(7,4)*Fraction(13,9),
    (2,1,1): Fraction(7,4)*Fraction(4,3)*Fraction(6,5),
    (1,1,1,1): Fraction(3,2)*Fraction(4,3)*Fraction(6,5)*Fraction(8,7),
}
assert max(low.values()) == Fraction(14,5) < 3

odd4 = {
    (4,): Fraction(121,81),
    (3,1): Fraction(40,27)*Fraction(6,5),
    (2,2): Fraction(13,9)*Fraction(31,25),
    (2,1,1): Fraction(13,9)*Fraction(6,5)*Fraction(8,7),
    (1,1,1,1): Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11),
}
assert max(odd4.values()) == Fraction(768,385) < 2
assert Fraction(576,385) < Fraction(12,7)
assert Fraction(40,27) < Fraction(12,7)

# Exact factor equations in the surviving symbolic branches.
sol_a3 = []
for q in range(3,100,2):
    for r in range(q+2,200,2):
        if (3*q-5)*(3*r-5) == 40:
            sol_a3.append((q,r))
assert sol_a3 == [(3,5)]

sol_a2 = []
for r in range(5,100,2):
    for s in range(r+2,200,2):
        if (2*r-7)*(2*s-7) == 63:
            sol_a2.append((r,s))
assert sol_a2 == []

LIMIT = 1_000_000
spf = list(range(LIMIT+1))
spf[1] = 1
for p in range(2, int(LIMIT**0.5)+1):
    if spf[p] == p:
        for m in range(p*p, LIMIT+1, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p,0)+1
        n //= p
    return f

def sigma_from_factor(f):
    s = 1
    for p,a in f.items():
        s *= (p**(a+1)-1)//(p-1)
    return s

hits = []
triperfect = []
for n in range(2, LIMIT+1):
    f = factor(n)
    sig = sigma_from_factor(f)
    if sig == 3*n:
        om = sum(f.values())
        triperfect.append((n,om))
        if om <= 5:
            hits.append((n,om))

assert hits == [(120,5)], hits
print("VERIFY_OK", f"limit={LIMIT}", f"triperfect={triperfect}", f"low_layer={hits}")
