from math import isqrt


def dual_degree(d, e):
    return d * e * (d + e - 2)


def pell_solutions(count):
    x, u = 1, 0
    out = []
    for k in range(1, count + 1):
        x, u = 5 * x + 24 * u, x + 5 * u
        m = 3 * u
        n = (x - 1) // 2
        assert x * x - 24 * u * u == 1
        assert x % 2 == 1
        assert dual_degree(2, m) == dual_degree(3, n)
        out.append((k, x, u, m, n, dual_degree(2, m)))
    return out


solutions = pell_solutions(12)
assert solutions[:4] == [
    (1, 5, 1, 3, 2, 18),
    (2, 49, 10, 30, 24, 1800),
    (3, 485, 99, 297, 242, 176418),
    (4, 4801, 980, 2940, 2400, 17287200),
]

for a, b, c in zip(solutions, solutions[1:], solutions[2:]):
    assert c[3] == 10 * b[3] - a[3]
    assert c[4] == 10 * b[4] - a[4] + 4

bound = 5000
brute = []
for m in range(2, bound + 1):
    D = 2 * m * m
    if D % 3:
        continue
    disc = 1 + 4 * (D // 3)
    s = isqrt(disc)
    if s * s != disc or (s - 1) % 2:
        continue
    n = (s - 1) // 2
    if 2 <= n <= bound and dual_degree(3, n) == D:
        brute.append((m, n))

pell_in_box = [(m, n) for _, _, _, m, n, _ in solutions if m <= bound and n <= bound]
assert brute == pell_in_box
print('VERIFY_OK', len(brute), 'collisions through', bound, brute)
