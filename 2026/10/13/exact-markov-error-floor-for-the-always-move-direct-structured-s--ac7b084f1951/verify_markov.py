from fractions import Fraction
from itertools import product


def check_q(q: int) -> None:
    p = Fraction(1, 2**q)
    assert p < Fraction(1, 2)
    r = p / (1 - p)
    pi0 = (1 - 2*p) / (2*(1-p))
    pi1 = (1 - 2*p) / (4*(1-p)**2)

    # Detailed balance at 0<->1 and on a positive edge.
    assert pi0 * Fraction(1, 2) == pi1 * (1-p)
    assert pi1 * p == (pi1*r) * (1-p)

    # Exact geometric-series normalization.
    total = pi0 + 2*pi1/(1-r)
    assert total == 1

    # sum_{n>=1} n^2 r^(n-1) = (1+r)/(1-r)^3.
    second = 2*pi1*(1+r)/(1-r)**3
    target = Fraction(1, 2) / (1-2*p)**2
    assert second == target

    # Objective time-average factor after multiplying by eta^2/2.
    objective_factor = second / 2
    claimed_factor = Fraction(1, 4) / (1-2*p)**2
    assert objective_factor == claimed_factor


def check_q1_walk(max_t: int = 10) -> None:
    for t in range(max_t + 1):
        if t == 0:
            assert Fraction(0, 1) == t
            continue
        total = 0
        for signs in product((-1, 1), repeat=t):
            s = sum(signs)
            total += s*s
        expected = Fraction(total, 2**t)
        assert expected == t


for q in range(2, 13):
    check_q(q)
check_q1_walk()
print("VERIFY_OK")
