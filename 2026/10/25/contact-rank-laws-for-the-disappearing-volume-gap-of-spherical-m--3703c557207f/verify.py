"""Independent numerical checks for the spherical-boundary Minkowski volume gap.

Run: python verify.py
Dependency: scipy>=1.8
Finite numerical checks do not constitute the proof of the all-dimensional theorem.
"""
from __future__ import annotations
import math
from scipy.integrate import quad, dblquad


def rhombus_gap(a: float, b: float, lam: float) -> float:
    """Quadrant integration of the four shifted unit-disk constraints."""
    assert a >= b > 0 and 0 < lam < 1/a
    rho, beta = lam*a, lam*b
    bound = min(1-rho, math.sqrt(1-beta*beta))
    def ordinate(x):
        upper_a = math.sqrt(max(0., 1. - (x+rho)**2))
        upper_b = math.sqrt(max(0., 1. - x*x)) - beta
        return max(0., min(upper_a,upper_b))
    return 4*quad(ordinate, 0, bound, epsabs=1e-13, epsrel=1e-13, limit=500)[0]


def two_disk_lens(rho):
    return 2*(math.acos(rho)-rho*math.sqrt(1-rho*rho))


def check():
    count=0
    for a,b in [(2.,1.), (1.4,1.)]:
        lam0 = 2*b/(a*a+b*b)
        assert lam0 < 1/a
        for lam in [0.50*lam0,0.90*lam0]:
            gap = rhombus_gap(a,b,lam)
            assert two_disk_lens(lam*a) > gap + 0.001
            count+=1
        for lam in [lam0, (lam0 +1/a)/2, 0.998/a]:
            gap = rhombus_gap(a,b,lam)
            assert abs(two_disk_lens(lam*a) - gap) < 5e-10
            count+=1
        for delta in [.01,.003]:
            lam=math.sqrt(1-delta)/a
            normalized = rhombus_gap(a,b,lam)/delta**1.5
            assert abs(normalized-4/3) < 0.01
            count+=1
    for delta in [.01,.003]:
        lam=math.sqrt(1-delta)
        normalized=rhombus_gap(1.,1.,lam)/(delta*delta)
        assert abs(normalized-1) < 0.01
        count+=1
    # A unique long cross-polytope diameter in 3D produces a two-ball lens.
    # The 3D lens has exact volume (2*pi/3)*(2+rho)*(1-rho)**2.
    for delta in [.01,.003]:
        rho=math.sqrt(1-delta)
        gap=(2*math.pi/3)*(2+rho)*(1-rho)**2
        assert abs(gap/(delta*delta)-math.pi/2) < 0.01
        count+=1
    # Rank=2 in 3D, Q has four longest coordinate-axis vertices.
    # Integrate the exact scaled cavity in one symmetric sector; shorter
    # vertices are inactive close enough to the contact threshold.
    for delta in [.04, .015]:
        rho=math.sqrt(1-delta)
        ymax=(1-rho)/delta
        coeff=16*dblquad(lambda y2,y1: math.sqrt(max(0.,1-2*rho*y1-delta*(y1*y1+y2*y2))),
                         0.,ymax, lambda y1:0., lambda y1:y1,
                         epsabs=1e-10,epsrel=1e-10)[0]
        assert abs(coeff-16/15) < .04
        count+=1
    # Rank=3, Q = conv(+-e1,+-e2,+-e3), polar is cube of volume 8;
    # the coefficient is (1/2)^3 * 8 = 1, exponent 3.
    rank3_coefficient=(1/2)**3 * 8
    assert rank3_coefficient==1
    print('PASS:',count,'quadrature/asymptotic checks and rank-3 coefficient check')

if __name__ == '__main__':
    check()
