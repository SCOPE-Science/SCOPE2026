from fractions import Fraction

# Exact arithmetic replay of the source's lower-threshold reset.
yB = Fraction(10, 1)
tau = Fraction(2, 1)
yA = Fraction(7, 1)
p1 = Fraction(1, 4)

# Model-consistent successor: y^+ = yB - tau.
f_model = (yB - tau) - yA
# Expression printed in the proof of Theorem 3.1.
f_printed = yB * (1 - p1) - yA
assert f_model == 1
assert f_printed == Fraction(1, 2)
assert f_model != f_printed

# The proof says a second point with a negative successor is needed,
# then displays f(A1)=y_B1-y_B>0 after choosing y_B1>y_B.
yB1 = Fraction(12, 1)
f_A1_displayed = yB1 - yB
assert f_model > 0
assert f_A1_displayed > 0

# Two positive endpoint values alone do not certify an IVT zero.
assert not (f_model <= 0 <= f_A1_displayed or f_A1_displayed <= 0 <= f_model)
print("VERIFY_OK")
