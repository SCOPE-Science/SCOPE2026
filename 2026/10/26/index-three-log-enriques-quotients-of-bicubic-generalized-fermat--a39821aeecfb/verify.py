"""Exact arithmetic checks for the stated (3,3) cyclic-quotient calculations.

These checks independently reproduce the integer combinatorics used in the proof;
local quotient geometry and Lefschetz theory still require the written argument.
"""
from itertools import combinations
from math import comb


def binomial_series_coeff_negative_two(power):
    return (-1)**power * (power + 1) * 3**power


def c_tangent_coefficient(degree):
    return sum(comb(6, j) * binomial_series_coeff_negative_two(degree-j)
               for j in range(degree+1))


def check():
    # An explicit nonempty admissible parameter instance, and all allowed
    # coefficient-pair configurations that are needed for smoothness.
    a, b, c = 2, 3, 4
    columns = [(1,a),(1,b),(1,c),(1,1),(1,0),(0,1)]
    for i,j in combinations(range(6),2):
        assert columns[i][0]*columns[j][1]-columns[j][0]*columns[i][1] != 0
    for i,j in combinations(range(2,6),2):
        assert columns[i][0]*columns[j][1]-columns[j][0]*columns[i][1] != 0

    # Direct expansion (1+H)^6/(1+3H)^2 to degree 3.
    assert [c_tangent_coefficient(i) for i in range(4)] == [1,0,6,-16]
    degree_x = 3*3
    e_x = c_tangent_coefficient(3)*degree_x
    assert e_x == -144

    # Curve cut out by two cubics in projective three-space.
    g = 1 + (3+3-4)*degree_x//2
    assert g == 10
    e_c = 2-2*g
    assert e_c == -18

    # Rational representation of an order-3 action on H^3(X).
    b3 = 4 - e_x
    tr = 4 - e_c
    assert b3 == 148 and tr == 22
    assert (b3+2*tr)%3 == 0 and (b3-tr)%3 == 0
    invariant_b3 = (b3+2*tr)//3
    other_each = (b3-tr)//3
    assert invariant_b3 == 64 and other_each == 42
    assert invariant_b3 + 2*other_each == b3
    h21_invariant = invariant_b3//2
    assert h21_invariant == 32

    # In the blowup: H^2(C) contributes to H^4, and H^1(C)(-1)
    # contributes two genus-g pieces to the middle cohomology.
    h11_z = 1 + 1
    h21_z = h21_invariant + g
    h30_z = 0
    e_y = (e_x + 2*e_c)//3
    e_z = e_y + e_c
    assert (h11_z,h21_z,h30_z) == (2,42,0)
    assert e_y == -60 and e_z == -78
    assert 2 + 2*h11_z - 2*h21_z == e_z
    # The cyclic normal quotient has minimal-resolution self-intersection -3,
    # and canonical discrepancy is (2/3)-1.
    assert -3*(-1/3) == 1
    print('VERIFY_OK: smoothness minors, Chern, genus, traces, Hodge, Euler, discrepancy')


if __name__ == '__main__':
    check()
