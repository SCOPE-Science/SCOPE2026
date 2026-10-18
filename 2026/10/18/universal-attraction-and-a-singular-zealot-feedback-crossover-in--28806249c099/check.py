"""Reproduce finite numerical consequences of a reciprocal-complexity mean-field theorem.

The claims for continuum parameters and singular limits rest on analysis, not this script.
Run: python3 check.py (Python 3 standard library only).
"""
import math


def drift(u, z, rho):
    return (1 - z - u) * u ** (1 + rho) - (u - z) * (1 - u) ** (1 - rho)


def a_z(u, z):
    return math.log(u / (u-z)) - math.log((1-u) / (1-u-z))


def b(u):
    return -math.log(u * (1-u))


def equilibrium(z, rho):
    assert 0 < z < 0.5 and abs(rho) < 1
    if rho == 0:
        return 0.5
    if rho < 0:
        return 1 - equilibrium(z, -rho)
    lo, hi = math.nextafter(z, 1.0), 0.5
    for _ in range(150):
        m = (lo + hi)/2
        if m == lo or m == hi:
            break
        if a_z(m, z) / b(m) > rho:
            lo = m
        else:
            hi = m
    return (lo + hi)/2


def C(u):
    return (1-2*u)/(u*(1-u)*(-math.log(u*(1-u))))


def universal(c):
    if c == 0:
        return .5
    if c < 0:
        return 1-universal(-c)
    lo, hi = 1e-15, 0.5
    for _ in range(130):
        m = (lo+hi)/2
        if C(m) > c:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def main():
    checks=0
    for z in (.01, .025, .07, .225, .4):
        for rho in (-.9,-.6,-.1,0,.1,.6,.9):
            u=equilibrium(z,rho)
            assert z<u<1-z and abs(drift(u,z,rho))<3e-13
            assert abs(u+equilibrium(z,-rho)-1)<1e-13
            if rho>0:
                assert z<u<.5
                assert drift((z+u)/2,z,rho)>0
                assert drift((u+1-z)/2,z,rho)<0
            if rho<0:
                assert .5<u<1-z
            checks+=1
    for z in (.025,.075,.225):
        eps=1e-6
        empirical=(equilibrium(z,eps)-equilibrium(z,-eps))/(2*eps)
        analytical=-(1-2*z)*math.log(4)/(8*z)
        assert abs((empirical-analytical)/analytical)<1e-8
        checks+=1
    for rho in (.2,.5,.8):
        z=1e-7
        u=equilibrium(z,rho)
        ratio=(u-z)/z**(1+rho)
        assert abs(ratio-1)<.1
        checks+=1
    for c in (-4,-1,-.5,0,.5,1,4):
        for z in (1e-3,1e-4,1e-5):
            u=equilibrium(z,c*z)
            assert abs(u-universal(c))<.003
            checks+=1
    sample=equilibrium(.225,.6)
    assert .3068<sample<.3070
    print(f"PASS: {checks} finite checks; sample U*(0.225, 0.6)={sample:.15f}")
    print(f"Crossover U(1)={universal(1):.15f}; U(-1)={universal(-1):.15f}")
    print("Universal uniqueness and limiting statements are proved analytically in RESULT.md.")


if __name__ == '__main__':
    main()
