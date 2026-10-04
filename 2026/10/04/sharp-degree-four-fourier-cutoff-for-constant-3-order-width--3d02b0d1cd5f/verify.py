from fractions import Fraction
from math import sqrt, cos, pi, isclose

u = Fraction(10, 39)
J = (80*u - 156*u*u) / 15
assert J == Fraction(80, 117)
assert 1 - J/2 == Fraction(77, 117)

# Curvature/support coefficient relations for r=1.
a2_sq = Fraction(16*190, 117*117)
curv2_sq = Fraction(16*190, 39*39)
assert curv2_sq == 9*a2_sq
assert Fraction(20,39) == -15*Fraction(-4,117)

# Perfect-square coefficient check:
# (40/39)(x-sqrt(190)/20)^2
assert Fraction(40,39)*Fraction(190,400) == Fraction(19,39)
assert Fraction(40,39) == Fraction(40,39)
# linear coefficient has magnitude 4 sqrt(190)/39
assert Fraction(16*190,39*39) == Fraction(3040,1521)

# Root-of-unity cancellation for modes 1,2,4 in w_3.
for n in (1,2,4):
    for th in (0.13, 0.77, 1.81):
        s=sum(cos(n*(th+2*pi*j/3)) for j in range(3))
        assert abs(s) < 1e-12

# Diagnostic sampling of the exact square factor.
for k in range(10001):
    th=2*pi*k/10000
    rho=1-(4*sqrt(190)/39)*cos(2*th)+(20/39)*cos(4*th)
    sq=(40/39)*(cos(2*th)-sqrt(190)/20)**2
    assert rho > -1e-12
    assert isclose(rho,sq,rel_tol=1e-11,abs_tol=1e-11)

print('VERIFY_OK')
