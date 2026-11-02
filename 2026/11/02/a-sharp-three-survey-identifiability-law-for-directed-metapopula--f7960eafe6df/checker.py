"""Exact-rational checks for the three-survey directed-dispersal inverse law.

This code is independent of floating-point and uses Python's standard library only.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def equilibrium(c, phi, gamma, h, e):
    assert all(z > 0 for z in (c, phi, gamma, h, e)) and h <= 1
    assert c*h > e*(h+phi*(1-h)), "parameters must support positive occupancy"
    p = (c*h - e*(phi*(1-h)+h))/(c+e*(gamma-1))
    assert 0 < p < h
    assert c*(h-p) == e*(phi*(1-h)+gamma*p+(h-p))
    return p


def determinant3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def inverse_three(data):
    # data = (h,e,p) at (h1,e1),(h2,e1),(h1,e2).
    (h1,e1,p1),(h2,e1b,p2),(h1b,e2,p3) = data
    assert h1==h1b and e1==e1b and h1!=h2 and e1!=e2
    U1,U2,U3 = ((h-p)/e for h,e,p in data)
    D = (U3-U1)/(p3-p1)
    B = (U2-U1-D*(p2-p1))/(h2-h1)
    a = U1-B*h1-D*p1
    b = a+B
    d = b+D
    assert a>0 and b>0 and d>0
    return F(1,1)/b,a/b,d/b


def test_explicit():
    c,phi,gamma=F(2),F(1,2),F(3,2)
    h1,h2,e1,e2=F(3,4),F(1,2),F(1,4),F(1,2)
    data=[(h1,e1,equilibrium(c,phi,gamma,h1,e1)),
          (h2,e1,equilibrium(c,phi,gamma,h2,e1)),
          (h1,e2,equilibrium(c,phi,gamma,h1,e2))]
    assert tuple(p for _,_,p in data)==(F(41,68),F(13,34),F(17,36))
    A=[[1-h,h-p,p] for h,e,p in data]
    assert determinant3(A)==F(5,153)
    assert inverse_three(data)==(c,phi,gamma)
    # A whole fixed-e habitat response is indistinguishable for the two triples.
    for h in (F(1,2),F(2,3),F(3,4),F(4,5),F(1)):
        assert equilibrium(c,phi,gamma,h,e1)==equilibrium(F(15,4),F(1),F(3),h,e1)
        assert equilibrium(c,phi,gamma,h,e1)==(15*h-1)/17
    assert equilibrium(c,phi,gamma,h1,e2)!=equilibrium(F(15,4),F(1),F(3),h1,e2)
    return data


def test_exhaustive():
    rates = [F(1), F(3,2), F(2), F(3), F(4)]
    prefs = [F(1,2), F(2,3), F(1), F(3,2), F(2)]
    habitats = [F(1,2),F(2,3),F(3,4),F(4,5),F(1)]
    checked=0
    for c,phi,gamma in product(rates,prefs,prefs):
        e1,e2=c/10,c/5
        for h1,h2 in product(habitats, habitats):
            if h1==h2: continue
            data=[(h1,e1,equilibrium(c,phi,gamma,h1,e1)),
                  (h2,e1,equilibrium(c,phi,gamma,h2,e1)),
                  (h1,e2,equilibrium(c,phi,gamma,h1,e2))]
            p1,p2,p3 = (item[2] for item in data)
            assert p3<p1
            mat=[[1-h,h-p,p] for h,e,p in data]
            assert determinant3(mat)==(h2-h1)*(p3-p1)!=0
            assert inverse_three(data)==(c,phi,gamma)
            # Entire fixed-e curve is affine; survey points collinear.
            hm=(h1+h2)/2
            pm=equilibrium(c,phi,gamma,hm,e1)
            assert 2*pm==p1+p2
            # Direct equation holds at each survey.
            for h,e,p in data:
                U=(h-p)/e
                assert U==phi/c*(1-h)+(h-p)/c+gamma/c*p
            checked+=1
    assert checked==2500
    return checked


if __name__ == '__main__':
    print('Exact example:', test_explicit())
    print('All-positive rational L-design cases:', test_exhaustive())
    print('PASS: equilibrium, determinant, recovery, single-axis alias, and no finite rounding')
