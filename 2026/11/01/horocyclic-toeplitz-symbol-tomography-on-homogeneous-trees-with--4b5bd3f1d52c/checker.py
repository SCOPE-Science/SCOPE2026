"""Supplementary exact and finite checks for the horocyclic Toeplitz filter.

Requires Python 3 and SymPy. These checks do not certify completeness of the
infinite basis or the infinite-dimensional statements; those use the proof.
"""
from itertools import product
from math import sqrt
import sympy as sp

r, s, z = sp.symbols('r s z')
W_series = r*z/(1-r*z) - 2*r*s*z/(1-r*s*z) + r*s*s*z/(1-r*s*s*z)
W_rational = r*(1-s)**2*z*(1+r*s*z)/((1-r*z)*(1-r*s*z)*(1-r*s*s*z))
assert sp.cancel(W_series - W_rational) == 0
Q = ((1-r*z)*(1-r*s*z)*(1-r*s*s*z)/(1+r*s*z))
K = (1+r)*(1+r*s)**2*(1+r*s*s)/((1-r)*(1-r*s)**2*(1-r*s*s))
assert sp.cancel(W_rational.subs(z, 1)/(-W_rational.subs(z, -1)) - K) == 0
assert sp.cancel(W_rational.subs(z, 1)*Q.subs(z, -1)/(r*(1-s)**2) - K) == 0
assert sp.simplify(K.subs({r: sp.Rational(1,2), s: sp.Rational(1,2)}) - sp.Rational(75,7)) == 0
# Exact positivity of the signed inverse coefficients follows from Q(-z)
# = (1+rz)(1+rsz)(1+rs^2 z)/(1-rs z). Check a few degrees.
for n in range(15):
    term = sp.expand(sp.series(Q.subs(z, -z), z, 0, n+1).removeO()).coeff(z, n)
    for rr, ss in [(sp.Rational(1,2), sp.Rational(1,2)),
                   (sp.Rational(1,3), sp.Rational(1,4))]:
        assert term.subs({r:rr, s:ss}) > 0

# Direct finite-tree level Gram test. The two wavelets attached to a vertex
# have a zero-mean first-child pattern, and the remaining descendants carry
# its level-dependent scalar extension.
def shape(q, h, ancestor, amplitudes, word):
    if len(word) <= len(ancestor) or word[:len(ancestor)] != ancestor:
        return 0.0
    j = word[len(ancestor)]
    m = len(word)-len(ancestor)
    cm = sum(q**(-t) for t in range(m))
    return cm*amplitudes[j]

for q in (2,3,4):
    a = [1/sqrt(2), -1/sqrt(2)] + [0]*(q-2)
    b = ([1/sqrt(6), 1/sqrt(6), -2/sqrt(6)] + [0]*(q-3)) if q >= 3 else None
    for depth in range(1,7):
        words = list(product(range(q), repeat=depth))
        for prefix in ((),(0,),(0,0)):
            if len(prefix) >= depth:
                continue
            wavelet_values = [shape(q, depth, prefix, a, w) for w in words]
            wavelet_l1 = sum(wavelet_values)
            assert abs(wavelet_l1) < 1e-8*(1+len(words))
            # A nonzero ancestral wavelet is constant over this prefix sector;
            # hence it is orthogonal to the descendant at each fixed level.
            if prefix:
                ancestor_values = [shape(q, depth, (), a, w) for w in words]
                inner = sum(x*y for x,y in zip(wavelet_values, ancestor_values))
                assert abs(inner) < 1e-8*(1+len(words))
            if b is not None:
                other_values = [shape(q, depth, prefix, b, w) for w in words]
                inner = sum(x*y for x,y in zip(wavelet_values, other_values))
                assert abs(inner) < 1e-8*(1+len(words))

# Abelian finite-truncation check for the sharp alternating extremizer.
for q in (2, 3, 5, 11):
    for alpha in (1.05, 1.5, 2.0, 5.0):
        rr=q**(1-alpha); ss=1/q
        weights = [rr**m*(1-ss**m)**2 for m in range(1,3001)]
        wn = sum(weights)
        theoretical = rr*(1-ss)**2*(1+rr*ss)/((1-rr)*(1-rr*ss)*(1-rr*ss**2))
        assert abs(wn-theoretical) < 1e-9*(1+theoretical)
        kk=(1+rr)*(1+rr*ss)**2*(1+rr*ss**2)/((1-rr)*(1-rr*ss)**2*(1-rr*ss**2))
        alt=sum(((-1)**m)*w for m,w in enumerate(weights, start=1))/wn
        assert abs(alt+1/kk) < 1e-8

print('PASS: rational transfer, inverse norm, direct finite-tree Gram cancellations, 16 parameter checks')
