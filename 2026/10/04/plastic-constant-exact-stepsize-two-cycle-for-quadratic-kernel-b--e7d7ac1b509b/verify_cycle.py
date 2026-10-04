from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

r = D("1.3")
for _ in range(30):
    r -= (r**3 - r - 1) / (3*r**2 - 1)

a = (1 + (1 + 2*r*r).sqrt()) / (2*r)
b = r*a
q = (a - 1)*(b - 1)

tol = D("1e-60")
assert abs(r**3 - r - 1) < tol
assert D(1) < a < b < D(2)
assert abs((1 + 1/r).sqrt() - r) < tol

def curvature(t):
    return 1 / (2*t*(t - 1)).sqrt()

assert curvature(a) > r
assert abs(curvature(b) - 1/r) < tol

def next_step(prev, cur):
    growth = (1 + cur/prev).sqrt()
    curv = curvature(cur)
    return cur * min(growth, curv)

steps = [b, a]
for _ in range(30):
    steps.append(next_step(steps[-2], steps[-1]))

for k, t in enumerate(steps):
    target = b if k % 2 == 0 else a
    assert abs(t - target) < D("1e-55")

x0 = D("1.23456789")
x = x0
xs = [x]
# gamma_1 uses normalized step a to produce x^1; subsequent steps alternate b,a,...
for k in range(1, 31):
    t = a if k % 2 == 1 else b
    x = (1 - t)*x
    xs.append(x)

for m in range(0, 16):
    if 2*m < len(xs):
        assert abs(xs[2*m] - (q**m)*x0) < D("1e-50")
    if 2*m + 1 < len(xs):
        assert abs(xs[2*m+1] - (1-a)*(q**m)*x0) < D("1e-50")

print("r =", r)
print("a =", a)
print("b =", b)
print("q =", q)
print("q^2 =", q*q)
print("VERIFY_OK")
