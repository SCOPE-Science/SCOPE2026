import math
import sympy as sp

x = sp.symbols("x")


def cartan(n):
    C = sp.zeros(n)
    for i in range(n):
        for j in range(i, min(n, i + 3)):
            C[i, j] = 1
    return C


def coxeter(n):
    C = cartan(n)
    return -C.inv() * C.T


def odd_formula(n):
    if n % 6 == 1:
        return sp.cancel((1 + x) * (1 + x ** (n + 2)) / (1 + x**3))
    if n % 6 in (3, 5):
        m = (n - (3 if n % 6 == 3 else 5)) // 6
        a = (n + 1) // 2
        b = (n + 3) // 2
        eps = -1 if m % 2 else 1
        return sp.cancel((1 + x) * (1 + eps * x**a) * (1 + eps * x**b) / (1 + x**3))
    raise ValueError("n must be odd")


def predicted_period(n):
    if n % 2 == 0:
        return math.lcm(2, 3, n // 2 + 1)
    if n % 12 in (9, 11):
        return None
    if n == 3:
        return 4
    if n == 5:
        return 8
    if n % 12 in (1, 7):
        return 2 * (n + 2)
    return math.lcm(n + 1, n + 3)


for n in range(1, 40, 2):
    p = coxeter(n).charpoly(x).as_expr()
    assert sp.expand(p - odd_formula(n)) == 0

for n in range(3, 30):
    M = coxeter(n)
    q = predicted_period(n)
    if q is None:
        p = sp.Poly(M.charpoly(x).as_expr(), x)
        assert p.eval(1) == 0
        assert p.diff().eval(1) == 0
        assert p.diff().diff().eval(1) != 0
        assert n - (M - sp.eye(n)).rank() == 1
    else:
        assert M**q == sp.eye(n)
        for d in sp.divisors(q):
            if d < q:
                assert M**d != sp.eye(n)

print("verification passed")
