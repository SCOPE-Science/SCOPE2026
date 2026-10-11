#!/usr/bin/env python3
from fractions import Fraction
from math import comb, sqrt, acos, pi
import cmath

# Exact symbolic coefficient identity for F(lambda + a E), where E = exp(-lambda theta).
# Keys are (power_lambda, power_E, power_a).
def add(d, key, value):
    d[key] = d.get(key, 0) + value

expanded = {}
for k in range(5):
    add(expanded, (4-k, k, k), comb(4,k))
for k in range(3):
    add(expanded, (2-k, k, k), 3*comb(2,k))
add(expanded, (1,0,0), -1)
add(expanded, (0,1,1), -1)
add(expanded, (0,0,0), 1)
expanded = {k:v for k,v in expanded.items() if v}
expected = {
    (4,0,0):1, (2,0,0):3, (1,0,0):-1, (0,0,0):1,
    (3,1,1):4, (1,1,1):6, (0,1,1):-1,
    (2,2,2):6, (0,2,2):3, (1,3,3):4, (0,4,4):1,
}
assert expanded == expected

# Exact zero-delay Routh-Hurwitz data for F(lambda+1/4).
a1 = Fraction(1,1)
a2 = Fraction(27,8)
a3 = Fraction(9,16)
a4 = Fraction(241,256)
d2 = a1*a2-a3
d3 = a1*a2*a3-a3*a3-a1*a1*a4
assert d2 == Fraction(45,16)
assert d3 == Fraction(41,64)
assert a1 > 0 and d2 > 0 and d3 > 0 and a4*d3 > 0
# For x^4 + p x^2 + q x + r, the depressed-quartic discriminant formula gives 697.
p, q, rr = 3, -1, 1
disc = 256*rr**3 - 128*p**2*rr**2 + 144*p*q**2*rr - 27*q**4 + 16*p**4*rr - 4*p**3*q**2
assert disc == 697

# Quartic and derivative.
def F(z):
    return z**4 + 3*z**2 - z + 1

def Fp(z):
    return 4*z**3 + 6*z - 1

def newton(z):
    for _ in range(80):
        dz = F(z)/Fp(z)
        z -= dz
        if abs(dz) < 1e-15:
            break
    return z

seeds = [0.2+0.56j, 0.2-0.56j, -0.2+1.66j, -0.2-1.66j]
roots = [newton(z) for z in seeds]
assert max(abs(F(z)) for z in roots) < 2e-13
# Distinctness and Vieta checks ensure the four Newton results are all roots.
for i in range(4):
    for j in range(i):
        assert abs(roots[i]-roots[j]) > 0.5
assert abs(sum(roots)) < 2e-12
prod = 1+0j
for z in roots:
    prod *= z
assert abs(prod-1) < 2e-12

upper = sorted([z for z in roots if z.imag > 0], key=lambda z:z.real, reverse=True)
assert len(upper) == 2
zp, zn = upper
r = zp.real
y1 = zp.imag
y2 = zn.imag
assert r > 0 and zn.real < 0
assert abs(zn.real + r) < 2e-12

a = 0.25
s = sqrt(a*a-r*r)
alpha = acos(r/a)
# Each tuple is (omega, smallest compatible theta).
candidates = [
    (y1+s, alpha/(y1+s)),
    (y2+s, (pi-alpha)/(y2+s)),
    (y2-s, (pi+alpha)/(y2-s)),
    (y1-s, (2*pi-alpha)/(y1-s)),
]
assert all(w > 0 and th > 0 for w,th in candidates)
ordered = sorted(candidates, key=lambda p:p[1])
wstar, thstar = ordered[0]
assert abs(wstar-0.7055705579827115) < 2e-14
assert abs(thstar-0.8762435337755021) < 2e-14
assert ordered[1][1] > 1.39

# Direct characteristic residual at the first crossing.
zshift = 1j*wstar + a*cmath.exp(-1j*wstar*thstar)
assert abs(F(zshift)) < 2e-12

# Transversality from scalar branch lambda + a exp(-lambda theta)=z.
lam = 1j*wstar
E = cmath.exp(-lam*thstar)
dl = a*lam*E/(1-a*thstar*E)
assert dl.real > 0.1479
assert abs(dl.real-0.14796571376147418) < 2e-13

# The paper's reported frequency is not among any positive crossing frequencies.
all_freq = sorted(w for w,_ in candidates)
assert max(all_freq) < 1.81
assert 2.0083 > max(all_freq)
# For reference, the printed approximate pair also has a large characteristic residual.
reported_residual = abs(F(1j*2.0083 + a*cmath.exp(-1j*2.0083*0.8)))
assert reported_residual > 2.10

print('VERIFY_OK')
print('roots=', [complex(round(z.real,15), round(z.imag,15)) for z in roots])
print('crossings=', [(round(w,15), round(th,15)) for w,th in candidates])
print('theta_star=', format(thstar,'.15f'))
print('omega_star=', format(wstar,'.15f'))
print('crossing_speed=', format(dl.real,'.15f'))
print('reported_pair_residual=', format(reported_residual,'.15f'))
