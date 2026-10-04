from fractions import Fraction
import cmath
import math

def step(x, mprev, alpha, lam, rho, beta):
    sig = 0 if x == 0 else (1 if x > 0 else -1)
    g = lam * (x + rho * sig)
    m = beta * mprev + (1 - beta) * g
    return x - alpha * m, m

def roots(beta, s):
    tr = 1 + beta - s
    disc = tr * tr - 4 * beta
    z = cmath.sqrt(disc)
    return (tr + z) / 2, (tr - z) / 2

beta = Fraction(1, 2)
lam = Fraction(2, 1)
rho = Fraction(3, 1)
s = Fraction(1, 1)
alpha = s / (lam * (1 - beta))
c = s * rho / (2 * (1 + beta) - s)
xp, mp = step(c, -2 * c / alpha, alpha, lam, rho, beta)
xm, mm = step(-c, 2 * c / alpha, alpha, lam, rho, beta)
assert xp == -c and mp == 2 * c / alpha
assert xm == c and mm == -2 * c / alpha

for beta in (0.0, 0.2, 0.5, 0.9):
    for frac in (0.2, 0.7, 0.99):
        s = frac * 2 * (1 + beta)
        lam = 1.7
        rho = 0.8
        alpha = s / (lam * (1 - beta))
        c = s * rho / (2 * (1 + beta) - s)
        xp, mp = step(c, -2 * c / alpha, alpha, lam, rho, beta)
        xm, mm = step(-c, 2 * c / alpha, alpha, lam, rho, beta)
        assert abs(xp + c) < 1e-11
        assert abs(mp - 2 * c / alpha) < 1e-11
        assert abs(xm - c) < 1e-11
        assert abs(mm + 2 * c / alpha) < 1e-11
        r1, r2 = roots(beta, s)
        assert max(abs(r1), abs(r2)) < 1

    s = 2 * (1 + beta) + 1e-6
    r1, r2 = roots(beta, s)
    assert max(abs(r1), abs(r2)) > 1

    lo = (1 - math.sqrt(beta)) ** 2
    hi = (1 + math.sqrt(beta)) ** 2
    for s in (lo, (lo + hi) / 2, hi):
        r1, r2 = roots(beta, s)
        assert abs(max(abs(r1), abs(r2)) - math.sqrt(beta)) < 1e-7

for beta in (0.0, 0.2, 0.5, 0.9):
    for excess in (0.0, 0.05):
        s = 2 * (1 + beta) + excess
        lam = 1.0
        rho = 0.7
        alpha = s / (lam * (1 - beta))
        x = 0.3
        mprev = 0.0
        mags = []
        signs = []
        for _ in range(20):
            mags.append(abs(x))
            signs.append(1 if x > 0 else -1)
            x, mprev = step(x, mprev, alpha, lam, rho, beta)
        assert all(signs[i] * signs[i + 1] == -1 for i in range(len(signs) - 1))
        assert all(mags[i + 1] > mags[i] for i in range(len(mags) - 1))

print("verification passed")
