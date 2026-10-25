"""Exact finite-path checks for the symmetry/velocity theorem.

Run: python verify_regenerating_symmetry.py
The analytic proof, not finite enumeration, establishes the all-order theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def moment_of_transition(law, right, left):
    return sum((prob * theta**right * (1-theta)**left
                for theta, prob in law), F(0))


def expected_displacement(law, steps):
    total = F(0)
    for increments in product((-1, 1), repeat=steps):
        position = 0
        departures = {}
        for sign in increments:
            counts = departures.setdefault(position, [0, 0])
            counts[0 if sign == 1 else 1] += 1
            position += sign
        path_probability = F(1)
        for rights, lefts in departures.values():
            path_probability *= moment_of_transition(law, rights, lefts)
        total += position * path_probability
    return total


def central_moment(law, power):
    return sum((prob * (theta-F(1,2))**power
                for theta, prob in law), F(0))


def predicted_coefficient(law, rank):
    copies = [(theta-F(1,2), prob) for theta, prob in law]
    even_sum = sum((pa*pb*(ya+yb)**(2*rank)
                    for ya, pa in copies for yb, pb in copies), F(0))
    return 2*central_moment(law, 2*rank+1)*even_sum


def verify_case(law, rank):
    assert sum((pr for _, pr in law), F(0)) == 1
    assert all(F(0)<theta<F(1) and pr>0 for theta,pr in law)
    assert central_moment(law, 1) == 0
    assert all(central_moment(law, 2*j+1) == 0 for j in range(1,rank))
    for length in range(1, 4*rank+1):
        assert expected_displacement(law, length) == 0, (rank,length)
    actual = expected_displacement(law, 4*rank+1)
    predicted = predicted_coefficient(law, rank)
    assert actual == predicted, (actual, predicted)
    return actual


if __name__ == '__main__':
    skew = [(F(1,4), F(3,5)), (F(7,8), F(2,5))]
    assert central_moment(skew, 2) == F(3,32)
    assert central_moment(skew, 3) == F(3,256)
    assert verify_case(skew,1) == F(9,2048)
    quintic = [(F(1,10), F(17,250)),
               (F(3,10), F(8,25)),
               (F(3,5), F(64,125)),
               (F(9,10), F(1,10))]
    assert central_moment(quintic, 3) == 0
    assert central_moment(quintic, 5) == F(18,78125)
    assert verify_case(quintic,2) == predicted_coefficient(quintic,2)
    symmetric = [(F(1,4), F(1,2)), (F(3,4), F(1,2))]
    assert all(expected_displacement(symmetric, n) == 0 for n in range(1,10))
    print('PASS: first-order skewness and second-order asymmetry hierarchy; '
          'symmetric controls; exact rational enumeration through nine steps')
