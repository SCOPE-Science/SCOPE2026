#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 60

u0 = mp.mpf("4.8")
v0 = mp.mpf("8.3")
a = mp.mpf("2.5")
c = mp.mpf("2.5")
d = mp.mpf("2")
p = mp.mpf("0.2")
m = mp.mpf("0.4")
T = mp.mpf("1.5")
k = mp.mpf("16")

Rinf = (1-p)*c*v0**m/(m*d*u0**(1-p))
RT = (1-p)*c*v0**m*(1-mp.e**(-m*d*T))/(m*d*u0**(1-p))
K = (1-p)*a*(mp.e**(d*T)-1)/(d*v0*mp.log(RT))

def Phi(t, kval):
    return (1-p)*a*(mp.e**(d*t)-1)/(kval*d*v0)

coarse_margin = RT * mp.e**(-Phi(T, k))
integral = mp.quad(lambda s: mp.e**(-m*d*s-Phi(s, k)), [0, T])
sharp_margin = (1-p)*c*v0**m*integral/u0**(1-p)

assert Rinf > 1
assert RT > 1
assert mp.mpf("15.37") < K < mp.mpf("15.39")
assert k > K
assert coarse_margin > 1
assert sharp_margin > 1
assert sharp_margin > coarse_margin

print("VERIFY_OK")
print("R_infinity", mp.nstr(Rinf, 30))
print("R_T", mp.nstr(RT, 30))
print("K_T", mp.nstr(K, 30))
print("coarse_margin_k16", mp.nstr(coarse_margin, 30))
print("sharp_margin_k16", mp.nstr(sharp_margin, 30))
