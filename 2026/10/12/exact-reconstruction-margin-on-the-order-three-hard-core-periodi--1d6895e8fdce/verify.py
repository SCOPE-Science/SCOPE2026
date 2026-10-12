from fractions import Fraction

def check(t):
    assert 0 < t < Fraction(1, 3)
    a = 1 + t
    lam = 1 / (a*a*t)
    b = a*t

    lam2_zprod = lam*lam*b**3
    lam_zsum = lam*(a**3 - 3*a*b)
    den = lam2_zprod + lam_zsum + 1
    s2 = lam2_zprod / den
    kappa = lam2_zprod / den

    assert lam2_zprod == t/a
    assert lam_zsum == (1 - 2*t)/t
    assert den == 1/(a*t)
    assert s2 == t*t
    assert kappa == t*t

    cert = 9*t*t / (1 + t*a*a)
    assert cert < Fraction(27, 43)
    assert 9*s2*s2 < Fraction(1, 9)
    return cert

count = 0
largest = Fraction(0, 1)
for q in range(4, 251):
    for p in range(1, q):
        t = Fraction(p, q)
        if t < Fraction(1, 3):
            largest = max(largest, check(t))
            count += 1

endpoint = Fraction(9, 1)*Fraction(1, 3)**2 / (
    1 + Fraction(1, 3)*Fraction(4, 3)**2
)
assert endpoint == Fraction(27, 43)

for q in range(4, 251):
    t = Fraction(1, q)
    assert 2 + t - t**3 > 0

print(f"VERIFY_OK exact_points={count} endpoint={endpoint} max_sample={largest}")
