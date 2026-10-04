import math


def fgrad(a, x, y):
    n = y - x*x
    f = x**4 + a*n*n
    gx = 4*x**3 - 4*a*x*n
    gy = 2*a*n
    return f, gx, gy


def short_step(a, x, y):
    f, gx, gy = fgrad(a, x, y)
    h = 1.0/(2.0*a)
    return x - h*gx, y - h*gy


def polyak_step(a, x, y):
    f, gx, gy = fgrad(a, x, y)
    den = gx*gx + gy*gy
    alpha = f/den
    return x - alpha*gx, y - alpha*gy


def epoch(a, x, y, k):
    pre = None
    for _ in range(k):
        x, y = short_step(a, x, y)
    pre = (x, y)
    x, y = polyak_step(a, x, y)
    return x, y, pre


def run_case(a, k, steps=15):
    x = 0.02
    y = x*x
    last_ratio = None
    last_u = None
    last_c = None
    for _ in range(steps):
        old_x = x
        x, y, pre = epoch(a, x, y, k)
        last_ratio = x/old_x
        last_u = (y - x*x)/(x*x)
        px, py = pre
        last_c = (py - px*px)/(px**4)
    return last_ratio, last_u, last_c


r1, u1, c1 = run_case(0.5, 1)
assert abs(r1 - 0.75) < 2e-6, (r1, u1, c1)
assert abs(u1 + 0.2) < 5e-5, (r1, u1, c1)

r2, u2, c2 = run_case(10.0, 2)
assert abs(r2 - 0.75) < 2e-6, (r2, u2, c2)
assert abs(u2 + 1.0/9.0) < 5e-5, (r2, u2, c2)
assert abs(c2 - 0.4) < 5e-5, (r2, u2, c2)

print('VERIFY_OK')
