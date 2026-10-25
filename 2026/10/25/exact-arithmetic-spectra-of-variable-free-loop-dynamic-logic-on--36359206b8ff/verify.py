"""Finite checks for cycle-spectrum arithmetic identities (stdlib only)."""
from itertools import product
from math import gcd


def semigroup_modulo(n, gens):
    reached = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for v in gens:
            y = (x + v) % n
            if y not in reached:
                reached.add(y)
                frontier.append(y)
    return reached


def loop_star_shift(n, d, b):
    """Whether some length b + t*d (t nonnegative) closes on the n-cycle."""
    residue = b % n
    seen = set()
    while residue not in seen:
        if residue == 0:
            return True
        seen.add(residue)
        residue = (residue + d) % n
    return False


def exact_cycle(n, target):
    return target % n == 0 and all(j % n for j in range(1, target))


def divides_prime_power(n, prime, e):
    d = prime ** e
    shift = prime ** (e - 1)
    return not loop_star_shift(n, d, shift)


def verify():
    subgroup_cases = 0
    for n in range(1, 19):
        for b in range(-8, 9):
            for gens in [()] + [(x,) for x in range(-4, 5)] + list(product(range(-3, 4), repeat=2)):
                g = gcd(n, *gens)
                got = ((-b) % n) in semigroup_modulo(n, gens)
                expected = (b % g == 0)
                assert got == expected, (n, b, gens, got, expected)
                subgroup_cases += 1
    powers = 0
    for n in range(1, 101):
        for p in (2, 3, 5, 7):
            for exponent in range(1, 5):
                assert divides_prime_power(n, p, exponent) == (n % (p ** exponent) == 0)
                powers += 1
    sizes = 0
    for n in range(1, 101):
        for m in range(1, 50):
            assert exact_cycle(n, m) == (n == m)
            sizes += 1
    # Sample semilinear components with negative/zero generators.
    semilinear_cases = 0
    for n in range(1, 25):
        for b in range(-5, 6):
            for generators in ((0, 0), (2, -3), (0, 4), (-3, -6), (4, 6), (1, 1)):
                reachable = semigroup_modulo(n, generators)
                expected = (b % gcd(n, *generators) == 0)
                assert ((-b) % n in reachable) == expected
                semilinear_cases += 1
    print('CYCLE_SPECTRA_ARITHMETIC_OK', subgroup_cases, powers, sizes, semilinear_cases)


if __name__ == '__main__':
    verify()
