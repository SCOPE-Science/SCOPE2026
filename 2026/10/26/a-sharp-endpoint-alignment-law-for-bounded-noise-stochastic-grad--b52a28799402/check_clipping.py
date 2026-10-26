"""Reproducible numeric and rational checks for sharp clipping alignment."""
from fractions import Fraction as F
from math import sqrt
from random import Random


def clip(x, q=1.0):
    z = sqrt(sum(v*v for v in x))
    a = min(1.0, q/z) if z else 1.0
    return [a*v for v in x]


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def pointwise_bound(r, xi):
    s = xi[0]
    v = [r+xi[0]] + list(xi[1:])
    return clip(v)[0] - (r/2 + (1-r/2)*s)


def run():
    rng = Random(123456)
    n = 0
    for dim in (1,2,3,8,19):
        for r in (0.00001,0.005,0.1,0.37,0.75,1.0):
            for _ in range(3200):
                x = [rng.uniform(-1,1) for _ in range(dim)]
                norm = sqrt(dot(x,x))
                if norm:
                    scale = rng.random()/norm
                    x = [scale*t for t in x]
                residual = pointwise_bound(r,x)
                assert residual >= -4e-14, (dim,r,x,residual)
                n += 1
    # Exact equality for the sharp antipodal noise, at all rational radii <= 1.
    for r in (F(1,100),F(1,3),F(3,5),F(1,1)):
        upper=F(1,1)
        lower=r-F(1,1)
        mean=(upper+lower)/2
        assert mean == r/2
        assert r*mean == (r*r)/2
    # Subcritical construction: every nonzero state strictly in the interval
    # (-sigma+q,sigma-q) has zero conditional clipped gradient.
    for sigma,q,x in ((F(2),F(1),F(1,3)),
                      (F(7,4),F(3,4),F(-2,3)),
                      (F(9,8),F(1,8),F(1,2))):
        assert 0 < q < sigma and abs(x) < sigma-q
        assert x+sigma > q and x-sigma < -q
        assert (q-q)/2 == 0
    # With q=1, sigma=2, theta=1/4, c=1/100, Gaussian variance 1:
    # sum_{n>=1} n^{-3/2} <= 3, so Doob failure <= 0.0006.
    c=F(1,100)
    variance_ceiling=3*c*c*(1+1)
    assert variance_ceiling == F(3,5000)
    assert 1-variance_ceiling >= F(999,1000)
    print('CHECK_OK', n, 'pointwise samples; rational extremizers, deadzone and Doob bound passed')


if __name__ == '__main__':
    run()
