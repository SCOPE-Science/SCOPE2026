"""Deterministic numerical checks for an exact planar Cauchy quadrature theorem.

The theorem itself is analytic; these tests validate normalization,
finite sample geometry, and the sharp exponent construction.
"""
import math
import random

PI = math.pi


def support(theta, weights, angle):
    return sum(w * abs(math.cos(angle - t)) for t, w in zip(theta, weights))


def extrema(theta, weights):
    """Exact extremal directions up to floating arithmetic: facet normals/vertices."""
    normals = sorted(((t + PI / 2) % PI) for t in theta)
    if len({round(q, 10) for q in normals}) != len(normals):
        raise ValueError("direction collisions")
    all_normals = sorted(normals + [t + PI for t in normals])
    minimum = min(support(theta, weights, a) for a in all_normals)
    outer = 0.0
    for i, a in enumerate(all_normals):
        b = all_normals[(i + 1) % len(all_normals)]
        if i == len(all_normals) - 1:
            b += 2 * PI
        middle = (a + b) / 2
        vx = sum(w * (1 if math.cos(middle - t) > 0 else -1) * math.cos(t)
                 for t, w in zip(theta, weights))
        vy = sum(w * (1 if math.cos(middle - t) > 0 else -1) * math.sin(t)
                 for t, w in zip(theta, weights))
        outer = max(outer, math.hypot(vx, vy))
    gaps = [all_normals[i+1]-all_normals[i] for i in range(len(all_normals)-1)]
    gaps += [all_normals[0] + 2*PI - all_normals[-1]]
    return minimum, outer, gaps


def optimum(n):
    x = PI / (2*n)
    r = 1 / (n * math.tan(x))
    return (2/PI-r)/2, r, x


def error(theta, weights):
    rr, large, gaps = extrema(theta, weights)
    return max(2/PI-rr, large-2/PI)/2, rr, large, gaps


def perturb_tangent(n, t):
    base = PI / n
    gaps = [base] * (2*n)
    for i, s in ((0, 1), (1, -1), (n, 1), (n+1, -1)):
        gaps[i] += s*t
    alpha = [0.0]
    for gap in gaps[:-1]:
        alpha.append(alpha[-1]+gap)
    radius = 2 / sum(math.tan(gap/2) for gap in gaps)
    edge_lengths = [radius * (math.tan(gaps[i-1]/2)+math.tan(gaps[i]/2)) for i in range(2*n)]
    theta = [alpha[i]+PI/2 for i in range(n)]
    weights = [edge_lengths[i]/2 for i in range(n)]
    assert abs(sum(weights)-1)<1e-12
    return theta, weights, gaps, radius


def main():
    rng = random.Random(107)
    count = 0
    for n in range(2, 31):
        theta = [j*PI/n for j in range(n)]
        weights = [1/n]*n
        e, r, large, gaps = error(theta, weights)
        best, ideal_r, x = optimum(n)
        assert abs(e-best) < 4e-13, (n, e, best)
        assert abs(r-ideal_r) < 4e-13
        assert abs(large-1/(n*math.sin(x))) < 4e-13
        assert max(abs(g-PI/n) for g in gaps) < 3e-13
        count += 1

        for _ in range(100):
            theta = [j*PI/n + rng.uniform(-0.002,0.002) for j in range(n)]
            pre_weights = [1+rng.uniform(-0.15,0.15) for _ in range(n)]
            weights = [z/sum(pre_weights) for z in pre_weights]
            e, radius, outer, gaps = error(theta, weights)
            assert e + 1e-12 >= best, (n, e, best)
            if e-best <= ideal_r/4:
                angular_variance = sum((g-PI/n)**2 for g in gaps)
                upper = 48*(e-best)/(x*ideal_r**2)
                assert angular_variance <= upper + 1e-11, (n, angular_variance, upper)
            count += 1

    # The tangent family witnesses the necessity of the square-root stability exponent.
    for n in (2,3,5,9,16):
        x = PI/(2*n)
        ideal_e, ideal_r, _ = optimum(n)
        previous = None
        for t in (0.005, 0.002, 0.001):
            theta, weights, prescribed_gaps, analytic_radius = perturb_tangent(n,t)
            e, r, _, measured_gaps = error(theta,weights)
            assert abs(r-analytic_radius) < 1e-12
            assert abs(e-ideal_e - (ideal_r-r)/2) < 2e-12
            assert abs(sum((g-PI/n)**2 for g in measured_gaps)-4*t*t)<3e-12
            predicted_delta = ideal_r**2 * (2*math.tan(x)/(math.cos(x)**2)) * t*t / 8
            observed_delta=e-ideal_e
            assert abs(observed_delta/predicted_delta-1)<0.002, (n,t,observed_delta,predicted_delta)
            if previous is not None:
                assert observed_delta < previous
            previous=observed_delta
            count += 1
    print(f"VERIFY_OK {count} normalizations, sample perturbations, and sharpness checks")


if __name__ == '__main__':
    main()
