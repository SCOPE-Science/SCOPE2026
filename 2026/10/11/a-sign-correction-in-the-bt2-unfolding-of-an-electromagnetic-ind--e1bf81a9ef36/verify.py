from decimal import Decimal, getcontext

getcontext().prec = 50
a = Decimal("4.537776612e-4")
b = Decimal("0.4552873824")
s11 = Decimal("-0.6956435964")
s12 = Decimal("43.44299811")
s21 = Decimal("0.2983460741")
s22 = Decimal("-18.63440137")

f1 = b**4 / a**3
f2 = b**2 / a**2
A1, A2 = f1*s11, f1*s12
B1, B2 = f2*s21, f2*s22
assert f1 > 0 and f2 > 0
assert A1 < 0 and A2 > 0 and B1 > 0 and B2 < 0

# Printed coefficients are rounded from higher-precision intermediate data.
assert abs(A1 - Decimal("-3.19889447e8")) < Decimal("1")
assert abs(A2 - Decimal("1.99771215e10")) < Decimal("20")
assert abs(B1 - Decimal("3.003345752e5")) < Decimal("1")
assert abs(B2 - Decimal("-1.875860118e7")) < Decimal("2")

slope = -A2/A1
assert abs(slope - Decimal("62.4500798")) < Decimal("1e-7")

# Normalize 4*betabar1 - betabar2^2 = 0 by -4*A1.
D = -4*A1
c11 = -(B1**2)/D
c12 = -(2*B1*B2)/D
c22 = -(B2**2)/D
cl1 = (4*A1)/D
cl2 = (4*A2)/D
assert abs(c11 - Decimal("-70.49377359")) < Decimal("1e-7")
assert abs(c12 - Decimal("8805.943066")) < Decimal("1e-6")
assert abs(c22 - Decimal("-275005.2569")) < Decimal("1e-4")
assert cl1 == Decimal("-1")
assert abs(cl2 - Decimal("62.4500798")) < Decimal("1e-7")

# A literal plus sign in the first constant unfolding term reverses the tangent.
printed_plus_slope = A2/A1
assert printed_plus_slope < 0
assert slope > 0
print("VERIFY_OK")
