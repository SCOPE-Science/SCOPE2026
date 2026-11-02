"""Exact integer checks for the nearest-integer 45-degree digital rotation.

Only finite checks are performed here. The all-lattice identity has an
independent geometric proof in the accompanying mathematical argument.
"""
from math import isqrt
from random import Random


def nearest_m_over_sqrt2(m: int) -> int:
    """Return the unique closest integer to m/sqrt(2), using integers only."""
    if m == 0:
        return 0
    magnitude = abs(m)
    value = (isqrt(2 * magnitude * magnitude) + 1) // 2
    return value if m > 0 else -value


def rounded_rotation(z):
    x, y = z
    return (nearest_m_over_sqrt2(x - y),
            nearest_m_over_sqrt2(x + y))


def quarter_turn(z):
    x, y = z
    return (-y, x)


def power(z, exponent):
    for _ in range(exponent):
        z = rounded_rotation(z)
    return z


def verify(z):
    w = rounded_rotation(z)
    assert power(z, 3) == quarter_turn(w)
    assert power(z, 9) == w
    assert power(w, 4) == (-w[0], -w[1])
    assert power(w, 8) == w
    assert (w == (0, 0)) == (z == (0, 0))
    if z != (0, 0):
        assert power(w, 1) != w
        assert power(w, 2) != w
        assert power(w, 4) != w
    return power(z, 8) == z


def main():
    N = 160
    periodic = 0
    transient = 0
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if verify((x, y)):
                periodic += 1
            else:
                transient += 1
    assert periodic + transient == (2*N + 1)**2
    assert rounded_rotation((2, 0)) == (1, 1)
    assert power((2, 0), 9) == power((2, 0), 1)
    assert power((2, 0), 8) != (2, 0)
    rng = Random(451006)
    for _ in range(20000):
        verify((rng.randrange(-10**18, 10**18),
                rng.randrange(-10**18, 10**18)))
    print(f'PASS: {((2*N + 1)**2):,} lattice seeds, 20,000 large exact seeds')
    print(f'Finite grid: {periodic:,} periodic seeds, {transient:,} preperiod-one seeds')
    print('Sharp preperiod witness (2,0) -> (1,1)')


if __name__ == '__main__':
    main()
