import math

def sign0(x):
    return 0.0 if x == 0.0 else (1.0 if x > 0.0 else -1.0)

def replay(beta1, beta2, G, eps, eta, T, v0=0.0):
    m = 0.0
    v = v0
    x = 0.0
    ms = []
    vs = []
    xs = []
    for t in range(1, T + 1):
        g = G if t % 2 else -G
        m = beta1 * m + (1.0 - beta1) * g
        v = v - (1.0 - beta2) * sign0(v - g*g) * g*g
        x = x - eta * m / (math.sqrt(v) + eps)
        ms.append(m)
        vs.append(v)
        xs.append(x)
    return ms, vs, xs

# Exact first-moment formula.
beta1 = 0.9
G = 2.0
p = (1.0 - beta1) * G / (1.0 + beta1)
ms, vs, xs = replay(beta1, 0.875, G, 0.03, 0.02, 100)
for t, m in enumerate(ms, 1):
    target = p * ((-1.0) ** (t-1)) * (1.0 - ((-beta1) ** t))
    assert abs(m - target) < 3e-15

# Integer reciprocal step: s=1/8, so q=8 and v locks exactly.
beta2 = 0.875
ms, vs, xs = replay(beta1, beta2, G, 0.03, 0.02, 2000)
for t in range(8, len(vs)):
    assert vs[t] == G*G
assert abs(xs[-1] / len(xs)) < 2e-4

# Noninteger reciprocal steps with opposite N parities.
for s in (3.0/32.0, 7.0/64.0):
    beta2 = 1.0 - s
    q = 1.0 / s
    N = int(math.floor(q))
    L = N * s * G * G
    U = (N + 1) * s * G * G
    eps = 0.03
    eta = 0.02
    ms, vs, xs = replay(beta1, beta2, G, eps, eta, 300000)

    # Exact two-cycle after crossing.
    for t in range(N + 1, min(N + 101, len(vs))):
        time = t + 1
        expected = U if ((time - (N + 1)) % 2 == 0) else L
        assert abs(vs[t] - expected) < 2e-14

    delta = 1.0 / (math.sqrt(L) + eps) - 1.0 / (math.sqrt(U) + eps)
    slope = ((-1) ** N) * eta * p * delta / 2.0
    empirical = xs[-1] / len(xs)
    assert abs(empirical - slope) < 2e-7
    assert empirical * slope > 0.0

# Initializing at the squared-gradient level suppresses the denominator phase.
s = 3.0/32.0
beta2 = 1.0 - s
ms, vs, xs = replay(beta1, beta2, G, 0.03, 0.02, 100000, v0=G*G)
assert all(v == G*G for v in vs)
assert abs(xs[-1] / len(xs)) < 4e-6

print("verification passed")
