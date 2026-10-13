from decimal import Decimal, getcontext
getcontext().prec = 80
L = Decimal(2).ln()
J1 = Decimal(5)/(Decimal(4)*L) - Decimal(3)/Decimal(2)
J2 = Decimal(11)/(Decimal(12)*L) - Decimal(7)/Decimal(9)
diff = Decimal(2)*J1 - J2
# Elementary positivity certificate used in the proof: exp(7/10)>2 from four Taylor terms.
x = Decimal(7)/Decimal(10)
lower_exp = Decimal(1) + x + x*x/Decimal(2) + x*x*x/Decimal(6)
assert lower_exp > Decimal(2)
assert L < Decimal(7)/Decimal(10)
assert Decimal(7)/Decimal(10) < Decimal(57)/Decimal(80)
assert diff > 0
print('ln2 =', L)
print('J(1) =', J1)
print('J(2) =', J2)
print('2 J(1)-J(2) =', diff)
print('Taylor lower bound exp(7/10) >', lower_exp)
print('VERIFY_OK')
