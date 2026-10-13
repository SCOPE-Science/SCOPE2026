from fractions import Fraction
from math import log2

a,b,c,d = 3,2,6,3
S = a*a+b*b+c*c+d*d
assert S == 58

purity = Fraction(a**4+b**4+c**4+d**4, S*S)
assert purity == Fraction(737,1682)

C1 = Fraction(2*(a*c+b*d), S)
C2 = Fraction(2*(a*b+c*d), S)
assert C1 == C2 == Fraction(24,29)

f1 = 1 - C1*C1/Fraction(2)
f2 = 1 - C2*C2/Fraction(2)
assert f1 == f2 == Fraction(553,841)

ratio = f1*f2/purity
assert ratio == Fraction(611618,619817)
assert ratio < 1

# The four traced-out labels for either cross pair are distinct.
labels_cross_1 = [(0,0),(1,0),(0,1),(1,1)]
labels_cross_2 = [(0,0),(0,1),(1,0),(1,1)]
assert len(set(labels_cross_1)) == 4
assert len(set(labels_cross_2)) == 4

print('residual_ratio =', ratio)
print('residual_bits =', log2(float(ratio)))
print('VERIFY_OK')
