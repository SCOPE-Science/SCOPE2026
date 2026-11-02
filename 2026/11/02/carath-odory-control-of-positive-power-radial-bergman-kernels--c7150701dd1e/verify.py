"""Finite independent arithmetic and sampled tests for radial Bergman-kernel identities.

The infinite-dimensional theorem requires the written harmonic-minimum proof.
"""
from fractions import Fraction
from math import cos, sin, pi

def tests():
    checked = 0
    for g in [Fraction(1,3), Fraction(1,2), Fraction(1), Fraction(7,3), Fraction(5)]:
        for q in [Fraction(0), Fraction(1,7), Fraction(1), Fraction(3), Fraction(29)]:
            c = g / (1 + q)
            d = g - c
            for n in range(48):
                moment = 1 / Fraction(n+1) + q / (n + g + 1)
                exact = 1 / moment
                mixed = Fraction(n+1, 1) / (1+q) * (1 + d / (n+c+1))
                assert exact == mixed
                checked += 1
    for x in [i/80 for i in range(80)]:
        for j in range(1, 240):
            theta = 2*pi*j/240
            t = complex(cos(theta), sin(theta))
            v = ((1-t)/(1-x*t)**2).real
            rhs = (1-cos(theta)) * (1+2*x-x*x*(1+2*cos(theta))) / (1-2*x*cos(theta)+x*x)**2
            assert v >= -1e-11 and abs(v-rhs)<1e-6*(1+abs(rhs))
            checked += 1
    for g in [.33, 1., 2.5, 11.]:
        for q in [0., .2, 1., 9.]:
            c=g/(1+q); d=g-c
            for rad in [.0, .4, .8, .95]:
                for j in range(64):
                    t=rad*complex(cos(2*pi*j/64),sin(2*pi*j/64))
                    # convergent coefficient series; 1200 terms suffice at radius <= .95
                    K=complex(0)
                    power=1+0j
                    for n in range(1200):
                        K += ((n+1)/(1+q)*(1+d/(n+1+c)))*power
                        power *= t
                    H=((1-t)*K).real
                    lower=(1+g)/(1+g+q)*(1-rad)/(1+rad)
                    assert H + 3e-9 >= lower
                    checked += 1
    return checked

if __name__=='__main__':
    print('PASS finite assertions:', tests())
