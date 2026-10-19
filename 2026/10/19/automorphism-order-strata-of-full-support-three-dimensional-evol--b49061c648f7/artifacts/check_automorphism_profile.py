#!/usr/bin/env python3
"""Independent finite-field census for full-support 3D evolution-algebra symmetry strata.

Run: python3 artifacts/check_automorphism_profile.py
No nonstandard packages required. All matrices and stabilizers are enumerated.
"""
from collections import Counter
from itertools import permutations, product


def finite_field(q):
    """Arithmetic in F_2, F_3, F_4, F_5, F_7, F_8 or F_9."""
    if q in (2, 3, 5, 7):
        return lambda a, b: (a + b) % q, lambda a, b: (a * b) % q
    # Ascending coefficients of irreducible monic polynomials.
    p, degree, modulus = {4: (2, 2, [1, 1, 1]),
                          8: (2, 3, [1, 1, 0, 1]),
                          9: (3, 2, [1, 0, 1])}[q]

    def digits(a):
        return [(a // p**i) % p for i in range(degree)]

    def add(a, b):
        da, db = digits(a), digits(b)
        return sum(((da[i] + db[i]) % p) * p**i for i in range(degree))

    def mul(a, b):
        da, db = digits(a), digits(b)
        v = [0] * (2 * degree - 1)
        for i in range(degree):
            for j in range(degree):
                v[i + j] = (v[i + j] + da[i] * db[j]) % p
        for k in range(len(v) - 1, degree - 1, -1):
            coeff = v[k]
            for j in range(degree):
                v[k - degree + j] = (v[k - degree + j] - coeff * modulus[j]) % p
        return sum(v[i] * p**i for i in range(degree))

    return add, mul


def predicted(q):
    d = 3 * (q-1)**3 * (q-2)**2 \
        + (q-1)**2 * (q-2) * (q-3) * (q*q - 3*q + 3)
    t = ((q-2) * (q-1)**2 if q % 2 == 0
         else (q-1) * (q*q - 4*q + 5))
    if q % 3 == 0:
        e = q*q - 3*q + 3
    elif q % 3 == 1:
        e = q*q - 5*q + 10
    else:
        e = (q-1) * (q-2)
    s = q - 2 - (1 if (q % 2 and q % 3) else 0)
    return {1: d - 3*t - e + 3*s, 2: 3 * (t-s), 3: e-s, 6: s}


def exhaustive(q):
    add, mul = finite_field(q)
    negatives = {a: next(b for b in range(q) if add(a, b) == 0)
                 for a in range(q)}

    def sub(a, b):
        return add(a, negatives[b])

    def det(m):
        positive = add(add(1, mul(m[0][1], mul(m[1][2], m[2][0]))),
                       mul(m[0][2], mul(m[1][0], m[2][1])))
        negative = add(add(mul(m[0][1], m[1][0]),
                           mul(m[0][2], m[2][0])),
                       mul(m[1][2], m[2][1]))
        return sub(positive, negative)

    group = tuple(permutations(range(3)))
    counts = Counter()
    for a, b, c, d, e, f in product(range(1, q), repeat=6):
        m = ((1, a, b), (c, 1, d), (e, f, 1))
        if det(m) == 0:
            continue
        stabilizer = sum(all(m[pi[i]][pi[j]] == m[i][j]
                             for i in range(3) for j in range(3))
                         for pi in group)
        counts[stabilizer] += 1
    observed = {k: counts[k] for k in (1, 2, 3, 6)}
    expected = predicted(q)
    assert observed == expected, (q, observed, expected)
    assert all(observed[k] * k % 6 == 0 for k in (1, 2, 3, 6))
    classes = {k: observed[k] * k // 6 for k in (1, 2, 3, 6)}
    print('q=%s, normalized labeled=%s, orders=%s, classes=%s'
          % (q, sum(observed.values()), observed, classes))


if __name__ == '__main__':
    for q in (2, 3, 4, 5, 7, 8, 9):
        exhaustive(q)
    print('ALL_EXACT_CHECKS_PASSED 7 finite fields')
