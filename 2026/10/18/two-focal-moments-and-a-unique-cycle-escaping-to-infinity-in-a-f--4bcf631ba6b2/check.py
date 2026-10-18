"""Supplementary numerical and exact-arithmetic diagnostics for compact-support Lienard return laws.
The universal statements are established analytically, not by finite computation.
Usage: python3 check.py
"""
import math
from fractions import Fraction as Q


def raw_moment(k, lam=Q(0)):
    # integral x F(x) (F(x)^2 + x^2/2) if k=3; x F(x) if k=1
    out = Q(0)
    for lo, hi, value in ((Q(-2), Q(-1), Q(1)), (Q(2), Q(3), Q(3, 5) + lam)):
        if k == 1:
            out += value * (hi**2 - lo**2)/2
        else:
            out += value**3 * (hi**2 - lo**2)/2 + value * (hi**4 - lo**4)/8
    return out


def one_round_energy(R, lam=0.0, subdivisions=240):
    # energy H=(x*x+y*y)/2, using x as the independent variable;
    # branch +1 before left turning, branch -1 after left turning.
    H = 0.5*R*R
    seq = ((3.0, 2.0, 0.6+lam, +1),
           (-1.0, -2.0, 1.0, +1),
           (-2.0, -1.0, 1.0, -1),
           (2.0, 3.0, 0.6+lam, -1))
    for a,b,f,sign in seq:
        dx=(b-a)/subdivisions
        def rhs(x,h):
            return x*f/(f-sign*math.sqrt(2*h-x*x))
        for k in range(subdivisions):
            x=a+k*dx
            d1=rhs(x,H)
            d2=rhs(x+dx/2,H+dx*d1/2)
            d3=rhs(x+dx/2,H+dx*d2/2)
            d4=rhs(x+dx,H+dx*d3)
            H+=dx*(d1+2*d2+2*d3+d4)/6
    return H-R*R/2


def check():
    asserts=0
    assert raw_moment(1)==0; asserts+=1
    assert raw_moment(3)==Q(51,25); asserts+=1
    assert raw_moment(1,Q(1,1000))==Q(1,400); asserts+=1
    for R in (12.0,20.0,40.0,80.0):
        scaled=one_round_energy(R)*R**3/2
        assert abs(scaled-51/25)<0.28, (R,scaled)
        asserts+=1
    for lam in (-0.001,-0.0002):
        predicted=math.sqrt(Q(102,125)/(-lam))
        assert one_round_energy(predicted*0.8,lam)>0
        assert one_round_energy(predicted*1.2,lam)<0
        asserts+=2
    for lam in (0.0,0.0002):
        assert one_round_energy(40,lam)>0
        asserts+=1
    print(f"{asserts} assertions passed; radial asymptotic and transition signs corroborated.")

if __name__=='__main__':
    check()
