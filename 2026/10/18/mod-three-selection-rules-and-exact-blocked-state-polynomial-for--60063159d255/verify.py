#!/usr/bin/env python3
"""Independent finite-ring checks for a three-body classical Ising chain."""
from collections import Counter


def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def power(A, n):
    R = [[int(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n & 1:
            R = multiply(R, A)
        A = multiply(A, A)
        n //= 2
    return R


def tr(A):
    return sum(A[i][i] for i in range(3))


def T(z):
    return [[0, 1, 0], [0, 0, 1], [z, 0, 1]]


def predicted(n, z):
    base = tr(power(T(z), n))
    if n % 3:
        return base
    Q = multiply(multiply(T(-z), T(-z)), T(z))
    return base + 3 * tr(power(Q, n // 3))


def energy_bits(bits, n):
    # J is set to one; the actual Hamiltonian, not a local-field shortcut.
    spins = [1 if bits & (1 << i) else -1 for i in range(n)]
    return -sum(spins[i] * spins[(i + 1) % n] * spins[(i + 2) % n]
                for i in range(n))


def brute(n):
    accepted = Counter()
    energies = Counter()
    checked = 0
    for bits in range(1 << n):
        E = energy_bits(bits, n)
        defects = (E + n) // 2
        assert E + n == 2 * defects
        energies[defects] += 1
        strict = all(energy_bits(bits ^ (1 << i), n) > E for i in range(n))
        if strict:
            accepted[defects] += 1
        checked += 1
    return accepted, energies, checked


def all_energy_poly(n, z):
    if n % 3:
        return (1 + z) ** n
    m = n // 3
    return (1 + z) ** n + 3 * (1 + z) ** m * (1 - z) ** (2 * m)


def run():
    tested = 0
    evaluations = 0
    for n in range(3, 16):
        a, e, c = brute(n)
        tested += c
        assert a[0] == (4 if n % 3 == 0 else 1)
        if n % 3:
            assert a[1] == n
        else:
            assert a[1] == 0
        if n >= 6 and n % 3 == 0:
            assert a[2] == 2 * n * (n // 3 - 1)
        for z in range(-2, n // 3 + 2):
            x = sum(v * z ** k for k, v in a.items())
            y = predicted(n, z)
            assert x == y, (n, z, x, y)
            x_all = sum(v * z ** k for k, v in e.items())
            assert x_all == all_energy_poly(n, z), (n, z, x_all)
            evaluations += 2
    # Unbounded-size exact integer identities for sample larger N with
    # independent cyclic-defect enumeration via combinations of positions.
    import itertools
    for n in range(16, 25):
        arr = Counter()
        for k in range(0, n // 3 + 1):
            for ds in itertools.combinations(range(n), k):
                if k >= 2 and any((ds[(j + 1) % k] - ds[j]) % n < 3 for j in range(k)):
                    continue
                if n % 3:
                    arr[k] += 1
                else:
                    ps = [sum(p % 3 == r for p in ds) % 2 for r in range(3)]
                    if ps[0] == ps[1] == ps[2]:
                        arr[k] += 4
        for z in (0, 1, 2):
            assert sum(v * z ** k for k, v in arr.items()) == predicted(n, z), n
            evaluations += 1
    print("PASS: exhaustive spin configurations:", tested)
    print("PASS: integer polynomial evaluations:", evaluations)
    print("PASS: finite rings N=3..24, independent spin/defect checks")
    print("N=3,6,9,12,15 blocked totals:", [predicted(n, 1) for n in (3, 6, 9, 12, 15)])


if __name__ == '__main__':
    run()
