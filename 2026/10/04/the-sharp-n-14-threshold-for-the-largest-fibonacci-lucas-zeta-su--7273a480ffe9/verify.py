from fractions import Fraction
from math import comb


def bernoulli(n):
    a = [Fraction(0) for _ in range(n + 1)]
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def weight(kind, j):
    if kind == "F":
        return fibonacci(j) + fibonacci(2 * j)
    if kind == "L":
        return lucas(2 * j) - lucas(j)
    raise ValueError(kind)


def magnitude(kind, N, j):
    assert N % 2 == 0 and j % 2 == 0 and 2 <= j <= N - 2
    m = N - j
    return Fraction(
        N * comb(N - 1, j) * weight(kind, j) * (2 ** (m - 1)), m
    ) * abs(bernoulli(m))


# Source weights in Proposition 7, equation (46).
assert [weight("F", j) for j in (2, 4, 6, 8, 10)] == [4, 24, 152, 1008, 6820]
assert [weight("L", j) for j in (2, 4, 6, 8, 10)] == [4, 40, 304, 2160, 15004]

# Exact rational check of the source's explicit final numerical inequality (50).
assert Fraction(12, 1) * Fraction(11, 4) ** 17 / (2 ** 26) < Fraction(81, 8)

expected = {
    "F": {
        12: (10, 8, Fraction(16984, 1)),
        14: (8, 6, Fraction(1793792, 5)),
        16: (8, 6, Fraction(24414208, 3)),
        18: (8, 6, Fraction(1240702976, 5)),
        20: (8, 6, Fraction(9515073536, 1)),
        22: (8, 6, Fraction(2224780214272, 5)),
        24: (8, 6, Fraction(373197717635072, 15)),
    },
    "L": {
        12: (10, 8, Fraction(44968, 1)),
        14: (8, 10, Fraction(14055184, 15)),
        16: (8, 6, Fraction(72550400, 3)),
        18: (8, 6, Fraction(3703447552, 5)),
        20: (8, 6, Fraction(199033323520, 7)),
        22: (8, 6, Fraction(6649987334144, 5)),
        24: (8, 6, Fraction(223116686262272, 3)),
    },
}

for kind in ("F", "L"):
    for N in range(12, 26, 2):
        values = sorted(
            ((magnitude(kind, N, j), j) for j in range(2, N - 1, 2)),
            reverse=True,
        )
        (largest, j_largest), (second, j_second) = values[:2]
        exp_j, exp_second, exp_gap = expected[kind][N]
        assert j_largest == exp_j
        assert j_second == exp_second
        assert largest - second == exp_gap
        assert all(largest > value for value, j in values[1:])

print("VERIFY_OK source_weights exact; source_bound_50 exact; N=12,14,16,18,20,22,24 exhaustive rational comparisons exact")
