#!/usr/bin/env python3
"""Exhaustive exact check of the chi=3 component-group exponent bound."""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import lcm


def cost(n: int) -> Fraction:
    return Fraction(n * n // 4, n)


def main() -> None:
    # The formulas c(2k)=k/2 and c(2k+1)=k(k+1)/(2k+1)
    # make c(n) strictly increasing. Since c(13)=42/13 > 3,
    # every admissible n is at most 12. Since c(n)>=c(2)=1/2,
    # an admissible multiset has at most six entries.
    assert cost(13) == Fraction(42, 13) > 3
    assert all(cost(n + 1) > cost(n) for n in range(2, 13))
    assert all(cost(n) >= Fraction(1, 2) for n in range(2, 13))

    feasible = []
    for size in range(1, 7):
        # Nondecreasing tuples enumerate each finite multiset exactly once.
        for ns in combinations_with_replacement(range(2, 13), size):
            total_cost = sum((cost(n) for n in ns), Fraction(0, 1))
            if total_cost <= 3:
                feasible.append((ns, total_cost, lcm(*ns)))

    assert len(feasible) == 78
    maximum = max(entry[2] for entry in feasible)
    maximizers = sorted(entry[0] for entry in feasible if entry[2] == maximum)
    assert maximum == 60
    assert maximizers == [(3, 4, 5)]
    assert sum((cost(n) for n in (3, 4, 5)), Fraction(0, 1)) == Fraction(43, 15)
    print(f"feasible_multisets={len(feasible)}")
    print(f"maximum_lcm={maximum}")
    print(f"unique_maximizer={maximizers[0]}")
    print(f"maximizer_cost={Fraction(43, 15)} <= 3")


if __name__ == "__main__":
    main()
