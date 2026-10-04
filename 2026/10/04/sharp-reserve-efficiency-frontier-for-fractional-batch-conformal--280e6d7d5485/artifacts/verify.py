from fractions import Fraction
import random

def e(n, B, v):
    return Fraction(n + 1) * v / (B + v)

def wealth(W, n, B, lam, v):
    return W * (1 - lam + lam * e(n, B, v))

def endpoint(B, h, n, lam):
    den = 1 + n * lam - h
    if den <= 0:
        return None
    return B * (h - 1 + lam) / den

alphas = [Fraction(1, 20), Fraction(1, 10), Fraction(1, 4)]
for alpha in alphas:
    for n in [1, 2, 5, 9]:
        for B in [Fraction(1, 2), Fraction(3, 1), Fraction(17, 4)]:
            for h in [Fraction(6, 5), Fraction(3, 2), Fraction(5, 2), Fraction(11, 2)]:
                W = 1 / (alpha * h)
                if not (0 < W < 1 / alpha):
                    continue
                for lam in [Fraction(0), Fraction(1, 10), Fraction(1, 3), Fraction(2, 3), Fraction(1)]:
                    U = endpoint(B, h, n, lam)
                    for v in [Fraction(0), Fraction(1, 100), Fraction(1, 4), Fraction(1), Fraction(7), Fraction(100)]:
                        inside = wealth(W, n, B, lam, v) < 1 / alpha
                        predicted = True if U is None else (v < U)
                        assert inside == predicted, (alpha, n, B, h, lam, v, U)

random.seed(20261001)
for _ in range(2000):
    n = random.randint(1, 20)
    B = Fraction(random.randint(1, 100), random.randint(1, 20))
    h = Fraction(random.randint(101, 400), 100)
    l1 = Fraction(random.randint(0, 49), 50)
    l2 = Fraction(random.randint(int(l1 * 50) + 1, 50), 50)
    U1 = endpoint(B, h, n, l1)
    U2 = endpoint(B, h, n, l2)
    if U1 is not None and U2 is not None:
        assert U2 < U1

for W in [Fraction(2), Fraction(7, 3), Fraction(5)]:
    for R in [W / 4, W / 2, 3 * W / 4]:
        cap = 1 - R / W
        for n, B in [(2, Fraction(3)), (7, Fraction(11, 2))]:
            for lam in [Fraction(0), cap / 2, cap]:
                for v in [Fraction(1, 10**8), Fraction(1, 100), Fraction(1), Fraction(1000)]:
                    assert wealth(W, n, B, lam, v) >= R
            if cap < 1:
                lam = (cap + 1) / 2
                found = False
                for k in range(1, 18):
                    v = Fraction(1, 10**k)
                    if wealth(W, n, B, lam, v) < R:
                        found = True
                        break
                assert found

print("VERIFY_OK")
