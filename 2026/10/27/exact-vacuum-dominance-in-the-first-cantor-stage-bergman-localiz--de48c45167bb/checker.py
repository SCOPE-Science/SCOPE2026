"""Rational corroboration for the first Cantor-stage Bergman localization."""
from fractions import Fraction as F

def quantities(r):
    a = r / (r + 3)
    b = 2*r / (2*r + 3)
    c = r / (r + 1)
    top = a + c - b
    exact = 2*r*(r*r+3*r+3)/((r+1)*(r+3)*(2*r+3))
    gap = a - b*top
    certificate = r*(4*r*r+9*r+9)/((r+1)*(r+3)*(2*r+3)**2)
    assert top == exact
    assert gap == certificate and gap > 0
    assert 0 < a < b < c < 1
    return a,b,c,top

checks = 0
for r in [F(1,100),F(1,3),F(1),F(7,2),F(10),F(200)]:
    a,b,c,top = quantities(r)
    checks += 4
    for k in range(1,81):
        eig = a**(k+1)+c**(k+1)-b**(k+1)
        assert F(0) < eig < top
        checks += 1
print(f"PASS: {checks} exact-rational assertions (no infinite-proof claim)")
