from fractions import Fraction
from math import comb, exp, log

# P(x)=(2+x^105)^8-(1+x^32)^15, with x^60=2.
poly = {}
def add(e, c):
    poly[e] = poly.get(e, 0) + c
for j in range(9):
    add(105*j, comb(8,j) * (2 ** (8-j)))
for j in range(16):
    add(32*j, -comb(15,j))

red = {}
for e, c in poly.items():
    q, r = divmod(e, 60)
    red[r] = red.get(r, 0) + c * (2 ** q)
red = {e:c for e,c in red.items() if c}
expected = {
    56:-6720, 52:-43680, 48:-80080, 45:116736, 44:-51480,
    40:-12012, 36:-910, 32:-15, 30:129024, 28:-1920,
    24:-29120, 20:-96096, 16:-102960, 15:122880, 12:-40040,
    8:-5460, 4:-210, 0:159743,
}
assert red == expected

lo = Fraction(1011, 1000)
hi = Fraction(253, 250)
assert lo ** 60 < 2 < hi ** 60

# Horner interval evaluation on the positive interval [lo,hi].
L = Fraction(0)
U = Fraction(0)
for e in range(max(red), -1, -1):
    vals = (L*lo, L*hi, U*lo, U*hi)
    L, U = min(vals), max(vals)
    c = red.get(e, 0)
    L += c
    U += c
assert L > 0

# For k=7/4, m(k)<0 is equivalent to
# (2+2^(7/4))^(8/15) > 1+2^(8/15).
# Raising to the 15th power and writing x=2^(1/60) gives P(x)>0,
# which the exact interval certificate above proves.

# Supplemental diagnostics only.
def mpow(a,b):
    return exp(b*log(a))
def m(k):
    C = 2.0 + 2.0**k
    return 2.0 - mpow(mpow(C, 2.0/(k+2.0)) - 1.0, (k+2.0)/2.0)
for k in (1.73, 1.7337, 1.734, 1.75):
    print(f"m({k}) = {m(k):.17g}")
print("exact polynomial interval lower =", float(L))
print("exact polynomial interval upper =", float(U))
print("VERIFY_OK")
