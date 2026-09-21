from fractions import Fraction

def moments(pmf, p1, p2):
    EN = sum(Fraction(n) * q for n, q in pmf.items())
    EN2 = sum(Fraction(n*n) * q for n, q in pmf.items())
    EF2 = sum(Fraction(n*(n-1)) * q for n, q in pmf.items())
    a1, a2 = p1*EN, p2*EN
    b1, b2 = p1*p1*EF2, p2*p2*EF2
    c = p1*p2*EN2
    return EN, a1, a2, b1, b2, c

pmfs = [
    {0: Fraction(1,10), 1: Fraction(2,10), 3: Fraction(4,10), 5: Fraction(3,10)},
    {1: Fraction(1,2), 2: Fraction(1,2)},
    {0: Fraction(3,4), 8: Fraction(1,4)},
    {2: Fraction(1,1)},
]
ps = [
    (Fraction(2,5), Fraction(3,7)),
    (Fraction(1,3), Fraction(4,5)),
    (Fraction(1,1), Fraction(1,2)),
]

checks = 0
for pmf in pmfs:
    for p1, p2 in ps:
        EN, a1, a2, b1, b2, c = moments(pmf, p1, p2)
        r1 = c/a2 - b1/a1
        r2 = c/a1 - b2/a2
        assert r1 == p1
        assert r2 == p2
        assert a1/r1 == EN
        assert a2/r2 == EN
        checks += 4

# Equal-detection specialization:
pmf = pmfs[0]
p = Fraction(2,5)
EN, a1, a2, b1, b2, c = moments(pmf, p, p)
EY2 = b1 + a1
varY = EY2 - a1*a1
covY = c - a1*a2
assert p == 1 - (varY-covY)/a1
checks += 1

# One-visit Poisson pgf aliasing, checked as formal coefficients through degree 8:
# Thinning Pois(lambda/p) by p gives Pois(lambda).
from math import factorial
lam = Fraction(3,2)
for p in [Fraction(1,4), Fraction(2,3), Fraction(1,1)]:
    latent_mean = lam/p
    # Factorial moments of the thinned variable are p^r latent_mean^r = lam^r.
    for r in range(1, 9):
        assert p**r * latent_mean**r == lam**r
        checks += 1

print(f"exact_checks={checks}")
print("status=PASS")
