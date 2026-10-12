from fractions import Fraction
import numpy as np

rng = np.random.default_rng(350055)

def direct_mime(Hs, qs, x, eta, K):
    c = sum(H @ x - q for H, q in zip(Hs, qs)) / len(Hs)
    ys = []
    for H, q in zip(Hs, qs):
        y = x.copy()
        gx = H @ x - q
        for _ in range(K):
            gy = H @ y - q
            g = gy - gx + c
            y = y - eta * g
        ys.append(y)
    return sum(ys) / len(ys), c

def central(Hbar, qbar, x, eta, K):
    z = x.copy()
    for _ in range(K):
        z = z - eta * (Hbar @ z - qbar)
    return z

for n in (2, 3, 5):
    for m in (2, 3, 6):
        for _ in range(20):
            Hs = []
            qs = []
            for _j in range(m):
                A = rng.normal(size=(n, n))
                H = A.T @ A + 0.25 * np.eye(n)
                Hs.append(H)
                qs.append(rng.normal(size=n))
            x = rng.normal(size=n)
            eta = 0.01 + 0.03 * rng.random()
            Hbar = sum(Hs) / m
            qbar = sum(qs) / m

            y1, c = direct_mime(Hs, qs, x, eta, 1)
            y2, _ = direct_mime(Hs, qs, x, eta, 2)
            y3, _ = direct_mime(Hs, qs, x, eta, 3)
            z1 = central(Hbar, qbar, x, eta, 1)
            z2 = central(Hbar, qbar, x, eta, 2)
            z3 = central(Hbar, qbar, x, eta, 3)

            assert np.linalg.norm(y1-z1) < 2e-12
            assert np.linalg.norm(y2-z2) < 2e-12

            V1 = sum((H-Hbar) @ (H-Hbar) for H in Hs) / m
            V2 = sum(H @ H for H in Hs) / m - Hbar @ Hbar
            assert np.linalg.norm(V1-V2) < 2e-11

            defect = -eta**3 * (V1 @ c)
            assert np.linalg.norm((y3-z3)-defect) < 5e-11

            lhs = float(c @ (y3-z3))
            rhs = -eta**3 * sum(np.linalg.norm((H-Hbar) @ c)**2 for H in Hs) / m
            assert abs(lhs-rhs) < 5e-11
            assert lhs <= 5e-11

h1 = Fraction(1, 1)
h2 = Fraction(3, 1)
eta = Fraction(1, 10)
x = Fraction(1, 1)
c = Fraction(h1+h2, 2) * x

def local_three(h):
    y = x
    for _ in range(3):
        g = h*(y-x) + c
        y -= eta*g
    return y

mime3 = (local_three(h1) + local_three(h2)) / 2
hbar = (h1+h2)/2
z = x
for _ in range(3):
    z -= eta*hbar*z

V = ((h1-hbar)**2 + (h2-hbar)**2)/2
assert z == Fraction(64, 125)
assert mime3 == Fraction(51, 100)
assert mime3-z == Fraction(-1, 500)
assert -eta**3 * V * c == Fraction(-1, 500)

print("verification passed")
