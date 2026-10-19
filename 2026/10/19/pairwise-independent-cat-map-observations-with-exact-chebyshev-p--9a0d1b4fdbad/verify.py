"""Exact finite Fourier checks of the explicit toral-automorphism identities.

Finite tests corroborate the separate all-time eigenvalue argument; they
are not certificates of the unrestricted theorem.
"""
from collections import defaultdict
from fractions import Fraction


def step(v, t):
    # Transpose of A=[[t-1,1],[t-2,1]], det A = 1, trace A = t.
    return ((t - 1) * v[0] + (t - 2) * v[1], v[0] + v[1])


def spectral_basis(t, k, n):
    v = k
    out = []
    for _ in range(n):
        # Coefficients of cos(2 pi v*x)+c cos(2 pi t v*x)
        out.append(v)
        v = step(v, t)
    return out


def fourier_integral(items, power):
    d = {(0, 0): Fraction(1)}
    for _ in range(power):
        nd = defaultdict(Fraction)
        for v, q in d.items():
            for f, c in items:
                nd[(v[0] + f[0], v[1] + f[1])] += q * c
        d = nd
    return d.get((0, 0), Fraction(0))


def harmonic(v, h):
    return [((s * h * v[0], s * h * v[1]), Fraction(1, 2)) for s in [-1,1]]


def triple_correl(a, b, c):
    out = Fraction(0)
    for va, pa in a:
        for vb, pb in b:
            for vc, pc in c:
                if va[0] + vb[0] + vc[0] == 0 and va[1] + vb[1] + vc[1] == 0:
                    out += pa*pb*pc
    return out


for TRACE in (3, 4, 5, 7):
    for k in ((1, 0), (1, 1), (2, 3)):
        freq = spectral_basis(TRACE, k, 8)
        for i in range(8):
            for j in range(i + 1, 8):
                assert triple_correl(harmonic(freq[i], 1), harmonic(freq[j], 1),
                                     [((0,0), Fraction(1))]) == 0
        for c in (-2, -1, 0, 1, 2):
            for N in range(1, 7):
                terms = []
                for v in freq[:N]:
                    terms += harmonic(v, 1)
                    if c:
                        terms += [(q, c*coef) for q, coef in harmonic(v, TRACE)]
                mean = fourier_integral(terms, 1)
                variance = fourier_integral(terms, 2)
                third = fourier_integral(terms, 3)
                assert mean == 0, (TRACE, k, c, N, 'mean', mean)
                assert variance == Fraction(N*(1+c*c), 2), (TRACE,k,c,N,'variance',variance)
                assert third == Fraction(3*c*max(0,N-2),2), (TRACE,k,c,N,'third',third)
        assert triple_correl(harmonic(freq[0],1), harmonic(freq[2],1), harmonic(freq[1],TRACE)) == Fraction(1,4)
print('VERIFY_OK')
