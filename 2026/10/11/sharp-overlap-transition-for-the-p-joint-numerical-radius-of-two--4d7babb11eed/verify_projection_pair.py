"""Independent finite sanity checks for the analytic two-projector p-joint-radius theorem.
No finite test is substituted for its analytic proof.
"""
from fractions import Fraction as F
from math import acos, cos, sin, log, isclose


def special_poly(c, z):
    return (2-c*c+2*c*z+(2*c*c-1)*z*z)/4

for c in [F(0),F(1,10),F(1,4),F(2,5),F(1,2),F(3,4),F(1)]:
    peak = c/(1-2*c*c) if c < F(1,2) else F(1)
    optimum = (1-c*c)**2/(2*(1-2*c*c)) if c < F(1,2) else (1+c)**2/4
    assert special_poly(c,peak)==optimum
    for j in range(-100,101):
        z=F(j,100)
        assert special_poly(c,z)<=optimum


def objective(p,g,theta):
    return (cos(theta)**(2*p)+cos(g-theta)**(2*p))/2

def threshold_profile(p,c):
    g=acos(c)
    alpha=g/2
    if c >= 1-1/p:
        return alpha, objective(p,g,alpha)
    def R(th):
        return log(sin(g-th)/sin(th))/log(cos(th)/cos(g-th))
    lo=1e-14
    hi=alpha*(1-1e-7)
    assert R(lo)>2*p-1 > R(hi),(p,c,R(lo),R(hi))
    for _ in range(100):
        mid=(lo+hi)/2
        if R(mid)>2*p-1: lo=mid
        else: hi=mid
    th=(lo+hi)/2
    return th,objective(p,g,th)

for p in [1.0,1.5,2.0,3.0,4.0,5.0]:
    for c in [0.1,0.25,0.4,0.5,0.7,0.9]:
        theta, f=threshold_profile(p,c)
        gamma=acos(c)
        sampled_max=max(objective(p,gamma,j*gamma/6000) for j in range(6001))
        assert f+2e-10 >= sampled_max,(p,c,theta,f,sampled_max)
        assert isclose(f,objective(p,gamma,theta),rel_tol=1e-14)
        assert isclose(f,objective(p,gamma,gamma-theta),rel_tol=1e-14)
        if c >= 1-1/p:
            assert isclose(theta,gamma/2,rel_tol=1e-14)
        else:
            assert 0 < theta < gamma/2

print('TWO_PROJECTION_P_JOINT_PHASE_AND_EUCLIDEAN_EXACT_CHECKS_OK')
