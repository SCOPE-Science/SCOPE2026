#!/usr/bin/env python3
import cmath
import math
import random

SQ105 = math.sqrt(105.0)
RHO = 0.5 * math.sqrt(SQ105 - 5.0)
K6 = 35.0 * (SQ105 - 3.0) / 48.0


def conv(p, q):
    out = [0j] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def moment6(a, b, c):
    q = conv(conv([a, b, c], [a, b, c]), [a, b, c])
    return sum(abs(w) ** 2 for w in q)


def envelope(x, y, z):
    u = x*x + z*z
    v = x*z
    t = y*y
    return (t**3 + 9*t*t*u + 12*t*t*v + 9*t*u*u + 18*t*u*v
            + 18*t*v*v + u**3 + 6*u*v*v)


def ratio(a, b, c):
    d = abs(a)**2 + abs(b)**2 + abs(c)**2
    return moment6(a, b, c) / (d**3) if d else 0.0


def main():
    assert abs(2*RHO**4 + 5*RHO**2 - 10) < 2e-13
    assert abs(24*K6*K6 + 105*K6 - 1225) < 2e-11
    ext = ratio(1.0, RHO, 1.0)
    assert abs(ext - K6) < 2e-13

    rng = random.Random(271106)
    max_ratio = 0.0
    for _ in range(20000):
        a = complex(rng.gauss(0,1), rng.gauss(0,1))
        b = complex(rng.gauss(0,1), rng.gauss(0,1))
        c = complex(rng.gauss(0,1), rng.gauss(0,1))
        m = moment6(a,b,c)
        e = envelope(abs(a),abs(b),abs(c))
        assert m <= e + 2e-10 * max(1.0,e)
        rr = ratio(a,b,c)
        max_ratio = max(max_ratio, rr)
        assert rr <= K6 + 2e-11

    for _ in range(20000):
        x = rng.random()*3
        y = rng.random()*3
        z = rng.random()*3
        d = x*x+y*y+z*z
        if d == 0:
            continue
        e = envelope(x,y,z)/(d**3)
        assert e <= K6 + 2e-11

    for j in range(97):
        beta = 2*math.pi*j/97
        lam = cmath.exp(1j*(0.17*j))*(1.0+0.01*j)
        a = lam
        b = lam*RHO*cmath.exp(1j*beta)
        c = lam*cmath.exp(2j*beta)
        assert abs(ratio(a,b,c)-K6) < 5e-12

    print('VERIFY_OK random_complex=20000 random_moduli=20000 rho=%.15f K6=%.15f C6=%.15f max_random=%.15f' %
          (RHO, K6, K6**(1.0/6.0), max_ratio))

if __name__ == '__main__':
    main()
