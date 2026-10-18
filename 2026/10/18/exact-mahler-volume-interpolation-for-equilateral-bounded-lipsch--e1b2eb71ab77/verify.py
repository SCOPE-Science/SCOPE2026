"""Exact arithmetic checks for the equilateral bounded-Lipschitz volume formulas.

The program independently evaluates the section density from signed orthants,
compares it with the proposed binomial polynomial, and calculates the polar
volume both by orthant exclusion and by section integration. Finite checks
supplement, but do not replace, the analytic argument for all dimensions.
"""
from fractions import Fraction as Q
from math import comb, factorial


def section_from_orthants(n, a, b):
    """Coarea density at sum=a-b inside the l1 ball of radius a+b."""
    assert n >= 2 and a >= b >= 0
    t = a - b
    d = n - 1
    total = t ** d / factorial(d)
    for positive in range(1, n):
        negative = n - positive
        for j in range(positive):
            total += (Q(comb(n, positive) * comb(positive - 1, j),
                        factorial(positive - 1) * factorial(negative - 1))
                      * t ** (positive - 1 - j)
                      * b ** (negative + j) / (negative + j))
    return total


def section_from_binomial(n, a, b):
    d = n - 1
    return sum(Q(comb(d, j) ** 2, factorial(d)) * a ** j * b ** (d-j)
               for j in range(n))


def density_coefficients(n):
    """Coefficients of sum_j binom(n-1,j)^2(1+t)^j(1-t)^(n-1-j)."""
    d = n - 1
    result = [0] * n
    for j in range(n):
        for i in range(j + 1):
            for k in range(d - j + 1):
                result[i+k] += (comb(d, j) ** 2 * comb(j, i)
                                * comb(d-j, k) * (-1) ** k)
    return result


def slab_probability(n, cutoff):
    """Exact probability |sum Y_i| <= cutoff for uniform Y in B_1^n."""
    assert Q(0) <= cutoff <= Q(1)
    c = density_coefficients(n)
    return Q(n, 2 ** (2*n-1)) * sum(
        Q(2 * c[k], k+1) * cutoff ** (k+1)
        for k in range(0, n, 2))


def polar_volume_direct(n, s):
    """Independent signed-orthant calculation of |B_1(s) cap {|sum|<=1}|."""
    assert s >= 1
    volume = Q(2, factorial(n))  # two homogeneous-sign orthants

    def excluded_cap(positive, negative):
        # Region with positive-total mass > 1 in a signed orthant.
        # Integrate negative total mass v up to (s-1)/2.
        stop = Q(s-1, 2)
        return sum(
            Q(comb(positive, j) * ((-1)**j * s**(positive-j)-1),
              (negative+j) * factorial(positive) * factorial(negative-1))
            * stop ** (negative+j)
            for j in range(positive+1))

    for positive in range(1, n):
        negative = n-positive
        whole = Q(s**n, factorial(n))
        volume += comb(n, positive) * (
            whole - excluded_cap(positive, negative)
                  - excluded_cap(negative, positive))
    return volume


def run():
    checks = 0
    for n in range(2, 12):
        for a, b in [(Q(1), Q(0)), (Q(1), Q(1)),
                     (Q(2), Q(1)), (Q(3), Q(1)),
                     (Q(7, 3), Q(2, 3)), (Q(5), Q(2))]:
            assert section_from_orthants(n, a, b) == section_from_binomial(n, a, b)
            checks += 1
        assert slab_probability(n, Q(1)) == 1
        checks += 1
    for n in range(2, 10):
        for s in (1, 2, 3, 4, 5):
            assert polar_volume_direct(n, s) == (
                Q(2**n * s**n, factorial(n)) * slab_probability(n, Q(1,s)))
            checks += 1
    for s in (1, 2, 3, 4, 5):
        assert s * slab_probability(2, Q(1,s)) == 1
        checks += 1
    assert slab_probability(3, Q(1,3)) == Q(10, 27)
    assert 3 * slab_probability(3, Q(1,3)) == Q(10,9)
    print(f"PASS {checks+2} exact-rational checks")


if __name__ == '__main__':
    run()
