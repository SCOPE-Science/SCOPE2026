"""Finite exact-arithmetic cross-check of the closed three-level passivity criterion.

Run with Python 3 using the standard library: python verify.py
The theorem for unbounded copy number is proved analytically in RESULT.md.
"""
from itertools import product


def criterion(n, p0, p1, p2):
    """Exact integer form of the claimed n-passivity criterion."""
    assert 1 <= p2 <= p1 <= p0 and n >= 1
    g = (n - 1) // 2
    if p0 * p2 == p1 * p1:
        return True
    if p0 * p2 < p1 * p1:
        return p0 ** (g + 1) * p2 ** g >= p1 ** (2*g + 1)
    return p1 ** (2*g + 1) >= p0 ** g * p2 ** (g + 1)


def enumerate_passivity(n, p0, p1, p2):
    """Independently enumerate all 3**n energy-eigenstate populations."""
    extremes = {}
    for occupations in product((0, 1, 2), repeat=n):
        energy = sum(occupations)
        weight = p0 ** occupations.count(0) * p1 ** occupations.count(1) * p2 ** occupations.count(2)
        old = extremes.get(energy)
        if old is None:
            extremes[energy] = (weight, weight)
        else:
            extremes[energy] = (min(old[0], weight), max(old[1], weight))
    return all(extremes[energy][0] >= extremes[energy + 1][1]
               for energy in range(2*n))


def gap_extrema(n):
    L = lambda e: max(0, e - n)
    U = lambda e: e // 2
    return (max(U(e) - L(e+1) for e in range(2*n)),
            max(U(e+1) - L(e) for e in range(2*n)))


def main():
    checked = 0
    for n in range(1, 10):
        assert gap_extrema(n) == ((n-1)//2, (n+1)//2)
        for p0 in range(1, 12):
            for p1 in range(1, p0+1):
                for p2 in range(1, p1+1):
                    assert criterion(n, p0, p1, p2) == enumerate_passivity(n, p0, p1, p2), (n, p0, p1, p2)
                    checked += 1
    for n in range(1, 121):
        assert gap_extrema(n) == ((n-1)//2, (n+1)//2)
    assert criterion(3, 8, 2, 1) and criterion(4, 8, 2, 1)
    assert not criterion(5, 8, 2, 1)
    assert not criterion(3, 9, 6, 1)
    assert all(criterion(n, 9, 3, 1) for n in range(1, 121))
    print(f'VERIFY_OK {checked} exact product-spectrum tests; 120 shell-extremum tests')

if __name__ == '__main__':
    main()
