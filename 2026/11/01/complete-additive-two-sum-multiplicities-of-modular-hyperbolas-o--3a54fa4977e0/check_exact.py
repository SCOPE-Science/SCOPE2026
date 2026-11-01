"""Exact checks of two-sum multiplicities on modular hyperbolas.

Only standard-library integer arithmetic is used.  The script compares the
complete multiplicity histogram, including zeros, with the theorem's strata.
"""
from collections import Counter
from math import gcd


def predicted(q, k):
    total = q ** (2 * k)
    units = (q - 1) * q ** (k - 1)
    h = Counter()
    h[units] += 1                        # s=t=0
    h[q ** (k // 2)] += units             # unit s,t, zero discriminant
    h[2] += units * (q - 3) * q ** (k - 1) // 2
    for j in range(1, (k - 1) // 2 + 1):
        h[2 * q ** j] += units * (q - 1) * q ** (k - 2 * j - 1) // 2
    for a in range(1, k):
        h[2 * q ** a] += (q - 1) ** 2 * q ** (2 * (k - a - 1)) // 2
    h[0] += total - sum(h.values())
    return +h


def check_pair_sums(q, k, units, add):
    entries = Counter()
    for x, xi in units.items():
        for y, yi in units.items():
            entries[(add(x, y), add(xi, yi))] += 1
    found = Counter(entries.values())
    found[0] += q ** (2 * k) - len(entries)
    found = +found
    assert found == predicted(q, k), (q, k, found, predicted(q, k))
    assert sum(r * count for r, count in found.items()) == len(units) ** 2
    energy = sum(r * r * count for r, count in found.items())
    expected_energy = 3 * (q - 1) * q ** (2 * k - 2) * (k * (q - 1) - 1)
    assert energy == expected_energy, (energy, expected_energy)
    return len(entries), energy


def cyclic(p, k):
    n = p ** k
    units = {x: pow(x, -1, n) for x in range(n) if gcd(x, n) == 1}
    size, energy = check_pair_sums(p, k, units, lambda x, y: (x + y) % n)
    print('CYCLIC_OK', p, k, 'sumset_size', size, 'energy', energy)


def dual_numbers(p):
    # F_p[e]/(e^2), represented as a + p*b with coefficientwise arithmetic.
    n = p * p
    def add(x, y):
        return ((x % p + y % p) % p) + p * ((x // p + y // p) % p)
    units = {}
    for a in range(1, p):
        for b in range(p):
            ai = pow(a, -1, p)
            units[a + p * b] = ai + p * ((-b * ai * ai) % p)
    size, energy = check_pair_sums(p, 2, units, add)
    print('DUAL_OK', p, 'sumset_size', size, 'energy', energy)


def f9_add(a, b):
    return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)


def f9_mul(a, b):
    # F_9 = F_3[u]/(u^2+1).
    a0, a1 = a % 3, a // 3
    b0, b1 = b % 3, b // 3
    return ((a0 * b0 - a1 * b1) % 3) + 3 * ((a0 * b1 + a1 * b0) % 3)


def f9_inv(a):
    if a == 0:
        raise ZeroDivisionError()
    a0, a1 = a % 3, a // 3
    d = pow((a0*a0 + a1*a1) % 3, -1, 3)
    return ((a0*d) % 3) + 3*((-a1*d) % 3)


def f9_dual():
    # F_9[e]/(e^2): 9^2=81 ring elements.
    def add(x, y):
        return f9_add(x % 9, y % 9) + 9 * f9_add(x // 9, y // 9)
    units = {}
    for a in range(1, 9):
        for b in range(9):
            ai = f9_inv(a)
            prod = f9_mul(f9_mul(ai, ai), b)
            minus_prod = (-prod % 3) + 3 * ((-(prod // 3)) % 3)
            units[a + 9*b] = ai + 9 * minus_prod
    size, energy = check_pair_sums(9, 2, units, add)
    print('F9_DUAL_OK', 'sumset_size', size, 'energy', energy)


if __name__ == '__main__':
    for p, k in [(3,1), (3,2), (3,3), (3,4),
                 (5,1), (5,2), (5,3), (7,2)]:
        cyclic(p, k)
    for p in [3, 5]:
        dual_numbers(p)
    f9_dual()
    print('ALL_TWO_SUM_CHECKS_OK')
