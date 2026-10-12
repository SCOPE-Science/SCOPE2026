import math
import random

def H(y, a, b, lam):
    return a*y + 0.5*b*y*y + (lam/3.0)*y**3

def h(y, a, b, lam):
    return a + b*y + lam*y*y

def survival(y, a, b, lam):
    return math.exp(-H(y,a,b,lam))

def cdf(y, a, b, lam):
    return 1.0 - survival(y,a,b,lam)

def pdf(y, a, b, lam):
    return h(y,a,b,lam)*survival(y,a,b,lam)

def admissible(a,b,lam,tol=1e-12):
    return a >= 0 and lam >= 0 and b >= -2.0*math.sqrt(a*lam)-tol and not (a==0 and b==0 and lam==0)

# Exact branch logic.
for a in (0.2, 1.0, 3.0):
    lam = 0.0
    for b in (0.0, 0.1, 2.0):
        assert admissible(a,b,lam)
        assert all(h(y,a,b,lam) >= 0 for y in (0.01,1,10,100))
        assert b >= 0

# Random admissible positive-lambda checks.
rng = random.Random(310084)
for _ in range(500):
    a = 10**rng.uniform(-2,1)
    lam = 10**rng.uniform(-2,1)
    lower = -2.0*math.sqrt(a*lam)
    b = lower + rng.random()*(4.0*math.sqrt(a*lam)+2.0)
    assert admissible(a,b,lam)
    if b < 0:
        ystar = -b/(2.0*lam)
        hmin = a - b*b/(4.0*lam)
        assert ystar > 0
        assert hmin >= -1e-12
        assert abs(h(ystar,a,b,lam)-hmin) < 1e-10
        assert b + 2.0*lam*(ystar/2.0) < 0
        assert b + 2.0*lam*(2.0*ystar) > 0
    else:
        assert all(b + 2.0*lam*y > 0 for y in (0.01,1,10))

# Source Figure 3 "decreasing linear" curve.
a,b,lam = 3.0,-0.05,0.0
assert not admissible(a,b,lam)
assert abs(h(60,a,b,lam)) < 1e-14
assert h(61,a,b,lam) < 0
assert pdf(61,a,b,lam) < 0
assert abs(H(120,a,b,lam)) < 1e-12
assert abs(cdf(120,a,b,lam)) < 1e-12
assert H(121,a,b,lam) < 0
assert cdf(121,a,b,lam) < 0
assert survival(121,a,b,lam) > 1

print("VERIFY_OK")
print("figure_h_30", format(h(30,a,b,lam), ".12f"))
print("figure_h_60", format(h(60,a,b,lam), ".12f"))
print("figure_pdf_61", format(pdf(61,a,b,lam), ".18e"))
print("figure_F_120", format(cdf(120,a,b,lam), ".12f"))
print("figure_F_121", format(cdf(121,a,b,lam), ".12f"))
print("figure_S_121", format(survival(121,a,b,lam), ".12f"))
