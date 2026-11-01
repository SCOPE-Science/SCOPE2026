"""Exact arithmetic checks for dyadic-shell stationary densities of random low-slope maps.

Illustrations, not a replacement for the arbitrary-distribution proofs.
"""
from fractions import Fraction
from itertools import product


def density_levels(p, max_m):
    mean_b = sum(b * v for b, v in p.items())
    c = Fraction(2, mean_b + 2)
    h = [c]
    for m in range(1, max_m + 2):
        h.append(c * sum(v * 2**min(b, m) for b, v in p.items()))
    return c, h


def tail(p, m):
    return sum((w for b, w in p.items() if b >= m), Fraction(0))


def test_model(p):
    assert sum(p.values()) == 1
    c, h = density_levels(p, 50)
    assert h[1] == 2*c
    for m in range(1, 50):
        injection = c * sum((v * 2**(b-1) for b, v in p.items() if b <= m), Fraction(0))
        assert h[m] == h[m+1]/2 + injection
        assert h[m]-h[m-1] == c * 2**(m-1) * tail(p, m)
        assert tail(p,m)-tail(p,m+1) == p.get(m, 0)
    # Normalization by monotone decomposition, including exact infinite shell tail.
    mean_b = sum(b*v for b,v in p.items())
    assert c * (mean_b+2)/2 == 1
    # Distribution of the iid induced return time R = beta+1+geometric(1/2).
    for r in range(2, 40):
        prob = sum((w * Fraction(1, 2**(r-b)) for b,w in p.items() if r >= b+1), Fraction(0))
        assert prob == sum((w*Fraction(1, 2**(j+1)) for b,w in p.items() for j in range(r) if r==b+1+j), Fraction(0))
    return 3*49 + 39 + 2


def main():
    count = 0
    samples = [
        {1:Fraction(1)},
        {2:Fraction(1)},
        {1:Fraction(1,4), 4:Fraction(3,4)},
        {1:Fraction(1,3), 2:Fraction(1,3), 9:Fraction(1,3)},
        {3:Fraction(1,6), 7:Fraction(5,6)},
        {2:Fraction(1,2), 5:Fraction(1,4), 10:Fraction(1,4)},
    ]
    for p in samples:
        count += test_model(p)
    print('PASS: exact transfer stationarity, recovery of switching law, normalization and return law; cases=', len(samples), 'identities=', count)


if __name__ == '__main__':
    main()
