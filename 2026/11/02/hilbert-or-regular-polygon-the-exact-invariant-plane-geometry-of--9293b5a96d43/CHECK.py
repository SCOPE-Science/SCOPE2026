"""Finite numerical checks of the angular formula for invariant Lipschitz planes.

These checks supplement, but do not replace, the infinite-dimensional
classification and ellipsoid lower bound proved analytically.
"""
import math


def run():
    passed = 0
    for p, q in [(1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                 (1, 8), (2, 9), (2, 11), (3, 14)]:
        theta = 2 * math.pi * p / q
        N = q if q % 2 == 0 else 2 * q
        phases = [theta * (j + 0.5) for j in range(q)]
        exact_min = math.cos(math.pi / N)
        sample = [max(abs(math.cos(t - phase)) for phase in phases)
                  for t in (math.pi * j / 4096 for j in range(4096))]
        observed_min = min(sample)
        assert exact_min - 1e-9 <= observed_min <= exact_min + .0004
        passed += 1
        assert abs(1 / exact_min - 1 / math.cos(math.pi / N)) < 1e-12
        passed += 1
        for a, b in [(1., 0.), (0., 1.), (.25, -.75), (1.25, .4)]:
            norm_by_difference = max(abs(
                a * (math.cos((j + 1) * theta) - math.cos(j * theta)) +
                b * (math.sin((j + 1) * theta) - math.sin(j * theta)))
                for j in range(q))
            norm_by_phase = 2 * math.sin(theta / 2) * max(abs(
                -a * math.sin(phase) + b * math.cos(phase))
                for phase in phases)
            assert abs(norm_by_difference - norm_by_phase) < 1e-10
            passed += 1
    assert passed == 54, passed
    print(f"{passed} finite comparisons passed; infinite claims follow from the proof.")


if __name__ == '__main__':
    run()
