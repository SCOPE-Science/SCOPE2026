"""Reproduce exact two-point boundary-chord moment identities for triangles.

Run: python checker.py. Dependency: sympy (see requirements.txt).
The universal inequalities are proved in RESULT.md; finite tests here are supplemental.
"""
from __future__ import annotations
import math
import random
import sympy as sp


def symbolic_moments():
    a, b, c = sp.symbols('a b c', positive=True)
    u, v = sp.symbols('u v', real=True)
    L = a + b + c
    # Same-edge distances: endpoints uniform independently on a segment.
    same2 = sp.integrate(sp.integrate((u-v)**2, (u, 0, 1)), (v, 0, 1))
    same4 = sp.integrate(sp.integrate((u-v)**4, (u, 0, 1)), (v, 0, 1))
    assert same2 == sp.Rational(1, 6)
    assert same4 == sp.Rational(1, 15)

    m2num, m4num = sum(z**4 for z in (a,b,c))/6, sum(z**6 for z in (a,b,c))/15
    for aa, bb, cc in ((a,b,c), (b,c,a), (c,a,b)):
        # Both segments originate at the same vertex, and cc is the opposite edge.
        D2 = aa**2*u**2 + bb**2*v**2 - (aa**2+bb**2-cc**2)*u*v
        avg2 = sp.integrate(sp.integrate(D2, (u,0,1)), (v,0,1))
        avg4 = sp.integrate(sp.integrate(sp.expand(D2**2), (u,0,1)), (v,0,1))
        closed2 = (aa**2+bb**2)/12 + cc**2/4
        S = aa**2 + bb**2 - cc**2
        closed4 = (aa**4+bb**4)/5 + (S*S + 2*aa**2*bb**2)/9 - (aa**2+bb**2)*S/4
        assert sp.cancel(avg2-closed2)==0
        assert sp.cancel(avg4-closed4)==0
        m2num += 2*aa*bb*avg2
        m4num += 2*aa*bb*avg4
    M2 = m2num/L**2
    M4 = m4num/L**2
    H2 = 16*(L/2)*(L/2-a)*(L/2-b)*(L/2-c)/L**4
    P2 = (a*b+a*c+b*c)/L**2
    formula2 = L**2*(1-3*H2)/24
    formula4 = L**4*(3-45*H2+20*H2*P2)/720
    assert sp.cancel(M2-formula2)==0
    assert sp.cancel(M4-formula4)==0
    print('symbolic conditional integrations and both moment formulas: PASS')
    return a,b,c,L,M2,M4,H2,P2


def scalar_certificates():
    h,p,z=sp.symbols('h p z',positive=True)
    Q = 4*(3-45*h+20*h*p)/(5*(1-3*h)**2)
    assert sp.cancel(Q-sp.Rational(8,5)-4*(1-33*h-18*h*h+20*h*p)/(5*(1-3*h)**2))==0
    assert sp.cancel(sp.Rational(12,5)-Q-4*h*(27+27*h-20*p)/(5*(1-3*h)**2))==0
    lower = 1-28*h-18*h*h + 15*h**sp.Rational(5,3)
    zexpr=sp.expand(lower.subs(h,z**3/27))
    assert sp.factor(sp.diff(zexpr,z)) == -z*z*(252-25*z*z+12*z**3)/81
    assert sp.simplify(zexpr.subs(z,1))==0
    print('exact sharp-ratio algebra and monotone scalar certificate: PASS')


def closed_moments(a,b,c):
    L=a+b+c
    H=((L-2*a)*(L-2*b)*(L-2*c))/L**3
    P=(a*b+a*c+b*c)/L**2
    return L*L*(1-3*H)/24, L**4*(3-45*H+20*H*P)/720


def reconstruction():
    for sides in ((sp.Rational(3,8),sp.Rational(3,8),sp.Rational(1,4)),
                  (sp.Rational(3,10),sp.Rational(7,20),sp.Rational(7,20)),
                  (sp.Rational(2,5),sp.Rational(7,20),sp.Rational(1,4)),
                  (sp.Rational(1,3),)*3):
        a,b,c = sides
        L=sum(sides)
        m2,m4=closed_moments(a,b,c)
        H=sp.factor((1-24*m2/L**2)/3)
        P=sp.factor((720*m4/L**4-3+45*H)/(20*H))
        Q=sp.factor((4*P-1-H)/8)
        targets=[a/L,b/L,c/L]
        assert sp.factor(P-sum(targets[i]*targets[j] for i in range(3) for j in range(i+1,3)))==0
        assert sp.factor(Q-sp.prod(targets))==0
        t=sp.symbols('t')
        assert sp.expand(t**3-t**2+P*t-Q-sp.prod(t-v for v in targets))==0
    print('exact shape reconstruction on rational test families: PASS')


def simulation():
    rng=random.Random(20261014)
    for a,b,c in ((3.,4.,5.),(1.,1.,1.),(.2,1.,1.1),(1.,1.4,1.5)):
        cx=(b*b+c*c-a*a)/(2*c)
        cy=math.sqrt(b*b-cx*cx)
        v=((0.,0.), (c,0.), (cx,cy))
        ends=((v[0],v[1]),(v[1],v[2]),(v[2],v[0]))
        lens=(c,a,b)
        L=a+b+c
        vals=[]
        N=60000
        for _ in range(N):
            pts=[]
            for _ in range(2):
                r=rng.random()*L
                i=next((j for j in range(3) if r < sum(lens[:j+1])),2)
                u=rng.random()
                A,B=ends[i]
                pts.append((A[0]+u*(B[0]-A[0]),A[1]+u*(B[1]-A[1])))
            D2=(pts[0][0]-pts[1][0])**2+(pts[0][1]-pts[1][1])**2
            vals.append(D2)
        m2=sum(vals)/N
        m4=sum(q*q for q in vals)/N
        e2,e4=closed_moments(a,b,c)
        assert abs(m2/float(e2)-1)<.04
        assert abs(m4/float(e4)-1)<.04
    print('four independent direct geometric pair-sampling checks: PASS')


if __name__=='__main__':
    symbolic_moments()
    scalar_certificates()
    reconstruction()
    simulation()
    print('TRIANGLE_BOUNDARY_CHORD_MOMENTS_OK')
