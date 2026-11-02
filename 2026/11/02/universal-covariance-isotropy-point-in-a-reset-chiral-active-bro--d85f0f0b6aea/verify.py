#!/usr/bin/env python3
"""Independent renewal-age quadrature for stationary chiral active motion moments."""
import math
import numpy as np
from scipy.integrate import quad


def formula(r, dr, omega, v, dt):
    a = r + dr - 1j * omega
    b = r + 4 * dr - 2j * omega
    mean = v / a
    q = v * v * (r - 2 * dr) / (a * a * b)
    trace = 4 * dt / r + v * v * (r + 2 * dr) / (r * abs(a)**2)
    cov = np.array([[.5*(trace + q.real), .5*q.imag],
                    [.5*q.imag, .5*(trace - q.real)]])
    return mean, q, trace, cov


def age_moments(t, dr, omega, v, dt):
    c = dr - 1j * omega
    e = 4 * dr - 2j * omega
    z = v * (-np.expm1(-c*t)) / c
    z2 = 2 * v * v / (e-c) * ((-np.expm1(-c*t)) / c - (-np.expm1(-e*t)) / e)
    zabs2 = 4 * dt*t + 2*v*v * (t/c.conjugate() + np.expm1(-c.conjugate()*t)/(c.conjugate()**2)).real
    return z, z2, zabs2


def stationary_by_quadrature(r, dr, omega, v, dt):
    def integrate(fn):
        def f(t): return r * math.exp(-r*t) * fn(*age_moments(t,dr,omega,v,dt))
        return quad(f, 0, np.inf, epsabs=2e-10, epsrel=2e-10, limit=200)[0]
    mean = integrate(lambda z,z2,zabs2:z.real) + 1j*integrate(lambda z,z2,zabs2:z.imag)
    z2 = integrate(lambda z,z2,zabs2:z2.real) + 1j*integrate(lambda z,z2,zabs2:z2.imag)
    zabs2 = integrate(lambda z,z2,zabs2:zabs2)
    return mean, z2-mean**2, zabs2-abs(mean)**2


def main():
    checks=0
    grids=[
       (.25,.5,0,1.3,0), (1.0,.5,0,1.3,.2),
       (1,.5,1.3,.7,.25), (4,.5,8.0,2.0,4.0),
       (.11,.3,3.0,.8,.03), (.8,1.0,5,.4,1),
       (.2,.01,-1,.6,0.3), (10,3,-2,3,1),
       (.7,.35,0,.9,.1), (.7,.35,12,.9,.1),
       (1.1,.35,-12,.9,.1), (2,.35,2,.9,.1)
    ]
    for args in grids:
        r,dr,om,v,dt=args
        mean,q,trace,cov = formula(*args)
        qm,qq,qt = stationary_by_quadrature(*args)
        for a,b in [(mean,qm),(q,qq),(trace,qt)]:
            assert abs(a-b)<max(1,abs(a))*1e-7, (args,a,b)
            checks+=1
        assert min(np.linalg.eigvalsh(cov))>-1e-10
        checks+=1
        _,qflip,_,_ = formula(r,dr,-om,v,dt)
        assert abs(q.conjugate()-qflip)<1e-10
        checks+=1
        if abs(r-2*dr)<1e-12:
            assert abs(q)<1e-12 and abs(cov[0,0]-cov[1,1])<1e-12
            checks+=1
        else:
            assert abs(q)>1e-12
            checks+=1
        detv = (np.linalg.eigvalsh(cov)[-1]-np.linalg.eigvalsh(cov)[0])
        assert math.isclose(detv,abs(q),rel_tol=1e-9,abs_tol=1e-11)
        checks+=1
    print('PASS',checks,'independent finite quadrature, matrix, parity and isotropy checks')

if __name__=='__main__': main()
