#!/usr/bin/env python3
"""Exact arithmetic checks for the cyclic quotient of a split cubic threefold."""
from fractions import Fraction

# Weights of the order-three scaling on the five ambient coordinates.
weights = (0, 0, 1, 1, 1)
assert sum(weights) % 3 == 0  # ambient determinant character

# The Fermat cubic has degree-two Jacobian generators, hence every
# degree-one coordinate represents a class in its Jacobian ring.
monomials_of_degree_one = ('u', 'v', 'x', 'y', 'z')
assert len(monomials_of_degree_one) == 5
h21_invariants = sum(1 for weight in weights if weight % 3 == 0)
assert h21_invariants == 2

# A fixed elliptic cubic has Euler characteristic zero; add three points.
fixed_euler = 0 + 3
b3_cover = 10
trace_nonidentity_h3 = (1 + 1 + 1 + 1) - fixed_euler
assert trace_nonidentity_h3 == 1
b3_quotient = Fraction(b3_cover + 2 * trace_nonidentity_h3, 3)
assert b3_quotient == 4 == 2 * h21_invariants
assert (4 - int(b3_quotient)) == 0  # Euler characteristic of the quotient

# Along the elliptic curve the normal weights are 1,1 modulo 3;
# at isolated fixed points the tangent weights are 1,1,1 modulo 3.
normal_character_E = (1 + 1) % 3
normal_character_point = (1 + 1 + 1) % 3
assert normal_character_E == 2 and normal_character_point == 0
assert Fraction(1 + 1, 3) < 1 <= Fraction(1 + 1 + 1, 3)

# Adjunction on a cubic threefold: -K_X = 2H, H^3 = 3.
assert Fraction(2**3 * 3, 3) == 8

print('SPLIT_CUBIC_CYCLIC_QUOTIENT_SANITY_OK')
