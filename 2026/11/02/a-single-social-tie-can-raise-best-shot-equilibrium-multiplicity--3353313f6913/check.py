"""Independent, exact-enumeration checks for the chorded-ring best-shot game."""
from __future__ import annotations


def sequences(limit: int):
    c = [1, 0, 1]
    p = [3, 0, 2]
    for k in range(3, limit + 1):
        c.append(c[k - 2] + c[k - 3])
        p.append(p[k - 2] + p[k - 3])
    return c, p


def enumerated_equilibria(n: int, d: int) -> int:
    adjacent = [(1 << ((v - 1) % n)) | (1 << ((v + 1) % n))
                for v in range(n)]
    adjacent[0] |= 1 << d
    adjacent[d] |= 1
    total = 0
    for profile in range(1 << n):
        valid = True
        for v in range(n):
            selected = (profile >> v) & 1
            neighbors_selected = (profile & adjacent[v]) != 0
            if (selected and neighbors_selected) or (not selected and not neighbors_selected):
                valid = False
                break
        total += int(valid)
    return total


def formula(n: int, d: int, c, p) -> int:
    return p[n] - c[d] * c[n - d] + 2 * c[d - 2] * c[n - d - 2]


def main():
    c, p = sequences(1300)
    checks = 0
    for n in range(5, 18):
        vals = {}
        for d in range(2, n - 1):
            observed = enumerated_equilibria(n, d)
            expected = formula(n, d, c, p)
            assert observed == expected, (n, d, observed, expected)
            checks += 1
            vals[d] = observed
        assert min(vals.values()) == p[n] - c[n - 3], n
        checks += 1
        assert set(d for d, value in vals.items() if value == min(vals.values())) == {3, n - 3}, n
        checks += 1
    for n in range(6, 1301):
        assert formula(n, 2, c, p) - p[n] == c[n - 4] - c[n - 5], n
        assert (formula(n, 2, c, p) >= p[n]), n
        checks += 2
    for d in range(2, 100):
        for m in range(2, 100):
            n = d + m
            D = c[n - 3] - c[d] * c[m] + 2 * c[d - 2] * c[m - 2]
            assert (D == 0) == (d == 3 or m == 3), (d, m, D)
            checks += 1
    for d in range(2, 97):
        for m in range(5, 100):
            def D(z):
                return c[d+z-3] - c[d]*c[z] + 2*c[d-2]*c[z-2]
            assert D(m) == D(m-2) + D(m-3), (d, m)
            checks += 1
    for n in (100, 300, 800, 1200):
        a = 1.324717957244746
        expected = 1 - 1 / (2 * a + 3)
        ratio = 1 - c[n-3] / p[n]
        assert abs(ratio - expected) < 1e-12, (n, ratio)
        checks += 1
    print(f'VERIFY_OK assertions={checks}; exhaustive n=5..17; induction identity d=2..96,m=5..99')


if __name__ == '__main__':
    main()
