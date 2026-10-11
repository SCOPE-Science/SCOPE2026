from itertools import product
from math import isclose


def direct(x, t):
    best = 0.0
    for eps in product((-1.0, 1.0), repeat=len(x)):
        a = max(abs(u + e) for u, e in zip(x, eps))
        b = max(abs(u - e) for u, e in zip(x, eps))
        best = max(best, ((a**t + b**t) / 2.0) ** (1.0 / t))
    return best


def formula(x, t):
    vals = sorted((abs(u) for u in x), reverse=True)
    s2 = vals[1]
    return ((2.0**t + (1.0 + s2)**t) / 2.0) ** (1.0 / t)


cases = [
    (1.0, 0.0),
    (1.0, 0.25),
    (1.0, 1.0),
    (1.0, 0.75, 0.25),
    (-1.0, 0.6, -0.2),
    (0.2, -1.0, 0.5, -0.1),
]
for x in cases:
    for t in (1.0, 1.5, 2.0, 3.0, 7.0):
        a = direct(x, t)
        b = formula(x, t)
        if not isclose(a, b, rel_tol=1e-12, abs_tol=1e-12):
            raise SystemExit((x, t, a, b))
print("VERIFY_OK")
