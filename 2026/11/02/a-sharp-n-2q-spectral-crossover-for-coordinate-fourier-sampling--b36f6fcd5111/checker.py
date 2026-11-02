"""Independent finite checks of additive-character restriction spectra on GL(n,q).

Run with Python 3 and NumPy. Prime-field and GF(4) arithmetic are implemented
explicitly; no external data files are needed. Numerical checks do not prove
statements quantified over arbitrary finite fields or dimensions.
"""
from itertools import product
from math import hypot, pi, sqrt
import numpy as np


def theoretical_levels(q, n):
    r = q - 1
    u = 1.0 / (q**n - 1)
    t = 1.0 / (q**(n - 1) - 1)
    v = u * t
    A = 1 + u
    R = A - r * (n - 1) * (u + v)
    I = A + r * (u + v)
    T = A + r * (-(2*n - 1)*u + (n - 1)**2 * v)
    C = -n * sqrt(r) * u
    minus = (1 + T - hypot(1 - T, 2*C)) / 2
    plus = (1 + T + hypot(1 - T, 2*C)) / 2
    values = ([A] * (n*n*(q-2)) + [R] * (2*(n-1)) +
              [I] * ((n-1)**2) + [minus, plus])
    return sorted(values), (minus, plus, A, R, I, T, C)


def field_mul(a, b, q):
    if q != 4:
        return a*b % q
    # F_4 = F_2[alpha]/(alpha^2+alpha+1).
    p = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                p ^= (1 << (i+j))
    if p & 4:
        p ^= 7  # alpha^2=alpha+1
    return p


def field_add(a, b, q):
    return (a ^ b) if q == 4 else (a+b) % q


def field_nonzero(q, n, flat):
    M = [list(flat[n*i:n*(i+1)]) for i in range(n)]
    pivots = 0
    for col in range(n):
        where = next((i for i in range(pivots, n) if M[i][col]), None)
        if where is None:
            continue
        M[where], M[pivots] = M[pivots], M[where]
        inverse = next(a for a in range(1, q) if field_mul(M[pivots][col], a, q) == 1)
        M[pivots] = [field_mul(inverse, x, q) for x in M[pivots]]
        for row in range(pivots+1, n):
            factor = M[row][col]
            if factor:
                M[row] = [field_add(M[row][j], field_mul(factor, M[pivots][j], q), q)
                          for j in range(n)] if q == 4 else [
                    (M[row][j] - factor*M[pivots][j]) % q for j in range(n)]
        pivots += 1
        if pivots == n:
            return True
    return False


def character(a, q):
    if q == 4:
        # Tr(0)=Tr(1)=0; Tr(alpha)=Tr(alpha+1)=1.
        return 1.0 if a in (0, 1) else -1.0
    return np.exp(2j*pi*a/q)


def check_direct(q, n):
    points = [vec for vec in product(range(q), repeat=n*n) if field_nonzero(q, n, vec)]
    freq = [(i, a) for i in range(n*n) for a in range(1, q)]
    E = np.empty((len(points), 1+len(freq)), dtype=complex)
    E[:, 0] = 1
    for x, M in enumerate(points):
        for k, (i, a) in enumerate(freq, 1):
            E[x, k] = character(field_mul(M[i], a, q), q)
    G = E.conj().T @ E / len(points)
    actual = np.linalg.eigvalsh(G)
    predicted, values = theoretical_levels(q, n)
    error = float(np.max(np.abs(actual - predicted)))
    assert error < 2e-12, (q, n, error)
    count = 1
    for i in range(n):
        count *= (q**n - q**i)
    assert count == len(points), (q, n, count, len(points))
    return len(points), E.shape[1], error


def run():
    cases = [(2, 2), (3, 2), (5, 2), (4, 2), (2, 3), (3, 3), (2, 4)]
    samples = 0
    worst = 0.0
    for q, n in cases:
        count, cols, error = check_direct(q, n)
        samples += count
        worst = max(worst, error)
        print(f"direct q={q}, n={n}: matrices={count}, characters={cols}, max_abs_error={error:.2e}")
    analytic_checks = 0
    for q in (2, 3, 4, 5, 7, 11):
        for n in range(2, 25):
            spectrum, (lo, hi, A, R, I, T, C) = theoretical_levels(q, n)
            assert len(spectrum) == 1 + n*n*(q-1)
            assert lo > 0 and abs(lo-min(spectrum)) < 1e-12
            assert R <= A <= I
            # Exact integer sign certificate for the I-versus-plus comparison.
            phase_numerator = (2*q-n)*(q**(n-1)-1) - (q-1)*(n-2)
            assert (phase_numerator > 0) == (n < 2*q)
            if abs(I-hi) > 1e-11:
                assert (I > hi) == (n < 2*q)
            assert abs(max(spectrum) - max(I, hi)) < 1e-12
            assert abs(sum(spectrum)-(1+n*n*(q-1))) < 5e-9
            analytic_checks += 1
    print(f"PASS direct_cases={len(cases)} enumerated_invertible_matrices={samples} "
          f"formula_order_checks={analytic_checks} max_direct_error={worst:.2e}")


if __name__ == '__main__':
    run()
