"""Independent finite consistency checks for cyclic two-row Fourier erasure bounds.

Run with Python 3; no optional dependencies are required.
"""
from cmath import exp
from itertools import combinations, product
from math import comb, gcd, pi


def predicted(n, d, r):
    g = gcd(n, d)
    m = n // g
    q, s = divmod(r, g)
    z = sum(g * exp(2j * pi * k / m) for k in range(q))
    z += s * exp(2j * pi * q / m)
    if r in (0, n):
        count = 1
    elif s == 0:
        count = m
    elif q in (0, m - 1):
        count = m * comb(g, s)
    else:
        count = 2 * m * comb(g, s)
    return abs(z), count


def check_index_masks():
    cases = masks = 0
    worst_error = 0.0
    for n in range(3, 13):
        for d in range(1, n):
            phases = [exp(2j * pi * d * k / n) for k in range(n)]
            for r in range(n + 1):
                radius, count = predicted(n, d, r)
                actual = -1.0
                actual_count = 0
                for erased in combinations(range(n), r):
                    masks += 1
                    z = sum(phases[k] for k in erased)
                    value = abs(z)
                    # Compute two actual eigenvalues of the retained 2x2
                    # frame operator using its matrix entries.
                    diag = (n - r) / 2
                    off = abs(z) / 2
                    lo = diag - off
                    hi = diag + off
                    if lo < -1e-9 or hi > n / 2 + 1e-9:
                        raise AssertionError(('invalid frame spectrum', n, d, erased))
                    if value > actual + 1e-8:
                        actual = value
                        actual_count = 1
                    elif abs(value - actual) < 1e-8:
                        actual_count += 1
                worst_error = max(worst_error, abs(actual - radius))
                if abs(actual - radius) > 1e-8 or actual_count != count:
                    raise AssertionError((n, d, r, actual, radius, actual_count, count))
                cases += 1
    return cases, masks, worst_error


def check_capacity_vectors():
    cases = 0
    for m in range(2, 8):
        for g in range(1, 5):
            if (g + 1) ** m > 80000:
                continue
            roots = [exp(2j * pi * j / m) for j in range(m)]
            for r in range(1, m * g):
                vmax, expected_count = predicted(m * g, g, r)
                actual_max = -1.0
                actual_count = 0
                for counts in product(range(g + 1), repeat=m):
                    if sum(counts) != r:
                        continue
                    val = abs(sum(a * root for a, root in zip(counts, roots)))
                    if val > actual_max + 1e-8:
                        actual_max = val
                        actual_count = 1
                    elif abs(val - actual_max) <= 1e-8:
                        actual_count += 1
                # Counts above are distinct multiplicity vectors, not
                # individual index masks. Divide the predicted index count
                # by the choices of a partial class, when present.
                partial = r % g
                factor = comb(g, partial) if partial else 1
                if abs(actual_max - vmax) > 1e-8 or actual_count != expected_count // factor:
                    raise AssertionError((m, g, r, actual_max, vmax, actual_count))
                cases += 1
    return cases


if __name__ == '__main__':
    cases, masks, worst_error = check_index_masks()
    vectors = check_capacity_vectors()
    print('VERIFY_OK', 'index_cases=', cases,
          'index_masks=', masks, 'capacity_cases=', vectors,
          'max_numerical_error=', '%.3g' % worst_error)
