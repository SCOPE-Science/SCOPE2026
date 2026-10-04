from fractions import Fraction
from itertools import product

def run_path(mu, h, alpha, x0, signs):
    eta = alpha / mu
    v = mu * x0
    x_prev = x0
    x = x0 - eta * v
    vs = [v]
    xs = [x0, x]
    for sig in signs:
        a = mu * (1 + sig*h)
        v = a * (x - x_prev) + v
        x_next = x - eta * v
        x_prev, x = x, x_next
        vs.append(v)
        xs.append(x)
    return xs, vs

mu = Fraction(7, 3)
h = Fraction(1, 2)
alpha = Fraction(4, 5)
x0 = Fraction(11, 7)

for n in range(1, 7):
    for signs in product((-1, 1), repeat=n):
        xs, vs = run_path(mu, h, alpha, x0, signs)
        p = Fraction(1)
        for j, sig in enumerate(signs, start=1):
            p *= 1 - alpha*(1 + sig*h)
            assert vs[j] == mu*x0*p

for n in range(1, 7):
    total = Fraction(0)
    for signs in product((-1, 1), repeat=n):
        _, vs = run_path(mu, h, alpha, x0, signs)
        total += vs[n] * vs[n]
    total /= 2**n
    q = (1-alpha)**2 + (alpha*h)**2
    assert total == (mu*x0)**2 * q**n

r = 1-alpha
q = (1-alpha)**2 + (alpha*h)**2
m = Fraction(1)
Q = Fraction(1)
for n in range(1, 8):
    Q_new = 1 + 2*r*m + q*Q
    m_new = 1 + r*m
    es2 = Fraction(0)
    for signs in product((-1, 1), repeat=n):
        p = Fraction(1)
        S = Fraction(1)
        for sig in signs:
            p *= 1-alpha*(1+sig*h)
            S += p
        es2 += S*S
    es2 /= 2**n
    assert es2 == Q_new
    m, Q = m_new, Q_new

mu = Fraction(1)
h = Fraction(1, 2)
alpha = Fraction(1)
x0 = Fraction(1)
for n in range(1, 7):
    vals = []
    for signs in product((-1, 1), repeat=n):
        xs, vs = run_path(mu, h, alpha, x0, signs)
        vals.append(xs[-1])
        assert abs(vs[-1]) == Fraction(1, 2**n)
    vals = sorted(vals)
    assert len(set(vals)) == 2**n
    spacing = Fraction(1, 2**(n-1))
    for a, b in zip(vals, vals[1:]):
        assert b-a == spacing
    assert vals[0] == -1 + Fraction(1, 2**n)
    assert vals[-1] == 1 - Fraction(1, 2**n)

def mse_factor(alpha, h):
    return alpha*h*h / (2-alpha*(1+h*h))

assert mse_factor(Fraction(1), Fraction(1,2)) == Fraction(1,3)
for hh in (Fraction(1,5), Fraction(1,2), Fraction(4,5)):
    cap = Fraction(2, 1) / (1 + hh*hh)
    for aa in (cap/Fraction(10), cap/Fraction(2), cap*Fraction(9,10)):
        assert mse_factor(aa, hh) > 0

print("verification passed")
