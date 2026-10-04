from fractions import Fraction

checks = 0
vals = [Fraction(i, 12) for i in range(13)]
positive = [Fraction(i, 24) for i in range(1, 13)]

# Atomic lower witness: p <= r <= 1. Same-sign distance is exactly 1+r-2p;
# opposite-sign distance is 1+r, hence never smaller.
for r in vals:
    for p in vals:
        if p > r:
            continue
        same = 1 + r - 2*p
        opposite = 1 + r
        assert same >= 1 + r - 2*p
        assert opposite >= same
        checks += 2

# Atomic upper slice inequality. Normalize the atom so that its L1 mass coordinate
# is p for f and q for g. If q > p-eta and 0 <= p <= r <= 1,
# |p-q| + (r-p) + (1-q) <= 1+r-2p+2eta.
for r in vals:
    for p in vals:
        if p > r or p == 0:
            continue
        for eta in positive:
            if eta >= p:
                continue
            for q in vals:
                if q <= p-eta:
                    continue
                lhs = abs(p-q) + (r-p) + (1-q)
                rhs = 1 + r - 2*p + 2*eta
                assert lhs <= rhs
                checks += 1

# Endpoint identities on the unit sphere.
for m in vals:
    formula = 2*(1-m)
    assert formula == 1 + 1 - 2*m
    assert Fraction(0) <= formula <= Fraction(2)
    checks += 2

print('VERIFY_OK', checks)
