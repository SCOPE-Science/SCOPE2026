import math

def coefficients(xi, eta, b):
    c = 1.0 / math.sqrt(1.0 + 0.25 * math.sqrt(xi) * b)
    d = 1.0 / (1.0 + 0.25 * math.sqrt(xi * eta) * b)
    r = 0.5 * xi * xi * c * d
    s = xi * eta * d
    return c, d, r, s

def advance_buffer(xi, b):
    c = 1.0 / math.sqrt(1.0 + 0.25 * math.sqrt(xi) * b)
    return b + xi * xi * c * (1.0 + b)

def replay(xi, eta, N):
    b = 0.0
    P = 1.0
    X = 0.0
    samples = {}
    for t in range(N):
        c, d, r, s = coefficients(xi, eta, b)
        assert 0.0 <= r <= 0.5 + 1e-15
        P *= 1.0 - r
        X += s / P
        b = advance_buffer(xi, b)
        if t in (999, 9999, N - 1):
            samples[t + 1] = (b, c, d, r, s, P, X)
    return b, P, X, samples

# Check asymptotic constants at several source-permitted global rates and scales.
for xi in (0.1, 0.3, 0.7, 1.0):
    for eta in (0.2, 1.0, 3.0):
        N = 200000
        b, P, X, samples = replay(xi, eta, N)
        t = float(N)
        c, d, r, s = coefficients(xi, eta, b)
        assert abs((b / (t*t)) / (xi ** 3.5) - 1.0) < 0.01
        assert abs((t*c) / (2.0/(xi*xi)) - 1.0) < 0.01
        assert abs((t*t*d) / (4.0/(xi**4 * math.sqrt(eta))) - 1.0) < 0.02
        assert abs((t**3*r) / (4.0/(xi**4 * math.sqrt(eta))) - 1.0) < 0.03
        assert abs((t*t*s) / (4.0*math.sqrt(eta)/(xi**3)) - 1.0) < 0.02
        assert P > 0.0
        assert X > 0.0

# Concrete witness xi=eta=1.
xi = eta = 1.0
N = 300000
b, P, XN, samples = replay(xi, eta, N)
assert 0.17 < P < 0.18
assert 16.3 < XN < 16.5

x0 = 20.0
b = 0.0
x = x0
for t in range(N):
    c, d, r, s = coefficients(xi, eta, b)
    assert x > 0.0
    x = (1.0-r)*x - s
    b = advance_buffer(xi, b)
assert x > 0.5

# Variation-of-constants reconstruction at a finite horizon.
b = 0.0
P = 1.0
S = 0.0
x = x0
for t in range(5000):
    c, d, r, s = coefficients(xi, eta, b)
    Pn = P * (1.0-r)
    S += s / Pn
    x = (1.0-r)*x - s
    b = advance_buffer(xi, b)
    P = Pn
assert abs(x - P*(x0-S)) < 1e-10

print("verification passed")
