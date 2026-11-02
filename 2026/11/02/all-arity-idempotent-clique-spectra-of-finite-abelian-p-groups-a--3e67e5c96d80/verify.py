"""Independent finite-case checks for the cyclic p-group idempotent census.

Python 3, standard library only.  Run: python verify.py
This enumerates every endomorphism of the displayed small groups, rather
than generating samples from the derived counting formula.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, prod


def aut_order(exponents, prime):
    counts = Counter(exponents)
    exponent = sum(min(a, b) for a in exponents for b in exponents)
    value = Fraction(prime**exponent)
    for multiplicity in counts.values():
        for i in range(1, multiplicity + 1):
            value *= Fraction(prime**i - 1, prime**i)
    assert value.denominator == 1
    return value.numerator


def weak_computations(exponents, prime, tuple_length):
    """Orbit-stabilizer prediction using ordered colored summands."""
    counts = Counter(exponents)
    colors = 2**tuple_length
    splits = []
    for a, multiplicity in sorted(counts.items()):
        options = (v for v in product(range(multiplicity + 1), repeat=colors)
                   if sum(v) == multiplicity)
        splits.append((a, tuple(options)))
    top = aut_order(exponents, prime)
    result = 0
    for allocation in product(*(options for _, options in splits)):
        orders = []
        for color in range(colors):
            factor_type = [a for (a, _), row in zip(splits, allocation)
                           for _ in range(row[color])]
            orders.append(aut_order(factor_type, prime))
        denominator = prod(orders)
        assert top % denominator == 0
        result += top // denominator
    return result


def enumerate_idempotents(exponents, prime):
    n = len(exponents)
    moduli = [prime**a for a in exponents]
    ranges = [range(0, moduli[i], prime**max(exponents[i] - exponents[j], 0))
              for i in range(n) for j in range(n)]

    def multiply(left, right):
        return tuple(sum(left[i*n+k]*right[k*n+j] for k in range(n)) % moduli[i]
                     for i in range(n) for j in range(n))

    answer = []
    for matrix in product(*ranges):
        if multiply(matrix, matrix) == matrix:
            answer.append(matrix)
    return answer, multiply


def maximal_clique_sizes(neighbors):
    """Enumerate maximal cliques by Bron-Kerbosch with pivoting."""
    sizes = []

    def recurse(R, P, X):
        if not P and not X:
            sizes.append(len(R))
            return
        pivot = max(P | X, key=lambda v: len(P & neighbors[v])) if (P | X) else None
        branch = list(P - (neighbors[pivot] if pivot is not None else set()))
        for v in branch:
            recurse(R | {v}, P & neighbors[v], X & neighbors[v])
            P.remove(v)
            X.add(v)

    recurse(set(), set(range(len(neighbors))), set())
    return sizes


def expected_maximal(exponents, prime):
    denominator = prod((prime**a - prime**(a-1)) for a in exponents)
    denominator *= prod(factorial(c) for c in Counter(exponents).values())
    numerator = aut_order(exponents, prime)
    assert numerator % denominator == 0
    return numerator // denominator


def check(exponents, prime):
    matrices, multiply = enumerate_idempotents(exponents, prime)
    n = len(matrices)
    neighbors = [set() for _ in matrices]
    for i in range(n):
        for j in range(i + 1, n):
            if multiply(matrices[i], matrices[j]) == multiply(matrices[j], matrices[i]):
                neighbors[i].add(j)
                neighbors[j].add(i)

    # Loops appear in tuple counts but not in clique graphs.
    closed = [neighbors[i] | {i} for i in range(n)]
    observed = (
        n,
        sum(len(row) for row in closed),
        sum(len(closed[i] & closed[j]) for i in range(n) for j in closed[i]),
    )
    predicted = tuple(weak_computations(exponents, prime, k) for k in (1, 2, 3))
    assert observed == predicted, (exponents, prime, observed, predicted)
    maximal = maximal_clique_sizes(neighbors)
    assert len(maximal) == expected_maximal(exponents, prime)
    assert set(maximal) == {2**len(exponents)}
    print(f"CHECK_OK prime={prime} exponents={exponents} "
          f"T1={observed[0]} T2={observed[1]} T3={observed[2]} "
          f"maximal={len(maximal)}")


def main():
    for prime, group in ((2, (1, 2)), (2, (1, 3)),
                         (2, (1, 1, 2)), (2, (1, 1, 3)),
                         (3, (1, 2)), (3, (1, 3))):
        check(group, prime)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
