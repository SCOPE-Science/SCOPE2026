#!/usr/bin/env python3
"""Exact residue-sign checks of a prime cyclic Euler form, with independent Fourier checks.

Only standard-library Python is needed. This verifies finite cases, not the
unbounded-prime argument, which is supplied in the accompanying proof.
"""
from math import cos, pi, sin, gcd


def primes_below(n):
    return [p for p in range(3, n) if all(p % d for d in range(2, int(p**0.5) + 1))]


def q_twice(u, a, b):
    """Twice the quadratic form, avoiding fractions."""
    n = len(u)
    return sum((u[j] - u[(j+a) % n])**2
               + (u[j] - u[(j+b) % n])**2
               - (u[j] - u[(j+a+b) % n])**2
               for j in range(n))


def polar_hessian(n, a, b):
    """The integer matrix P such that Q(u)=u^T P u / 2."""
    P = [[0] * n for _ in range(n)]
    for step, sign in ((a, 1), (b, 1), (a+b, -1)):
        for j in range(n):
            P[j][j] += 2*sign
            P[j][(j+step) % n] -= sign
            P[j][(j-step) % n] -= sign
    return P


def direct_lambda(p, t, k):
    A = 2*pi*k/p
    B = 2*pi*t*k/p
    return 1-cos(A)-cos(B)+cos(A+B)


def residue_sign(p, t, k):
    r = ((-t)*k) % p
    difference = abs(k-r)
    return 1 if 2*difference < p else -1


def predicted_positive_ratios(p):
    return {(-1) % p, (-2) % p, (-pow(2, -1, p)) % p}


sign_cases = 0
classes = 0
for p in primes_below(200):
    ratios = set()
    for t in range(1, p):
        signs = [residue_sign(p, t, k) for k in range(1, p)]
        assert all(s in (-1, 1) for s in signs)
        # Independently check the nonzero spectrum via a second trigonometric expression.
        if p <= 79:
            for k, s in enumerate(signs, 1):
                lam = direct_lambda(p, t, k)
                assert abs(lam) > 1e-9, (p, t, k, lam)
                assert s*lam > 0, (p, t, k, lam)
                r = (-t*k) % p
                factor = 4*sin(pi*k/p)*sin(pi*r/p)*cos(pi*(k-r)/p)
                assert abs(lam-factor) < 1e-10, (p, t, k, lam, factor)
                sign_cases += 1
        if all(s > 0 for s in signs):
            ratios.add(t)
    assert ratios == predicted_positive_ratios(p), (p, ratios, predicted_positive_ratios(p))
    classes += 1

# Compare exact integer polar matrices against the original difference form,
# including repeated steps and the zero step, and check Fourier eigenvectors.
matrix_checks = 0
for p in (3, 5, 7, 11, 13):
    for t in range(1, p):
        P = polar_hessian(p, 1, t)
        assert all(P[i][j] == P[j][i] for i in range(p) for j in range(p))
        assert all(sum(row) == 0 for row in P)
        for i in range(p):
            v = [0] * p
            v[i] = 1
            assert 2*q_twice(v, 1, t) == 2*P[i][i]
            for j in range(i+1, p):
                w = v[:]
                w[j] = 1
                # q_twice(w) = w^T P w by definition of P.
                assert q_twice(w, 1, t) == P[i][i]+P[j][j]+2*P[i][j]
        for k in range(1, p):
            # The polar matrix P has eigenvalues twice those of Q's matrix.
            fk = [cos(2*pi*k*j/p) for j in range(p)]
            eigenval = 2*direct_lambda(p, t, k)
            err = max(abs(sum(P[i][j]*fk[j] for j in range(p)) - eigenval*fk[i]) for i in range(p))
            assert err < 1e-10, (p, t, k, err)
        matrix_checks += 1

# Exact arithmetic witness to negativity in every nonexceptional multiplier.
negative_witnesses = 0
for p in primes_below(200):
    for c in range(3, (p-1)//2 + 1):
        k = (p-1)//c
        r = c*k
        assert 1 <= k and 1 <= r < p
        assert abs(k-r)*2 > p, (p, c, k, r)
        negative_witnesses += 1

print('VERIFY_OK primes=' + str(classes)
      + ' exact_negative_witnesses=' + str(negative_witnesses)
      + ' trigonometric_sign_cases=' + str(sign_cases)
      + ' exact_integer_polar_cases=' + str(matrix_checks))
