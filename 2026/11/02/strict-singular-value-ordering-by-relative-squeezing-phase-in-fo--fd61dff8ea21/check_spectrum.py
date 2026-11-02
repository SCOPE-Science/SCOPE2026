#!/usr/bin/env python3
"""Finite matrix and algebraic checks for quadratic Fock cross-product spectra.

Requires Python 3.10+ and NumPy. These finite checks supplement, not replace,
the infinite-dimensional proof in RESULT.md.
"""
import cmath
import math
import numpy as np


def operator_matrix(r, t, cutoff):
    out = np.zeros((cutoff, cutoff), dtype=np.complex128)
    for n in range(cutoff):
        for k in range(n, cutoff, 2):
            j = (k - n) // 2
            coeff = math.exp(n * math.log(r) +
                0.5 * (math.lgamma(k + 1) - math.lgamma(n + 1)) -
                math.lgamma(j + 1))
            out[k, n] = coeff * t**j
    return out


def constants(r, t, s):
    ds = 1 - 4 * abs(s)**2
    b = r**4 / ds
    a = t + s * r**4 / ds
    p = 1 + b**2 - 4 * abs(a)**2
    discr = p * p - 4 * b**2
    assert discr > 0
    d = (p + math.sqrt(discr)) / 2
    q = b / d
    leading = ds**(-0.25) * d**(-0.25)
    return a, b, d, q, leading


def run():
    checks = 0
    samples = [
        (.6, .11+.03j, .08-.02j),
        (.75, .1, .05),
        (.7, .17j, .12j),
        (.7, .17j, -.12j),
        (.4, .01+.09j, -.2j),
        (.8, .07+.03j, .05-.08j),
        (.35, .2, .25j),
        (.62, -.08+.11j, -.11-.06j),
    ]
    for r, t, s in samples:
        assert 2 * abs(t) < 1 - r*r and 2 * abs(s) < 1 - r*r
        checks += 1
        a, b, d, q, lead = constants(r, t, s)
        assert 0 < q < 1 and 0 < b < d <= 1+1e-12
        checks += 1
        assert 2 * abs(a) + b < 1
        checks += 1
        assert abs(d*d - (1+b*b-4*abs(a)**2)*d + b*b) < 1e-11
        checks += 1
        assert abs((d-b)**2 / d - ((1-b)**2-4*abs(a)**2)) < 1e-11
        checks += 1
        Wt, Ws = operator_matrix(r,t,85),operator_matrix(r,s,85)
        singular = np.linalg.svd(Wt @ Ws.conjugate().T,compute_uv=False)
        for n in range(7):
            approx = lead * q**(n/2)
            assert abs(singular[n] - approx) <= 2e-7 * max(1, approx), (r,t,s,n,singular[n],approx)
            checks += 1
        dtrace = (1-4*abs(t)**2)*(1-4*abs(s)**2)-2*r**4+r**8-8*r**4*(t*s.conjugate()).real
        assert dtrace > 0
        checks += 1
        predicted_hs_square = 1 / math.sqrt(dtrace)
        assert abs(predicted_hs_square - lead**2/(1-q)) < 1e-10
        checks += 1
        assert abs(sum(singular**2) - predicted_hs_square) < 3e-7
        checks += 1

    for r, ut, us in ((.3,.1,.13),(.65,.08,.17),(.8,.04,.05)):
        assert 2*max(ut,us)<1-r*r
        values=[]
        for j in range(25):
            angle=math.pi*j/24
            _,_,_,q,lead=constants(r,ut,us*cmath.exp(1j*angle))
            values.append([lead*q**(n/2) for n in range(8)])
        for j in range(24):
            for n in range(8):
                assert values[j][n] > values[j+1][n]
                checks+=1
    print('PASS',checks,'deterministic matrix/algebra/phase assertions')

if __name__=='__main__':
    run()
