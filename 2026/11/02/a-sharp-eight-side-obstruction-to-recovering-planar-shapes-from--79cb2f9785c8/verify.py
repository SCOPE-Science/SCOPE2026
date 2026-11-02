#!/usr/bin/env python3
"""Reproduce finite and symbolic consistency checks for a planar zonogon width-correlation theorem.

Requires only the Python 3 standard library. The universal assertions are proved in RESULT.md;
finite grid calculations here are supplemental checks and are not claims of exhaustive proof.
"""
from __future__ import annotations
import cmath
import math
import sys
from collections import Counter
from itertools import combinations

A = (0, 1, 4, 6)
B = (0, 1, 3, 7)
N = 12

def interval_classes(S):
    return sorted(min((v-u) % N, (u-v) % N) for u,v in combinations(S,2))

def orbit(S):
    return {tuple(sorted((sg*a+t)%N for a in S)) for sg in (1,-1) for t in range(N)}

def width(S,theta):
    return sum(abs(math.cos(theta-math.pi*a/N)) for a in S)

def bispectrum(S):
    zeta=cmath.exp(-2j*math.pi/N)
    F=lambda k: sum(zeta**(k*a) for a in S)
    return F(1)**2*F(-2)

def primitive(A,B,t):
    st,ct=math.sin(t),math.cos(t)
    return (A**3*st-B**3*ct+(A*B**2-A**3/3)*st**3
            +(B**3/3-A**2*B)*ct**3)

def cube_moment_exact_integral(S):
    """Exact-piecewise primitive, evaluated with floating-point trig at rational-pi endpoints."""
    breaks=sorted(set([0.0,math.pi]+[((a+6)%N)*math.pi/N for a in S]))
    integral=0.0
    for lo,hi in zip(breaks,breaks[1:]):
        middle=(lo+hi)/2
        signs=[1 if math.cos(middle-math.pi*a/N)>0 else -1 for a in S]
        aa=sum(s*math.cos(math.pi*a/N) for s,a in zip(signs,S))
        bb=sum(s*math.sin(math.pi*a/N) for s,a in zip(signs,S))
        integral+=primitive(aa,bb,hi)-primitive(aa,bb,lo)
    return integral/math.pi

def main():
    checks=0
    def ck(expr,description):
        nonlocal checks
        assert expr,description
        checks+=1
    ck(interval_classes(A)==list(range(1,7)),"A difference classes")
    ck(interval_classes(B)==list(range(1,7)),"B difference classes")
    ck(B not in orbit(A),"dihedral inequivalence")
    for S in (A,B):
        gaps=sorted(((S[(i+1)%4]-S[i])%N for i in range(4)))
        ck(sum(gaps)==N,"cyclic gaps")
        ck(len(gaps)==4,"four distinct sides")
    area=(3+math.sqrt(2)+math.sqrt(3)+math.sqrt(6))/2
    ck(abs(area-sum(math.sin(math.pi*j/12) for j in range(1,7)))<1e-13,
       "exact area radical identity")
    c1,c2=2/(3*math.pi),-2/(15*math.pi)
    bA,bB=bispectrum(A),bispectrum(B)
    ck(abs(bA-(-2*math.sqrt(3)-2j))<1e-12,"A bispectrum")
    ck(abs(bB-( 2*math.sqrt(3)-2j))<1e-12,"B bispectrum")
    ck(abs(c1*c1*c2*(bA-bB)-32*math.sqrt(3)/(135*math.pi**3))<1e-14,
       "third angular correlation Fourier coefficient")
    tA,tB=map(cube_moment_exact_integral,(A,B))
    expected=(11*math.sqrt(2)-3*math.sqrt(6)-8)/math.pi
    ck(abs(tA-tB-expected)<1e-12,"exact piecewise cubic-moment difference")
    ck(expected>0,"strict cubic-moment separation")
    # Trapezoidal quadrature corroborates continuum second-order correlation equality.
    mesh=2**16
    theta=[math.pi*i/mesh for i in range(mesh)]
    wA=[width(A,x) for x in theta]
    wB=[width(B,x) for x in theta]
    for j in range(17):
        t=math.pi*j/16
        corrA=sum(wA[i]*width(A,theta[i]+t) for i in range(mesh))/mesh
        corrB=sum(wB[i]*width(B,theta[i]+t) for i in range(mesh))/mesh
        ck(abs(corrA-corrB)<2e-8,f"autocorrelation lag {j}")
    # Exhaustive discrete-grid sanity check of 3-direction uniqueness, not a proof for all angles.
    for n in range(4,19):
        seen={}
        for S in combinations(range(n),3):
            dist=tuple(sorted(min((v-u)%n,(u-v)%n) for u,v in combinations(S,2)))
            orb=min(tuple(sorted(((sg*a+t)%n for a in S))) for sg in (1,-1) for t in range(n))
            ck(dist not in seen or seen[dist]==orb,f"3-point homometry n={n}")
            seen[dist]=orb
    if "--symbolic" in sys.argv:
        import sympy as sy  # Optional; exact radical computation, not needed for basic checks.
        P=sy.pi
        def exact_cubic(S):
            breaks=sorted(set([sy.S(0),P]+[((a+6)%N)*P/N for a in S]),key=float)
            out=sy.S(0)
            for lo,hi in zip(breaks,breaks[1:]):
                mid=(lo+hi)/2
                signs=[1 if float(sy.cos(mid-P*a/N))>0 else -1 for a in S]
                u=sum(z*sy.cos(P*a/N) for z,a in zip(signs,S))
                v=sum(z*sy.sin(P*a/N) for z,a in zip(signs,S))
                f=lambda x:u**3*sy.sin(x)-v**3*sy.cos(x)+(u*v**2-u**3/sy.S(3))*sy.sin(x)**3+(v**3/sy.S(3)-u**2*v)*sy.cos(x)**3
                out+=f(hi)-f(lo)
            return sy.simplify(sy.expand_trig(out)/P)
        exactA=exact_cubic(A)
        exactB=exact_cubic(B)
        ck(sy.simplify(exactA-(sy.sqrt(6)+3*sy.sqrt(3)+9*sy.sqrt(2)+sy.Rational(109,3))/P)==0,"A exact cubic")
        ck(sy.simplify(exactB-(-6*sy.sqrt(2)+9*sy.sqrt(3)+12*sy.sqrt(6)+133)/(3*P))==0,"B exact cubic")
        ck(sy.simplify((exactA-exactB)-(11*sy.sqrt(2)-3*sy.sqrt(6)-8)/P)==0,"exact separation")
    print("VERIFY_OK",checks,"checks",f"area={area:.15g}",f"cube_difference={tA-tB:.15g}")
if __name__=='__main__':main()
