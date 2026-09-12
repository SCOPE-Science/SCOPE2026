"""Unit-obstruction data for k = Q(sqrt29): fundamental unit + mod-25 norm test.

1. eps = 2 + omega, omega = (1+sqrt29)/2: norm -1; minimality by trace-bound search.
2. 5 splits: (29/5) = 4/5 -> Kronecker (29/5) = +1 since 29 = 4^2+13... computed directly.
3. prime ideals above 5 via Dedekind (x^2 - x - 7 mod 5 splits distinctly).
4. Q5-embeddings: Hensel roots of x^2 - x - 7 mod 25, exact via Hensel lifts.
5. eps images mod 25 in each Q5 factor; 4th powers != 1 mod 25 -> non-5th-powers -> not local norms.
"""
import json
from sympy import factorint

D = 29
# minimal polynomial of omega=(1+sqrt29)/2: x^2 - x - 7
f = lambda X: X**2 - X - 7

# --- 1. splitting of 5: Kronecker (29/5) = (4/5) = +1 (4 = 2^2)
kr = pow(29, (5 - 1) // 2, 5)
print("29^2 mod 5 =", kr, "-> (29/5) = +1, 5 SPLITS in Q(sqrt29)")

# distinct roots mod 5
roots5 = [a for a in range(5) if f(a) % 5 == 0]
print("roots of x^2-x-7 mod 5:", roots5)
assert len(roots5) == 2 and len(set(roots5)) == 2
# derivative nonzero -> unramified, distinct primes
assert all((2 * a - 1) % 5 != 0 for a in roots5)

# --- 2. fundamental unit: omega=(1+sqrt29)/2, N = -7; eps = 2+omega, N(eps) = ?
# N(a + b*sqrt29) with omega = (1+s)/2: represent eps = 2 + (1+s)/2 = (5+s)/2.
# N((5+s)/2) = (25-29)/4 = -1. eps > 1; regulator log(eps) ~ 1.647.
import math
s = math.sqrt(29)
om = (1 + s) / 2
eps = 2 + om
print("N(eps) =", (25 - 29) / 4, " eps =", eps, " log(eps) =", math.log(eps))
# minimality: every unit of norm +1 is +/- eps^{2k}; smallest totally-positive unit >1 is eps^2.
# Any unit u>1 with u < eps^2: u = eps (norm -1) is the only candidate; check no unit in (1, eps).
# Trace bound: u + u' = t in Z (u' = conjugate if norm +1... ) exact diophantine scan:
# units of norm +-1: (a^2 - 29 b^2)/4 = +-1 with a,b same parity, value (a+b s)/2 in (1,eps).
sols = []
for a in range(-40, 41):
    for b in range(-20, 21):
        if (a - b) % 2 != 0:
            continue
        if (a * a - 29 * b * b) not in (4, -4):
            continue
        v = (a + b * s) / 2
        if 1 < v < eps - 1e-9:
            sols.append((a, b, v))
print("units strictly in (1, eps):", sols)
assert sols == [], "fundamental unit minimality fails!"
print("eps = (5+sqrt29)/2 is the FUNDAMENTAL unit (norm -1); E_k = {+-eps^n}.")

# --- 3. mod-25 roots (Hensel): lift each mod-5 root
roots25 = []
for r in roots5:
    a = r
    for _ in range(6):  # Newton: a -> a - f(a)/f'(a) mod 25
        fp = 2 * a - 1
        inv = pow(fp, -1, 25)
        a = (a - f(a) * inv) % 25
    assert f(a) % 25 == 0
    assert a % 5 == r
    roots25.append(a)
print("Hensel roots mod 25:", roots25)
# omega images; eps = 2 + omega images
epsimg = [(2 + r) % 25 for r in roots25]
print("eps images mod 25 at the two primes above 5:", epsimg)
p4 = [(e**4) % 25 for e in epsimg]
print("eps^4 mod 25:", p4)
assert all(v != 1 for v in p4), "eps would be a 5th power mod 25!"
print("Neither eps-image is a 5th power mod 25 (5th powers in (Z/25)^x are exactly {u: u^4 = 1}).")

# local-norm lemma check: |(Z/25)^x| = 20, 5th powers: {u^5}; u^5=1-ish count check
fifths = sorted(set(pow(u, 5, 25) for u in range(1, 25) if u % 5 != 0))
print("5th powers mod 25:", fifths)
fourth1 = sorted(u for u in range(1, 25) if u % 5 != 0 and pow(u, 4, 25) == 1)
print("{u: u^4=1}:", fourth1)
assert fifths == fourth1, "lemma: im(x->x^5) == ker(x->x^4) in (Z/25)^x"
assert not any(e in fifths for e in epsimg)

# extra: eps^4 images exactly, for the record
print("exact eps^4 values:", p4)
out = {"splits": True, "roots_mod5": roots5, "roots_mod25": roots25,
       "eps_images_mod25": epsimg, "eps4_mod25": p4,
       "fifth_powers_mod25": fifths}
with open("unit_obstruction.json", "w") as fh:
    json.dump(out, fh, indent=1)
print("saved unit_obstruction.json")
