import math

def A(m):
    return ((m - 1.0) / m) ** (m - 1)

def witness(weights):
    q = len(weights)
    alpha2 = q / (q - 1.0)
    den = 1.0
    for p in weights:
        den *= 1.0 + alpha2 * p
    return alpha2 / den

for weights in ([1/3, 1/3, 1/3], [0.5, 0.3, 0.2], [0.4, 0.2, 0.2, 0.2]):
    q = len(weights)
    val = witness(weights)
    assert val >= A(q) - 1e-14
    if max(weights) - min(weights) > 1e-12:
        assert val > A(q)

for q in (10, 30, 100, 3000):
    scaled = q * (A(q) - math.exp(-1.0))
    if q == 3000:
        assert abs(scaled - 1.0/(2.0*math.e)) < 4e-5

for q in (2, 3, 5, 10):
    for mult in (2, 5, 20):
        n = q * mult
        assert A(q) > A(n)

print('VERIFY_OK')
