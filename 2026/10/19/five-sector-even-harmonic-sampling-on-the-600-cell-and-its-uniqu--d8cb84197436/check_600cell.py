"""Independent exact group, character and numerical Gram checks for 600-cell sampling.

Run: python check_600cell.py. Requires NumPy for the numerical matrix check.
"""
from collections import Counter
from itertools import permutations, product
from math import sqrt
import numpy as np

ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
PHI_PRIME = (1, -1)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def mul(a, b):
    # (a+b phi)(c+d phi), with phi^2 = phi + 1.
    return (a[0] * b[0] + a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def scale(n, a):
    return (n * a[0], n * a[1])


def sum_pairs(v):
    z = ZERO
    for a in v:
        z = add(z, a)
    return z


def exact_quaternion_mul(q, r):
    # Each coordinate is represented by (a+b phi)/2.
    a, b, c, d = q
    e, f, g, h = r
    terms = [
        [mul(a, e), neg(mul(b, f)), neg(mul(c, g)), neg(mul(d, h))],
        [mul(a, f), mul(b, e), mul(c, h), neg(mul(d, g))],
        [mul(a, g), neg(mul(b, h)), mul(c, e), mul(d, f)],
        [mul(a, h), mul(b, g), neg(mul(c, f)), mul(d, e)],
    ]
    out = []
    for part in terms:
        s = sum_pairs(part)
        assert s[0] % 2 == 0 and s[1] % 2 == 0
        out.append((s[0] // 2, s[1] // 2))
    return tuple(out)


def norm_numerator(q):
    return sum_pairs(mul(z, z) for z in q)


def icosians():
    q = []
    for i in range(4):
        for sign in (-1, 1):
            v = [ZERO] * 4
            v[i] = (2 * sign, 0)
            q.append(tuple(v))
    for signs in product((-1, 1), repeat=4):
        q.append(tuple((t, 0) for t in signs))
    for p in permutations(range(4)):
        if sum(p[i] > p[j] for i in range(4)
               for j in range(i + 1, 4)) % 2:
            continue
        for a, b, c in product((-1, 1), repeat=3):
            base = [ZERO, (a, 0), (-b, b), (0, c)]
            q.append(tuple(base[j] for j in p))
    return q


def decimal_pair(p):
    return (p[0] + p[1] * (1 + sqrt(5)) / 2) / 2


CLASS_SIZES = (1, 15, 20, 12, 12)
REPS = [
    (ONE, ONE, ONE, ONE, ONE),
    (scale(3, ONE), neg(ONE), ZERO, PHI, PHI_PRIME),
    (scale(3, ONE), neg(ONE), ZERO, PHI_PRIME, PHI),
    (scale(4, ONE), ZERO, ONE, neg(ONE), neg(ONE)),
    (scale(5, ONE), ONE, neg(ONE), ZERO, ZERO),
]
DIMS = [1, 3, 3, 4, 5]
RANKS = [1, 9, 25, 25, 41, 43, 51, 59, 50, 59, 60, 59, 60, 59, 59,
         60, 60, 59, 60, 59, 60, 60, 60, 59, 60, 60, 60, 60, 60, 59]


def classes(degree):
    assert degree >= 0 and degree % 2 == 0
    k = degree // 2
    v2 = [ONE, neg(ONE)][k % 2]
    v3 = [ONE, ZERO, neg(ONE)][k % 3]
    v5a = [ONE, PHI, ZERO, neg(PHI), neg(ONE)][k % 5]
    v5b = [ONE, PHI_PRIME, ZERO, neg(PHI_PRIME), neg(ONE)][k % 5]
    return (scale(degree + 1, ONE), v2, v3, v5a, v5b)


def multiplicities(degree):
    c = classes(degree)
    result = []
    for chi in REPS:
        z = sum_pairs(scale(CLASS_SIZES[j], mul(c[j], chi[j])) for j in range(5))
        assert z[1] == 0, (degree, z)
        assert z[0] % 60 == 0, (degree, z)
        result.append(z[0] // 60)
    return result


def theoretical_spectrum(degree):
    m = multiplicities(degree)
    spectrum = []
    for d, a in zip(DIMS, m):
        spectrum.extend([60 * (degree + 1) * a / d] * d ** 2)
    return np.array(sorted(spectrum), dtype=float)


def direct_gram(x, degree):
    s = np.clip(x @ x.T, -1.0, 1.0)
    if degree == 0:
        u = np.ones_like(s)
    else:
        u0 = np.ones_like(s)
        u1 = 2 * s
        for j in range(2, degree + 1):
            u0, u1 = u1, 2 * s * u1 - u0
        u = u1
    return (degree + 1) * u


def main():
    checks = 0
    roots = icosians()
    assert len(roots) == len(set(roots)) == 120
    for q in roots:
        assert norm_numerator(q) == (4, 0)
        checks += 1
    root_set = set(roots)
    for q in roots:
        assert tuple(neg(v) for v in q) in root_set
        for r in roots:
            assert exact_quaternion_mul(q, r) in root_set
            checks += 1
    selected = []
    for q in roots:
        first = next(z for z in q if z != ZERO)
        if decimal_pair(first) > 0:
            selected.append(q)
    assert len(selected) == len(set(selected)) == 60
    expected_abs = {(4, 0): 1, (0, 0): 15, (2, 0): 20,
                    (-2, 2): 12, (0, 2): 12}
    for q in selected:
        c = Counter()
        for r in selected:
            dot = sum_pairs(mul(a, b) for a, b in zip(q, r))
            if dot not in expected_abs:
                dot = neg(dot)
            assert dot in expected_abs
            c[dot] += 1
            checks += 1
        assert c == expected_abs, c
    for i, a in enumerate(REPS):
        for j, b in enumerate(REPS):
            z = sum_pairs(scale(CLASS_SIZES[k], mul(a[k], b[k]))
                          for k in range(5))
            assert z == (60 * int(i == j), 0)
            checks += 1
    for degree in range(0, 60, 2):
        m = multiplicities(degree)
        assert min(m) >= 0
        assert sum(d * a for d, a in zip(DIMS, m)) == degree + 1
        rank = sum(d * d for d, a in zip(DIMS, m) if a > 0)
        assert rank == RANKS[degree // 2], (degree, rank)
        assert multiplicities(degree + 60) == [a + d for a, d in zip(m, DIMS)]
        checks += 5
    assert next((i * 2 for i, rank in enumerate(RANKS) if rank == 60)) == 20
    assert RANKS[11] == 59 and RANKS[-1] == 59
    assert all(v > 0 for v in multiplicities(60))
    tight_59 = []
    for degree in range(0, 60, 2):
        m = multiplicities(degree)
        if sum(d * d for d, a in zip(DIMS, m) if a > 0) == 59:
            if len(set((m[j] * DIMS[1]) // DIMS[j]
                       for j in range(1, 5) if m[j] * DIMS[1] % DIMS[j] == 0)) == 1 \
                       and all(m[j] * DIMS[1] % DIMS[j] == 0 for j in range(1, 5)):
                tight_59.append(degree)
    assert tight_59 == [58], tight_59
    assert classes(58)[1:] == (neg(ONE),) * 4

    x = np.array([[decimal_pair(v) for v in q] for q in selected], dtype=float)
    assert np.max(np.abs(np.sum(x * x, axis=1) - 1)) < 1e-13
    for degree in range(0, 62, 2):
        g = direct_gram(x, degree)
        ev = np.sort(np.linalg.eigvalsh(g))
        expected = theoretical_spectrum(degree)
        assert np.allclose(ev, expected, rtol=1e-10, atol=2e-7), (
            degree, float(np.max(np.abs(ev - expected))))
        checks += 60
        if degree == 58:
            j = np.ones((60, 60))
            assert np.max(np.abs(g - 3540 * (np.eye(60) - j / 60))) < 1e-8
        if degree == 20:
            y = np.array([(j ** 2 + 3 * j + 1) / 37 for j in range(60)])
            z = np.linalg.solve(g, y)
            assert np.max(np.abs(g @ z - y)) < 1e-9
    print(f'PASS: {checks} exact structural and numerical spectral assertions, '
          '60 quaternion lines, even degrees 0..60, and analytic period identity.')


if __name__ == '__main__':
    main()
