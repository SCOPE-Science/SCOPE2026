#!/usr/bin/env python3
"""Finite diagnostics for the exact Hardy q-Berezin constant-symbol profile.

Run: python3 check_q_berezin.py
Standard-library-only checks. The all-parameter theorem uses the written analytic proof.
"""
import cmath
import math
import random


def profile(a, q):
    k = math.sqrt(max(0.0, 1.0 - q*q))
    b = math.sqrt(max(0.0, 1.0 - a*a))
    return 2.0*q/(1.0 - a*k + q*b)


def pair(a, q, phi):
    k = math.sqrt(max(0.0, 1.0-q*q))
    b = math.sqrt(max(0.0, 1.0-a*a))
    r = (a+k)/(1.0+a*k+q*b)
    s = (r-k)/(1.0-k*r)
    return r*cmath.exp(1j*phi), s*cmath.exp(1j*phi)


def overlap(u,v):
    return (math.sqrt((1-abs(u)**2)*(1-abs(v)**2)) / (1-u.conjugate()*v))


def matrix_element(u,v,c):
    return (math.sqrt((1-abs(u)**2)*(1-abs(v)**2)) / (1-u.conjugate()*c))


def near(x,y,eps=1e-9):
    return abs(x-y) <= eps*(1+abs(x)+abs(y))


def check():
    rng = random.Random(23061017)
    assertions = 0
    for ai in range(19):
        a = ai/20
        for qi in range(1,21):
            q = qi/20
            k = math.sqrt(max(0,1-q*q))
            b = math.sqrt(1-a*a)
            L = 1+a*k+q*b
            D = 1-a*k+q*b
            r = (a+k)/L
            u,v=pair(a,q,.271)
            c=a*cmath.exp(.271j)
            assert 0<=r<1
            assert near(overlap(u,v),q,2e-12)
            assert near(abs(matrix_element(u,v,c)),profile(a,q),2e-12)
            assert near(profile(a,q)/ (1/b), 2*q*b/D,2e-12)
            assert near(1-profile(a,q)*b, ((a-k)**2+(b-q)**2)/(2*D), 2e-12)
            assertions += 5
            if a>0 and q<1:
                q_shift=q+1e-4*(1-q)
                assert 0<profile(a,q_shift)<1/b+1e-9
                assertions+=1
            # The analytic perfect-square upper bound at random radii.
            for _ in range(25):
                rho=rng.random()*.999
                lhs=2*(1-k*rho)*(1-a*rho)-D*(1-rho*rho)
                rhs=((L*rho-a-k)**2)/L
                assert near(lhs,rhs,2e-11)
                assert lhs>-3e-12
                assertions+=2
                theta=2*math.pi*rng.random()
                ur=rho*cmath.exp(1j*theta)
                s=(rho-k)/(1-k*rho)
                vr=s*cmath.exp(1j*theta)
                val=abs(matrix_element(ur,vr,c))
                assert near(overlap(ur,vr),q,2e-12)
                assert val<=profile(a,q)+2e-12
                assertions+=2
            # Upper branch must be bounded by the lower branch at equal radius.
            sminus=(r-k)/(1-k*r)
            splus=(r+k)/(1+k*r)
            um=r
            assert abs(matrix_element(um,sminus,a))>=abs(matrix_element(um,splus,a))-1e-12
            assertions+=1
            # Direct truncated vector calculation for a generic constrained pair.
            if a<.85 and 0.15<=q<=.95:
                rho=rng.uniform(.02,.82)
                ang=rng.uniform(-math.pi,math.pi)
                u=rho*cmath.exp(1j*ang)
                s=(rho-k)/(1-k*rho)
                v=s*cmath.exp(1j*ang)
                N=160
                ku=[math.sqrt(1-rho*rho)*u.conjugate()**j for j in range(N)]
                kv=[math.sqrt(1-s*s)*v.conjugate()**j for j in range(N)]
                finite_overlap=sum(x*y.conjugate() for x,y in zip(ku,kv))
                finite_eval=sum(ku[j]*c**j for j in range(N))
                assert near(finite_overlap,q,1e-11)
                assert near(finite_eval*kv[0].conjugate(),matrix_element(u,v,c),1e-11)
                assertions+=2
    # Norm-saturation uniqueness at the indicated overlap.
    for ai in range(0,20):
        a=ai/20
        b=math.sqrt(1-a*a)
        assert near(profile(a,b),1/b,2e-12)
        for q in [.05,.15,.25,.35,.45,.55,.65,.75,.85,.95,1.0]:
            if abs(q-b)>1e-8:
                assert profile(a,q)<1/b-1e-12
            assertions+=1
        assertions+=1
    print(f"PASS {assertions} finite diagnostic assertions")


if __name__=='__main__':
    check()
