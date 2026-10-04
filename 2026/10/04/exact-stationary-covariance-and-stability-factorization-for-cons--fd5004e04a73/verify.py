from fractions import Fraction

def formulas(a, s, tau2):
    den = (2-a)*(2-s)*(a+s-a*s)
    E = a*tau2/(2-a)
    C = -(1-a)*s*E/(a+s-a*s)
    V = a*s*tau2*(2-a-s+a*s)/den
    Vsgd = s*tau2/(2-s)
    R = a*(2-a-s+a*s)/((2-a)*(a+s-a*s))
    return E, C, V, Vsgd, R

tests = [
    (Fraction(1,5), Fraction(1,4)),
    (Fraction(1,3), Fraction(3,5)),
    (Fraction(1,2), Fraction(1)),
    (Fraction(4,5), Fraction(7,5)),
    (Fraction(1), Fraction(9,5)),
]
tau2 = Fraction(7,11)

for a, s in tests:
    E, C, V, Vsgd, R = formulas(a, s, tau2)
    assert abs(1-s) < 1
    assert abs(1-a) < 1
    assert E == (1-a)**2*E + a*a*tau2
    assert C == (1-a)*((1-s)*C - s*E)
    assert V == (1-s)**2*V + s*s*E - 2*s*(1-s)*C
    assert Vsgd == (1-s)**2*Vsgd + s*s*tau2
    assert V == R*Vsgd
    if a < 1:
        assert R < 1
        assert 1-R == 2*s*(1-a)/((2-a)*(a+s-a*s))
    else:
        assert R == 1
    assert 2*s*(1-(s-1)*(1-a)**2) > 0

a = Fraction(2,7)
errors = []
for s in (Fraction(1,10), Fraction(1,2), Fraction(1), Fraction(19,10)):
    E, _, _, _, _ = formulas(a, s, tau2)
    errors.append(E)
assert len(set(errors)) == 1

s = Fraction(3,4)
for k in (100,1000,10000):
    a = Fraction(1,k)
    _, _, V, _, _ = formulas(a, s, tau2)
    assert abs(float((V/tau2)/a) - 0.5) < 2.0/k

for s in (Fraction(0), Fraction(2), Fraction(5,2)):
    assert abs(1-s) >= 1

print("verification passed")
