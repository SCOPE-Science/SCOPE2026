#!/usr/bin/env python3
from fractions import Fraction as F
import mpmath as mp

# Source parameter values.
b1 = F(121,1000)
muh = F(121,10000)
beta1 = F(14,100)
beta2 = F(2,100)
beta3 = F(10,100)
deltah = F(8,10)
gammah = F(25,100)
b2 = F(2,1000)
gammav = F(23,100)
deltav = F(1,1000)

qh = muh + deltah + gammah
qv = gammav + deltav
Sh = b1 / muh
Sv = b2 / gammav

a = beta1 * Sh / qh
c = beta2 * beta3 * Sh * Sv / (qh * qv)
T = a + c
theta = c / T

sens_T = {
    "b1": F(1),
    "mu_h": -(F(1) + muh/qh),
    "beta2": theta,
    "beta1": a/T,
    "lambda_h": F(0),
    "delta_h": -deltah/qh,
    "gamma_h": -gammah/qh,
    "b2": theta,
    "gamma_v": -theta*(F(1)+gammav/qv),
    "beta3": theta,
    "delta_v": -theta*(deltav/qv),
}

assert Sh == 10
assert Sv == F(1,115)
assert sens_T["lambda_h"] == 0
assert sens_T["delta_h"] < 0
assert sens_T["gamma_h"] < 0
assert sens_T["beta1"] > F(999,1000)
assert sens_T["beta2"] < F(1,1000)
assert sens_T["beta3"] < F(1,1000)
assert sens_T["b2"] < F(1,1000)

mp.mp.dps = 60
am = mp.mpf(a.numerator) / a.denominator
cm = mp.mpf(c.numerator) / c.denominator
Rm = (am + mp.sqrt(am*am + 4*cm))/2
assert abs(Rm*Rm - am*Rm - cm) < mp.mpf("1e-55")
assert Rm > 1
assert mp.mpf(T.numerator)/T.denominator > 1

# Finite-difference replay for selected spectral sensitivities.
params = {
    "b1": mp.mpf("0.121"),
    "mu_h": mp.mpf("0.0121"),
    "beta1": mp.mpf("0.14"),
    "beta2": mp.mpf("0.02"),
    "beta3": mp.mpf("0.10"),
    "lambda_h": mp.mpf("1"),
    "delta_h": mp.mpf("0.8"),
    "gamma_h": mp.mpf("0.25"),
    "b2": mp.mpf("0.002"),
    "gamma_v": mp.mpf("0.23"),
    "delta_v": mp.mpf("0.001"),
}

def Rngm(p):
    qh = p["mu_h"] + p["delta_h"] + p["gamma_h"]
    qv = p["gamma_v"] + p["delta_v"]
    sh = p["b1"]/p["mu_h"]
    sv = p["b2"]/p["gamma_v"]
    aa = p["beta1"]*sh/qh
    cc = p["beta2"]*p["beta3"]*sh*sv/(qh*qv)
    return (aa + mp.sqrt(aa*aa + 4*cc))/2

R0 = Rngm(params)
eps = mp.mpf("1e-7")
fd = {}
for key in ["beta1","beta2","lambda_h","delta_h","gamma_h"]:
    pplus = dict(params)
    pminus = dict(params)
    if key == "lambda_h":
        # R does not depend on lambda_h at all.
        pplus[key] *= 1+eps
        pminus[key] *= 1-eps
    else:
        pplus[key] *= 1+eps
        pminus[key] *= 1-eps
    fd[key] = (Rngm(pplus)-Rngm(pminus))/(2*eps*R0)

assert abs(fd["lambda_h"]) < mp.mpf("1e-45")
assert fd["delta_h"] < 0
assert fd["gamma_h"] < 0
assert fd["beta1"] > mp.mpf("0.99")
assert fd["beta2"] < mp.mpf("0.001")

print("VERIFY_OK")
print("Sh0", Sh)
print("Sv0", Sv)
print("T", mp.nstr(mp.mpf(T.numerator)/T.denominator, 30))
print("R_NGM", mp.nstr(Rm, 30))
for k,v in sens_T.items():
    print("S_T_"+k, mp.nstr(mp.mpf(v.numerator)/v.denominator, 24))
for k,v in fd.items():
    print("FD_R_"+k, mp.nstr(v, 24))
