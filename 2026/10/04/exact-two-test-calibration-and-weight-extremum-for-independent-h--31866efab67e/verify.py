import math
from scipy.integrate import quad
from scipy.optimize import brentq


def closed_form(h, w):
    if w == 0.0 or w == 1.0:
        return h
    t = w * (1.0 - w)
    return h + h*h*t*math.log(1.0 + (1.0-h)/(h*h*t))


def direct_integral(h, w):
    if w == 0.0 or w == 1.0:
        return h
    a = h*w/(1.0-h*(1.0-w))
    survival = quad(lambda u: 1.0 - h*(1.0-w)*u/(u-h*w), a, 1.0,
                    epsabs=2e-13, epsrel=2e-13, limit=200)[0]
    return 1.0-survival

for h, w in [(0.05,0.2),(0.33,0.4),(0.9,0.1),(0.2,0.5)]:
    assert abs(closed_form(h,w)-direct_integral(h,w)) < 2e-11
    assert abs(closed_form(h,w)-closed_form(h,1.0-w)) < 2e-15

vals = [closed_form(0.05,w) for w in (0.1,0.2,0.3,0.4,0.5)]
assert all(a < b for a,b in zip(vals, vals[1:]))

h = 0.05
eq = h + 0.5*h*h*math.log((2.0-h)/h)
assert abs(closed_form(h,0.5)-eq) < 2e-15
assert abs(eq-0.05457945205766206) < 2e-15

cut = brentq(lambda x: closed_form(x,0.5)-0.05, 1e-12, 0.05,
             xtol=1e-14, rtol=1e-14)
assert abs(cut-0.04602921464598153) < 2e-14

for w in (0.0,1.0):
    assert closed_form(0.05,w) == 0.05

print('VERIFY_OK')
print('size_at_0.05=', format(eq,'.17g'))
print('calibrated_0.05_cutoff=', format(cut,'.17g'))
