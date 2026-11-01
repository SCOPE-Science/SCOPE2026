"""Reproducible tests for orientational-reset anisotropy bounds.

All computations use Python's standard library and exact analytic moment identities.
Numerical checks are not substitutes for the continuum-process proof.
"""
import cmath
import math
import random


def moments(lam, atoms):
    # atoms is a sequence of (angle, weight).
    r1 = sum(w * cmath.exp(1j * angle) for angle, w in atoms)
    r2 = sum(w * cmath.exp(2j * angle) for angle, w in atoms)
    p1 = lam / (lam + 1.0)
    p2 = lam / (lam + 4.0)
    m1 = p1 * r1
    m2 = p2 * r2
    variance_x = (1 + m2.real) / 2 - m1.real**2
    variance_y = (1 - m2.real) / 2 - m1.imag**2
    return variance_x, variance_y


def bounds(lam, a):
    k = lam + 1.0
    p1 = lam / k
    p2 = lam / (lam + 4.0)
    return ((p2 * (2*a*a-1) - p1*p1*a*a)/k,
            (p2 - p1*p1*a*a)/k)


def verify():
    n=0
    for a in (0., .17, .5, math.sqrt(3)/2, .91, .97, 1.):
        angle=math.acos(a)
        bottom=[(-angle,.5),(angle,.5)]
        top=[(0.,(1+a)/2),(math.pi,(1-a)/2)]
        for lam in (.01,.2,.5,1.,2.,4.,10.,100.):
            lo, hi =bounds(lam,a)
            for test,expected in ((bottom,lo),(top,hi)):
                vx, vy=moments(lam,test)
                val=(vx-vy)/(lam+1.)
                assert math.isclose(val, expected, rel_tol=2e-11,abs_tol=1e-12), (a,lam,val,expected)
                n+=1
            # Discrete mixtures of extreme laws preserve prescribed polarization.
            for s in (.12,.4,.79):
                atoms=[(ang, w*s) for ang,w in bottom]+[(ang,w*(1-s)) for ang,w in top]
                vx,vy=moments(lam,atoms)
                val=(vx-vy)/(lam+1.)
                assert lo-1e-12 <= val <= hi+1e-12
                n+=1
    # Cross-check previously evaluated delta-orientation diffusivity formulas.
    for lam in (.12,.5,1.,2.,4.,10.):
        vx,vy=moments(lam,[(0.,1.)])
        known_x=(4+10*lam)/((lam+1)**3*(lam+4))/2
        known_y=4/((lam+1)*(lam+4))/2
        assert math.isclose(vx/(lam+1),known_x,rel_tol=1e-12)
        assert math.isclose(vy/(lam+1),known_y,rel_tol=1e-12)
        n+=2
    # Reentrant strict negativity of the maximum for all laws.
    for a in (.88, .91, .97, .999):
        disc=math.sqrt(4*a*a-3)
        lminus=(2*a*a-1-a*disc)/(1-a*a)
        lplus=(2*a*a-1+a*disc)/(1-a*a)
        assert lminus<2<lplus
        for l,negative in ((lminus*.9,False),((lminus+2)/2,True),(2,True),((2+lplus)/2,True),(lplus*1.1,False)):
            assert (bounds(l,a)[1]<0)==negative, (a,l,negative)
            n+=1
    # Explicit direct stationary Fourier-generator relation.
    random.seed(7741)
    for _ in range(50):
        weights=[random.random() for j in range(4)]
        weights=[u/sum(weights) for u in weights]
        atoms=[(random.uniform(-math.pi,math.pi),u) for u in weights]
        lam=10**random.uniform(-2,2)
        n1=sum(u*cmath.exp(1j*t) for t,u in atoms)
        n2=sum(u*cmath.exp(2j*t) for t,u in atoms)
        p1=lam/(lam+1)
        p2=lam/(lam+4)
        for j,stat in ((1,p1*n1),(2,p2*n2)):
            # Generator acting on exp(i*j*theta) has expectation zero.
            assert abs(-(j*j+lam)*stat+lam*sum(u*cmath.exp(1j*j*t) for t,u in atoms))<1e-12
            n+=1
    print('PASS',n,'independent numerical/algebraic tests')

if __name__=='__main__':verify()
