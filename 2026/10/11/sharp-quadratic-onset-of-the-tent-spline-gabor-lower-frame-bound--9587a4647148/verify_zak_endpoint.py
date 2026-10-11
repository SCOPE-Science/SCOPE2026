"""Finite exact checks supplementing the analytic Zak-frame-bound theorem.

Run: python3 verify_zak_endpoint.py
Uses only the Python standard library. Finite checks are not a proof of the
limiting frame-bound formula; the accompanying analytic argument is essential.
"""
from fractions import Fraction as F
from math import pi
import cmath


def plus(x):
    return max(x, 0)


def weights(b, x):
    """Numerators b*Q2((x-k)/b) for every nonzero compact-support term."""
    return [(k, plus(b - abs(x - k))) for k in range(-4, 6)
            if abs(x - k) < b]


def alt_numerator(b, x):
    return sum((-1 if k % 2 else 1) * v for k, v in weights(b, x))


def zak(b, x, gamma):
    return sum(float(v)*cmath.exp(2j*pi*k*gamma)
               for k, v in weights(b, x))/float(b)**1.5


def energy(q, b, x, gamma):
    return sum(abs(zak(b, (x + F(j,q)) % 1, gamma))**2
               for j in range(q))


checks = 0
for q in range(2, 21):
    e0 = F(1, 2*q)
    c = 2 + e0
    for delta in (F(0), F(1,1000), F(1,300), F(1,100)):
        eps = e0+delta
        b = c+delta
        for numerator in range(0, 31):
            x = F(numerator, 31)
            want = plus(eps-x)-plus(x-1+eps)
            assert alt_numerator(b,x) == want, (q,delta,x)
            checks += 1
        if delta:
            samples = [e0+F(j,q) for j in range(q)]
            raw = sum(alt_numerator(b,x)**2 for x in samples)
            assert raw == 2*delta**2, (q,delta,raw)
            checks += 1
    # The imaginary first derivative of b^(3/2) * Zak / (2*pi*i),
    # at gamma = 1/2 and the entire critical regular grid, equals 2*eps.
    for j in range(q):
        x = e0+F(j,q)
        derivative = sum(k*(-1 if k % 2 else 1)*v for k,v in weights(c,x))
        assert derivative == 2*e0, (q,j,derivative)
        checks += 1

for q in range(2,8):
    delta=F(1,1000)
    b=2+F(1,2*q)+delta
    x=F(1,2*q)
    trial = energy(q,b,x,.5)
    expected = 2*float(delta)**2/float(b)**3
    assert abs(trial-expected)<1e-13, (q,trial,expected)
    # A mesh of nearby phases/locations checks the local minimizer;
    # it does not prove global or continuum minimality.
    near=[]
    for i in range(-8,9):
        for j in range(-8,9):
            near.append(energy(q,b,x+F(i,4)*delta,.5+j*float(delta)/8))
    assert min(near) >= expected-1e-12 and min(near) <= expected+1e-12
    print(f'q={q}: trial/delta^2={trial/float(delta)**2:.12f}, '
          f'limiting coefficient={2/float(2+F(1,2*q))**3:.12f}')
    checks += len(near)+1

print(f'PASS: {checks} exact identities or supplementary mesh checks')
