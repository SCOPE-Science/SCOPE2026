"""Exact finite checks accompanying the quintic binomid classification."""
from fractions import Fraction
from math import prod

EXPECTED = [
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1),
    (0, 0, 0, 1, 1),
    (0, 0, 0, 1, 2),
    (0, 0, 0, 1, 3),
    (0, 0, 1, 1, 2),
    (0, 0, 1, 2, 3),
    (0, 1, 2, 3, 4),
]


def first_test_candidates(degree):
    """Rigorous prefix bound: each branch terminates without a hard cutoff."""
    answer = []
    nodes = 0

    def extend(prefix, ratio):
        nonlocal nodes
        nodes += 1
        if len(prefix) == degree:
            if ratio.denominator == 1:
                answer.append(tuple(prefix))
            return
        remaining = degree - len(prefix)
        a = prefix[-1] if prefix else 0
        least_integer_above_ratio = ratio.numerator // ratio.denominator + 1
        while ratio * Fraction(a + 2, a + 1) ** remaining >= least_integer_above_ratio:
            extend(prefix + [a], ratio * Fraction(a + 2, a + 1))
            a += 1

    extend([], Fraction(1, 1))
    return answer, nodes


def f(a, n):
    return prod(n + x for x in a)


def divisible(a, n, k):
    top = prod(f(a, t) for t in range(n - k + 1, n + 1))
    bottom = prod(f(a, t) for t in range(1, k + 1))
    return top % bottom == 0


def E(modulus, x, y):
    from math import floor
    return sum(
        (x + y + s) // modulus - (x + s) // modulus
        - (y + s) // modulus + s // modulus
        for s in (0, 0, 0, 1, 3)
    )


if __name__ == '__main__':
    candidates, nodes = first_test_candidates(5)
    assert nodes == 927939, nodes
    assert len(candidates) == 1323, len(candidates)
    survivors = sorted(a for a in candidates if divisible(a, 3, 1) and divisible(a, 4, 2))
    assert survivors == EXPECTED, survivors
    print('Exact exhaustive quintic candidate count:', len(candidates))
    print('Exact prefix recursion nodes:', nodes)
    print('Finite recognition survivors:', survivors)

    for modulus in range(2, 65):
        bad = [(x, y, E(modulus, x, y)) for x in range(modulus)
               for y in range(modulus) if E(modulus, x, y) < 0]
        assert bad == ([(1, 1, -1)] if modulus == 4 else []), (modulus, bad)
    assert E(2, 1, 1) == 1
    print('Shift-carry checks: moduli 2..64 (unique negative E_4 at (1,1))')

    for a in EXPECTED:
        for n in range(1, 81):
            for k in range(n + 1):
                assert divisible(a, n, k), (a, n, k)
    print('Generalized binomial integrality checks: 8 families, rows 1..80')
    print('VERIFY_OK')
