import math

A = math.asinh(1.0)


def chebyshev_T(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return x
    t0, t1 = 1.0, x
    for _ in range(1, n):
        t0, t1 = t1, 2.0*x*t1 - t0
    return t1


def V(n, t):
    return 0.5*(1.0 - chebyshev_T(n, 1.0 - 2.0*t))


def stationarity(n, d, y):
    m = d - 1
    s = math.sinh(y)
    c = math.cosh(y)
    return 1.0 - s**(2*m) - m*n*math.tanh(y/n)*s**(2*m-1)*c


def y_star(n, d):
    assert d >= 3 and d % 2 == 1
    lo, hi = 0.0, A
    for _ in range(100):
        mid = 0.5*(lo + hi)
        if stationarity(n, d, mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def delta(n, d):
    if d == 1:
        return 0.0, 0.0
    y = y_star(n, d)
    s = math.sinh(y)
    val = math.sinh(y/n)**2 * (1.0 - s**(2*(d-1)))
    return val, y


def epsilon(n):
    return math.sinh(A/n)**2


def kappa(d):
    assert d >= 3 and d % 2 == 1
    m = d - 1
    def f(y):
        s = math.sinh(y)
        c = math.cosh(y)
        return 1.0 - s**(2*m) - m*y*s**(2*m-1)*c
    lo, hi = 0.0, A
    for _ in range(100):
        mid = 0.5*(lo + hi)
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    y = 0.5*(lo + hi)
    val = y*y*(1.0 - math.sinh(y)**(2*m))
    return val, y


print(f"A^2 = {A*A:.15f}")
for d in (3, 5, 7):
    kap, y = kappa(d)
    m = d - 1
    beta = m/(m+1)**(1.0 + 1.0/m)
    print(f"d={d}: kappa={kap:.15f}, beta={beta:.15f}, ratio_to_uniform={kap/(A*A):.15f}, y_inf={y:.15f}")

for n in (2, 4, 8, 16):
    for d in (3, 5, 7):
        de, y = delta(n, d)
        t = -math.sinh(y/n)**2
        q = de + t*(1.0 - V(n, t)**(d-1))
        print(f"n={n:2d}, d={d}: delta={de:.15e}, epsilon={epsilon(n):.15e}, ratio={de/epsilon(n):.12f}, q(t*)={q:.3e}")

# Dense sign check of the sharpened polynomial over a bounded window that includes
# the only region where negativity could occur. The analytic proof covers all t<=1.
worst = 1.0
worst_case = None
for n in (2, 3, 4, 6):
    for d in (3, 5, 7):
        de, _ = delta(n, d)
        local = float('inf')
        for j in range(20001):
            t = -2.0*epsilon(n) + (1.0 + 2.0*epsilon(n))*j/20000.0
            q = de + t*(1.0 - V(n, t)**(d-1))
            local = min(local, q)
        if local < worst:
            worst = local
            worst_case = (n, d)
print(f"dense_check_min={worst:.3e} at n,d={worst_case}")
