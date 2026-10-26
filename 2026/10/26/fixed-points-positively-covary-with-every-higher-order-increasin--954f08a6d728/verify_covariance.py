"""Exact verifier of fixed-point / increasing-subsequence covariance identities."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def prediction(n, k):
    c = comb(n, k)
    ranks = [[Fraction(comb(x - 1, j - 1) * comb(n - x, k - j), c)
              for x in range(1, n + 1)] for j in range(1, k + 1)]
    for row in ranks:
        assert sum(row) == 1
    collision = sum((q * q for row in ranks for q in row), Fraction(0))
    cov = Fraction(c, factorial(k)) * (collision - Fraction(k, n))
    return cov, collision


def subseq_counts(p):
    n = len(p)
    ending = [[0] * (n + 1) for _ in range(n + 1)]
    for v in p:
        for k in range(n, 1, -1):
            ending[k][v] += sum(ending[k - 1][1:v])
        ending[1][v] += 1
    return [sum(ending[k]) for k in range(n + 1)]


def verify():
    assertions = 0
    for n in range(3, 9):
        perms = 0
        sums = [0] * (n + 1)
        joint = [0] * (n + 1)
        fixedsum = 0
        for p in permutations(range(1, n + 1)):
            f = sum(v == i for i, v in enumerate(p, start=1))
            z = subseq_counts(p)
            perms += 1
            fixedsum += f
            for k in range(3, n + 1):
                sums[k] += z[k]
                joint[k] += f * z[k]
        assert perms == factorial(n)
        assert fixedsum == perms
        assertions += 2
        for k in range(3, n + 1):
            calculated = Fraction(joint[k], perms) - Fraction(sums[k], perms)
            predicted, collision = prediction(n, k)
            assert Fraction(sums[k], perms) == Fraction(comb(n, k), factorial(k))
            assert calculated == predicted, (n, k, calculated, predicted)
            assert predicted > 0
            assert collision > Fraction(k, n)
            assert predicted >= Fraction(comb(n, k), factorial(k)) * Fraction(k - 1, n * (n-k+1))
            assertions += 5
        print(f"n={n}: {perms} permutations, exact identities agree")
    for n in range(3, 151):
        for k in range(3, min(n, 17) + 1):
            cov, energy = prediction(n, k)
            assert cov > 0
            assertions += 1
        # Includes a separate large-parameter check of the fixed-k leading coefficient.
    for k in range(3, 13):
        coeff = Fraction(4 ** (k - 1), factorial(2*k-1)) - Fraction(k, factorial(k)**2)
        assert coeff > 0
        assertions += 1
    print(f"PASS: {assertions} exact rational assertions plus exhaustive enumeration")


if __name__ == '__main__':
    verify()
