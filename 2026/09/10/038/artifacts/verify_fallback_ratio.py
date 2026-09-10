"""INDEPENDENT verifier for fallback 64-cap bush ratio (lane-586).

Recomputes R(f*) from the datum record ONLY (cap list + B* + coefficients),
with independently chosen MC boxes/seeds and an exactness cross-check of Eg
against direct numerical quadrature of the oscillatory integral at one point.
Success iff R(f*) >= 3/2.
"""
import json, random, math, cmath

rec = json.load(open("output/artifacts/fallback_datum.json"))
s = rec["profile_s"]
caps = [tuple(c) for c in rec["cap_centers"]]
N = len(caps)
assert N == 64 and rec["coefficients"] == "all_ones"
s2 = s*s

def Eg(w1, w2, x1, x2, x3):
    a = 1.0/(2.0*s2) - 1j*x3
    b1 = 1j*x1 + w1/s2
    b2 = 1j*x2 + w2/s2
    c = -(w1*w1+w2*w2)/(2.0*s2)
    return math.pi/a * cmath.exp(c + (b1*b1+b2*b2)/(4.0*a))

# Exactness cross-check: direct midpoint quadrature of E g at one point.
# Domain must cover Gaussian tails (+-8s), NOT the cap box (s << cell).
w1, w2 = caps[0]
X = (100.0, -50.0, 1000.0)
nq = 200
ext = 8*s
lo1, hi1 = w1-ext, w1+ext
lo2, hi2 = w2-ext, w2+ext
h1, h2 = (hi1-lo1)/nq, (hi2-lo2)/nq
t = 0j
for i in range(nq):
    u1 = lo1+(i+0.5)*h1
    for j in range(nq):
        u2 = lo2+(j+0.5)*h2
        g = math.exp(-((u1-w1)**2+(u2-w2)**2)/(2*s2))
        t += g*cmath.exp(1j*(X[0]*u1+X[1]*u2+X[2]*(u1*u1+u2*u2)))
direct = t*h1*h2
closed = Eg(w1, w2, *X)
rel = abs(direct-closed)/abs(closed)
print(f"Eg cross-check: rel err = {rel:.2e} -> {'OK' if rel < 2e-2 else 'MISMATCH'}")
assert rel < 2e-2

wbar1 = sum(w[0] for w in caps)/N
wbar2 = sum(w[1] for w in caps)/N

def S(x1, x2, x3):
    t = 0j
    for (a1, a2) in caps:
        t += Eg(a1, a2, x1, x2, x3)
    return t

# Numerator: INDEPENDENT box choice (W=640, H=40000, seed 99)
random.seed(99)
M1 = 15000
W, H = 640.0, 40000.0
vol = (2*W)*(2*W)*(2*H)
acc = acc2 = 0.0
for _ in range(M1):
    x3 = random.uniform(-H, H)
    x1 = random.uniform(-2*wbar1*x3-W, -2*wbar1*x3+W)
    x2 = random.uniform(-2*wbar2*x3-W, -2*wbar2*x3+W)
    p = abs(S(x1, x2, x3))**4
    acc += p; acc2 += p*p
mean = acc/M1; var = acc2/M1-mean*mean
INT = vol*mean; INT_se = vol*math.sqrt(var/M1)

# Denominator: independent seed/box (W2=2560, seed 123)
a1, a2 = caps[0]
M2 = 15000
W2, H2 = 2560.0, 65536.0
Tv = (2*W2)*(2*W2)*(2*H2)
acc = acc2 = 0.0
for _ in range(M2):
    x3 = random.uniform(-H2, H2)
    x1 = random.uniform(-2*a1*x3-W2, -2*a1*x3+W2)
    x2 = random.uniform(-2*a2*x3-W2, -2*a2*x3+W2)
    p = abs(Eg(a1, a2, x1, x2, x3))**4
    acc += p; acc2 += p*p
mean = acc/M2; var = acc2/M2-mean*mean
ONE = Tv*mean; ONE_se = Tv*math.sqrt(var/M2)

R = (INT/(N*ONE**0.5)**2)**0.25
Rlo = ((INT-2*INT_se)/((N*((ONE+2*ONE_se)**0.5))**2))**0.25
print(f"VERIFY: R = {R:.4f} (conservative -2se: {Rlo:.4f}) vs 1.5")
print("VERIFY_OK" if Rlo >= 1.5 else "VERIFY_FAIL")
