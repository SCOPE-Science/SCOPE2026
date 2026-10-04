from fractions import Fraction as F

# Printed decimals interpreted exactly.
c = F(33, 100)
a = F(169, 100)
mu = F(0)

# Delta = a^2 + 4*c*mu = a^2 + (33/25)*mu.
assert 4*c == F(33, 25)
delta = a*a + 4*c*mu
assert delta == a*a

# Hidden-case roots r_± = (-a ± sqrt(delta))/(2c), with sqrt(delta)=a.
r_minus = (-a-a)/(2*c)
r_plus = (-a+a)/(2*c)
assert r_minus == F(-169, 33)
assert r_plus == 0

# Critical forcing Delta=0 at fixed a.
mu_crit = -a*a/(4*c)
assert mu_crit == F(-28561, 13200)

# Sharp standard-deviation envelope is half the equilibrium gap.
half_gap = (r_plus-r_minus)/2
assert half_gap == F(169, 66)

# A separate rational example checks root sum/product against c*x^2+a*x-mu.
a2 = F(1)
mu2 = F(0)
r1 = F(-100, 33)
r2 = F(0)
assert r1+r2 == -a2/c
assert r1*r2 == -mu2/c

print("VERIFY_OK")
