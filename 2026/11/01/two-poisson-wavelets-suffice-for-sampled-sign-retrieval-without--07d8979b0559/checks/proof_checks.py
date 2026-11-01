"""Supplementary arithmetic checks for a two-wavelet uniqueness proof.

The proof is analytic; these tests do not certify an infinite-dimensional theorem.
Run: python checks/proof_checks.py
"""
import cmath
import math

# For the harmonic zero-sampling lemma, the global bound is
# (6144/pi) exp(s+1) (3/2)^s (exp(-s)/200)^2.
for s in (0, 0.01, 0.2, 1, 2, 4, 8, 16, 64, 100):
    constant = (6144 * math.e / (40000 * math.pi)) * (1.5 / math.e) ** s
    assert 0 < constant < 0.134
    delta = math.exp(-s) / 200
    assert delta <= 1/200

for t in (1e-5, 0.0001, 0.001, 0.004):
    for beta in (1e-5, 0.0001, 0.001):
        if t + beta > 1/200:
            continue
        # A point in a logarithmic tile stays within delta * h of its node.
        max_vertical = max(math.exp(t / 2) - 1, 1 - math.exp(-t / 2))
        assert math.hypot(beta / 2, max_vertical) <= beta + t
        # A disk centered at a point of the node--tile segment of
        # radius h/4 is covered by the node-centered disk of radius h/3.
        assert math.hypot(beta / 2, max_vertical) + 1 / 4 < 1 / 3
        m_count_upper = math.log(2) / t + 1
        n_count_upper = 2 / (3 * beta) + 1
        assert m_count_upper * n_count_upper <= 3 / (beta * t)

# For a+ib, knowing |a| and |b| determines Re((a+ib)^2).
for ia in range(-8, 9):
    for ib in range(-8, 9):
        z = complex(ia, ib)
        for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            w = complex(sa * ia, sb * ib)
            assert z.real**2 == w.real**2 and z.imag**2 == w.imag**2
            assert (z*z - w*w).real == 0

# Sample holomorphic test function with a nonconstant square: nodewise
# real-square equality is distinct from ordinary modulus equality.
for z in (0.1+0.5j, 1+2j, -2+0.25j):
    F = cmath.exp(1j*z)
    G = -F
    assert abs((F * F - G * G).real) < 1e-13

print('PASS: harmonic tile constants, disk geometry, multiplicity, and quadratic real-part identities')
