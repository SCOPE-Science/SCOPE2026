#!/usr/bin/env python3
"""Reproducible algebraic and eigenbasis tests for a three-site weighted wave propagator.
Requires Python 3 and NumPy; no external data or file reads.
"""
from math import gcd, pi, sqrt, cos
import numpy as np
from numpy.polynomial import Chebyshev


def spectrum(m, k):
    m1, m2, m3 = map(float, m)
    k1, k2 = map(float, k)
    s = k1 * (1/m1 + 1/m2) + k2 * (1/m2 + 1/m3)
    p = k1*k2*(m1+m2+m3)/(m1*m2*m3)
    gap = sqrt(s*s - 4*p)
    lower, upper = (s-gap)/2, (s+gap)/2
    b = k1*k2/(m2*sqrt(m1*m3))
    c = np.array([b/(lower*upper),-b/(lower*gap),b/(upper*gap)])
    h = np.array([
        [k1/m1, -k1/sqrt(m1*m2), 0],
        [-k1/sqrt(m1*m2), (k1+k2)/m2, -k2/sqrt(m2*m3)],
        [0, -k2/sqrt(m2*m3), k2/m3],
    ])
    return h, lower, upper, c


def exact_rational_amplitude(m, k, p, q):
    h, lo, hi, c = spectrum(m, k)
    assert gcd(p, q) == 1 and p > q > 0
    assert abs(sqrt(hi/lo) - p/q) < 3e-12
    poly = Chebyshev([c[0]]) + c[1] * Chebyshev.basis(q) + c[2] * Chebyshev.basis(p)
    interior = [float(z.real) for z in poly.deriv().roots()
                if abs(z.imag) < 1e-9 and -1 < z.real < 1]
    xs = [-1, 1] + interior
    exact = max(float(poly(x)**2) for x in xs)
    xgrid = np.linspace(-1, 1, 20001)
    grid = float(np.max(poly(xgrid)**2))
    assert exact + 1e-10 >= grid
    return exact


def main():
    n = 0
    rng = np.random.default_rng(20261015)
    for _ in range(350):
        m = np.exp(rng.uniform(-1.4, 2.5, 3))
        k = np.exp(rng.uniform(-1.1, 2, 2))
        h, low, high, c = spectrum(m, k)
        eig, vectors = np.linalg.eigh(h)
        assert np.allclose(eig, [0,low,high],atol=2e-10)
        assert np.allclose(vectors[0,:]*vectors[2,:], c, rtol=2e-9,atol=1e-10)
        assert abs(sum(c)) < 1e-10
        assert c[0]>0 and c[1]<0 and c[2]>0
        ceiling = 2*abs(c[1])
        assert 0 < ceiling <= 1 + 1e-10
        for t in [0, .2, 1, 3, 7, 29]:
            analytic = float(c[0] + c[1]*cos(t*sqrt(low)) + c[2]*cos(t*sqrt(high)))
            matrix = (vectors*np.cos(t*np.sqrt(np.maximum(eig,0)))) @ vectors.T
            assert abs(analytic-matrix[0,2]) < 3e-10
            assert abs(analytic) < ceiling+1e-10
            n += 1
    h,low,high,c = spectrum([12,8,12],[1,1])
    assert abs(sqrt(high/low)-2)<1e-12
    assert abs(c[0]+c[1]*(-1)+c[2]*1-1)<1e-12
    # A realizable three-component configuration: 24,6,24 internal arcs,
    # one weak edge between adjacent components. Its frequency ratio is 3.
    h,low,high,c = spectrum([24,6,24],[1,1])
    assert abs(sqrt(high/low)-3)<1e-12
    assert abs(exact_rational_amplitude([24,6,24],[1,1],3,1)-64/81)<1e-12
    # Test each parity class and global Chebyshev optimization.
    for p,q in [(2,1),(3,1),(3,2),(4,3),(5,2),(5,3),(7,4),(8,5),(9,7)]:
        assert gcd(p,q)==1
        mass_middle = 2/((p/q)**2-1)
        case = [1,mass_middle,1]
        result = exact_rational_amplitude(case,[1,1],p,q)
        if p%2==0 and q%2==1:
            assert abs(result-1)<4e-11
        else:
            assert result < 1-1e-9
    # Kronecker approximation examples, including equal internal masses.
    for m,ratio in [([12,12,12],sqrt(3)),([6,12,6],sqrt(2))]:
        h, low, high, c = spectrum(m,[1,1])
        assert abs(sqrt(high/low)-ratio)<2e-12
        approximate=[]
        for q in range(1,20000,2):
            p=2*round(ratio*q/2)
            approximate.append((abs(ratio-p/q),q,p))
        _,q,p = min(approximate)
        t=q*pi/sqrt(low)
        amplitude = c[0] + c[1]*cos(t*sqrt(low)) + c[2]*cos(t*sqrt(high))
        assert amplitude > .9999999
    print(f"PASS {n} independent matrix/cosine comparisons, nine rational exact maxima, two irrational approximations, plus explicit perfect and parity-obstructed cases")


if __name__ == '__main__':
    main()
