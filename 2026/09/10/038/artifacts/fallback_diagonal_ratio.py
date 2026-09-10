"""Decisive honest Gaussian-datum ratio, diagonal-following boxes (lane-586).

Fixes centering bug in fallback_gaussian_ratio.py: beams from caps at mean
centre wbar travel along x' = -2*wbar*x3 (diagonal), so the numerator box must
follow the diagonal. Uses corner block (cells [0,8)x[0,8), wbar~(1/64,1/64))
so the stem stays near-vertical and long inside B_{R0}. Closed-form Gaussian
Eg via cmath (exact up to fp). Generous direction: numerator box wide
(half-width 512 transverse around diagonal, x3 +-32768, all inside B_{R0});
denominator single-tube box wide (may slightly overestimate denominator ->
underestimates ratio, i.e. conservative for a PASS claim, generous for FAIL).
Success iff R >= 1.5. Stdlib, seeded.
"""
import random, math, cmath

s = 1.0/512.0
s2 = s*s
cell = 1.0/256.0
# corner block: 8x8 adjacent canonical cells at corner of [0,1]^2
block = [((i+0.5)*cell, (j+0.5)*cell) for i in range(8) for j in range(8)]
N = 64
wbar1 = sum(w[0] for w in block)/N
wbar2 = sum(w[1] for w in block)/N
print(f"wbar=({wbar1:.5f},{wbar2:.5f})")

def Eg(w1, w2, x1, x2, x3):
    a = 1.0/(2.0*s2) - 1j*x3
    b1 = 1j*x1 + w1/s2
    b2 = 1j*x2 + w2/s2
    c = -(w1*w1+w2*w2)/(2.0*s2)
    return math.pi/a * cmath.exp(c + (b1*b1+b2*b2)/(4.0*a))

def S(x1, x2, x3):
    t = 0j
    for (w1, w2) in block:
        t += Eg(w1, w2, x1, x2, x3)
    return t

# Numerator: diagonal-following box, x3 in [-32768,32768], transverse
# box half-width W=512 around xc=-2*wbar*x3. Vertices inside B_65536?
# max |x|: x3=32768: xc=(-2160,-2160), corner +512 -> |x|~ sqrt(2672^2*2+32768^2)~32980 < 65536 OK.
random.seed(11)
M1 = 15000
W = 512.0
H = 32768.0
box_vol = (2*W)*(2*W)*(2*H)
acc = acc2 = 0.0
for _ in range(M1):
    x3 = random.uniform(-H, H)
    xc1 = -2*wbar1*x3; xc2 = -2*wbar2*x3
    x1 = random.uniform(xc1-W, xc1+W)
    x2 = random.uniform(xc2-W, xc2+W)
    p = abs(S(x1, x2, x3))**4
    acc += p; acc2 += p*p
mean = acc/M1; var = acc2/M1 - mean*mean
INT = box_vol*mean; INT_se = box_vol*math.sqrt(var/M1)
print(f"numerator INT = {INT:.4e} +- {INT_se:.3e} (M={M1})")

# Denominator: single tube (block[0]) around its own ray, x3 +-65536, half-width 2048
w1, w2 = block[0]
M2 = 15000
W2 = 2048.0; H2 = 65536.0
Tvol = (2*W2)*(2*W2)*(2*H2)
acc = acc2 = 0.0
for _ in range(M2):
    x3 = random.uniform(-H2, H2)
    x1 = random.uniform(-2*w1*x3-W2, -2*w1*x3+W2)
    x2 = random.uniform(-2*w2*x3-W2, -2*w2*x3+W2)
    p = abs(Eg(w1, w2, x1, x2, x3))**4
    acc += p; acc2 += p*p
mean = acc/M2; var = acc2/M2 - mean*mean
ONE = Tvol*mean; ONE_se = Tvol*math.sqrt(var/M2)
print(f"single-tube L4^4 = {ONE:.4e} +- {ONE_se:.3e} (M={M2})")

DEN = (N*ONE**0.5)**2
R4 = INT/DEN
R = R4**0.25
R4hi = (INT+2*INT_se)/((N*(max(ONE-2*ONE_se,0.5*ONE))**0.5)**2)
print(f"ratio R = {R:.4f} (R^4={R4:.4f}, +2se {R4hi**0.25:.4f}) vs 1.5 -> {'PASS' if R>=1.5 else 'FAIL'}")
