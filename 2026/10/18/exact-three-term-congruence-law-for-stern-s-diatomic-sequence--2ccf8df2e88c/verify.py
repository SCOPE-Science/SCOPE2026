"""Self-contained finite checks of the stated Stern three-term congruence law."""
from collections import Counter, deque
from fractions import Fraction
from math import gcd


def stern(limit):
    s = [0, 1] + [0] * (limit + 1)
    for n in range(2, limit + 2):
        s[n] = s[n // 2] if n % 2 == 0 else s[n // 2] + s[n // 2 + 1]
    return s


def states(m):
    return [(a, b) for a in range(m) for b in range(m) if gcd(a, b, m) == 1]


def mass(m, a, b, c, J=None):
    if gcd(a, b, m) != 1:
        return Fraction(0)
    d = gcd(2 * b, m)
    q = m // d
    delta = (a + c - b) % m
    if delta % d:
        return Fraction(0)
    r = 0 if q == 1 else (delta // d) * pow(2 * b // d, -1, q) % q
    if J is None:
        J = len(states(m))
    return Fraction(2 ** (q - r - 1), J * (2 ** q - 1))


def verify():
    s = stern(1 << 18)
    for n in range(200000):
        t, z = 0, n + 1
        while z % 2 == 0:
            z //= 2
            t += 1
        assert s[n + 2] == (2 * t + 1) * s[n + 1] - s[n]

    for m in range(2, 13):
        sm = states(m)
        J = len(sm)
        assert J == sum(1 for a in range(m) for b in range(m)
                        if gcd(a, b, m) == 1)
        total = Fraction(0)
        for a in range(m):
            for b in range(m):
                p = sum((mass(m, a, b, c, J) for c in range(m)), Fraction(0))
                assert p == Fraction(1, J) if (a, b) in sm else p == 0
                total += p
        assert total == 1

        # Primitive-pair state graph is strongly connected: check L/R orbits.
        seen = {(1 % m, 1 % m)}
        queue = deque(seen)
        while queue:
            a, b = queue.popleft()
            for pair in ((a, (a + b) % m), ((a + b) % m, b)):
                if pair not in seen:
                    seen.add(pair)
                    queue.append(pair)
        assert seen == set(sm)

    start, end = 1 << 16, 1 << 17
    for m in (3, 4, 6, 7):
        counts = Counter((s[n] % m, s[n + 1] % m, s[n + 2] % m)
                         for n in range(start, end))
        J = len(states(m))
        largest_error = max(
            abs(Fraction(counts[a, b, c], end - start) - mass(m, a, b, c, J))
            for a in range(m) for b in range(m) for c in range(m)
        )
        assert largest_error < Fraction(1, 400), (m, largest_error)
    print('VERIFY_OK: identity=200000, moduli=2..12, empirical-row=65536')


if __name__ == '__main__':
    verify()
