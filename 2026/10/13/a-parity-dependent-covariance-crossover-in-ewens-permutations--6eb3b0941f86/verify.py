"""Exact finite-sample checks for the Ewens even-cycle-mass covariance theorem.

Python standard library only. All moment comparisons use Fraction.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, sqrt


def rising(x, n):
    ans = Fraction(1)
    for i in range(n):
        ans *= x + i
    return ans


def permutation_statistics(p):
    seen = [False] * len(p)
    components = 0
    even_mass = 0
    for i in range(len(p)):
        if seen[i]:
            continue
        components += 1
        j = i
        size = 0
        while not seen[j]:
            seen[j] = True
            size += 1
            j = p[j]
        if size % 2 == 0:
            even_mass += size
    return components, even_mass


def exhaustive(n, theta):
    mass = total_even = total_cycles = mixed = Fraction(0)
    for p in permutations(range(n)):
        k, even_mass = permutation_statistics(p)
        weight = theta ** k
        mass += weight
        total_even += weight * even_mass
        total_cycles += weight * k
        mixed += weight * k * even_mass
    assert mass == rising(theta, n)
    mean = total_even / mass
    covariance = mixed / mass - mean * total_cycles / mass
    return mean, covariance


def independent_cycle_formula(n, theta):
    """Fixed-cycle expectations and their differentiated finite sum."""
    mean = derivative = Fraction(0)
    for j in range(2, n + 1, 2):
        term = theta * Fraction(factorial(n), factorial(n - j)) / rising(theta + n - j, j)
        mean += term
        log_derivative = Fraction(1, theta) - sum(
            (Fraction(1, theta + k) for k in range(n - j, n)), Fraction(0)
        )
        derivative += term * log_derivative
    return mean, theta * derivative


def independent_integral_formula(n, theta):
    """Polynomial integration with rational parameter; exact, no quadrature."""
    mean = derivative = Fraction(0)
    for j in range(n - 1):
        coefficient = comb(n - 2, j) * (-1) ** (n - 2 - j) * 2**j
        mean += Fraction(coefficient, theta + j + 1)
        derivative -= Fraction(coefficient, (theta + j + 1) ** 2)
    scale = n * (n - 1)
    return scale * mean, theta * scale * derivative


def numerical_derivative(n, theta):
    """Stable beta-binomial recurrence for independent numerical sign checks."""
    p = theta / (theta + n - 1)
    log_derivative = 1 / theta - 1 / (theta + n - 1)
    result = 0.0
    for j in range(1, n + 1):
        if j % 2 == 0:
            result += n * p * log_derivative
        if j < n:
            p *= (n - j) / (theta + n - j - 1)
            log_derivative -= 1 / (theta + n - j - 1)
    return result


def critical_theta(n):
    assert n >= 3 and n % 2 == 1
    lo, hi = 1.0, 2.0
    assert numerical_derivative(n, lo) > 0
    assert numerical_derivative(n, hi) < 0
    for _ in range(65):
        mid = (lo + hi) / 2
        if numerical_derivative(n, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    comparisons = 0
    for n in range(2, 9):
        for theta in (Fraction(1, 4), Fraction(1), Fraction(3, 2), Fraction(3)):
            brute = exhaustive(n, theta)
            cycle = independent_cycle_formula(n, theta)
            integral = independent_integral_formula(n, theta)
            assert brute == cycle == integral, (n, theta, brute, cycle, integral)
            comparisons += 2  # The two moment identities, checked against enumeration.
    sign_checks = 0
    for n in range(2, 34):
        for theta in (Fraction(1), Fraction(2)):
            _, covariance = independent_cycle_formula(n, theta)
            if n % 2 == 0:
                assert covariance < 0, (n, theta)
            elif theta == 1:
                assert covariance > 0, (n, theta)
            else:
                assert covariance < 0, (n, theta)
            sign_checks += 1
    roots = {n: critical_theta(n) for n in (3, 5, 7, 9, 21, 51, 101)}
    assert abs(roots[3] - sqrt(2)) < 1e-11
    assert all(1 < value < 2 for value in roots.values())
    print('PASS: ', comparisons, 'exact moment checks; ', sign_checks,
          'rational sign checks; ', len(roots), 'numerical crossover brackets', sep='')
    print('Crossovers:', {k: round(v, 9) for k, v in roots.items()})


if __name__ == '__main__':
    main()
