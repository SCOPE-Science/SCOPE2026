"""Exact rational audit of a finite sibling coupon-deficit example.

The stopping time is the first drawing at which every coupon type has
appeared.  After the stopping time the j-th album lacks a type precisely
when that type has appeared fewer than j times.  Occupancy is capped at j.

Requires only the Python 3 standard library. Run:
    python coupon_variance_checker.py
This is a finite verification, not a substitute for the asymptotic proof.
"""
from fractions import Fraction
from functools import lru_cache


def deficit_law(probabilities, j):
    p = tuple(Fraction(x) for x in probabilities)
    n = len(p)
    assert n >= 2 and j >= 2
    assert sum(p) == 1 and all(x > 0 for x in p)

    @lru_cache(None)
    def law(state):
        if min(state) >= 1:
            count = sum(x < j for x in state)
            return tuple(Fraction(i == count) for i in range(n + 1))
        active = sum(p[i] for i in range(n) if state[i] < j)
        assert active > 0
        total = [Fraction(0) for _ in range(n + 1)]
        for i in range(n):
            if state[i] == j:
                continue
            nxt = list(state)
            nxt[i] += 1
            child = law(tuple(nxt))
            for k in range(n + 1):
                total[k] += p[i] * child[k]
        return tuple(x / active for x in total)

    result = law((0,) * n)
    assert sum(result) == 1
    assert result[0] == 0
    assert all(x >= 0 for x in result)
    return result


def moments(probabilities, j):
    probabilities_of_counts = deficit_law(probabilities, j)
    mean = sum(k * mass for k, mass in enumerate(probabilities_of_counts))
    second = sum(k * k * mass for k, mass in enumerate(probabilities_of_counts))
    return probabilities_of_counts, mean, second - mean * mean


def main():
    one_third = Fraction(1, 3)
    uniform_law, uniform_mean, uniform_var = moments(
        [one_third, one_third, one_third], 3
    )
    assert uniform_law == (
        Fraction(0), Fraction(17, 108), Fraction(35, 108), Fraction(14, 27)
    )
    assert uniform_mean == Fraction(85, 36)
    assert uniform_var == Fraction(707, 1296)

    uneven_law, uneven_mean, uneven_var = moments(
        [Fraction(4, 9), Fraction(4, 9), Fraction(1, 9)], 3
    )
    assert uneven_law == (
        Fraction(0), Fraction(272569, 656100),
        Fraction(185131, 656100), Fraction(1984, 6561)
    )
    assert uneven_mean == Fraction(45853, 24300)
    assert uneven_var == Fraction(416326091, 590490000)
    assert uneven_var - uniform_var == Fraction(5887451, 36905625) > 0
    assert uneven_mean < uniform_mean
    assert uneven_var < 1  # Universal range-bound for N=3.

    # Distinct finite instance checking state transitions in two types.
    binary_law, _, binary_var = moments([Fraction(2, 3), Fraction(1, 3)], 4)
    assert binary_law[1] + binary_law[2] == 1
    assert Fraction(0) <= binary_var <= Fraction(1, 4)

    print("Exact finite sibling-deficit certificate: PASS")
    print("uniform variance:", uniform_var)
    print("nonuniform variance:", uneven_var)
    print("strict difference:", uneven_var - uniform_var)


if __name__ == "__main__":
    main()
