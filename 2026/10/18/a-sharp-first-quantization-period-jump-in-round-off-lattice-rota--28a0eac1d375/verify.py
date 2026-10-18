#!/usr/bin/env python3
"""Exact integer checks for a sharp first-resonance law in lattice rotations.

All general mathematical claims are proved in RESULT.md; checks here are finite.
"""

def height(x, y):
    return abs(x) + abs(y) - int(x < 0 and y < 0)


def limiting_map(z):
    x, y = z
    return (-y - int(x < 0), x)


def roundoff_map(z, numerator, denominator):
    x, y = z
    return ((numerator * x) // denominator - y, x)


def phase(z, radius):
    x, y = z
    m = 4 * radius + 1
    if x >= 0 and y >= 0:
        return (-4 * y) % m
    if x < 0 and y >= 0:
        return (2 + 4 * y) % m
    if x < 0 and y < 0:
        return (3 + 4 * (-x - 1)) % m
    return (4 * (-y)) % m


def cycle(start, fn, upper_bound):
    seen = {}
    z = start
    while z not in seen:
        assert len(seen) <= upper_bound, (start, len(seen), upper_bound)
        seen[z] = len(seen)
        z = fn(z)
    assert z == start, ('nonzero preperiod', start, z)
    return seen


def main():
    for r in range(1, 41):
        shell = {(x, y) for x in range(-r - 2, r + 3)
                          for y in range(-r - 2, r + 3)
                          if height(x, y) == r}
        assert len(shell) == 4 * r + 1
        phases = {phase(z, r) for z in shell}
        assert phases == set(range(4 * r + 1))
        for z in shell:
            Gz = limiting_map(z)
            assert Gz in shell
            assert phase(Gz, r) == (phase(z, r) + 1) % (4 * r + 1)
            # Parameter 1/(r+1) lies strictly below the first threshold.
            assert roundoff_map(z, 1, r + 1) == Gz
        protected = cycle((r, 0), lambda z: roundoff_map(z, 1, r + 1),
                          4 * r + 1)
        assert set(protected) == shell
    for q in range(2, 121):
        fn = lambda z: roundoff_map(z, 1, q)
        visited = cycle((q, 0), fn, 8 * q - 2)
        assert len(visited) == 8 * q - 2
        assert sum(height(*z) == q for z in visited) == 4 * q + 1
        assert sum(height(*z) == q + 1 for z in visited) == 4 * q - 3
        assert all(height(*z) in (q, q + 1) for z in visited)
        for r in range(q):
            # At lambda=1/q, strictly inner-shell states are unchanged.
            assert roundoff_map((r, 0), 1, q) == limiting_map((r, 0))
        assert height(*fn((q, 0))) == q + 1
    # Small complete itineraries independent of the phase argument.
    expected = {
        2: [(2, 0), (1, 2), (-2, 1), (-2, -2), (1, -2), (2, 1),
            (0, 2), (-2, 0), (-1, -2), (1, -1), (1, 1), (-1, 1),
            (-2, -1), (0, -2)],
        3: [(3, 0), (1, 3), (-3, 1), (-2, -3), (2, -2), (2, 2),
            (-2, 2), (-3, -2), (1, -3), (3, 1), (0, 3), (-3, 0),
            (-1, -3), (2, -1), (1, 2), (-2, 1), (-2, -2),
            (1, -2), (2, 1), (-1, 2), (-3, -1), (0, -3)]
    }
    for q, itinerary in expected.items():
        actual = list(cycle((q, 0), lambda z: roundoff_map(z, 1, q),
                            8 * q - 2))
        assert actual == itinerary
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
