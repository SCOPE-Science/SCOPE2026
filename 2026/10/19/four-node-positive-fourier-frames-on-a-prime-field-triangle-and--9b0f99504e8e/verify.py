#!/usr/bin/env python3
"""Independent finite sanity checks of explicit positive Fourier tight-frame designs."""
import cmath
import math

PRIMES = (5, 7, 11, 13, 17, 31, 101)
max_entry_error = 0.0
for p in PRIMES:
    a = (p - 1) // 2
    h = math.cos(math.pi / p)
    w0 = (2*h - 1) / (2*(1+h))
    w = 1 / (2*(1+h))
    assert w0 > 0 and w > 0 and a > p/3 and a < 2*p/3
    assert len({(0,0),(a,0),(0,a),(-a % p,-a % p)}) == 4
    designs = [((0,0),w0), ((a,0),w), ((0,a),w), (((-a)%p,(-a)%p),w)]
    def gram(items):
        mat = [[0j] * 3 for _ in range(3)]
        for (s,t),weight in items:
            v = [1,cmath.exp(2j*math.pi*s/p),cmath.exp(2j*math.pi*t/p)]
            for i in range(3):
                for j in range(3):
                    mat[i][j] += weight * v[i] * v[j].conjugate()
        return mat
    for family in (designs, [((t, 2*t % p),1/p) for t in range(p)]):
        g = gram(family)
        max_entry_error = max(max_entry_error, max(abs(g[i][j]-(1 if i==j else 0)) for i in range(3) for j in range(3)))
        assert max(abs(g[i][j]-(1 if i==j else 0)) for i in range(3) for j in range(3)) < 1e-12
    assert abs((w - w0) - math.tan(math.pi/(2*p))**2) < 1e-12
    print('p=%3d four-node weights %.12g, %.12g; rational nodes=%d; verified' % (p,w0,w,p))
print('PASS: %d prime orders, %d frames; worst entry discrepancy %.3g' % (len(PRIMES),2*len(PRIMES),max_entry_error))
