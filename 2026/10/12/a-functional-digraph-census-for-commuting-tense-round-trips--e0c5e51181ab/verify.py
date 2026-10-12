"""Independent finite checks of deterministic tense round-trip commutation.

Run with Python 3 using only the standard library. Infinite-set and asymptotic
claims require the mathematical proof in RESULT.md and are not certified by
finite enumeration.
"""
from fractions import Fraction
from itertools import product
from math import factorial

EXPECTED = [1, 1, 2, 12, 108, 1100, 13350, 194502, 3280424,
            62480952, 1328405130]


def direct_image(f, a):
    return {f[x] for x in a}


def inverse_image(f, a):
    return {x for x in range(len(f)) if f[x] in a}


def is_saturated(f):
    image = set(f)
    return inverse_image(f, direct_image(f, image)) == image


def direct_commutation(f):
    n = len(f)
    image = set(f)
    for bits in range(1 << n):
        a = {i for i in range(n) if bits >> i & 1}
        c = lambda b: inverse_image(f, direct_image(f, b))
        interior = lambda b: b & image
        if c(interior(a)) != interior(c(a)):
            return False
    return True


def exp_series(u, size):
    e = [Fraction(0) for _ in range(size + 1)]
    e[0] = 1
    for n in range(1, size + 1):
        e[n] = sum(k * u[k] * e[n-k] for k in range(1, n+1)) / n
    return e


def counts_egf(size):
    u = [Fraction(0) for _ in range(size + 1)]
    eu = [Fraction(0) for _ in range(size + 1)]
    eu[0] = 1
    for n in range(1, size + 1):
        # u=z(exp(z)+exp(u)-2), solved coefficient-by-coefficient.
        if n >= 2:
            u[n] = Fraction(1, factorial(n-1)) + eu[n-1]
        eu[n] = sum(k * u[k] * eu[n-k] for k in range(1, n+1)) / n
    cycle_node = [Fraction(0)] + eu[:size]
    a = [Fraction(0) for _ in range(size+1)]
    a[0] = 1
    for n in range(1, size + 1):
        a[n] = sum(cycle_node[k] * a[n-k] for k in range(1, n+1))
    values = [x * factorial(i) for i, x in enumerate(a)]
    assert all(x.denominator == 1 for x in values)
    return [int(x) for x in values]


def main():
    values = counts_egf(10)
    assert values == EXPECTED, values
    print('EGF coefficients n=0..10:', values)
    for n in range(1, 7):
        passed = 0
        for f in product(range(n), repeat=n):
            cond = is_saturated(f)
            image = set(f)
            siblings = all((i in image) == (j in image)
                           for i in range(n) for j in range(n)
                           if f[i] == f[j])
            assert cond == siblings, (n, f, 'siblings mismatch')
            # Every Boolean valuation checked for all maps through n=5.
            if n <= 5:
                assert direct_commutation(f) == cond, (n, f, 'modal mismatch')
            passed += bool(cond)
        assert passed == values[n], (n, passed, values[n])
        print('size', n, 'all_maps', n**n, 'accepted', passed,
              'all_event_checks', n <= 5)
    # Explicit three-point nonbijective positive and two-point obstruction.
    assert is_saturated((0, 0, 1))
    assert not is_saturated((0, 0))
    assert direct_commutation((0, 0, 1))
    assert not direct_commutation((0, 0))
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
