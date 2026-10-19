"""Reproduce numerical checks for the explicit sharp radius formulas."""
import cmath
import math

SIN, COS = math.sin, math.cos
STAR = math.atan((SIN(1)-COS(1))/(SIN(1)+COS(1)-1))

def h(s):
    return math.cosh(math.sqrt(max(0.0,1.0-s*s)))

def hp(s):
    v = math.sqrt(max(0.0,1.0-s*s))
    return -s * (math.sinh(v)/v if v>1e-9 else 1.0)

def psi(s,a):
    return hp(s)*COS(s+a) + h(s)*SIN(s+a) - SIN(a)

def branch_s(a):
    if a==0: return 0.0
    if a>=STAR: return -1.0
    lo,hi=-1.0,0.0
    assert psi(lo,a)<0<psi(hi,a)
    for _ in range(100):
        mid=(lo+hi)/2
        if psi(mid,a)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def norm_sq(s,a):
    d=h(s)+COS(s+2*a)
    return (h(s)-COS(s))/d if d>1e-15 else float('inf')

def radius(a):
    if a>=STAR:
        return SIN(.5)/COS(a-.5)
    return math.sqrt(norm_sq(branch_s(a),a))

def direct_radius(a, theta):
    w=cmath.exp(1j*theta)
    z=(cmath.exp(w)-1)/(cmath.exp(w)+cmath.exp(-2j*a))
    return abs(z)

def run():
    assert 0.6679<STAR<0.6680
    assert abs(radius(0)-math.tanh(.5))<1e-14
    assert abs(radius(STAR)-0.4862647618817628)<1e-13
    assert abs(radius(1.56)-SIN(.5)/COS(1.06))<1e-14
    for a in [0, 0.1, 0.3, 0.5, STAR-1e-5, STAR, STAR+1e-5, 0.8, 1.1, 1.55]:
        s=branch_s(a)
        assert -1-1e-14<=s<=1e-14
        if 0<a<STAR: assert abs(psi(s,a))<2e-14
        r=radius(a)
        if a>=STAR: assert abs(r*r-norm_sq(-1,a))<1e-12
        # Direct boundary search uses complex exponentials and Möbius inverse.
        brute=min(direct_radius(a,2*math.pi*j/36000) for j in range(36000))
        assert abs(brute-r)<2e-6, (a,r,brute)
        for k in range(4001):
            ss=-1+2*k/4000
            assert norm_sq(ss,a)>=r*r-2e-12, (a,ss)
    from math import e
    c=e*(e-1)*(3-e)/(2*(e+1)**2)
    for a in [0.01,0.005]:
        estimated=(radius(a)-radius(0))/a**2
        assert abs(estimated-c)<2e-5
    print('checks_passed: boundary grids, analytic branches, endpoint values, local series')

if __name__=='__main__': run()
