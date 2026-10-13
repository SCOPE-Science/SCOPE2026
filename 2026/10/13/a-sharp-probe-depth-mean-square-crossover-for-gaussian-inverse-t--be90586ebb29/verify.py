"""Symbolic and numerical checks for a two-dimensional inverse-trace SLQ benchmark.

Uses exact SymPy arithmetic for algebraic identities, deterministic quadrature
for angular integrals, and seeded Gaussian sampling for numerical diagnostics.
Those diagnostics are not substitutes for the analytical proof.
"""
from __future__ import annotations
import math
import random
import sympy as sp


def check(symbolic=True):
    u, b, B = sp.symbols('u b B', positive=True)
    a = u**2*b
    target = 1/a + 1/b
    e_q = 2 / sp.sqrt(a*b)
    e_q2 = 4*(a+b)/(a*b)**sp.Rational(3, 2)
    v_q = sp.simplify(e_q2 - e_q**2)
    v_d = 2*(1/a**2 + 1/b**2)
    s = sp.factor((e_q-target)**2+v_q/B)
    d = sp.factor(2*v_d/B)
    star = 4*(u**4-u**3+u**2-u+1)/(u-1)**4
    assert sp.simplify(v_q - 4*(u*u-u+1)/(b*b*u**3)) == 0
    assert sp.simplify(s - ((u-1)**4/u**4 + 4*(u*u-u+1)/(B*u**3))/b**2) == 0
    assert sp.simplify(d - 4*(1+u**-4)/(B*b**2)) == 0
    assert sp.simplify(d-s - (4*(u**4-u**3+u**2-u+1)-B*(u-1)**4)/(B*b*b*u**4)) == 0
    assert sp.simplify(sp.diff(star,u)+4*(u+1)*(3*u*u-4*u+3)/(u-1)**5) == 0
    assert sp.simplify((d/2-s).subs(B,2)-2*(u-1)**2/(b*b*u**3)) == 0
    assert sp.simplify((d-s).subs(B,4)-(3*u*u-5*u+3)/(b*b*u**3)) == 0
    for uu,bb in [(sp.Rational(2),sp.Rational(3)),(sp.Rational(3,2),sp.Rational(1,3)),(sp.Rational(5),sp.Rational(1))]:
        aa=uu*uu*bb
        gg=sp.Matrix([sp.Rational(2,3), sp.Rational(3,5)])
        H=sp.diag(aa,bb)
        v=gg/sp.sqrt(gg.dot(gg))
        alpha=sp.simplify((v.T*H*v)[0])
        w=H*v-alpha*v
        beta=sp.sqrt(sp.simplify(w.dot(w)))
        v2=w/beta
        alpha2=sp.simplify((v2.T*H*v2)[0])
        T2=sp.Matrix([[alpha,beta],[beta,alpha2]])
        q1=sp.simplify(gg.dot(gg)/alpha)
        q2=sp.simplify(gg.dot(gg)*T2.inv()[0,0])
        assert sp.simplify(q1 - gg.dot(gg)**2 / (gg.T*H*gg)[0]) == 0
        assert sp.simplify(q2 - (gg.T*H.inv()*gg)[0]) == 0
        assert sp.simplify(T2.det()-H.det())==0

    # High-order periodic trapezoidal quadrature, independent of SymPy symbolic work.
    for aa,bb in [(1.0,1.0),(2.0,1.0),(16.0,3.0),(100.0,1.0)]:
        size=16384
        iq=iq2=0.0
        for k in range(size):
            th=2.0*math.pi*(k+.5)/size
            den=aa*math.cos(th)**2+bb*math.sin(th)**2
            iq+=1.0/den
            iq2+=1.0/(den*den)
        iq/=size; iq2/=size
        assert math.isclose(iq,1/math.sqrt(aa*bb),rel_tol=1e-9)
        assert math.isclose(iq2,(aa+bb)/(2*(aa*bb)**1.5),rel_tol=1e-9)

    def rate(v):
        return 4*(v**4-v**3+v*v-v+1)/(v-1)**4
    assert rate(1.0001)>1.0e16
    assert abs(rate(10**5)-4)<.00013
    for bbgt in [6,8,10,12,24,50]:
        lo,hi=1.000000001, 1e6
        for _ in range(100):
            mid=(lo+hi)*.5
            if rate(mid)>bbgt:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        assert abs(rate(root)-bbgt)<5e-8
        assert rate(root*.99)>bbgt and rate(root*1.01)<bbgt
        if bbgt==8:
            assert math.isclose(root,5.106964607734753,rel_tol=1e-11)

    rng=random.Random(20261009)
    n=160000
    for aa,bb in [(4.0,1.0),(36.0,1.0)]:
        smq=smq2=smd=smd2=0.0
        for _ in range(n):
            x,y=rng.gauss(0,1),rng.gauss(0,1)
            qq=(x*x+y*y)**2/(aa*x*x+bb*y*y)
            dd=x*x/aa+y*y/bb
            smq+=qq; smq2+=qq*qq; smd+=dd; smd2+=dd*dd
        smq/=n; smq2/=n; smd/=n; smd2/=n
        assert math.isclose(smq,2/math.sqrt(aa*bb),rel_tol=.016)
        assert math.isclose(smq2,4*(aa+bb)/(aa*bb)**1.5,rel_tol=.04)
        assert math.isclose(smd,1/aa+1/bb,rel_tol=.016)
        assert math.isclose(smd2-(smd*smd),2*(1/aa**2+1/bb**2),rel_tol=.05)
    print('VERIFY_OK exact symbolic identities, three rational 2-node Krylov certificates, 8 angular integrations, six budget boundaries, 320000 Gaussian diagnostics')

if __name__ == '__main__':
    check()
