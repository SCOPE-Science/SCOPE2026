from fractions import Fraction as F

def sign_surd(a, b):
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    lhs = a*a
    rhs = 2*b*b
    if lhs == rhs:
        return 0
    if a > 0 and b < 0:
        return 1 if lhs > rhs else -1
    if a < 0 and b > 0:
        return -1 if lhs > rhs else 1
    raise AssertionError("unreachable")

def derivative_sign_factor(k, h):
    # 1 + sqrt(2) - k + (3 + 2*sqrt(2))*h
    return F(1-k) + 3*h, F(1) + 2*h

for k in range(3):
    assert sign_surd(*derivative_sign_factor(k, F(0))) > 0

for n in range(4, 16):
    p = F(3*n-2)
    q = F(-(2*n-1))
    # Substitute h_n=p+q*sqrt(2) into
    # 2+sqrt(2)-n+(3+2*sqrt(2))*h_n.
    A = F(2-n) + (3*p + 4*q)
    B = F(1) + (2*p + 3*q)
    assert A == 0 and B == 0

for n in range(4, 16):
    assert sign_surd(F(3*n-2), F(-(2*n-1))) > 0

assert sign_surd(F(10), F(-7)) > 0

# At h=1/20, k=3 the scaled sign factor is
# (-37 + 22*sqrt(2))/20, hence negative.
assert derivative_sign_factor(3, F(1,20)) == (F(-37,20), F(11,10))
assert sign_surd(F(-37), F(22)) < 0
assert sign_surd(*derivative_sign_factor(3, F(1,20))) < 0
# The unscaled derivative bracket is (44-37*sqrt(2))/40.
assert sign_surd(F(44), F(-37)) < 0

# Above h_4, e.g. h=1/8, the critical derivative is positive.
assert sign_surd(*derivative_sign_factor(3, F(1,8))) > 0

for h in [F(1,20), F(1,8), F(1), F(5)]:
    signs = [sign_surd(*derivative_sign_factor(k,h)) for k in range(12)]
    seen_negative = False
    for s in signs:
        if s < 0:
            seen_negative = True
        if seen_negative:
            assert s < 0

print("VERIFY_OK")
