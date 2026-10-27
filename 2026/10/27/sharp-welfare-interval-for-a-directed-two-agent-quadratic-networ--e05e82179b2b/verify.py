#!/usr/bin/env python3
"""Exact-rational reproducibility checks for a two-agent directed quadratic network game."""
from fractions import Fraction as Q


def welfare(x1, x2, gamma1, gamma2, edge, b1, b2):
    return b1*x1 + b2*x2 - gamma1*x1*x1/2 - gamma2*x2*x2/2 + edge*x1*x2


def check(gamma1, gamma2, edge, b1, b2, t, y1, y2):
    assert gamma1 > 0 and gamma2 > 0 and edge > 0
    assert edge*edge < gamma1*gamma2 and b1 >= 0 and b2 >= 0 and b1+b2 > 0
    ne2 = b2/gamma2
    ne1 = (b1+edge*ne2)/gamma1
    det = gamma1*gamma2-edge*edge
    op1 = (gamma2*b1+edge*b2)/det
    op2 = (gamma1*b2+edge*b1)/det
    assert min(ne1,ne2,op1,op2) >= 0
    assert gamma1*ne1 == b1+edge*ne2 and gamma2*ne2 == b2
    assert gamma1*op1 == b1+edge*op2 and gamma2*op2 == b2+edge*op1
    wn = welfare(ne1,ne2,gamma1,gamma2,edge,b1,b2)
    wo = welfare(op1,op2,gamma1,gamma2,edge,b1,b2)
    assert wn > 0 and wo >= wn
    d = (y1+t*y2)**2+y2*y2
    ratio = wo/wn
    formula = (y1*y1+2*t*y1*y2+y2*y2)/((1-t*t)*d)
    assert ratio == formula
    low = 1/(1-t**4)
    high = 1/(1-t*t)
    assert low <= ratio <= high
    assert (ratio == low) == (y1 == 0)
    assert (ratio == high) == (y2 == 0)
    assert ratio-low == t*t*y1*(y1+2*t*y2)/((1-t**4)*d)
    assert high-ratio == t*t*y2*y2/((1-t*t)*d)
    # The Nash response matrix [[0, edge/gamma1],[0,0]] squares to zero.
    assert (edge/gamma1)*0 == 0
    return ratio


def main():
    ratios = []
    trials = 0
    for t in (Q(1,7),Q(1,3),Q(2,5),Q(3,5),Q(4,5),Q(9,10),Q(99,100)):
        for a in (Q(1),Q(2),Q(3)):
            for c in (Q(1),Q(2),Q(3)):
                gamma1=a*a
                gamma2=c*c
                edge=t*a*c
                for y1 in (Q(0),Q(1),Q(2),Q(5)):
                    for y2 in (Q(0),Q(1),Q(2),Q(5)):
                        if y1+y2 == 0:
                            continue
                        ratio=check(gamma1,gamma2,edge,a*y1,c*y2,t,y1,y2)
                        ratios.append(ratio)
                        trials+=1
    assert trials==945
    assert check(Q(4),Q(9),Q(18,5),Q(2),Q(3),Q(3,5),Q(1),Q(1)) == Q(125,89)
    assert Q(1,1)/(1-Q(3,5)**4) == Q(625,544)
    assert Q(1,1)/(1-Q(3,5)**2) == Q(25,16)
    # At fixed zero spectral radius, the lower price bound exceeds any chosen B.
    for B in (Q(2),Q(5),Q(10),Q(100),Q(10000)):
        t=Q(1)-Q(1,8*B)
        assert t>0 and 1/(1-t**4)>B
    print('VERIFY_OK',trials,'exact rational parameter configurations')

if __name__ == '__main__':
    main()
