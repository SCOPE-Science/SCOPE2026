"""Verify the disproof pair for the quantum-plane derived-classification target.

Checks, over any alg.-closed k of char 0 (values lie in the prime field Q):
 1. q=(2,3,5), q'=(4,6,5) are generic (no entry 1 or a root of unity).
 2. Diagonal Zhang twist with scales (a,b,c)=(2,1,1) sends q -> q'.
 3. Twist invariant q12*q23/q13 is preserved.
 4. q' is OUTSIDE the S3-permutation + independent-inversion orbit of q.
 5. Twisted quadratic relations hold under the star product.
"""
from fractions import Fraction

q = {"q12": Fraction(2), "q13": Fraction(3), "q23": Fraction(5)}
a, b, c = Fraction(2), Fraction(1), Fraction(1)

# 1. generic: entries != 1; positive integers != 1 are never roots of unity in char 0
for k, v in q.items():
    assert v != 1, k
    assert v > 1  # hence v^r - 1 != 0 in Q for all r>=1
qp = {"q12": a * q["q12"] / b, "q13": a * q["q13"] / c, "q23": b * q["q23"] / c}
print("q  =", dict(q))
print("q' =", {k: str(v) for k, v in qp.items()})
assert (qp["q12"], qp["q13"], qp["q23"]) == (Fraction(4), Fraction(6), Fraction(5))
for k, v in qp.items():
    assert v != 1, k
    assert v > 1

# 2/3. twist invariant J = q12*q23/q13 preserved
J = q["q12"] * q["q23"] / q["q13"]
Jp = qp["q12"] * qp["q23"] / qp["q13"]
print("J =", J, " J' =", Jp)
assert J == Jp == Fraction(10, 3)

# 4. orbit exclusion: every entry of any S3-permuted + independently inverted
#    triple lies in {2^+-1, 3^+-1, 5^+-1}; but q12' = 4 is in none of these.
allowed = {Fraction(2), Fraction(1, 2), Fraction(3), Fraction(1, 3),
           Fraction(5), Fraction(1, 5)}
print("allowed values mod perm/inv:", sorted(allowed))
assert qp["q12"] not in allowed, "q12'=4 must lie outside the orbit alphabet"
# exhaustive check over all 6 perms x (2^3 sign choices): multiset test
import itertools
base = [Fraction(2), Fraction(3), Fraction(5)]
orbit = set()
for perm in itertools.permutations(base):
    for s in itertools.product([1, -1], repeat=3):
        t = tuple(p ** e for p, e in zip(perm, s))
        orbit.add(t)
target = (Fraction(4), Fraction(6), Fraction(5))
assert target not in orbit, "q' must not be in the orbit"
print("orbit size:", len(orbit), "| q' in orbit:", target in orbit)

# 5. twisted-relation check: y*x - q12 x*y maps to a*q12*xy - q12'*b*xy = 0 etc.
#    (monomial xy, xz, yz coefficients under star product)
checks = {
    "q12": a * q["q12"] - qp["q12"] * b,
    "q13": a * q["q13"] - qp["q13"] * c,
    "q23": b * q["q23"] - qp["q23"] * c,
}
print("relation residuals:", checks)
assert all(v == 0 for v in checks.values())

print("ALL CHECKS PASSED")
