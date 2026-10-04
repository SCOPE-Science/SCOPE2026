from decimal import Decimal, getcontext
getcontext().prec = 60

D = Decimal
Lam = D('22.22')
mu = D('0.2')
beta = D('0.003')
gamma = D('0.1')
p0 = D('0.1')
sigma = D('0.002')

p = p0 * sigma
R0 = beta * Lam / ((gamma + mu) * (p + mu))
C = (p + mu) * (R0 - D(1))

assert abs(R0 - D(101) / D(91)) < D('1e-55')
assert abs(C - D('0.022')) < D('1e-55')


def endemic_root(u0, u2, a, b):
    e = a / b
    def f(I):
        return beta * I + e * sigma * u0 * I / (D(1) + e * u2 * I) - C
    lo = D(0)
    hi = C / beta
    assert f(lo) < 0 and f(hi) > 0
    for _ in range(240):
        mid = (lo + hi) / D(2)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    root = (lo + hi) / D(2)
    assert abs(f(root)) < D('1e-50')
    return root

u0 = D('0.5')
u2 = D('0.01')
a = D('0.2')
b = D('0.55')
I0 = endemic_root(u0, u2, a, b)

# One-at-a-time comparative statics around the source baseline.
assert endemic_root(D('0.2'), u2, a, b) > I0 > endemic_root(D('0.8'), u2, a, b)
assert endemic_root(u0, D('0.005'), a, b) < I0 < endemic_root(u0, D('0.02'), a, b)
assert endemic_root(u0, u2, D('0.1'), b) > I0 > endemic_root(u0, u2, D('0.4'), b)
assert endemic_root(u0, u2, a, D('0.3')) < I0 < endemic_root(u0, u2, a, D('0.8'))

# Direct positivity checks for the derivatives at the baseline root.
e = a / b
den = D(1) + e * u2 * I0
F_I = beta + e * sigma * u0 / (den * den)
F_u0 = e * sigma * I0 / den
F_u2 = -(e * e * sigma * u0 * I0 * I0) / (den * den)
F_e = sigma * u0 * I0 / (den * den)
assert F_I > 0 and F_u0 > 0 and F_u2 < 0 and F_e > 0

# Large-u0 scaling: u0*I* -> C*b/(a*sigma).
target = C * b / (a * sigma)
I_big = endemic_root(D('1000000'), u2, a, b)
scaled = D('1000000') * I_big
assert abs(scaled - target) / target < D('1e-4')

print('VERIFY_OK')
