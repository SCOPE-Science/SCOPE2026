from fractions import Fraction as F
from decimal import Decimal, getcontext

# Exact rational forced-swap witness.
a = F(18)
b = F(24)
d = F(82)
tr = a + d
det = a*d - b*b
assert tr == 100
assert det == 900
assert F(10) + F(90) == tr
assert F(10) * F(90) == det
assert F(90,10) == 9
mult = b/a
assert mult == F(4,3)
assert mult > 1

# Representative safe condition number kappa=4.
safe = F(4-1, 2*2)
assert safe == F(3,4)
assert safe < 1

# High-precision boundary.
getcontext().prec = 80
D = Decimal
sqrt2 = D(2).sqrt()
kstar = D(3) + D(2)*sqrt2
sqrtk = kstar.sqrt()
cstar = (kstar-D(1))/(D(2)*sqrtk)
assert abs(cstar-D(1)) < D("1e-70")

# The witness family has the claimed trace/determinant identities.
for k in [D("1.5"), D("4"), D("9"), D("25")]:
    sq = k.sqrt()
    aa = D(2)*k
    bb = (k-D(1))*sq
    dd = k*k+D(1)
    trace = aa+dd
    determinant = aa*dd-bb*bb
    assert abs(trace-(k+D(1))**2) < D("1e-65")
    assert abs(determinant-k*(k+D(1))**2) < D("1e-65")
    ratio = abs(bb)/aa
    sharp = (k-D(1))/(D(2)*sq)
    assert abs(ratio-sharp) < D("1e-65")

print("VERIFY_OK")
print("kappa_star", kstar)
print("witness_multiplier", mult)
