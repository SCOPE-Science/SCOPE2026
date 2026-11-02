#!/usr/bin/env python3
"""Exact rational consistency checks for a stationary harmonic run-and-tumble model.

These finite checks supplement, and do not replace, the analytical proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def polynomial(g, a, b, d):
    s = a + b
    p = a * b
    return (2*(d-4)*g**4 + (7*d-34)*s*g**3
            + ((6*d-54)*s*s + (8*d+4)*p)*g*g
            + (12*d*s*p-36*s**3)*g
            - 4*s*s*(2*s*s+p))


def displayed_cov(g, a, b, d, v=F(1)):
    den = (d*d*(d+2)*(g+a)*(g+2*a)*(g+b)*(g+2*b)
           *(a+b)*(g+a+b)*(g+a+2*b)*(g+2*a+b))
    return 2*v**4*polynomial(g,a,b,d)/den


def generator_cov(g, a, b, d, v=F(1)):
    ex = v*v/(d*a*(a+g))
    ey = v*v/(d*b*(b+g))
    # u, w are orthogonal components of one uniformly redrawn sphere direction.
    c1 = v/(d*(d+2)*(a+g)) # E[X u w^2]
    c2 = v/(d*(d+2)*(b+g)) # E[Y w u^2]
    c3 = v*(c1+c2)/(a+b+g) # E[X Y u w]
    c4 = (2*v*c1+g*ex/d)/(2*a+g) # E[X^2 w^2]
    c5 = (2*v*c2+g*ey/d)/(2*b+g) # E[Y^2 u^2]
    c6 = v*(c5+2*c3)/(a+2*b+g) # E[X u Y^2]
    c7 = v*(c4+2*c3)/(2*a+b+g) # E[X^2 Y w]
    exxyy = v*(c6+c7)/(a+b)
    return exxyy-ex*ey


def renewal_cov(g, a, b, d, v=F(1)):
    """Independent derivation from conditional sphere moments and Poisson ages."""
    def lap(k):
        return g/(g+k)
    coeff = (1, -2, 1)
    def mean_a(x, z):
        return (lap(z)-2*lap(z+x)+lap(z+2*x))/(x*x)
    def mean_ab(x, y):
        return sum(coeff[i]*coeff[j]*lap(i*x+j*y)
                   for i,j in product(range(3), repeat=2))/(x*x*y*y)
    zx = mean_a(a,F(0))/(1-lap(2*a))
    zy = mean_a(b,F(0))/(1-lap(2*b))
    ab = mean_ab(a,b)
    rho = lap(2*(a+b))
    zxy = (ab + mean_a(a,2*b)*zy + mean_a(b,2*a)*zx)/(1-rho)
    same = ab/(1-rho)
    return v**4*(zxy-zx*zy-F(2)*same/(d+2))/d**2


def check():
    count = 0
    rng = Random(20261029)
    examples = [(2,1,1,F(1)),(3,1,2,F(2)),(4,2,5,F(4)),
                (5,1,1,F(6)),(5,1,2,F(9)),(5,1,2,F(10)),
                (10,1,1,F(1)),(12,3,7,F(4))]
    for _ in range(340):
        d = rng.randint(2,35)
        a = F(rng.randint(1,14),rng.randint(1,10))
        b = F(rng.randint(1,14),rng.randint(1,10))
        g = F(rng.randint(1,14),rng.randint(1,10))
        examples.append((d,a,b,g))
    for d,a,b,g in examples:
        a,b,g=F(a),F(b),F(g)
        for v in (F(1),F(3,2)):
            assert displayed_cov(g,a,b,d,v)==generator_cov(g,a,b,d,v)
            assert displayed_cov(g,a,b,d,v)==renewal_cov(g,a,b,d,v)
            count+=2
        assert displayed_cov(g,a,b,d)==displayed_cov(g,b,a,d)
        count+=1
        if d<=4:
            assert displayed_cov(g,a,b,d)<0
            count+=1
        if d>=5:
            g0=3*(a+b)/(d-4)
            assert polynomial(g0,a,b,d)<=0
            assert (polynomial(g0,a,b,d)==0)==(a==b)
            count+=2
    for d in range(5,41):
        for mu in (F(1,3),F(1),F(7,4)):
            g0=6*mu/(d-4)
            assert displayed_cov(g0,mu,mu,d)==0
            assert displayed_cov(g0/2,mu,mu,d)<0
            assert displayed_cov(2*g0,mu,mu,d)>0
            count+=3
    # Quasi-static orientation: exact spherical fourth cumulant.
    for d in (2,3,4,5,11,31):
        for a,b in ((F(1),F(2)),(F(3,7),F(5,2))):
            assert displayed_cov(F(0),a,b,d)==-2/(d*d*(d+2)*a*a*b*b)
            count+=1
    print('PASS:',count,'exact-rational assertions')

if __name__=='__main__':
    check()
