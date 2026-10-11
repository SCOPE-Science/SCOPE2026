"""Reproducible diagnostics for the expected vertex count of central box sections.

No external dependencies; analytic arguments, not this finite program, prove the theorem.
"""
from itertools import product
from math import asin, pi, sqrt
import random


def predicted(half_widths):
    d = len(half_widths)
    assert d >= 2 and all(a > 0 for a in half_widths)
    total = sum(a*a for a in half_widths)
    return (2**d / pi) * sum(asin(a/sqrt(total)) for a in half_widths)


def edge_intersection_count(half_widths, normal):
    """Count transversal edge-hyperplane intersections, independent of predicted()."""
    d = len(half_widths)
    count = 0
    for moving in range(d):
        other = [j for j in range(d) if j != moving]
        for signs in product((-1, 1), repeat=d-1):
            value = sum(sign * half_widths[j] * normal[j]
                        for sign, j in zip(signs, other))
            if abs(value) < abs(half_widths[moving] * normal[moving]):
                count += 1
    return count


def run():
    # Closed-form finite-dimensional benchmarks, including the dimension-2 boundary case.
    assert abs(predicted((1., 1.)) - 2.) < 1.e-13
    assert abs(predicted((1., 1., 1., 1.)) - 32./3.) < 1.e-13
    assert abs(predicted((1., 1., 1.)) - (24./pi)*asin(1./sqrt(3.))) < 1.e-13

    cases = [(1., 1., 1.), (2., 1., 0.5),
             (1., 1., 1., 1.), (3., 1., 2., .5),
             (1., 1., 1., 1., 1.), (1., 2., 3., 4., 5.)]
    rng = random.Random(20261008)
    measured = []
    for a in cases:
        samples = 9000
        total = sum(edge_intersection_count(a, [rng.gauss(0, 1) for _ in a])
                    for _ in range(samples))
        observed, theoretical = total/samples, predicted(a)
        # A supplemental finite Monte Carlo test, not an error certificate.
        assert abs(observed - theoretical) < .22, (a, observed, theoretical)
        measured.append((len(a), round(observed, 6), round(theoretical, 6)))

    # Transfer checks deliberately cover coordinates above the inflection 1/2.
    for d in range(3, 12):
        for _ in range(8000):
            weights = [rng.expovariate(1) for _ in range(d)]
            s = sum(weights)
            p = [t/s for t in weights]
            i = max(range(d), key=p.__getitem__)
            j = min(range(d), key=p.__getitem__)
            before = predicted([sqrt(x) for x in p])
            delta = (p[i]-p[j])*rng.uniform(.025, .475)
            p[i] -= delta
            p[j] += delta
            after = predicted([sqrt(x) for x in p])
            assert after > before - 1e-12, (d, before, after)

    # Near-cube quadratic coefficient from the actual second derivative.
    for d in (4, 5, 9):
        uniform = [1/d]*d
        eps = 1e-4
        moved = uniform.copy()
        moved[0] += eps
        moved[1] -= eps
        f0 = sum(asin(sqrt(t)) for t in uniform)
        f1 = sum(asin(sqrt(t)) for t in moved)
        c = (d-2)*d*d/(8*(d-1)**1.5)
        approximate = c*2*eps*eps
        assert abs((f0-f1)/approximate - 1.) < 2e-6

    print('VERIFY_OK')
    print('counted_example_means', measured)
    print('transfer_trials', 9*8000)
    print('local_Hessian_checks', (4, 5, 9))

if __name__ == '__main__':
    run()
