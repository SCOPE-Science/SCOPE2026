"""Reproducible finite checks for a checkerboard-weighted fractional translation norm.

All infinite-dimensional statements require the analytic Fourier argument in RESULT.md.
Uses only Python's standard library.
"""
import cmath
import math
import random


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def star(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def matrices(a, b, t):
    assert a > 0 and b > 0
    sa, sb = math.sqrt(a), math.sqrt(b)
    p, q = (sa + sb)/2, (sa - sb)/2
    ip, iq = (1/sa + 1/sb)/2, (1/sa - 1/sb)/2
    root = [[p, q], [q, p]]
    iroot = [[ip, iq], [iq, ip]]
    d = [[1, 0], [0, cmath.exp(-1j*math.pi*t)]]
    return mm(mm(root, d), iroot)


def spectral_norm(b):
    c = mm(star(b), b)
    trace = (c[0][0] + c[1][1]).real
    det = (c[0][0]*c[1][1] - c[0][1]*c[1][0]).real
    discriminant = max(0., trace*trace - 4*det)
    return math.sqrt((trace + math.sqrt(discriminant))/2), trace, det


def formula(a, b, t):
    beta = abs(a-b)/(2*math.sqrt(a*b))
    h = beta * abs(math.sin(math.pi*t/2))
    return math.sqrt(1+h*h)+h


def assert_close(x, y, atol=1e-10, rtol=1e-10):
    assert abs(x-y) <= atol+rtol*max(abs(x),abs(y)), (x,y)


def main():
    checks = 0
    rng = random.Random(2417)
    cases = [(1,1,0),(1,1,.37),(1,9,-1.75),(4,1,.5),
             (4,1,1),(2,7,.3),(.2,6,2.4),(50,.01,-3.6)]
    cases += [(math.exp(rng.uniform(-3,3)), math.exp(rng.uniform(-3,3)),
               rng.uniform(-7,7)) for _ in range(360)]
    for a,b,t in cases:
        matrix = matrices(a,b,t)
        sn,tr,det = spectral_norm(matrix)
        beta = abs(a-b)/(2*math.sqrt(a*b))
        assert_close(sn, formula(a,b,t))
        assert_close(tr, 2+4*beta**2*math.sin(math.pi*t/2)**2)
        assert_close(det, 1)
        assert_close(sn * formula(a,b,-t), formula(a,b,t)**2)
        assert_close(formula(a,b,t+2), formula(a,b,t))
        checks += 5
    for a,b in [(1,1),(1,9),(4,1),(.2,6),(7,2)]:
        assert_close(formula(a,b,0),1)
        assert_close(formula(a,b,2),1)
        assert_close(formula(a,b,1),math.sqrt(max(a/b,b/a)))
        checks+=3
    # Independent Fourier integral checks against the prescribed Cauchy kernel.
    # The endpoint jump makes midpoint quadrature O(N^-1), not an exact certificate.
    nquad=16384
    for t in [-1.35,-.7,.25,.5,1.3]:
        for k in [-3,-1,0,1,3]:
            numeric = sum(cmath.exp(1j*t*(math.pi-theta) - 1j*k*theta)
                          for theta in ((j+.5)*2*math.pi/nquad for j in range(nquad)))/nquad
            analytic = math.sin(math.pi*t)/(math.pi*(k+t))
            assert abs(numeric-analytic)<3e-7, (t,k,numeric,analytic)
            checks+=1
    print('VERIFY_OK', 'finite_checks', checks,
          'scope', '2x2 matrix norm and multiplier coefficients; not an infinite-dimensional proof')

if __name__ == '__main__':
    main()
