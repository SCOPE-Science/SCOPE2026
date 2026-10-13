"""Independent exact-arithmetic checks for complete-bipartite graph-state fidelity.

Only the Python standard library is required.  This finite checker corroborates,
but does not replace, the all-size inequalities proved in RESULT.md.
"""
from fractions import Fraction


def exact_formula(a, b, r):
    t, u = (1 + r) / 2, (1 - r) / 2
    ea, eb = t**a + u**a, t**b + u**b
    oa, ob = t**a - u**a, t**b - u**b
    return (ea * eb + r**b * oa + r**a * ob + r**(a+b)) / 4


def explicit_stabilizer_sum(a, b, r):
    n = a + b
    neighbors = []
    low = (1 << a) - 1
    high = ((1 << b) - 1) << a
    for vertex in range(n):
        neighbors.append(high if vertex < a else low)
    total = Fraction(0)
    for generators in range(1 << n):
        z_support = 0
        selected = generators
        while selected:
            single = selected & -selected
            z_support ^= neighbors[single.bit_length() - 1]
            selected ^= single
        total += r ** ((generators | z_support).bit_count())
    return total / (1 << n)


def main():
    checks = 0
    for n in range(2, 12):
        for a in range(1, n):
            b = n - a
            for r in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                      Fraction(3, 4), Fraction(1)]:
                left = exact_formula(a, b, r)
                right = explicit_stabilizer_sum(a, b, r)
                assert left == right, (n, a, r, left, right)
                checks += 1
    for n in range(4, 60):
        for r in [Fraction(1, 11), Fraction(1, 3),
                  Fraction(1, 2), Fraction(9, 10)]:
            f = [exact_formula(a, n - a, r)
                 for a in range(1, n // 2 + 1)]
            assert all(f[i] > f[i+1] for i in range(len(f)-1))
            checks += len(f) - 1
    # A known local-Clifford special case: K_{1,n-1} = GHZ star.
    for n in range(2, 30):
        for r in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            t, u = (1+r)/2, (1-r)/2
            assert exact_formula(1, n-1, r) == (t**n + u**n + r**n)/2
            checks += 1
    # The finite-n ratio approaches two for every interior noise parameter.
    for r in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
        n = 240
        ratio = exact_formula(1, n-1, r) / exact_formula(n//2, n//2, r)
        assert abs(ratio - 2) < Fraction(1, 1000000), (r, ratio)
        checks += 1
    # An exact illustrative strict contrast.
    r = Fraction(1, 2)
    assert exact_formula(1, 3, r) == Fraction(49, 256)
    assert exact_formula(2, 2, r) == Fraction(45, 256)
    checks += 2
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    main()
