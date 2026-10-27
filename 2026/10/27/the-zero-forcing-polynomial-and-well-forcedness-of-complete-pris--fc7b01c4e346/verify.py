"""Exhaustive small-order check for the zero-forcing polynomial of clique prisms.

Run with Python 3.9 or later; uses only the standard library.
"""
from collections import Counter
from math import comb


def force(n, initial_blue):
    """Directly apply the standard open-neighborhood color-change rule."""
    order = 2 * n
    full = (1 << order) - 1
    neighborhoods = []
    for vertex in range(order):
        neighbor_mask = 0
        for other in range(order):
            if vertex != other and (vertex // n == other // n or vertex % n == other % n):
                neighbor_mask |= 1 << other
        neighborhoods.append(neighbor_mask)
    blue = initial_blue
    while True:
        newly_blue = 0
        whites = full ^ blue
        for vertex in range(order):
            if (blue >> vertex) & 1:
                white_neighbors = neighborhoods[vertex] & whites
                if white_neighbors.bit_count() == 1:
                    newly_blue |= white_neighbors
        if not newly_blue:
            return blue == full
        blue |= newly_blue


def formula(n):
    coefficients = Counter()
    for r in range(n + 1):
        coefficients[n + r] += 2 * comb(n, r)
    coefficients[2 * n] -= 1
    coefficients[2 * n - 2] += n * n
    for v in range(2, n - 1):
        coefficients[2 * n - 1 - v] += 2 * n * comb(n, v)
    coefficients[n] += 2 * n * (n - 1)
    return +coefficients


def test():
    for n in range(3, 9):
        forcing = [force(n, mask) for mask in range(1 << (2 * n))]
        measured = Counter(mask.bit_count() for mask, yes in enumerate(forcing) if yes)
        expected = formula(n)
        assert measured == expected, (n, measured, expected)
        assert min(measured) == n
        assert measured[n] == 2 * n * (n - 1) + 2
        assert sum(measured.values()) == 2 * (n + 1) * (2 ** n) - n * n - 6 * n - 1
        minimal_sizes = Counter()
        for mask, yes in enumerate(forcing):
            if yes and all(not forcing[mask ^ (1 << i)] for i in range(2 * n) if (mask >> i) & 1):
                minimal_sizes[mask.bit_count()] += 1
        assert minimal_sizes == {n: 2 * n * (n - 1) + 2}, (n, minimal_sizes)
        print('n=%d all_coefficients=%s inclusion_minimal=%s' % (n, dict(sorted(measured.items())), dict(minimal_sizes)))
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
