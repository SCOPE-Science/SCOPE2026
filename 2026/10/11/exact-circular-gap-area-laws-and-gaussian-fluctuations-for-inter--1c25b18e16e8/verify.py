"""Numerical checks for a circular array of congruent-disk intersections.

Requires only Python 3 and its standard library. Run: python verify.py
Numerical comparisons are not substitutes for the analytic proof.
"""
import math
import random
from fractions import Fraction

PI = math.pi


def rho(t, radius):
    return -math.cos(t) + math.sqrt(radius * radius - math.sin(t) ** 2)


def integrate_simpson(function, a, b, steps=1024):
    if steps % 2:
        raise ValueError("steps must be even")
    step = (b-a)/steps
    total = function(a) + function(b)
    for j in range(1, steps):
        total += (4 if j % 2 else 2)*function(a+j*step)
    return total*step/3


def gap_score(s, radius):
    return integrate_simpson(lambda x: rho(x, radius)**2, 0, s/2, 1024)


def area_gaps(angles, radius):
    sorted_angles = sorted((angle % (2*PI)) for angle in angles)
    gaps = [sorted_angles[j+1]-sorted_angles[j] for j in range(len(angles)-1)]
    gaps += [2*PI-sorted_angles[-1]+sorted_angles[0]]
    return sum(gap_score(s, radius) for s in gaps)


def area_polar_direct(angles, radius, steps=32768):
    center_angles = [angle % (2*PI) for angle in angles]
    def integrand(t):
        return .5*min((math.cos(t-c)+math.sqrt(radius**2-math.sin(t-c)**2))**2 for c in center_angles)
    return integrate_simpson(integrand, 0, 2*PI, steps)


def rising(m,k):
    return math.prod(range(m,m+k))


def test():
    seed = random.Random(20261510)
    count = 0
    largest_error = 0.0
    for radius in (1.05,1.25,1.75,3.0):
        for m in (2,3,4,6,9):
            for case in range(3):
                if case == 0:
                    angles = [2*PI*j/m for j in range(m)]
                elif case == 1:
                    angles = [2*PI*seed.random() for _ in range(m)]
                else:
                    angles = [2*PI*seed.random()**3 for _ in range(m)]
                gap_area = area_gaps(angles, radius)
                direct_area = area_polar_direct(angles, radius)
                error = abs(gap_area-direct_area)
                largest_error = max(largest_error,error)
                assert error < 3e-6, (radius,m,case,gap_area,direct_area,error)
                regular = m*gap_score(2*PI/m,radius)
                assert gap_area+1e-10 >= regular,(radius,m,case)
                count += 1
    # Independent expressions for the first and second moments of summed cubic gaps.
    for m in (3,5,12,25):
        first = Fraction(6,(m+1)*(m+2))
        assert first == Fraction(6*m,rising(m,3))
        second = Fraction(720*m+36*m*(m-1),rising(m,6))
        variance = second-first*first
        assert variance > 0
        count += 3
    # Delta-method influence variance from exponential moments.
    moment_3 = math.factorial(3)
    variance_e3 = math.factorial(6)-moment_3**2
    covariance_e3_e1 = math.factorial(4)-moment_3
    assert variance_e3+18**2-36*covariance_e3_e1 == 360
    count += 1
    # Leading moment coefficients: random-to-regular excess ratio tends to six.
    for m in (100,1000,10000):
        ratio = 6*m*m/((m+1)*(m+2))
        assert 5.8 < ratio < 6
        count += 1
    print(f"VERIFY_OK independent_polar_cases=60 other_checks={count-60} max_area_error={largest_error:.3g}")


if __name__ == '__main__':
    test()
