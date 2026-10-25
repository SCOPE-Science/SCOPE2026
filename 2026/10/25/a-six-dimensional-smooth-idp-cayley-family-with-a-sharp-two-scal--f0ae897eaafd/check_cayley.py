#!/usr/bin/env python3
"""Exact arithmetic checks for Cayley boxes; no external dependencies."""
from math import comb


def blocks(k):
    for b0 in range(k+1):
        for b1 in range(k-b0+1):
            for b2 in range(k-b0-b1+1):
                yield b0,b1,b2,k-b0-b1-b2


def count(k,a,b):
    total=0
    for c in blocks(k):
        total+= ((1+a*c[0]+b*c[1]+c[2]+c[3])
                 *(1+a*c[0]+c[1]+b*c[2]+c[3])
                 *(1+a*c[0]+c[1]+c[2]+b*c[3]))
    return total


def h_formula(a,b):
    return (1,
            a**3+3*a*a+3*a+12*b+6,
            4*a**3+3*a*a*b+6*a*a+12*a*b+9*a+9*b*b+18*b+6,
            (a+b+1)**3)


def reconstruct(k,h):
    return sum(h[j]*comb(k+6-j,6) for j in range(min(k,3)+1))


def discrepancy_coeff(a,b):
    return (15*a**6+42*a**5+93*a**4+131*a**3+123*a*a+87*a+30
      +b*(21*a**5+117*a**4+300*a**3+387*a*a+387*a+186)
      +b*b*(6*a**4+132*a**3+306*a*a+495*a+378)
      +b**3*(-a**3+51*a*a+177*a+282)
      +69*b**4)


def polynomial_ray(t):
    return (-38109*t**6+2554782*t**5+124559085*t**4
           +13812575*t**3+503943*t*t+6783*t+30)


def run():
    ct=0
    for a in range(1,13):
        for b in range(1,17):
            h=h_formula(a,b)
            values=[count(k,a,b) for k in range(7)]
            assert all(values[k]==reconstruct(k,h) for k in range(7)),(a,b,values,h)
            assert h[1]**2>h[2]
            assert h[2]**2-h[1]*h[3]==discrepancy_coeff(a,b)
            ct+=1
    for t in range(1,201):
        assert discrepancy_coeff(t,36*t)==polynomial_ray(t)
        assert (polynomial_ray(t)<0)==(t>=100)
    a,b=100,3600
    h=h_formula(a,b)
    assert h==(1,1073506,233085706,50694081101),h
    assert discrepancy_coeff(a,b)==-91453884891670
    assert discrepancy_coeff(99,3564)==395358876665409
    print('CAYLEY_HSTAR_EXACT_OK pairs=',ct,'ray_steps=200','witness_h=',h)

if __name__=='__main__':run()
