from fractions import Fraction
from math import prod


def verify(K, N):
    weights = [Fraction(0), 2 * K - 1]
    weights.extend((K * (j + 1) - 1) / (K * j) for j in range(2, N + 1))
    P = [Fraction(1)]
    for j in range(1, N + 1):
        P.append(P[-1] * weights[j])
    assert all(weights[j] >= weights[j + 1] for j in range(1, N))
    for j in range(N + 1):
        orbit = [P[j] / P[j - k] for k in range(j + 1)]
        expected = K * (j + 1) if j > 0 else Fraction(1)
        assert sum(orbit) == expected
        for horizon in range(1, 2 * N + 4):
            assert sum(orbit[:horizon]) <= K * horizon
    for n in range(1, N + 1):
        envelope = (K * (n + 1) - 1) * prod(
            (1 - Fraction(1) / (K * j) for j in range(2, n + 1)),
            start=Fraction(1),
        )
        assert P[n] == envelope
        assert max(P[j] / P[j - n] for j in range(n, N + 1)) == envelope


for K in [Fraction(1), Fraction(5, 4), Fraction(3, 2),
          Fraction(2), Fraction(7, 2), Fraction(17, 3)]:
    for N in range(1, 12):
        verify(K, N)
print('EXACT_FINITE_CHECK_OK for rational K and sizes 1..11')
