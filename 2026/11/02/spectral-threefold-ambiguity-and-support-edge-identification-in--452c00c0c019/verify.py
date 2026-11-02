"""Reproduce algebraic spectral aliases for a telegraph-driven damped oscillator.
Only Python's standard library is required. Tests are independent of particle simulation.
Run: python verify.py
"""
import math
import random
from fractions import Fraction


def spectral_denominator(q,p,c):
    # Coefficients of monic polynomial in z=omega^2 (high to low).
    return (1., c*c+q*q-2*p,
            p*p+c*c*(q*q-2*p), c*c*p*p)


def spectral_density(omega,q,p,c,f):
    z=omega*omega
    return (2*c*f*f)/((z+c*c)*(z*z+(q*q-2*p)*z+p*p))


def stationary_variance_from_generator(q,p,c,f):
    # Stationary generator identities:
    # <v sigma>=c<x sigma>, <x sigma>=f/(p+c*q+c^2),
    # <v^2>=f<v sigma>/q, <x v>=0,
    # p<x^2>=<v^2>+f<x sigma>.
    xs=f/(p+c*q+c*c)
    vs=c*xs
    vel2=f*vs/q
    x2=(vel2+f*xs)/p
    return x2,vel2,xs,vs


def alias_from_poles(u,v,w,K,choice):
    poles=[u,v,w]
    c=poles.pop(choice)
    a,b=poles
    return (a+b,a*b,c,math.sqrt(K/c))


def support_radius(q,p,c,f):
    assert q*q>=4*p-1e-12
    return f/p


def recovery_from_support(poles,K,R):
    product=math.prod(poles)
    c=R*R*product*product/K
    remaining=list(poles)
    j=min(range(3), key=lambda k:abs(remaining[k]-c))
    selected=remaining.pop(j)
    assert abs(selected-c)<1e-8*max(1,abs(c))
    a,b=remaining
    return (a+b,a*b,selected,math.sqrt(K/selected))


def check():
    # Exact rational example: all three systems have the same rational PSD.
    poles=[1,2,3]
    K=6
    expected=(1,14,49,36) # (z+1)(z+4)(z+9)
    assert all(spectral_denominator(*alias_from_poles(*poles,K,j)[:3])==expected
               for j in range(3))
    # Original exact stationary variance equals 1/10, velocity variance 1/10.
    for j in range(3):
        q,p,c,f=alias_from_poles(*poles,K,j)
        x2,v2,_,_=stationary_variance_from_generator(q,p,c,f)
        assert abs(x2-0.1)<1e-14
        assert abs(v2-0.1)<1e-14
        R=support_radius(q,p,c,f)
        assert abs(R*R-c/6)<1e-14
        recovered=recovery_from_support(poles,K,R)
        assert all(abs(x-y)<1e-12 for x,y in zip((q,p,c,f),recovered))
    rng=random.Random(20261026)
    checks=0
    for trial in range(500):
        poles=[math.exp(rng.uniform(-1.5,1.5)) for _ in range(3)]
        K=math.exp(rng.uniform(-1,2))
        aliases=[alias_from_poles(*poles,K,j) for j in range(3)]
        # An independently calculated denominator from q,p,c is symmetric.
        reference=spectral_denominator(*aliases[0][:3])
        for q,p,c,f in aliases:
            poly=spectral_denominator(q,p,c)
            for left,right in zip(poly,reference):
                assert math.isclose(left,right,rel_tol=1e-12,abs_tol=1e-12)
                checks+=1
            for om in (0.,0.11,0.8,2.7,12.):
                target=spectral_density(om,*aliases[0])
                assert math.isclose(spectral_density(om,q,p,c,f),target,rel_tol=1e-12,abs_tol=1e-14)
                checks+=1
            R=support_radius(q,p,c,f)
            r=recovery_from_support(poles,K,R)
            for x,y in zip((q,p,c,f),r):
                assert math.isclose(x,y,rel_tol=1e-12,abs_tol=1e-12)
                checks+=1
            # Independent stationarity generator route matches aliases.
            x2,v2,_,_=stationary_variance_from_generator(q,p,c,f)
            xx,vv,_,_=stationary_variance_from_generator(*aliases[0])
            assert math.isclose(x2,xx,rel_tol=1e-12)
            assert math.isclose(v2,vv,rel_tol=1e-12)
            checks+=2
    # Collision cases: the fiber has 2 members or just 1.
    for poles,expected_n in (([1,1,2],2),([1,1,1],1),([1,2,3],3)):
        choices={(round(q,8),round(p,8),round(c,8),round(f,8))
                 for q,p,c,f in (alias_from_poles(*poles,6,j) for j in range(3))}
        assert len(choices)==expected_n
        checks+=1
    # Underdamped mechanical quadratic discriminant is negative, so no
    # mechanical pole can be exchanged with the unique real noise pole.
    for _ in range(500):
        p=math.exp(rng.uniform(-2,2))
        q=2*math.sqrt(p)*rng.uniform(0.01,0.999)
        assert q*q*(q*q-4*p)<0
        checks+=1
    print('PASS: exact 3-fold example, support decoding, collisions, underdamped uniqueness')
    print('PASS:', checks, 'randomized deterministic independent assertions')


if __name__=='__main__':
    check()
