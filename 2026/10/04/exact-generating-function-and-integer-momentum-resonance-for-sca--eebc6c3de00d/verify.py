from fractions import Fraction
import math

def sf_fraction(beta, s, n, x1=Fraction(1, 1)):
    x = x1
    z = x1
    xs = {1: x}
    zs = {1: z}
    ys = {}
    for t in range(1, n):
        y = (1 - beta) * z + beta * x
        ys[t] = y
        znew = z - s * y
        xnew = Fraction(t, t + 1) * x + Fraction(1, t + 1) * znew
        x, z = xnew, znew
        xs[t + 1] = x
        zs[t + 1] = z
    ys[n] = (1 - beta) * z + beta * x
    return xs, zs, ys

def sf_float(beta, s, n, x1=1.0):
    x = x1
    z = x1
    xs = {1: x}
    zs = {1: z}
    for t in range(1, n):
        y = (1 - beta) * z + beta * x
        znew = z - s * y
        xnew = t / (t + 1) * x + znew / (t + 1)
        x, z = xnew, znew
        xs[t + 1] = x
        zs[t + 1] = z
    return xs, zs

def gf_coeffs(beta, s, n, x1=1.0):
    r = beta / (1 - beta)
    A = 1 - s * (1 - beta)
    # coefficients of (1-q)^r
    num = [1.0]
    for k in range(1, n + 1):
        num.append(num[-1] * (k - 1 - r) / k)
    # coefficients of (1-Aq)^(-r)
    den = [1.0]
    for k in range(1, n + 1):
        den.append(den[-1] * A * (r + k - 1) / k)
    h = []
    for k in range(n + 1):
        h.append(sum(num[j] * den[k - j] for j in range(k + 1)))
    c = x1 / (s * beta)
    # G = c(1-H), so for k>=1 the coefficient is -c*h[k].
    return {k: -c * h[k] for k in range(1, n + 1)}

# Exact resonance at beta=1/2, m=1, s=2.
xs, zs, ys = sf_fraction(Fraction(1, 2), Fraction(2, 1), 4)
assert xs[1] == 1
assert xs[2] == 0
assert zs[3] == 0 and xs[3] == 0 and ys[3] == 0

# Exact default-style resonance beta=9/10, m=9, s=10.
m = 9
beta = Fraction(9, 10)
s = Fraction(10, 1)
xs, zs, ys = sf_fraction(beta, s, 12)
for t in range(1, m + 1):
    predicted = Fraction(1, m) * ((-1) ** (t + 1)) * math.comb(m, t)
    assert xs[t] == predicted
assert xs[m + 1] == 0
assert zs[m + 2] == 0 and xs[m + 2] == 0 and ys[m + 2] == 0

# Direct generating-function coefficient agreement in a noninteger case.
beta = 0.4
s = 1.0
xs, zs = sf_float(beta, s, 40)
coeff = gf_coeffs(beta, s, 40)
for t in range(1, 41):
    assert abs(xs[t] - coeff[t]) < 2e-12

# Noninteger asymptotic constant.
r = beta / (1 - beta)
pred = -(1.0 / (s * beta)) * (s * (1 - beta)) ** (-r) / math.gamma(-r)
xs, zs = sf_float(beta, s, 20000)
scaled = xs[20000] * 20000 ** (r + 1)
assert abs(scaled / pred - 1.0) < 2e-4

# Stable interior: both reported and base states decay.
for beta in (0.0, 0.2, 0.4, 0.8, 0.9):
    ceiling = 2 / (1 - beta)
    for frac in (0.1, 0.5, 0.9):
        s = frac * ceiling
        xs, zs = sf_float(beta, s, 6000)
        assert abs(xs[6000]) < 1e-3
        assert abs(zs[6000]) < 1e-3

# Supercritical: the state grows.
for beta in (0.0, 0.2, 0.4, 0.8):
    ceiling = 2 / (1 - beta)
    xs, zs = sf_float(beta, 1.05 * ceiling, 300)
    assert abs(zs[300]) > 10

# Boundary example with beta<1/2: x decays but z grows, so full-state convergence fails.
beta = 0.25
s = 2 / (1 - beta)
xs, zs = sf_float(beta, s, 20000)
assert abs(xs[20000]) < 0.05
assert abs(zs[20000]) > 5

print("verification passed")
