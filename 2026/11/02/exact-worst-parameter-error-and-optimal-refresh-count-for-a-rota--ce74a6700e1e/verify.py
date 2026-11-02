"""Independent finite checks for rotating two-mode randomized range approximation.

Run: python verify.py
All formula claims for arbitrary dimensions/parameters require the analytic proof.
"""
import math

N_CHECKS = 0


def check(condition, message):
    global N_CHECKS
    N_CHECKS += 1
    if not condition:
        raise AssertionError(message)


def close(a, b, tolerance=2e-10):
    return abs(a - b) <= tolerance * max(1.0, abs(a), abs(b))


def matrix_error_ratio(eps, theta, phi, radial=1.0):
    c, s = math.cos(theta), math.sin(theta)
    a00, a01, a11 = c * c + eps * s * s, (1.0 - eps) * c * s, s * s + eps * c * c
    x, y = radial * math.cos(phi), radial * math.sin(phi)
    v0, v1 = a00 * x + a01 * y, a01 * x + a11 * y
    d = v0 * v0 + v1 * v1
    u0, u1 = v0 / math.sqrt(d), v1 / math.sqrt(d)
    z0, z1 = u0 * a00 + u1 * a01, u0 * a01 + u1 * a11
    b00, b01, b10, b11 = a00 - u0 * z0, a01 - u0 * z1, a01 - u1 * z0, a11 - u1 * z1
    return (b00 * b00 + b01 * b01 + b10 * b10 + b11 * b11) / (eps * eps)


def exact_pointwise(eps, theta, phi):
    return 1 / (math.cos(phi - theta)**2 + eps**2 * math.sin(phi - theta)**2)


def q_of(eps, threshold):
    if threshold <= 1:
        return 0.0
    if threshold >= eps**-2:
        return 1.0
    delta = math.sqrt((1 / threshold - eps * eps) / (1 - eps * eps))
    return 2 * math.acos(delta) / math.pi


def cdf(eps, sweep, threshold):
    if threshold < 1:
        return 0.0
    if threshold >= eps**-2:
        return 1.0
    return max(0.0, q_of(eps, threshold) - sweep / math.pi)


def angular_distance(sweep, phi):
    if sweep >= math.pi:
        return 0.0
    d = (phi - math.pi / 2) % math.pi
    return 0.0 if d <= sweep else min(d - sweep, math.pi - d)


def worst_ratio(eps, sweep, phi):
    d = angular_distance(sweep, phi)
    return 1 / (eps**2 + (1 - eps**2) * math.sin(d)**2)


def mean_formula(eps, sweep):
    if sweep >= math.pi:
        return eps**-2
    if sweep <= 0:
        return eps**-1
    return sweep / (math.pi * eps**2) + 2 / (math.pi * eps) * math.atan(math.tan((math.pi - sweep) / 2) / eps)


