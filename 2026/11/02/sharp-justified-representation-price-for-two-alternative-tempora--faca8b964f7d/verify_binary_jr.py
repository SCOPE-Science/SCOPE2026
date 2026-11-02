"""Exact-arithmetic finite checks for temporal two-alternative JR price.
Usage: python verify_binary_jr.py
"""
from itertools import product
from fractions import Fraction


def solve(profile, n, horizon):
    options = []
    for t in range(horizon):
        a = sum(1 << i for i in range(n) if profile[i * horizon + t] & 1)
        b = sum(1 << i for i in range(n) if profile[i * horizon + t] & 2)
        options.append((a, b))
    optimum = sum(max(a.bit_count(), b.bit_count()) for a, b in options)
    fair = 0
    all_voters = (1 << n) - 1
    for selections in product((0, 1), repeat=horizon):
        sat, welfare = 0, 0
        for t, x in enumerate(selections):
            supported = options[t][x]
            sat |= supported
            welfare += supported.bit_count()
        if sat == all_voters and welfare > fair:
            fair = welfare
    assert fair > 0
    return optimum, fair


def run_exhaustive(n, horizon):
    total = equality = 0
    bound = Fraction(horizon * (n - 1), horizon * (n - 1) - (n - 2))
    for profile in product((1, 2, 3), repeat=n * horizon):
        optimum, fair = solve(profile, n, horizon)
        assert Fraction(optimum, fair) <= bound
        if Fraction(optimum, fair) == bound and n > 2:
            equality += 1
            minority = [i for i in range(n)
                        if all(profile[i * horizon + t] != profile[j * horizon + t]
                               for t in range(horizon)
                               for j in range(n) if j != i)]
            # Every ballot is exclusive, one fixed minority, other voters agree each round.
            polarized = any(all(profile[i * horizon + t] in (1, 2)
                                and profile[i * horizon + t] != profile[j * horizon + t]
                                and all(profile[j * horizon + t] == profile[k * horizon + t]
                                        for k in range(n) if k != i)
                                for t in range(horizon)
                                for j in range(n) if j != i)
                            for i in range(n))
            assert polarized, (n, horizon, profile)
        total += 1
    expected_equal = n * 2**horizon if n > 2 else None
    if expected_equal is not None:
        assert equality == expected_equal, (equality, expected_equal)
    print(f'CHECK_OK n={n} horizon={horizon} profiles={total} equality={equality} sharp={bound}')


def run_sample(n, horizon, count=1000):
    state = 0xB631F
    bound = Fraction(horizon * (n - 1), horizon * (n - 1) - (n - 2))
    for _ in range(count):
        profile = []
        for j in range(n * horizon):
            state = (1103515245 * state + 12345) & 0x7fffffff
            profile.append(1 + (state % 3))
        optimum, fair = solve(profile, n, horizon)
        assert Fraction(optimum, fair) <= bound
    print(f'CHECK_OK n={n} horizon={horizon} deterministic_samples={count} sharp={bound}')


if __name__ == '__main__':
    run_exhaustive(3, 3)
    run_exhaustive(3, 4)
    run_sample(4, 4)
