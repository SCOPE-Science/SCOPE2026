#!/usr/bin/env python3
"""Exact rational examples of the three-coordinate obstruction."""
from fractions import Fraction


def main():
    for k in range(2, 102):
        t = Fraction(1, k)
        c = (1 - t*t) / (1 + t*t)
        s = 2*t / (1 + t*t)
        b = s / (2*c)
        norm = 1 / c
        assert c*c + s*s == 1
        assert norm*norm == 1 + 4*b*b and c + 2*b*s == norm
        deficit = 1 - 1/norm
        truncation_error = 2*b/norm
        assert deficit > 0
        assert truncation_error**2 == deficit * (1 + 1/norm)
    print("100 exact Pythagorean instances verified")


if __name__ == "__main__":
    main()
