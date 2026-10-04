#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 80

gamma = mp.mpf("0.5")
dt = mp.mpf(1)

# Exact invariant fractional submodel:
# Caputo D^(1/2) R = -R, R(0)=1.
R0 = mp.mpf(1)
R1 = mp.e * mp.erfc(1)
R2 = mp.e**2 * mp.erfc(mp.sqrt(2))

# m=2 coefficients read directly from the source recurrence.
C2 = dt**gamma * (3 + 2*gamma) / mp.gamma(gamma + 2)
C3 = dt**gamma * (2*gamma**2 + 9*gamma + 12) / (2 * mp.gamma(gamma + 3))

assert mp.almosteq(C2, 4 / mp.gamma(mp.mpf("2.5")))
assert mp.almosteq(C3, 17 / (2 * mp.gamma(mp.mpf("3.5"))))

# In the submodel, g1 = R and g5 = -R.
# The first-history terms cancel. The printed higher g5 corrections
# use Q-history; Q is identically zero, so those recovery corrections vanish.
delta_N3 = C2 * (R1 - R0) + C3 * (R2 - 2*R1 + R0)
N3_printed = 1 + delta_N3

target = mp.mpf("-0.49207893684378897698958743925941614169899191666249712")
assert abs(delta_N3 - target) < mp.mpf("1e-50")
assert N3_printed < mp.mpf("0.51")
assert N3_printed > mp.mpf("0.50")

# With R rather than Q in the recovery corrections, every susceptible
# correction is paired by its negative recovery correction.
corrected_residual = (
    C2 * ((R1-R0) + (-(R1-R0)))
    + C3 * ((R2-2*R1+R0) + (-(R2-2*R1+R0)))
)
assert corrected_residual == 0

print("VERIFY_OK")
print("R0", mp.nstr(R0, 30))
print("R1", mp.nstr(R1, 30))
print("R2", mp.nstr(R2, 30))
print("C2", mp.nstr(C2, 30))
print("C3", mp.nstr(C3, 30))
print("delta_N3", mp.nstr(delta_N3, 40))
print("N3_printed", mp.nstr(N3_printed, 40))
print("corrected_residual", corrected_residual)
