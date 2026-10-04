from fractions import Fraction as F


def soft(x, t):
    if x > t:
        return x - t
    if x < -t:
        return x + t
    return F(0)


def step(b, lam, rho, z, u):
    x = (b + rho * (z - u)) / (1 + rho)
    zn = soft(x + u, lam / rho)
    un = u + x - zn
    return x, zn, un


def first_active_by_iteration(b, lam, rho, cap=200):
    z = u = F(0)
    for k in range(1, cap + 1):
        _, z, u = step(b, lam, rho, z, u)
        if z > 0:
            return k, z, u
    raise AssertionError("activation cap too small")


def first_active_by_exact_inequality(b, lam, rho, cap=200):
    q = F(1, 1) / (1 + rho)
    target = (b - lam) / b
    p = F(1)
    for j in range(1, cap + 1):
        p *= q
        if p < target:
            return j
    raise AssertionError("inequality cap too small")


def check_case(b, lam, rho):
    assert b > lam > 0 and rho > 0
    j1, zj, uj = first_active_by_iteration(b, lam, rho)
    j2 = first_active_by_exact_inequality(b, lam, rho)
    assert j1 == j2
    assert uj == lam / rho
    target = b - lam
    assert F(0) < zj < target

    z, u = zj, uj
    factor = rho / (1 + rho)
    initial_error = z - target
    for n in range(1, 13):
        _, z, u = step(b, lam, rho, z, u)
        assert u == lam / rho
        assert z - target == factor ** n * initial_error
        assert z != target


cases = [
    (F(2), F(1), F(1)),
    (F(3), F(1), F(1, 2)),
    (F(5), F(2), F(3)),
    (F(7), F(3), F(1, 4)),
    (F(11), F(4), F(10)),
]
for case in cases:
    check_case(*case)

# Exact threshold-equality witness.
b, lam, rho = F(2), F(1), F(1)
z = u = F(0)
_, z1, u1 = step(b, lam, rho, z, u)
assert z1 == 0 and u1 == 1
_, z2, u2 = step(b, lam, rho, z1, u1)
assert z2 == F(1, 2) and u2 == 1
z, u = z2, u2
for n in range(0, 12):
    if n:
        _, z, u = step(b, lam, rho, z, u)
    assert z == 1 - F(1, 2 ** (n + 1))

print("VERIFY_OK")
