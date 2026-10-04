from decimal import Decimal, getcontext
getcontext().prec = 60

lam = Decimal(1)
eta = Decimal(1) / Decimal(2)
r = Decimal(3)
nu = Decimal(1) / Decimal(2)
t0 = Decimal(10)
a = eta * lam
s = nu / eta

lower = ((r - 1) * (2*r - 1) * eta) / ((r - 1) * eta - nu)
assert r > 1
assert Decimal(0) < nu < (r - 1) * eta
assert Decimal(0) < a < 1
assert t0 >= max(r, lower, (r - 1)/(r + 1))

x = Decimal(1)
z = Decimal(1)
last = None
N = 200000
for k in range(N):
    t = t0 + k
    q = x / z
    assert Decimal(0) < q <= 1
    y = ((t-r)/t)*x + (r/t)*z
    assert y > 0 and z > 0
    x_next = (1-a)*y
    nu_k = nu*(t-1)/t
    z_next = z - (nu_k/r)*lam*y
    assert z_next > 0
    if k == N-1:
        last = (t*x/z, t*y/z, t*(Decimal(1)-z_next/z))
    x, z = x_next, z_next

pred = (r*(1-a)/a, r/a, s)
tol = Decimal('1e-4')
for got, want in zip(last, pred):
    assert abs(got-want) < tol, (got, want)
print('VERIFY_OK')
