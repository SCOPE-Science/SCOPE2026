from itertools import product
from collections import Counter


def add(a, b, sign=1):
    m = max(len(a), len(b))
    out = [0] * m
    for i in range(m):
        out[i] = (a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def ppow(a, k):
    out = [1]
    for _ in range(k):
        out = mul(out, a)
    return out


def formula(r, n):
    A = [1, 1, 1, 1]
    B = [1, 1]
    C1 = [0, 1, 1, 1]
    D = [0, 0, 1, 1]

    Ar = ppow(A, r)
    An = ppow(A, n)
    Br = ppow(B, r)
    Br1 = ppow(B, r - 1)

    rx2Br1 = [0, 0] + [r * c for c in Br1]
    case1 = mul(add(add(Ar, Br, -1), rx2Br1, -1), An)

    Cn = ppow(C1, n)
    first = mul(Br1, Cn)
    xr1 = [0] * r
    xr1[r - 1] = 1
    diff = add(Br1, xr1, -1)
    xn = [0] * n + [1]
    second = mul(diff, xn)
    core = add(first, second, -1)
    case2 = [0, 0] + [r * c for c in core]

    case3 = mul(Br, ppow(D, n))
    return add(add(case1, case2), case3)


def is_drdf(labels, r, n):
    N = r + n
    for v, value in enumerate(labels):
        if v < r:
            neighbors = [u for u in range(N) if u != v]
        else:
            neighbors = list(range(r))
        if value == 0:
            threes = sum(labels[u] == 3 for u in neighbors)
            twos = sum(labels[u] == 2 for u in neighbors)
            if threes < 1 and twos < 2:
                return False
        elif value == 1:
            if not any(labels[u] >= 2 for u in neighbors):
                return False
    return True


def brute(r, n):
    counts = Counter()
    for labels in product(range(4), repeat=r + n):
        if is_drdf(labels, r, n):
            counts[sum(labels)] += 1
    return counts


assignments = 0
coefficient_checks = 0
minimum_checks = 0
total_checks = 0
for r in range(2, 5):
    for n in range(2, 5):
        assignments += 4 ** (r + n)
        got = brute(r, n)
        poly = formula(r, n)
        expected = {i: c for i, c in enumerate(poly) if c}
        assert got == expected, (r, n, got, expected)
        coefficient_checks += len(poly)
        assert min(got) == 3
        assert got[3] == r
        minimum_checks += 1
        total_formula = ((4 ** r - 2 ** r - r * 2 ** (r - 1)) * 4 ** n
                         + r * (2 ** (r - 1) * 3 ** n - (2 ** (r - 1) - 1))
                         + 2 ** (r + n))
        assert sum(got.values()) == total_formula
        total_checks += 1

print(f"VERIFY_OK r_range=2..4 n_range=2..4 assignments={assignments} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} total_checks={total_checks} max_order=8")
