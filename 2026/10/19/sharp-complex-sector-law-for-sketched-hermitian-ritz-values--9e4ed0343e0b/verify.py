"""Reproduce the exact two-mode witnesses and randomized finite checks.

These finite tests corroborate, but do not prove, the universal sector theorem.
Python 3.9+ standard library only.
"""
from fractions import Fraction as F
from math import atan2, asin, cos, sin, sqrt, pi
from random import Random


def close(a, b, tol=3e-12):
    assert abs(a-b) <= tol*max(1.0, abs(a), abs(b)), (a,b)


def quotient(mu, L, u, h11, h12, h22):
    """One-vector sketched Rayleigh quotient for a diagonal two-mode A."""
    u0, u1 = u
    Au0, Au1 = mu*u0, L*u1
    # T=I+H is Hermitian; convention h12=T[0,1].
    Tu0, Tu1 = (1+h11)*u0+h12*u1, h12.conjugate()*u0+(1+h22)*u1
    n = u0.conjugate()*((1+h11)*Au0+h12*Au1) + u1.conjugate()*(h12.conjugate()*Au0+(1+h22)*Au1)
    d = u0.conjugate()*Tu0+u1.conjugate()*Tu1
    assert abs(d.imag) < 1e-11 and d.real>0
    return n/d


def run():
    # Exact rational entries for the nonreal equality construction.
    # For u=(3,1)/sqrt(10) and A=diag(1,9), H12=(-1+2sqrt(2)i)/15.
    assert F(9,10)+F(9,10)==F(9,5)
    assert F(1,1)+F(6,10)*F(-1,15)==F(24,25)
    assert F(9,5)+F(-3,15)==F(8,5)
    assert F(8,5)/F(24,25)==F(5,3)
    assert F(8,25)/F(24,25)==F(1,3)
    assert F(1+8,225)==F(1,25)  # norm-square of the off-diagonal H12

    eps=1/5
    u=(3/sqrt(10), 1/sqrt(10))
    z=quotient(1,9,u,0,complex(-1,2*sqrt(2))/15,0)
    close(z, complex(5,sqrt(2))/3)
    exact_angle=atan2(sqrt(2),5)
    bound_angle=asin(eps*(9-1)/(2*sqrt(9)*sqrt(1-eps*eps)))
    close(atan2(z.imag,z.real),bound_angle)
    close(exact_angle,bound_angle)

    # Attainment at the singular/negative frontier, with REAL sketches.
    threshold=3/5
    for e in (threshold, .75):
        lam=quotient(1,9,u,0,-e,0)
        expected=(F(9,5)-3*e)/(1-F(3,5)*e)
        close(lam,expected)
        if e==threshold: close(lam,0)
        else: assert lam.real<0

    # Random complex sketches and trial directions; finite checks only.
    rng=Random(20260408)
    cases=0
    for kappa in (1.01,1.3,2.0,4.0,9.0,30.0,100.0):
        tau=2*sqrt(kappa)/(kappa+1)
        for factor in (.03,.2,.5,.75,.95):
            e=tau*factor
            phi_max=asin(e*(kappa-1)/(2*sqrt(kappa)*sqrt(1-e*e)))
            for j in range(250):
                # Hermitian H=tI+[x,y+iz;y-iz,-x]; |t|+||(x,y,z)|| <= e.
                s=rng.random()*e
                t=(rng.random()*2-1)*(e-s)
                x,y,z=(rng.uniform(-1,1) for _ in range(3))
                r=sqrt(x*x+y*y+z*z)
                if r==0: continue
                x,y,z=s*x/r,s*y/r,s*z/r
                h11=t+x; h22=t-x; h12=complex(y,z)
                angle=rng.uniform(0,pi/2)
                phase=rng.uniform(-pi,pi)
                u=(cos(angle),sin(angle)*complex(cos(phase),sin(phase)))
                lam=quotient(1,kappa,u,h11,h12,h22)
                assert abs(atan2(lam.imag,lam.real)) <= phi_max+5e-12, (kappa,e,lam,phi_max)
                cases+=1
    print('VERIFY_OK exact_fraction_identities=6 sharp_complex_equality=1 '
          'sharp_threshold_witnesses=2 random_complex_embedding_cases='+str(cases))


if __name__=='__main__': run()
