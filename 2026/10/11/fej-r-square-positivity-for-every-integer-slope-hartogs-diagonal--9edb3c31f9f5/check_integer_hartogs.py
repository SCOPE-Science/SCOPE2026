"""Exact finite cross-checks of two independent integer formulas.

This is a reproducibility check, not the proof for the infinite family.
Only Python's standard library is required.
"""


def add(terms, degree, coefficient):
    terms[degree] = terms.get(degree, 0) + coefficient


def from_primary_formula(m):
    # Edholm--Mathew (2026), Theorem 1.3, (1.4), specialized to n=1.
    d = m - 1
    terms = {d: m * m}
    for j in range(m - 1):
        kappa = j
        add(terms, j, (j + 1) * (kappa + 1))
        add(terms, j + 1, (j + 1) * (m - kappa - 1))
        add(terms, j + d, (m - j - 1) * (kappa + 1))
        add(terms, j + d + 1, (m - j - 1) * (m - kappa - 1))
    return [terms.get(k, 0) for k in range(2 * d + 1)]


def closed_coefficient_formula(m):
    d = m - 1
    return [1 + (d + 3) * min(k, 2 * d - k)
            if k != d else d * d + 4 * d + 1
            for k in range(2 * d + 1)]


def from_fejer_square(m):
    d = m - 1
    # Coefficient of s^(d+j) in s^d [d+(d+2)F_d+F_(d+1)];
    # F_k(e^{it}) = |1+...+e^{i(k-1)t}|^2.
    return [d * (k == d)
            + (d + 2) * max(d - abs(k - d), 0)
            + max(d + 1 - abs(k - d), 0)
            for k in range(2 * d + 1)]


def from_edholm_2016(m):
    p, q = {}, {}
    for ell in range(1, m):
        add(p, ell - 1, ell * (m - ell))
    for ell in range(1, m + 1):
        add(q, ell - 1, ell * ell)
        add(q, m + ell - 1, (m - ell) * (m - ell))
    result = {}
    # N(s,t) = p(s)t^2 + q(s)t + s^m p(s), t=s;
    # Q(s) = s^(-1) N(s,s).
    for exponent, coefficient in p.items():
        add(result, exponent + 1, coefficient)
        add(result, exponent + m - 1, coefficient)
    for exponent, coefficient in q.items():
        add(result, exponent, coefficient)
    return [result.get(k, 0) for k in range(2 * m - 1)]


def run():
    for m in range(2, 502):
        a = from_primary_formula(m)
        b = from_edholm_2016(m)
        c = closed_coefficient_formula(m)
        d = from_fejer_square(m)
        assert a == b == c == d, (m, a, b, c, d)
        assert len(a) == 2 * (m - 1) + 1
        assert a[0] == a[-1] == 1
        assert a == list(reversed(a))
    print('CHECK_OK: Edholm--Mathew and Edholm formulas match the closed coefficient form')
    print('CHECK_OK: independent Fourier/Fejer-square coefficient identity for every m=2..501')
    print('CHECK_OK: degrees, nonzero constants, reciprocal symmetry in all 500 checks')
    print('Infinite assertion is established by the coefficient argument in RESULT.md, not by this finite check.')


if __name__ == '__main__':
    run()
