"""Exact, dependency-free checks of three-seed antagonistic adsorption probabilities."""
from fractions import Fraction
from itertools import permutations
from math import factorial, comb


def neighbors(v):
    x, y = v
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}


def boundary(seed):
    b = set(seed)
    return sorted(set().union(*(neighbors(x) for x in b)) - b)


def ordered_integral(seed):
    """Integrate independent unit-rate exponential arrival clocks by ordering seeds."""
    b = tuple(sorted(seed))
    a = boundary(b)
    result = Fraction(0)
    for order in permutations(b):
        rank = {v: i for i, v in enumerate(order)}
        counts = [0] * len(b)
        for v in a:
            counts[min(rank[u] for u in b if v in neighbors(u))] += 1
        term = Fraction(1)
        for i in range(len(b)):
            term /= len(b) - i + sum(counts[i:])
        result += term
    return result


def permutation_dp(seed):
    """Independent exact count of valid uniform arrival permutations."""
    b = tuple(sorted(seed))
    a = boundary(b)
    k = len(b)
    n = k + len(a)
    assert n <= 18
    adj = [sum(1 << i for i, u in enumerate(b) if v in neighbors(u)) for v in a]
    ways = [0] * (1 << n)
    ways[0] = 1
    for mask in range(1 << n):
        if not ways[mask]:
            continue
        seed_seen = mask & ((1 << k) - 1)
        available = ((1 << n) - 1) ^ mask
        while available:
            bit = available & -available
            available -= bit
            j = bit.bit_length() - 1
            if j < k or seed_seen & adj[j - k]:
                ways[mask | bit] += ways[mask]
    return Fraction(ways[-1], factorial(n))


def tests():
    checked = 0
    def test(condition):
        nonlocal checked
        assert condition
        checked += 1
    line = ((0, 0), (1, 0), (2, 0))
    bend = ((0, 0), (1, 0), (0, 1))
    for shape, expected, bound in ((line, Fraction(1, 48), 8),
                                    (bend, Fraction(2, 63), 7)):
        test(len(boundary(shape)) == bound)
        test(ordered_integral(shape) == expected)
        test(permutation_dp(shape) == expected)
        for tx in range(-1, 2):
            for ty in range(-1, 2):
                for rot in range(4):
                    placed = []
                    for x, y in shape:
                        for _ in range(rot):
                            x, y = -y, x
                        placed.append((x + tx, y + ty))
                    test(ordered_integral(placed) == expected)
                    test(permutation_dp(placed) == expected)
    pair = ((0, 0), (1, 0))
    test(ordered_integral(pair) == Fraction(1, 16))
    test(permutation_dp(pair) == Fraction(1, 16))
    test(Fraction(2, 63) / Fraction(1, 48) == Fraction(32, 21))
    test(Fraction(4 * 2, 63) / (Fraction(2, 48) + Fraction(4 * 2, 63)) == Fraction(64, 85))
    test(Fraction(64, 85) - Fraction(2, 3) == Fraction(22, 255))
    for l in (7, 8, 13, 17):
        n = l * l
        straight_count = 2 * n
        bent_count = 4 * n
        test(straight_count + bent_count == 6 * n)
        joint = (straight_count * Fraction(1, 48) + bent_count * Fraction(2, 63)) / comb(n, 3)
        test(joint == Fraction(85 * n, 504 * comb(n, 3)))
    # Different shapes supply an independent check of the general finite-boundary formula.
    shapes = [((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (3, 0)),
              ((0, 0), (1, 0), (2, 1)), ((0, 0), (1, 0), (2, 2)),
              ((0, 0), (1, 0), (0, 3)), ((0, 0), (1, 1), (2, 0)),
              ((0, 0), (1, 0), (0, 2)), ((0, 0), (1, 1), (1, -1))]
    for shape in shapes:
        test(ordered_integral(shape) == permutation_dp(shape))
    print(f"PASS: {checked} exact assertions; straight=1/48, bent=2/63, selected-bend=64/85")


if __name__ == '__main__':
    tests()
