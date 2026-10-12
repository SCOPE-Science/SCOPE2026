from decimal import Decimal, getcontext

getcontext().prec = 80

def survival(z, eps):
    exponent = -eps * (Decimal(z) + (Decimal(2) ** z) - Decimal(1))
    return exponent.exp()

def pmf(z, eps):
    return survival(z, eps) - survival(z + 1, eps)

eps = Decimal("0.01")
p0, p1, p2 = (pmf(z, eps) for z in range(3))
det = p1*p1 - p0*p2
ratio = p1*p1/(p0*p2)

assert det < Decimal(0)
assert ratio < Decimal(1)
assert abs(ratio - Decimal("0.9135598872191721690262653215883022509")) < Decimal("3e-38")

vals = []
for s in ("1e-3", "1e-4", "1e-5", "1e-6"):
    e = Decimal(s)
    q0, q1, q2 = (pmf(z, e) for z in range(3))
    vals.append((q1*q1 - q0*q2)/(e*e))

assert abs(vals[-1] + Decimal(1)) < Decimal("3e-5")
assert abs(vals[-1] + Decimal(1)) < abs(vals[0] + Decimal(1))

print("VERIFY_OK")
print("determinant", det)
print("ratio", ratio)
print("scaled_limits", vals)
