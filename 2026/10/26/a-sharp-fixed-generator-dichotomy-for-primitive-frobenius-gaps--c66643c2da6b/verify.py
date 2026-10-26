"""Exact integer checks for explicit primitive-Frobenius obstructions.

The finite cases test construction identities; the infinite theorem follows
from the divisibility argument in the accompanying mathematical proof.
"""
from math import gcd, prod
from fractions import Fraction


def witness(a: int, L: int):
    assert a >= 3 and L >= 2 and L % 2 == 0
    N = prod(a * j - 1 for j in range(1, L + 1))
    threshold = Fraction(N, a * L)
    # positive b = a*k-1, smallest one strictly exceeding threshold
    k = (N // (a * L) + 1) // a + 1
    b = a * k - 1
    # Correct minimality is verified by an explicit integer comparison.
    if b <= threshold:
        b += a
    assert b > threshold and b - a <= threshold
    return N, b


def run():
    cases = 0
    feasible = 0
    for a in range(3, 14):
        for L in range(2, 15, 2):
            N, b = witness(a, L)
            assert gcd(a, b) == 1
            assert N % a == 1 and b % a == a - 1
            assert Fraction(N, b) >= Fraction(a * L, 1) / (1 + Fraction(a * a * L, N))
            # Independently generate every potential nonnegative solution,
            # without assuming the modular characterization in advance.
            solutions = []
            for y in range(N // b + 1):
                if (N - b * y) % a == 0:
                    x = (N - b * y) // a
                    assert x >= 0
                    solutions.append((x, y))
                    assert 1 <= (y + 1) // a <= L
                    assert y % a == a - 1
                    assert N % y == 0 and x % y == 0
                    assert gcd(x, y) >= a - 1
            assert solutions
            assert not any(gcd(x, y) == 1 for x, y in solutions)
            cases += 1
            feasible += len(solutions)
    samples = [(a, L, *witness(a, L)) for a in [3, 4, 5] for L in [2, 4, 6]]
    print('VERIFY_OK cases=%d nonprimitive_solutions=%d exact_integer_conditions=PASS' % (cases, feasible))
    print('SAMPLES', samples)

if __name__ == '__main__':
    run()
