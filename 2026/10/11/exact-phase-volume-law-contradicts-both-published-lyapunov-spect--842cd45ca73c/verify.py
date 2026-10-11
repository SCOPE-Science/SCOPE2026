from fractions import Fraction as F

sigma = F(10)
b = F(8, 3)
d = F(19, 3)
required = -(sigma + 1 + 5*b + d)
assert required == F(-92, 3)

r43 = [F("1.1281"), F("0.0073"), F("-1.3786"), F("-1.3774"), F("-1.6688")]
r25 = [F("-0.5246"), F("-0.5358"), F("-6.9952"), F("-2.0305"), F("-4.1633")]
s43 = sum(r43, F(0))
s25 = sum(r25, F(0))
assert s43 == F(-16447, 5000)
assert s25 == F(-71247, 5000)
assert s43 - required == F(410659, 15000)
assert s25 - required == F(246259, 15000)
assert s43 != required and s25 != required

T = F(500)
assert required*T == F(-46000, 3)
assert s43*T == F(-16447, 10)
assert s25*T == F(-71247, 10)
print("VERIFY_OK")
