#!/usr/bin/env python3
"""Independent finite-degree checks of the characteristic-two binomial expansion.

The written proof covers all powers q>=4; these are illustrative exact checks.
"""
from math import comb


def expansion_exponents(q):
    # Coefficient of t^j in (a*t+b)^(q+2) over F_2;
    # retain just exponents, since nonzero monomial coefficients are all 1.
    return [j for j in range(q + 3) if comb(q + 2, j) % 2]


def run():
    for n in range(2, 7):
        q = 2**n
        expected = [0, 2, q, q + 2]
        assert expansion_exponents(q) == expected
        assert len({0, 1, 2, q, q + 2}) == 5
        # The t^2 coefficient has shape a^2*b^q, so b must vanish
        # for any ordinary geometric automorphism (a != 0, a,b in a field).
        assert comb(q + 2, 2) % 2 == 1
        assert comb(q + 2, 1) % 2 == 0
        print(f"VERIFY_OK n={n} q={q} binomial_degrees={expected} t2_obstruction=present")
    print("VERIFY_OK characteristic_two_projective_stabilizer_polynomial_pattern")


if __name__ == "__main__":
    run()
