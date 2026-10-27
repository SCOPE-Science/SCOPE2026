#!/usr/bin/env python3
"""Verify exact algebra and sample spectra of a planar primal-dual update."""
import math
import numpy as np
import sympy as sp


def verify():
    t, z = sp.symbols('t z', nonzero=True)
    u = 1 / (1 + t)
    M = sp.Matrix([[u, -u * t * z], [u * t * (2 * u - 1),
                                    u - 2 * u**2 * t**2 * z]])
    tr = 2 * u - 2 * u**2 * t**2 * z
    det = u**2 * (1 - t**2 * z)
    assert sp.factor(M.trace() - tr) == 0
    assert sp.factor(M.det() - det) == 0
    assertions = 2
    def conjugate_on_circle(q):
        return q.subs(z, 1/z)
    tc, dc = conjugate_on_circle(tr), conjugate_on_circle(det)
    schur_margin = sp.factor((1 - det * dc)**2 - (tr - tc * det) * (tc - tr * dc))
    c = (z + 1/z) / 2
    predicted = 4 * t**4 * (1 + c) * ((2*t+1)**2*c - 2*t**4 + 6*t**2 + 8*t + 3) / (1+t)**8
    assert sp.factor(schur_margin - predicted) == 0
    positive_margin = 2*t*(2+(3+c)*t+2*t**2)/(1+t)**4
    assert sp.factor(1-det*dc-positive_margin) == 0
    assertions += 2
    h = (2*t**4-6*t**2-8*t-3)/(2*t+1)**2
    assert sp.factor(sp.diff(h, t) - 4*(t+1)*(2*t**3+1)/(2*t+1)**3) == 0
    assert sp.factor(h+1 - 2*(t**2-t-1)*(t**2+t+1)/(2*t+1)**2)==0
    assert sp.factor(h-1 - 2*(t+1)**2*(t**2-2*t-2)/(2*t+1)**2)==0
    assertions += 3
    for tv in (0.02, 0.1, 0.5, 1.0, 1.5, 1.618, 1.7, 2.0, 2.5, 2.7, 2.732, 2.75, 3, 8):
        uv = 1 / (1 + tv)
        hv = (2*tv**4 - 6*tv**2-8*tv-3)/(2*tv+1)**2
        for theta in np.linspace(0, math.pi, 37):
            cc, ss = math.cos(theta), math.sin(theta)
            Rm = np.array([[cc, ss], [-ss, cc]])
            I = np.eye(2)
            real_update = np.block([[uv*I, -uv*tv*Rm],
                                    [uv*tv*(2*uv-1)*I, uv*I-2*uv**2*tv**2*Rm]])
            lam = np.linalg.eigvals(real_update)
            spectral_radius = max(abs(lam))
            predicted_stable = theta < math.pi - 1e-10 and cc > hv
            if predicted_stable:
                assert spectral_radius < 1 - 1e-10, (tv, theta, spectral_radius)
            elif theta < math.pi - 1e-10:
                assert spectral_radius > 1 + 1e-10, (tv, theta, spectral_radius)
            else:
                assert abs(spectral_radius-1) < 1e-8, (tv, theta, spectral_radius)
            assertions += 1
            x = np.array([0.8, -0.3]); y = np.array([-0.7, 0.4])
            x1 = (x - tv*Rm@y)/(1+tv)
            y1 = (y + tv*(2*x1-x))/(1+tv)
            observed = real_update@np.r_[x,y]
            assert np.allclose(observed, np.r_[x1,y1], rtol=1e-12, atol=1e-12)
            assertions += 1
    assert abs((2*2**4 - 6*2**2 - 8*2 - 3)/(2*2+1)**2 + 11/25) < 1e-14
    assertions += 1
    print(f'PASS: {assertions} checks (7 symbolic identities, spectral/recurrence grids, threshold identity).')


if __name__ == '__main__':
    verify()
