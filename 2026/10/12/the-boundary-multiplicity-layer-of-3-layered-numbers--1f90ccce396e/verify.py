from fractions import Fraction


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n):
    ds = [1]
    for p, a in factor(n).items():
        ds = [d * p**e for d in ds for e in range(a + 1)]
    return sorted(ds)


def ipp(p, a):
    return Fraction(p ** (a + 1) - 1, p**a * (p - 1))


def abundancy(n):
    z = Fraction(1, 1)
    for p, a in factor(n).items():
        z *= ipp(p, a)
    return z


maxima = {
    (1,): Fraction(3, 2),
    (2,): Fraction(7, 4),
    (1, 1): Fraction(2, 1),
    (3,): Fraction(15, 8),
    (2, 1): Fraction(7, 3),
    (1, 1, 1): Fraction(12, 5),
    (4,): Fraction(31, 16),
    (3, 1): Fraction(5, 2),
    (2, 2): Fraction(91, 36),
    (2, 1, 1): Fraction(14, 5),
    (1, 1, 1, 1): Fraction(96, 35),
}
assert all(v < 3 for v in maxima.values())
assert ipp(2, 5) == Fraction(63, 32)
assert ipp(2, 4) * ipp(3, 1) == Fraction(31, 12)
assert ipp(2, 3) * ipp(3, 2) == Fraction(65, 24)
assert abundancy(120) == 3
assert abundancy(180) == Fraction(91, 30)
assert ipp(2, 2) * ipp(3, 2) * ipp(7, 1) == Fraction(26, 9)
assert ipp(2, 2) * ipp(3, 1) * ipp(5, 2) == Fraction(217, 75)
assert ipp(3, 2) * ipp(2, 1) * ipp(5, 1) * ipp(7, 1) == Fraction(104, 35)
assert ipp(2, 2) * ipp(5, 1) * ipp(7, 1) * ipp(11, 1) == Fraction(144, 55)
assert ipp(2, 2) * ipp(3, 1) * ipp(7, 1) * ipp(11, 1) == Fraction(32, 11)
assert ipp(2, 1) * ipp(3, 1) * ipp(5, 1) * ipp(7, 1) * ipp(11, 1) == Fraction(1152, 385)

parts = {
    120: [[120], [60, 40, 20], [30, 24, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1]],
    180: [[180, 2], [90, 60, 20, 12], [45, 36, 30, 18, 15, 10, 9, 6, 5, 4, 3, 1]],
    420: [[420, 28], [210, 140, 84, 14], [105, 70, 60, 42, 35, 30, 21, 20, 15, 12, 10, 7, 6, 5, 4, 3, 2, 1]],
    660: [[660, 12], [330, 220, 110, 11, 1], [165, 132, 66, 60, 55, 44, 33, 30, 22, 20, 15, 10, 6, 5, 4, 3, 2]],
    780: [[780, 4], [390, 260, 130, 3, 1], [195, 156, 78, 65, 60, 52, 39, 30, 26, 20, 15, 13, 12, 10, 6, 5, 2]],
}
for n, groups in parts.items():
    assert sum(factor(n).values()) == 5
    flat = [d for g in groups for d in g]
    assert len(flat) == len(set(flat))
    assert sorted(flat) == divisors(n)
    sums = [sum(g) for g in groups]
    assert sums[0] == sums[1] == sums[2]
    assert 3 * sums[0] == sum(divisors(n))

assert [abundancy(n) for n in parts] == [Fraction(3,1), Fraction(91,30), Fraction(16,5), Fraction(168,55), Fraction(196,65)]
print('VERIFY_OK omega_boundary=5 candidates=5 partitions=5')
