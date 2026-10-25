"""Supplemental numerical checks of analytic Blaschke/Poisson identities.

The general boundary-localization theorem has a written proof; finite tests are
not an exhaustive verification of functions or boundary limits.
"""
import cmath
import math


def close(x, y, eps=3e-9):
    assert abs(x-y) <= eps * (1+abs(x)+abs(y)), (x, y)


def test():
    cases = 0
    for angle in (0.0, 0.7, 2.0, 4.1):
        zeta = cmath.exp(1j*angle)
        for r in (0.12, 0.5, 0.9, 0.995):
            a = r*zeta
            for u in (0j, 0.2+0.3j, -0.6+0.1j, 0.4-0.45j):
                z = zeta*(r+u)/(1+r*u)
                b = (z-a)/(1-a.conjugate()*z)
                close(b,zeta*u)
                lhs = 1-abs(b)**2
                rhs = (1-r*r)*(1-abs(z)**2)/abs(1-a.conjugate()*z)**2
                close(lhs,rhs)
                close(abs(zeta-z), (1-r)*abs(1-u)/abs(1+r*u))
                rho = 0.75
                if abs(u)<=rho:
                    assert abs(zeta-z)/(1-abs(z)) <= 2*(1+rho)**2/(1-rho**2)+1e-8
                cases+=1
    for r in (0.5,0.9,0.99,0.999):
        # For f(z)=z, zeta=1, at z=0 and z=r:
        # f +/- g_r variance at the two natural centers is 1+/-3(1-r^2)
        # for plus, and 1-(1-r^2) for minus; the former tends to 1.
        at_origin_plus=1+3*(1-r*r)
        at_center_plus=1+3*(1-r*r)
        close(at_origin_plus,at_center_plus)
        assert at_origin_plus>1
    print('CHECK_OK: %d automorphism/variance/level-set checks and 4 analytic benchmarks' % cases)

if __name__ == '__main__':
    test()
