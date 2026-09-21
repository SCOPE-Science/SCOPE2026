from fractions import Fraction
from itertools import product, combinations

SIGNS = list(product((-1, 1), repeat=4))

def parity(s):
    out = 1
    for x in s:
        out *= x
    return out

# Each parity class is uniform on 8 sign vectors. Verify all proper sign marginals
# are exactly uniform, hence identical to three independent fair signs or fewer.
for tau in (-1, 1):
    cls = [s for s in SIGNS if parity(s) == tau]
    assert len(cls) == 8
    for r in (1, 2, 3):
        for I in combinations(range(4), r):
            counts = {}
            for s in cls:
                key = tuple(s[i] for i in I)
                counts[key] = counts.get(key, 0) + 1
            assert set(counts.values()) == {2 ** (3-r)}
            assert len(counts) == 2**r

# Exact persistence contributions for 0<eta<1, after conditioning on sign pattern.
# Patterns beginning with - fail immediately and need not be listed.
plus = {
    (1, 1, 1, 1): Fraction(1),
    (1, 1, -1, -1): Fraction(1, 2),
    (1, -1, 1, -1): Fraction(3, 8),
    (1, -1, -1, 1): Fraction(0),
}
minus = {
    (1, 1, 1, -1): Fraction(1),
    (1, 1, -1, 1): Fraction(1),
    (1, -1, 1, 1): Fraction(1, 2),
    (1, -1, -1, -1): Fraction(0),
}
p_plus = sum(plus.values(), Fraction(0)) / 8
p_minus = sum(minus.values(), Fraction(0)) / 8
q_iid = Fraction(35, 128)
assert p_plus == Fraction(15, 64)
assert p_minus == Fraction(5, 16)
assert (p_plus + p_minus) / 2 == q_iid
assert p_minus - p_plus == Fraction(5, 64)

# One-parameter parity tilt: P_theta(s)=2^-4(1+theta product(s)).
# Persistence is q_iid - (5/128) theta.
assert (p_plus - p_minus) / 2 == Fraction(-5, 128)

print("proper_subset_sign_marginals: exact iid for both parity classes")
print("p_plus =", p_plus)
print("p_minus =", p_minus)
print("iid_Sparre_Andersen =", q_iid)
print("separation =", p_minus - p_plus)
print("p_theta = 35/128 - (5/128)*theta")