def positive_branch_z(q):
    lo, hi = 1.0, 2.0
    def h(z):
        return z - 1 - math.log(z / q)
    while h(hi) < 0:
        hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if h(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def best_integer_k(q, t):
    z = positive_branch_z(q)
    real_k = t * z / (q * (z - 1))
    candidates = [max(1, int(math.floor(real_k))), max(1, int(math.ceil(real_k)))]
    def log_prob(k):
        return k * math.log(q - t / k) if k > t / q else -math.inf
    return max(candidates, key=log_prob), real_k


def run():
    # Direct matrix construction versus the eigen-coordinate formula.
    for eps in (0.0125, 0.1, 0.3, 0.75, 0.97):
        for j in range(80):
            theta = (j + 0.31) * 0.067
            for k in range(30):
                phi = (k + 0.71) * 0.111
                got = matrix_error_ratio(eps, theta, phi)
                expected = exact_pointwise(eps, theta, phi)
                check(close(got, expected, 1e-9), (eps, theta, phi, got, expected))
                check(close(matrix_error_ratio(eps, theta, phi, 7.0), got, 1e-9), 'radial invariance')

    # Direct finite angle scan of matrix residual as a separate supremum sanity check.
    for eps in (0.1, 0.35, 0.8):
        for sweep in (0.02, 0.3, 1.3, 2.8, math.pi, 4.1):
            for j in range(27):
                phi = (j + 0.33) * math.pi / 27
                scan = max(matrix_error_ratio(eps, sweep * k / 1200, phi)
                           for k in range(1201))
                exact = worst_ratio(eps, sweep, phi)
                check(-1e-9 <= exact - scan <= 0.0045 * max(1.0, exact),
                      (eps, sweep, phi, scan, exact))

    # Exact uniform-angle CDF and expectation against independent deterministic quadrature.
    count = 80000
    for eps in (0.08, 0.2, 0.6):
        for sweep in (0.0, 0.13, 0.49, 1.21, 2.44, math.pi, 4.2):
            samples = [worst_ratio(eps, sweep, (j + 0.5) * math.pi / count) for j in range(count)]
            actual_mean = sum(samples) / count
            check(close(actual_mean, mean_formula(eps, sweep), 2e-5), (eps, sweep, actual_mean, mean_formula(eps, sweep)))
            for threshold in (1.1, 1.5, 2.5, 5.0, eps**-2 * 0.95):
                if threshold >= eps**-2:
                    continue
                empirical = sum(x <= threshold for x in samples) / count
                predicted = cdf(eps, sweep, threshold)
                check(abs(empirical - predicted) < 5e-5, (eps, sweep, threshold, empirical, predicted))
            check(cdf(eps, sweep, eps**-2) == 1.0, 'endpoint atom')
            check(cdf(eps, sweep, 0.9) == 0.0, 'below optimum')

    # Shape and partition optimality: finite random-like deterministic cuts.
    for q in (0.06, 0.25, 0.48, 0.71, 0.93, 0.998):
        for sweep_norm in (0.001, 0.15, 0.6, 1.25, 3.1, 8.0):
            for k in (1, 2, 3, 6, 10):
                equal = max(0, q - sweep_norm / k) ** k
                for j in range(1, 51):
                    weights = [1.0 + abs(math.sin((j + 0.23) * (idx + 1.29))) for idx in range(k)]
                    total = sum(weights)
                    product = 1.0
                    for weight in weights:
                        product *= max(0, q - sweep_norm * weight / total)
                    check(product <= equal + 1e-12, (q, sweep_norm, k, product, equal))

    # Unique continuous maximum and integer maximizers; tails at k -> infinity.
    for q in (0.03, 0.1, 0.35, 0.68, 0.9, 0.995):
        z = positive_branch_z(q)
        check(z > 1 and close(z * math.exp(1 - z), q, 1e-9), 'Lambert branch root')
        for t in (0.001, 0.1, 0.4, 1, 3, 8):
            optimum, kc = best_integer_k(q, t)
            def log_prob(k):
                return k * math.log(q - t / k) if k > t / q else -math.inf
            compare = max(range(1, min(5000, max(100, int(2 * kc + 5)))), key=log_prob)
            check(optimum == compare, (q, t, optimum, compare, kc))
            check(close(kc, t * z / (q * (z - 1)), 1e-12), 'continuous optimum')
            check(log_prob(optimum) > -math.inf, 'positive optimal success')

    # Sharp one-versus-two equal-segment crossover for nonzero single-segment success.
    for q in (0.05, 0.2, 0.55, 0.8, 0.99):
        t0 = 2 * (math.sqrt(1 - q) - (1 - q))
        check(0 < t0 < q, 'crossover feasible')
        for t in (t0 * .9, t0, min(q * .999, t0 * 1.1)):
            p1 = max(0, q - t)
            p2 = max(0, q - t / 2)**2
            direction = t - t0
            check((p2 - p1) * direction >= -1e-12, (q, t, p1, p2))

    print('PASS', N_CHECKS, 'individually evaluated assertions')


if __name__ == '__main__':
    run()
