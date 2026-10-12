#!/usr/bin/env python3
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 80

# Source parameters.
nu = F(49,100)
betaE = F(10,1)
nuE = F(1,20)
deltaE = F(3,100)
deltaF = F(1,25)
deltaM = F(1,10)
gamma_s = F(1,1)
Mstar = F(5106,1)

# Reconstruct source carrying capacity from its displayed equilibrium calculation.
Estar = deltaM*Mstar/((1-nu)*nuE)
K = Estar/(1-(nuE+deltaE)*deltaF/(betaE*nu*nuE))

A = nu*(1-nu)*betaE**2*nuE**2
B = betaE/K
C = nuE+deltaE
D = (1-nu)*nuE*betaE
H = deltaM*gamma_s

assert A == F(2499,40000)
assert C == F(2,25)
assert D == F(51,200)
assert H == F(1,10)
assert K == F(416990000,20553)

def m(fr):
    return mp.mpf(fr.numerator)/fr.denominator

Am, Bm, Cm, Dm, Hm, df = map(m,[A,B,C,D,H,deltaF])

def Q(M):
    M = mp.mpf(M)
    u = Bm*Hm*M
    return Am/(Cm*(mp.sqrt(Dm+u)+mp.sqrt(u))**2)

# Direct algebraic identity at sample M values: q(F,M) never exceeds Q(M).
def q(Fv,Mv):
    Fv=mp.mpf(Fv); Mv=mp.mpf(Mv)
    return Am*Fv/((Bm*Fv+Cm)*(Dm*Fv+Hm*Mv*(Bm*Fv+Cm)))

for Mv in [0, 1, 36000, 120000, 300000]:
    for Fv in [mp.mpf("1e-8"), 1, 100, 10000, 1000000]:
        assert q(Fv,Mv) <= Q(Mv)*(1+mp.mpf("1e-60"))

period = mp.mpf(16)
def profile(t,s):
    return mp.mpf(s)*(mp.mpf("1.3")+mp.sin(mp.pi*t/8))

def avg_quad(s):
    f=lambda t: Q(profile(t,s))
    return mp.quad(f,[0,4,8,12,16])/16

def avg_simpson(s, n=65536):
    assert n % 2 == 0
    h=period/n
    total=Q(profile(0,s))+Q(profile(period,s))
    for j in range(1,n):
        total += (4 if j%2 else 2)*Q(profile(j*h,s))
    return total*h/(3*period)

a120 = avg_quad(120000)
a60 = avg_quad(60000)
s120 = avg_simpson(120000)
s60 = avg_simpson(60000)

assert abs(a120-s120) < mp.mpf("1e-13")
assert abs(a60-s60) < mp.mpf("1e-13")
assert a120 < df
assert a60 > df

target120 = mp.mpf("0.03822177095026780420534333624503042392619")
target60 = mp.mpf("0.07375017181441667510956997146688721081429")
assert abs(a120-target120) < mp.mpf("1e-38")
assert abs(a60-target60) < mp.mpf("1e-38")

root = mp.findroot(lambda s: avg_quad(s)-df, (110000,120000))
assert mp.mpf("114458.94") < root < mp.mpf("114458.96")

print("VERIFY_OK")
print("K", mp.nstr(m(K),30))
print("A", mp.nstr(Am,30))
print("B", mp.nstr(Bm,30))
print("avg_120000", mp.nstr(a120,45))
print("avg_60000", mp.nstr(a60,45))
print("simpson_diff_120000", mp.nstr(abs(a120-s120),10))
print("simpson_diff_60000", mp.nstr(abs(a60-s60),10))
print("s_env", mp.nstr(root,45))
