#!/usr/bin/env python3
"""Exact exhaustive cyclotomic certificate for nine-point phase-alphabet energies.

No external dependencies. Every arithmetic operation used in comparisons is integral.
"""
from itertools import product
from functools import cmp_to_key
from math import cos, sin, pi

# The monic defining polynomials, increasing coefficient order.
PHI = {2: (1, 1), 4: (1, 0, 1), 6: (1, -1, 1), 8: (1, 0, 0, 0, 1)}
EXPECTED = {2: (35, (16, 0), 12),
            4: (1225, (16, 0), 84),
            6: (9135, (4, 0), 6),
            8: (23765, (24, -16), 6)}
OCTARY_NORMALIZED_OPTIMIZERS = {
    (0, 1, 3, 7, 3, 7, 5, 4),
    (0, 2, 2, 5, 1, 6, 6, 4),
    (0, 3, 4, 2, 6, 0, 7, 4),
    (0, 5, 4, 6, 2, 0, 1, 4),
    (0, 6, 6, 3, 7, 2, 2, 4),
    (0, 7, 5, 1, 5, 1, 3, 4),
}

def cyclotomic_roots(q):
    phi = PHI[q]
    degree = len(phi) - 1
    roots = []
    coefficient = [1] + [0] * (degree - 1)
    for _ in range(q):
        roots.append(tuple(coefficient))
        nxt = [0] + coefficient[:-1]
        leading = coefficient[-1]
        for j in range(degree):
            nxt[j] -= leading * phi[j]
        coefficient = nxt
    assert coefficient == [1] + [0] * (degree - 1)
    return roots

def norm_pair(q, coeff):
    if q == 8:
        a, b, c, d = coeff
        return (a*a + b*b + c*c + d*d, a*(b-d) + c*(b+d))
    if q == 6:
        a, b = coeff
        return (a*a + a*b + b*b, 0)
    return (sum(v*v for v in coeff), 0)

def sign_radical(a, b):
    """Exact sign of a+b*sqrt(2) with a,b integral."""
    if a == 0:
        return (b > 0) - (b < 0)
    if b == 0:
        return (a > 0) - (a < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    if a > 0:
        return (a*a > 2*b*b) * 2 - 1
    return (2*b*b > a*a) * 2 - 1

def compare_pairs(left, right):
    return sign_radical(left[0]-right[0], left[1]-right[1])

def vanishing_phase_sequences(q, roots):
    """Enumerate every zero-sum 8-tuple with first phase normalized to 1."""
    degree = len(roots[0])
    for tail in product(range(q), repeat=7):
        exponents = (0,) + tail
        # An integer basis of Q(zeta_q); coordinates zero iff complex sum zero.
        totals = [0] * degree
        for exponent in exponents:
            for j, x in enumerate(roots[exponent]):
                totals[j] += x
        if not any(totals):
            yield exponents

def energy(q, exponents, roots):
    """Double autocorrelation-defect energy as an exact algebraic pair."""
    degree = len(roots[0])
    all_exps = (None,) + exponents
    totals = [0, 0]
    # C(-h) = conj(C(h)); the four positive shifts determine all eight.
    for h in range(1, 5):
        v = [0] * degree
        v[0] = 1  # The target is C(h)=-1.
        for j in range(1, 9):
            k = (j + h) % 9
            if k == 0:
                continue
            term = roots[(all_exps[k] - all_exps[j]) % q]
            for c in range(degree):
                v[c] += term[c]
        a, b = norm_pair(q, v)
        totals[0] += 2 * a
        totals[1] += 2 * b
    return tuple(totals)

def exact_census(q):
    roots = cyclotomic_roots(q)
    count = 0
    best = None
    minimizers = []
    values = set()
    for seq in vanishing_phase_sequences(q, roots):
        count += 1
        v = energy(q, seq, roots)
        values.add(v)
        if best is None or compare_pairs(v, best) < 0:
            best, minimizers = v, [seq]
        elif v == best:
            minimizers.append(seq)
    assert (count, best, len(minimizers)) == EXPECTED[q], (q, count, best, len(minimizers))
    if q == 8:
        assert set(minimizers) == OCTARY_NORMALIZED_OPTIMIZERS
        ordered = sorted(values, key=cmp_to_key(compare_pairs))
        assert ordered[:2] == [(24, -16), (40, -24)]
        # Direct independent complex arithmetic for one certificate witness.
        witness = minimizers[0]
        f = [0j] + [complex(cos(2*pi*j/q), sin(2*pi*j/q)) for j in witness]
        analytic = sum(abs(sum(f[(j+h)%9]*f[j].conjugate() for j in range(9))+1)**2
                       for h in range(1, 9))
        power_spectrum = [abs(sum(f[j]*complex(cos(-2*pi*j*k/9), sin(-2*pi*j*k/9))
                                  for j in range(9)))**2 for k in range(9)]
        spectral_defect = sum((power_spectrum[k]-9)**2 for k in range(1, 9))/9
        assert abs(analytic - (24-16*2**0.5)) < 1.e-11
        assert abs(spectral_defect - analytic) < 1.e-11
        assert abs(power_spectrum[0]) < 1.e-20
    print('q=', q, 'normalized zero-mean sequences=', count,
          'minimum=', best, 'normalized minimizers=', len(minimizers),
          'different energy levels=', len(values))
    return count, best, minimizers

if __name__ == '__main__':
    for alphabet in (2, 4, 6, 8):
        exact_census(alphabet)
    print('Exact cyclotomic checks: PASS')
