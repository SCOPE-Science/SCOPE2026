"""Exact finite checks for the dyadic distribution of two odd powers."""
from collections import Counter
from fractions import Fraction


def direct(d, n):
    m = 1 << n
    cubes = Counter(pow(x, d, m) for x in range(m))
    counts = [0] * m
    for a, ca in cubes.items():
        for b, cb in cubes.items():
            counts[(a + b) % m] += ca * cb
    assert sum(counts) == m * m
    return counts


def predicted(d, n, memory):
    if n == 0:
        return [1]
    modulus = 1 << n
    if n < d:
        return [((modulus if a % 2 else modulus // 2) +
                 ((modulus // 2)**2 if a == 0 else 0))
                for a in range(modulus)]
    prior = memory[n - d]
    return [(modulus if a % 2 else modulus // 2) +
            ((1 << (2 * d - 2)) * prior[a >> d] if not (a % (1 << d)) else 0)
            for a in range(modulus)]


def moment(d, n, moments):
    if n == 0:
        return Fraction(1)
    if n < d:
        return Fraction(7, 8) + Fraction(2)**(n-4)
    return Fraction(7, 8) + Fraction(2)**(d-4) * moments[n-d]


def main():
    checks = 0
    for d, N in ((3, 10), (5, 9), (7, 9), (9, 8)):
        memory = {0: [1]}
        moments = {0: Fraction(1)}
        for n in range(1, N+1):
            actual = direct(d, n)
            expected = predicted(d, n, memory)
            assert actual == expected, (d, n)
            M = Fraction(sum(t*t for t in actual), (1 << n)**3)
            assert M == moment(d, n, moments), (d, n, M)
            memory[n], moments[n] = expected, M
            checks += 1 << n
        if d == 3:
            for n in range(1, N+1):
                assert moments[n] < Fraction(7, 4)
    print('VERIFIED', checks, 'exact target counts across 36 cases')

if __name__ == '__main__':
    main()
