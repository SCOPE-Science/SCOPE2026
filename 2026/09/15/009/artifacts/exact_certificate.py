"""Exact rational certificate: degree-10 extremal polynomial hits 52416000 but is non-PSD.
Uses only stdlib (fractions). Reproduces WORKLOG section 1 and 3."""
from fractions import Fraction
from math import comb

d = 48
lam = 23

# f(t) = (t+1)(t+1/2)^2 (t+1/3)(t+1/6) t^2 (t-1/6)(t-1/3)(t-1/2), lowest-first coeffs
roots = [Fraction(-1), Fraction(-1,2), Fraction(-1,2), Fraction(-1,3), Fraction(-1,6),
         Fraction(0), Fraction(0), Fraction(1,6), Fraction(1,3), Fraction(1,2)]
coeffs = [Fraction(1)]
for r in roots:
    new = [Fraction(0)] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        new[i] += c * (-r)
        new[i + 1] += c
    coeffs = new
print("f coeffs lowest-first:", coeffs)
f1 = sum(coeffs)
print("f(1) =", f1)

def moment(k):
    if k % 2 == 1:
        return Fraction(0)
    num = Fraction(1); den = Fraction(1)
    for j in range(k // 2):
        num *= Fraction(2*j+1); den *= Fraction(d+2*j)
    return num/den

f0 = sum(c * moment(k) for k, c in enumerate(coeffs))
print("f0 =", f0, "=", float(f0))
print("f1/f0 =", f1 / f0)
assert f1 / f0 == 52416000

# Gegenbauer C polys (unnormalized), lowest-first
C = [[Fraction(1)], [Fraction(0), Fraction(2*lam)]]
for k in range(1, 12):
    tCk = [Fraction(0)] + C[k]
    term = [c * Fraction(2*(k+lam), k+1) for c in tCk]
    prev = C[k-1] + [Fraction(0)] * (len(term)-len(C[k-1]))
    term = [a - Fraction(k+2*lam-1, k+1)*b for a, b in zip(term, prev)]
    C.append(term)

def iprod(a, b):
    c = [Fraction(0)] * (len(a)+len(b))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return sum(c[k]*moment(k) for k in range(len(c)))

print("k | coef on normalized P_k")
for k in range(11):
    coef = iprod(coeffs, C[k]) / iprod(C[k], C[k]) * sum(C[k])
    print(k, coef, float(coef))
# signs: k=3,4 negative
assert iprod(coeffs, C[3]) < 0 and iprod(coeffs, C[4]) < 0

# Equality-case 11-design check
N = 52416000
A = {Fraction(-1):1, Fraction(-1,2):36848, Fraction(-1,3):1678887, Fraction(-1,6):12608784,
     Fraction(0):23766960, Fraction(1,6):12608784, Fraction(1,3):1678887,
     Fraction(1,2):36848, Fraction(1):1}
assert sum(A.values()) == N
for k in range(12):
    s = sum(cnt*(t**k) for t, cnt in A.items()) / N
    assert s == moment(k), (k, s, moment(k))
print("11-design moments 0..11: all match")
