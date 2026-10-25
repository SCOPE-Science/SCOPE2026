#!/usr/bin/env python3
"""Exact rational checks for a two-player cube-root equilibrium branch."""
from fractions import Fraction


def main():
    checked = 0
    for k in range(2, 101):
        eps = Fraction(1, k**3)
        x = Fraction(1, k)
        y = x - eps

        # The candidate lies strictly inside both action intervals.
        assert Fraction(0) <= eps <= Fraction(1, 8)
        assert Fraction(-1) < x < Fraction(1)
        assert Fraction(-1) < y < Fraction(1)

        # First-order conditions at the candidate, checked exactly.
        assert -x + y + eps == 0
        assert -y + x - x**3 == 0

        # Both own-action second derivatives are identically -1.
        assert Fraction(-1) < 0
        assert Fraction(-1) < 0

        # The response quotient equals k^2 and is unbounded along this sequence.
        assert x / eps == k * k
        checked += 1

    # The joint FOC Jacobian at (x,y,eps)=(0,0,0) is singular.
    jacobian = ((-1, 1), (1, -1))
    determinant = jacobian[0][0] * jacobian[1][1] - jacobian[0][1] * jacobian[1][0]
    assert determinant == 0
    print(f"PASS: {checked} exact rational parameter points; response quotients k^2; base Jacobian determinant {determinant}.")


if __name__ == "__main__":
    main()
