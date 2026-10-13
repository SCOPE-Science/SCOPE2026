from math import gcd


def chi_V(n, typ, j):
    if typ == "r":
        return n if j % n == 0 else 0
    return sum(1 for i in range(n) if (2 * i - j) % n == 0)


def preserves_character(n, a, b):
    for j in range(n):
        if chi_V(n, "r", j) != chi_V(n, "r", (a * j) % n):
            return False
        if chi_V(n, "f", j) != chi_V(n, "f", (a * j + b) % n):
            return False
    return True


def solve_c(n, b):
    return next((c for c in range(n) if (2 * c - b) % n == 0), None)


def p(n, a, c, i):
    return (a * i + c) % n


def pinv(n, a, c, j):
    return (pow(a, -1, n) * (j - c)) % n


def r(n, i):
    return (i + 1) % n


def f(n, i):
    return (-i) % n


def rpow(n, k, i):
    return (i + k) % n


def rb_f(n, b, i):
    return (b - i) % n


for n in range(3, 25):
    units = [a for a in range(n) if gcd(a, n) == 1]
    allowed = []
    for a in units:
        for b in range(n):
            got = preserves_character(n, a, b)
            predicted = (n % 2 == 1) or (b % 2 == 0)
            assert got == predicted, (n, a, b, got, predicted)
            if got:
                allowed.append((a, b))
                c = solve_c(n, b)
                assert c is not None
                for i in range(n):
                    lhs = p(n, a, c, r(n, pinv(n, a, c, i)))
                    assert lhs == rpow(n, a, i)
                    lhs = p(n, a, c, f(n, pinv(n, a, c, i)))
                    assert lhs == rb_f(n, b, i)
    predicted_count = n * len(units) if n % 2 else (n // 2) * len(units)
    assert len(allowed) == predicted_count

assert chi_V(4, "f", 0) == 2
assert chi_V(4, "f", 1) == 0
print("VERIFY_OK")
