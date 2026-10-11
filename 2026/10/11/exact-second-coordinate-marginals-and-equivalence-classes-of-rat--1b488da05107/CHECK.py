"""Finite reproducibility probes for inverse-branch trace identities.

No finite sample substitutes for the all-parameter Vieta proof in RESULT.md.
This script uses only the Python standard library.
"""


def phi(t, a, b, poles, residues):
    return a * t + b + sum(r / (p - t) for p, r in zip(poles, residues))


def derivative(t, a, poles, residues):
    return a + sum(r / (p - t) ** 2 for p, r in zip(poles, residues))


def preimages(s, a, b, poles, residues):
    sorted_poles = sorted(poles)
    intervals = [(-1e6, sorted_poles[0] - 1e-8)]
    intervals += [(u + 1e-8, v - 1e-8) for u, v in zip(sorted_poles, sorted_poles[1:])]
    intervals += [(sorted_poles[-1] + 1e-8, 1e6)]
    found = []
    for low, high in intervals:
        fl = phi(low, a, b, poles, residues) - s
        fh = phi(high, a, b, poles, residues) - s
        if fl * fh >= 0:
            continue
        for _ in range(75):
            mid = (low + high) / 2
            fm = phi(mid, a, b, poles, residues) - s
            if fm < 0:
                low = mid
            else:
                high = mid
        found.append((low + high) / 2)
    return found


def run():
    poles = [-1.0, 2.0]
    residues = [2.0, 0.6]
    b = 0.4
    for a in [0.0, 0.3, 2.0]:
        for s in [-8.0, -1.0, 0.0, 0.7, 6.0]:
            roots = preimages(s, a, b, poles, residues)
            expected_count = len(poles) + (1 if a > 0 else 0)
            assert len(roots) == expected_count, (a, s, roots)
            trace = sum(1.0 / derivative(t, a, poles, residues) for t in roots)
            expected = 1.0 / a if a > 0 else sum(residues) / (b - s) ** 2
            assert abs(trace - expected) <= 1e-8 * (1.0 + abs(expected)), (
                a, s, trace, expected
            )
    print('PASS: 15 nonexceptional inverse-branch trace comparisons')
    # Separate finite-difference check of the graph-weight Jacobian cancellation.
    for a in [0.0, 0.3, 2.0]:
        for t in [-3.0, -0.2, 0.5, 3.0]:
            v = phi(t, a, b, poles, residues)
            d = (v * v + 4.0) ** 0.5
            for sign in [-1.0, 1.0]:
                g = (-v + sign * d) / 2.0
                weight = g * g / (1.0 + g * g)
                h = 1e-5
                vp = phi(t + h, a, b, poles, residues)
                vm = phi(t - h, a, b, poles, residues)
                gp = (-vp + sign * (vp * vp + 4.0) ** 0.5) / 2.0
                gm = (-vm + sign * (vm * vm + 4.0) ** 0.5) / 2.0
                slope = abs((gp - gm) / (2.0 * h))
                expected = 1.0 / derivative(t, a, poles, residues)
                assert abs(weight / slope - expected) < 5e-8 * (1 + abs(expected))
    print('PASS: 24 finite-difference graph-Jacobian comparisons')



if __name__ == '__main__':
    run()
