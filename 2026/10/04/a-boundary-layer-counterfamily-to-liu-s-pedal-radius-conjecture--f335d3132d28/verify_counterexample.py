from fractions import Fraction
from decimal import Decimal, getcontext

# Exact data for y = 1/100 in the fixed triangle.
y = Fraction(1, 100)

# Pedal feet D=(dx,dy), E=(-dx,dy), F=(0,0).
dx = Fraction(2, 1) * (Fraction(2, 1) - y) / 5
dy = Fraction(2, 1) * (Fraction(1, 1) + 2*y) / 5
assert dx == Fraction(199, 250)
assert dy == Fraction(51, 125)

# Exact squared equal side and base length.
fd2 = dx*dx + dy*dy
assert fd2 == Fraction(4, 5) * (1 + y*y)
de = 2*dx
assert de == Fraction(199, 125)

# Pedal area from base times height divided by two.
Sp = de*dy/2
assert Sp == Fraction(4, 25) * (2-y) * (1+2*y)

# Circumradius Rp = DE*DF*EF/(4Sp), with DF*EF = fd2.
Rp = de*fd2/(4*Sp)
assert Rp == (1+y*y)/(1+2*y)
assert Rp == Fraction(10001, 10200)

# The reference triangle has sides 2,sqrt(5),sqrt(5), area 2.
R = Fraction(5, 4)

# Exact radical form of the pedal inradius at y=1/100:
# rp = 199*(sqrt(50005)-199)/25500.
# To prove Rp + sqrt(2)*rp - R > 0 it suffices to prove
# 398*sqrt(2)*(sqrt(50005)-199) > 13745.
assert 140*140 < 2*99*99          # sqrt(2) > 140/99
assert 1118*1118 < 50005*25       # sqrt(50005) > 1118/5
lower_num = 398*140*123
lower_den = 99*5
assert lower_num > 13745*lower_den

# Supplemental high-precision decimal evaluation.
getcontext().prec = 50
D = Decimal
sqrt2 = D(2).sqrt()
sqrt50005 = D(50005).sqrt()
rp = D(199) * (sqrt50005 - D(199)) / D(25500)
excess = D(Rp.numerator)/D(Rp.denominator) + sqrt2*rp - D(5)/D(4)
assert excess > 0
print('VERIFY_OK')
print('Rp =', D(Rp.numerator)/D(Rp.denominator))
print('rp =', rp)
print('excess =', excess)
