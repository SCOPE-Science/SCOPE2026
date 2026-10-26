"""Exhaustive finite check for the minimum degree in a six-variable loop class.

Class: b_i >= 2; loop matrix determinant degree d = product(b_i)-1;
positive primitive weights; ambient weighted projective space well-formed;
and sum(weights) < d. The lower-bound search checks only ambient well-formedness,
so it is a superset of well-formed hypersurfaces; the witness itself is well-formed.
The search bound 17280 is sufficient because the witness has product(b_i)=17280,
so any lower degree has smaller product.
"""
from itertools import permutations
from math import gcd, prod
from functools import reduce
from fractions import Fraction

BOUND = 17280
VARIABLES = 6


def sorted_multisets(prefix, last, product_so_far, output):
    if len(prefix) == VARIABLES:
        output.append(tuple(prefix))
        return
    for b in range(last, BOUND // product_so_far + 1):
        sorted_multisets(prefix + [b], b, product_so_far * b, output)


def loop_degree_and_weights(exponents):
    """Return d and integer weights solving b_i*a_i + a_(i+1) = d."""
    assert len(exponents) == VARIABLES and all(b >= 2 for b in exponents)
    d = prod(exponents) - 1  # determinant of a six-cycle exponent matrix
    b0, b1, b2, b3, b4, b5 = exponents
    alternating_tail = 1 - b5 + b5*b4 - b5*b4*b3 + b5*b4*b3*b2 - b5*b4*b3*b2*b1
    weights = [-alternating_tail]
    for i in range(VARIABLES - 1):
        weights.append(d - exponents[i] * weights[-1])
    assert all(exponents[i] * weights[i] + weights[(i + 1) % VARIABLES] == d
               for i in range(VARIABLES))
    return d, tuple(weights)


def gcd_all(values):
    return reduce(gcd, values, 0)


def well_formed(weights):
    return all(gcd_all([weights[j] for j in range(len(weights)) if j != i]) == 1
               for i in range(len(weights)))


def pairwise_coprime(weights):
    return all(gcd(weights[i], weights[j]) == 1
               for i in range(len(weights)) for j in range(i + 1, len(weights)))


multisets = []
sorted_multisets([], 2, 1, multisets)
normalized_tuples = 0
qualifying = []
for multiset in multisets:
    # Cyclic rotation preserves degree, weight sum, positivity, gcd, and
    # well-formedness, so every cyclic tuple can be rotated to put a minimum
    # exponent first. Enumerate every ordering of the remaining multiset.
    for tail in set(permutations(multiset[1:])):
        exponents = (multiset[0],) + tail
        normalized_tuples += 1
        d, weights = loop_degree_and_weights(exponents)
        if any(a <= 0 for a in weights):
            continue
        if gcd_all(weights) != 1:  # makes d the least common denominator
            continue
        if not well_formed(weights):
            continue
        if sum(weights) < d:
            qualifying.append((d, exponents, weights, sum(weights)))

minimum_degree = min(row[0] for row in qualifying)
witness_exponents = (4, 6, 5, 6, 6, 4)
witness_degree, witness_weights = loop_degree_and_weights(witness_exponents)
assert witness_degree == 17279
assert witness_weights == (3723, 2387, 2957, 2494, 2315, 3389)
assert sum(witness_weights) == 17265
assert witness_degree - sum(witness_weights) == 14
assert gcd_all(witness_weights) == 1
assert well_formed(witness_weights)
assert pairwise_coprime(witness_weights)
# The coordinate point with weight 2315 has quotient type
# 1/2315(3723, 2387, 2957, 2494). Its first Reid--Tai age is below one,
# so the example is explicitly noncanonical.
remainders = [a % 2315 for a in (3723, 2387, 2957, 2494)]
assert remainders == [1408, 72, 642, 179]
noncanonical_age = Fraction(sum(remainders), 2315)
assert noncanonical_age == Fraction(2301, 2315) < 1
assert minimum_degree == witness_degree
assert any(row[0] == witness_degree and row[1] == witness_exponents
           and row[2] == witness_weights for row in qualifying)
assert all(row[0] >= witness_degree for row in qualifying)

print(f"sorted_exponent_multisets={len(multisets)}")
print(f"normalized_tuples_checked={normalized_tuples}")
print(f"ambient_wellformed_numerical_candidates_with_product<=17280={len(qualifying)}")
print(f"minimum_weighted_degree={minimum_degree}")
print(f"witness_exponents={witness_exponents}")
print(f"witness_weights={witness_weights}")
print(f"sum_weights={sum(witness_weights)}")
print(f"canonical_class_coefficient={witness_degree - sum(witness_weights)}")
print(f"noncanonical_coordinate_age={noncanonical_age}")
print("VERIFY_OK")
