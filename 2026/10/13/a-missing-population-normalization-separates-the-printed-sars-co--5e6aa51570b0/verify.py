#!/usr/bin/env python3
from fractions import Fraction as F

N0 = F(59_310_000)
mu = F(100, 6413*365)          # 1/(64.13*365)
Lambda = mu*N0
p = F(176,1000)
q = F(24,1000)
gammaA = F(70,1000)
gammaV = F(61,1000)
kappa = F(80,1000)
delta = F(17826,10**9)
eps = F(1,2)

def D():
    z1 = p+q+mu
    return (F(1,1)/z1
            + p/(z1*(gammaA+mu))
            + q*eps/(z1*(kappa+gammaV+mu+delta)))

def r0_mass(beta):
    return beta*(Lambda/mu)*D()

def r0_freq(beta):
    return beta*D()

for beta in (F(34,1000), F(34,100)):
    assert r0_mass(beta) == N0*r0_freq(beta)

r03f = r0_freq(F(34,1000))
r04f = r0_freq(F(34,100))
r03m = r0_mass(F(34,1000))
r04m = r0_mass(F(34,100))

assert F(6114,10000) < r03f < F(6116,10000)
assert F(6114,1000) < r04f < F(6116,1000)
assert 36_000_000 < r03m < 37_000_000
assert 362_000_000 < r04m < 363_000_000

S0 = F(29_675_142)
E0 = F(21_968_562)
A0 = F(2_861_104)
V0 = F(715_275)
beta4 = F(34,100)
infectious = E0+A0+eps*V0
haz_mass = beta4*infectious
haz_freq = haz_mass/N0
assert infectious == F(50_374_607,2)
assert haz_mass == F(856_368_319,100)
assert haz_freq > F(1443,10000) and haz_freq < F(1444,10000)

beta_eff = beta4/N0
assert beta_eff == F(17,2_965_500_000)

print("VERIFY_OK")
print("N0", N0)
print("R0_table3_frequency", float(r03f))
print("R0_table3_mass", float(r03m))
print("R0_table4_frequency", float(r04f))
print("R0_table4_mass", float(r04m))
print("beta_table4_effective_mass", float(beta_eff))
print("initial_infectious_combination", float(infectious))
print("initial_force_mass_per_day", float(haz_mass))
print("initial_force_normalized_per_day", float(haz_freq))
