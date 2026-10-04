from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

def sqrt(x):
    return x.sqrt()

t2 = (D(1) + sqrt(D(5))) / D(2)
t3 = (D(1) + sqrt(D(1) + D(4) * t2 * t2)) / D(2)
t4 = (D(1) + sqrt(D(1) + D(4) * t3 * t3)) / D(2)
b2 = (t2 - D(1)) / t3
b3 = (t3 - D(1)) / t4
c = (D(1) + b2) * (D(1) + b3)
d = (D(1) + b3) * b2 + b3

rminus = b2 / c
r0 = b2 / (D(1) + b2)
rplus = (
    d - (D(1) + b2)
    + sqrt(((D(1) + b2) - d) ** 2 + D(4) * c * b2)
) / (D(2) * c)

tol = D("1e-65")
assert abs(rminus - D("0.15328608409917537989370469626977918742861346372966180512181144667190219941919861")) < D("1e-65")
assert abs(r0 - D("0.21981880260307686377713607886557863179528936254794656465540557893927572572212385")) < D("1e-65")
assert abs(rplus - D("0.28901030911469037856481554099048959241247924579052492317169205910419586845326350")) < D("1e-65")
assert D(0) < rminus < r0 < rplus < D(1)

def A(r):
    return (D(1) + b2) * r - b2

def B(r):
    return (D(1) + b3) * A(r) - b3

def hminus(r):
    return r * B(r) - A(r)

def hplus(r):
    return r * B(r) + A(r)

# Factor/root identities.
assert abs(hminus(D(1))) < tol
assert abs(hminus(rminus)) < tol
assert abs(hplus(rplus)) < tol
assert abs(A(r0)) < tol
assert abs(B(r0) + b3) < tol

# Sign pattern: objective rise iff hminus*hplus > 0.
samples = [
    (rminus / D(2), False),
    ((rminus + r0) / D(2), True),
    ((r0 + rplus) / D(2), True),
    ((rplus + D(1)) / D(2), False),
]
for r, should_rise in samples:
    rise = hminus(r) * hplus(r) > 0
    assert rise is should_rise

# Direct first-four-iterate replay, with x0=1.
def replay(r):
    x0 = D(1)
    x1 = r * x0
    x2 = r * x1
    x3 = r * (x2 + b2 * (x2 - x1))
    x4 = r * (x3 + b3 * (x3 - x2))
    return [x0, x1, x2, x3, x4]

for r, should_rise in samples:
    xs = replay(r)
    assert xs[1] * xs[1] < xs[0] * xs[0]
    assert xs[2] * xs[2] < xs[1] * xs[1]
    assert xs[3] * xs[3] < xs[2] * xs[2]
    assert (xs[4] * xs[4] > xs[3] * xs[3]) is should_rise

xs = replay(r0)
assert abs(xs[3]) < tol
assert abs(xs[4] + b3 * r0 ** 3) < tol
assert abs(xs[4]) > D("1e-6")

qlo = D(1) - rplus
qhi = D(1) - rminus
q0 = D(1) - r0
assert qlo < q0 < qhi
print("VERIFY_OK")
