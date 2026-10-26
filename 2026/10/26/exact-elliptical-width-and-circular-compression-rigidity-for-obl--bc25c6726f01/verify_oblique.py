"""Finite consistency checks for the exact oblique-spectrum elliptical-width theorem.
These tests are not a substitute for the analytical proof in RESULT.md.
Python standard library only.
"""
import cmath
import math
import random


def dot(a, b):
    return sum(t.conjugate() * s for t, s in zip(a, b))


def test(u, v, rng):
    A = abs(u)**2 + abs(v)**2
    B = (u.conjugate() * v).real
    D = (u.conjugate() * v).imag
    assert abs(D) > 1e-12
    h = math.sqrt(A*A - 4*B*B)
    k = -2*B/(A+h)
    optimal = 8*D*D/(A+h)
    z = [u+v, u-v, -u+v, -u-v]
    p = [(1+k)/4, (1-k)/4, (1-k)/4, (1+k)/4]

    def width_sq(w):
        m = sum(w[j]*z[j] for j in range(4))
        zz = [t-m for t in z]
        V = sum(w[j]*(abs(zz[j])**2) for j in range(4))
        c = sum(w[j]*zz[j]**2 for j in range(4))
        return max(0.0, (V*V-abs(c)**2)/V) if V > 1e-14 else 0.0

    assert abs(width_sq(p)-optimal) < 1e-10*max(1, optimal)
    for _ in range(24000):
        q = [rng.expovariate(1) for _ in range(4)]
        q = [s/sum(q) for s in q]
        assert width_sq(q) <= optimal + 1e-9*max(1, optimal)
    x = [math.sqrt(s)*cmath.exp(1j*2*math.pi*rng.random()) for s in p]
    var = sum(p[j]*abs(z[j])**2 for j in range(4))
    c = sum(p[j]*z[j]**2 for j in range(4))
    y = [(z[j].conjugate() - c.conjugate()/var*z[j])*x[j]/math.sqrt(optimal) for j in range(4)]
    assert abs(dot(x,x)-1) < 1e-11
    assert abs(dot(y,y)-1) < 1e-11
    assert abs(dot(x,y)) < 1e-11
    schur = [[dot(x,[z[j]*x[j] for j in range(4)]),dot(x,[z[j]*y[j] for j in range(4)])],
             [dot(y,[z[j]*x[j] for j in range(4)]),dot(y,[z[j]*y[j] for j in range(4)])]]
    assert abs(schur[0][0]) + abs(schur[1][1]) + abs(schur[1][0]) < 1e-10
    assert abs(schur[0][1]-math.sqrt(optimal)) < 1e-10
    return optimal, k


if __name__ == '__main__':
    rng = random.Random(1729)
    configs = [(1+0j,cmath.exp(1j*math.pi/3)),
               (2+0j,0.6+0.9j),(1+0j,0.02+0.03j),
               (1+0j,3j),(.3+1.1j,2-.6j)]
    for a,b in configs:
        val,k = test(a,b,rng)
        print('width_squared',format(val,'.14g'),'optimal_correlation',format(k,'.14g'))
    assert abs(test(1+0j,1j,rng)[0]-2) < 1e-12
    print('PASS: analytic witnesses and 144000 deterministic probability comparisons')
