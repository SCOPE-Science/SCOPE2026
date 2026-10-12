#!/usr/bin/env python3
"""Self-contained Gaussian-moment and sharp-spectrum regression checks.

The analytic all-dimension proof is in RESULT.md. Tests here are complementary.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from itertools import product
import math
import random


def poly_add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
    return {k:v for k,v in c.items() if v}


def poly_mul(a, b):
    out = {}
    for x, u in a.items():
        for y, v in b.items():
            k = (x[0]+y[0], x[1]+y[1])
            out[k] = out.get(k, F(0)) + u*v
    return {k:v for k,v in out.items() if v}


def gaussian_moment(power):
    if power & 1:
        return 0
    ans=1
    for z in range(power-1, 0, -2):
        ans*=z
    return ans


def gaussian_average(poly):
    return sum((v*gaussian_moment(a)*gaussian_moment(b)
                for (a,b),v in poly.items()), F(0))


def gauss_energy_2d():
    # Exact polynomial evaluation of f(x - alpha G_tau) - f(x).
    h1,h2=F(1),F(3)
    x1,x2=F(1,2),F(-2,5)
    g1,g2=h1*x1,h2*x2
    tau,alpha=F(1,7),F(1,5)
    one={(0,0):F(1)}
    u1={(1,0):F(1)};u2={(0,1):F(1)}
    quad=poly_add({(2,0):h1}, {(0,2):h2})
    linear=poly_add({(0,1):g2}, {}) # residual r=(0,g2)
    corr={k:tau*v/2 for k,v in quad.items()}
    scalar=poly_add(linear,corr)
    G1=poly_add({(0,0):g1},poly_mul(scalar,u1))
    G2=poly_mul(scalar,u2)
    step1=poly_add({(0,0):x1},{k:-alpha*v for k,v in G1.items()})
    step2=poly_add({(0,0):x2},{k:-alpha*v for k,v in G2.items()})
    actual=gaussian_average(poly_add({k:h1*v/2 for k,v in poly_mul(step1,step1).items()},
                                     {k:h2*v/2 for k,v in poly_mul(step2,step2).items()}))
    actual-= (h1*x1*x1+h2*x2*x2)/2
    tr=h1+h2
    tr2=h1*h1+h2*h2
    tr3=h1**3+h2**3
    m3=tr**3+6*tr*tr2+8*tr3
    numerator = h1*g1*g1 + h2*g2*g2 + g2*g2*tr + h2*g2*g2
    predicted=-alpha*(g1*g1+g2*g2)+alpha*alpha*(numerator+tau*tau*m3/4)/2
    assert actual==predicted,(actual,predicted)


def exact_high_dim_witness():
    # d=3, kappa=5, s=1/3; all entries are rational.
    d=3;kappa=F(5);s=F(1,3)
    R=F(1)+(d+1/kappa)*s
    t=F(1)
    gamma=t*R/2
    assert gamma == F(31,30)


def planar_transition():
    with localcontext() as ctx:
        ctx.prec=70
        five=Decimal(5)
        root=five.sqrt()
        kstar=(five+root)/2
        def bound(k):
            delta=Decimal(1)-Decimal(1)/k
            eigen=(Decimal(3)-root)/4
            return (Decimal(5)/2-delta*(Decimal(1)/2+eigen))/2
        assert abs(bound(kstar)-1) < Decimal('1e-63')
        for k in [Decimal('1'),Decimal('2'),Decimal('3.5'),kstar,Decimal('8'),Decimal('200')]:
            gamma=bound(k)
            formula=Decimal(5)/4-(Decimal(5)-root)/8*(1-1/k)
            assert abs(gamma-formula) < Decimal('1e-63')


def random_inequalities():
    rng=random.Random(342026)
    # For any given hint quality s, test the exact 2D spectral bound.
    for j in range(24000):
        s=rng.random()
        delta=rng.random()
        z=math.sqrt(1-2*s+5*s*s)
        lam=(1+s-z)/2
        R=1+(3-delta)*s-delta*lam
        t=min(1,1/(2*s)) if s else 1
        upper=1.25-(5-math.sqrt(5))/8*delta
        assert t*R/2<=upper+2e-13,(s,delta,R,upper)
    # For d>=3 with s>=0, exact trace inequality controls all H.
    for d in range(3,12):
        for j in range(900):
            s=rng.random();k=1+100*rng.random()
            t=min(1,1/(d*s)) if s else 1
            Rbound=1+(d+1/k)*s
            assert t*Rbound/2<=1+1/(2*d*k)+1e-13


if __name__=='__main__':
    gauss_energy_2d()
    exact_high_dim_witness()
    planar_transition()
    random_inequalities()
    print('VERIFY_OK: Gaussian sixth moments, exact rational witness, planar algebra, sampled spectral envelope')
