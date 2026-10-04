from math import comb
from fractions import Fraction


def stirling2_table(N):
    S = [[0] * (N + 1) for _ in range(N + 1)]
    S[0][0] = 1
    for n in range(1, N + 1):
        for k in range(1, n + 1):
            S[n][k] = S[n - 1][k - 1] + k * S[n - 1][k]
    return S


def restricted_growth_strings(n):
    if n == 0:
        yield ()
        return

    def rec(prefix, current_max):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(current_max + 2):
            prefix.append(value)
            yield from rec(prefix, max(current_max, value))
            prefix.pop()

    yield from rec([0], 0)


def injective_orbits(r, n):
    return 1 << comb(n, r)


def all_tuple_orbits(r, n, S):
    return sum(S[n][k] * (1 << comb(k, r)) for k in range(n + 1))


S = stirling2_table(50)

# Independent equality-pattern enumeration plus arbitrary hyperedge choices.
for r in range(2, 6):
    for n in range(8):
        by_blocks = [0] * (n + 1)
        for word in restricted_growth_strings(n):
            k = 0 if n == 0 else max(word) + 1
            by_blocks[k] += 1
        assert by_blocks == S[n][:n + 1]
        direct = sum(by_blocks[k] * (1 << comb(k, r)) for k in range(n + 1))
        assert direct == all_tuple_orbits(r, n, S)

expected_r2 = [1, 1, 3, 15, 127, 1895, 53071, 2953575, 337064047]
assert [all_tuple_orbits(2, n, S) for n in range(9)] == expected_r2
print("r=2 all_tuple=", expected_r2)

# Exact collision-layer decomposition, checked with rational arithmetic.
for r in range(2, 6):
    for n in range(2, 25):
        total = Fraction(all_tuple_orbits(r, n, S), injective_orbits(r, n))
        layers = sum(
            Fraction(S[n][n - j], 1 << (comb(n, r) - comb(n - j, r)))
            for j in range(n + 1)
        )
        assert total == layers

        if n >= max(r + 2, 5):
            d1 = comb(n - 1, r - 1)
            first = Fraction(comb(n, 2), 1 << d1)
            d2 = comb(n, r) - comb(n - 2, r)
            second = Fraction(S[n][n - 2], 1 << d2)
            assert total - 1 - first >= second

# Numerical check of the sharp leading correction.
for r in range(2, 6):
    values = []
    for n in (12, 18, 24, 32, 40):
        total = Fraction(all_tuple_orbits(r, n, S), injective_orbits(r, n))
        delta = Fraction(comb(n, 2), 1 << comb(n - 1, r - 1))
        values.append((n, float((total - 1) / delta)))
    print("r=", r, "normalized_excess=", values)
    assert abs(values[-1][1] - 1.0) < 1e-6

print("VERIFY_OK")
