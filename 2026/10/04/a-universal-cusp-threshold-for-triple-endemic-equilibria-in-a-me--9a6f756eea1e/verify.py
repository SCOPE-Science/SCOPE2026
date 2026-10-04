#!/usr/bin/env python3
import math

def bisect(fun, lo, hi, iters=200):
    flo = fun(lo)
    fhi = fun(hi)
    assert flo * fhi < 0.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        fm = fun(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)

R = 20.0
q = 0.43
m1 = 0.43
m2 = 0.5
a = b = n = 1.0
k = 20.0

Rc = 4.0 * math.exp(1.5)
qc = 2.0 * math.exp(-1.5)
assert R > Rc
assert abs(Rc - 17.92675628135226) < 1e-13
assert abs(qc - 0.44626032029685964) < 1e-13

def N(z):
    return 1.0 - z / R - (1.0 - 2.0 * z / R) * math.log(z)

def G(z):
    return math.log(z) / (z * (1.0 - z / R))

z_minus = bisect(N, 3.0, 4.0)
z_plus = bisect(N, 6.0, 7.0)
q_max = G(z_minus)
q_min = G(z_plus)

assert q_min < q < q_max
assert 0.4264 < q_min < 0.4266
assert 0.4338 < q_max < 0.4341

roots = [
    bisect(lambda z: G(z) - q, 2.0, 3.0),
    bisect(lambda z: G(z) - q, 4.0, 5.0),
    bisect(lambda z: G(z) - q, 7.0, 8.0),
]

Sq = (m2 * n - m1) / (b * m2)
checks = []
for z in roots:
    I = math.log(z) / m1
    S = n * z / b
    residual = I - (a / b) * math.exp(m1 * I) * (1.0 - math.exp(m1 * I) / R)
    assert abs(residual) < 1e-12
    assert S > Sq

    c = -m1 + m2 * n
    u = n * I / (S * (1.0 + m2 * n * I))
    v = n * (1.0 + c * I) / (1.0 + m2 * n * I)
    A = a * (1.0 - 2.0 * S / k)
    tr = A - u + v - n
    det = A * (v - n) + n * u

    gp = N(z) / (z * z * (1.0 - z / R) ** 2)
    det_identity = n * I * b * z * (1.0 - z / R) / (1.0 + m2 * n * I) * gp
    assert abs(det - det_identity) < 1e-12
    checks.append((S, I, tr, det))

assert checks[0][2] < 0.0 and checks[0][3] > 0.0
assert checks[1][3] < 0.0
assert checks[2][2] < 0.0 and checks[2][3] > 0.0

print("VERIFY_OK")
print("Rc", repr(Rc))
print("qc", repr(qc))
print("q_min", repr(q_min))
print("q_max", repr(q_max))
for row in checks:
    print("equilibrium", *(repr(x) for x in row))
