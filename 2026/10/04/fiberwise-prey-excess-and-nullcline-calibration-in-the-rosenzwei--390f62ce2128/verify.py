from fractions import Fraction as F

# Work at exact positive rational parameter values to replay the algebra.
m = F(2, 7)
h = F(3, 5)
r = F(11, 13)
Nstar = m*h/(1-m)
assert Nstar/(h+Nstar) == m
Pstar = r*(1-Nstar)*(h+Nstar)
assert Pstar > 0

# Factorization at several exact test values.
for N in [F(1,10), F(1,4), F(2,5), F(3,5)]:
    lhs = N/(h+N)-m
    rhs = h*(N-Nstar)/((h+N)*(h+Nstar))
    assert lhs == rhs
    defect = (N-Nstar)**2/(h+N)
    expanded = (h+N) - 2*(h+Nstar) + (h+Nstar)**2/(h+N)
    assert defect == expanded
    speed_weighted = (h+N)*lhs*lhs/(1-m)**2
    assert speed_weighted == defect

# Abstract regression-variance identity.
EA = F(7,5)
EB = EA
EB2 = F(19,6)
EAB = EB2
EA2 = F(23,5)
assert (EA2-EA*EA)-(EB2-EB*EB) == EA2-2*EAB+EB2

print('VERIFY_OK')
