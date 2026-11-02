#!/usr/bin/env python3
"""Reproduce exact coefficient identities and independently sample the Schur frontier."""
from fractions import Fraction as Q
from math import sqrt
import cmath

checks=0

def det3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def coeffs_direct(M):
    a=-sum(M[i][i] for i in range(3))
    b=sum(M[i][i]*M[j][j]-M[i][j]*M[j][i] for i,j in ((0,1),(0,2),(1,2)))
    return a,b,-det3(M)

def roots(a,b,c):
    # Direct Durand-Kerner cubic calculation, for a real monic polynomial.
    q=[1+0j,-0.6+1.2j,-0.8-1.1j]
    for _ in range(2000):
        old=q[:]
        for j in range(3):
            z=old[j]
            den=(z-old[(j+1)%3])*(z-old[(j+2)%3])
            if abs(den)<1e-27:
                den+=1e-27
            q[j]=z-(z**3+a*z**2+b*z+c)/den
        if max(abs(q[j]-old[j]) for j in range(3))<1e-12:
            break
    assert max(abs(z**3+a*z*z+b*z+c) for z in q)<1e-7, (a,b,c,q)
    return q

for si in range(1,19):
    s=Q(si,20)
    for ei in range(0,10):
        eta=Q(ei,10)
        v=1-eta*eta
        L=s*s+6*s+1
        disc=float(L*L-16*s*v*(1+s)**2)
        star=4*float((1+s)**2)/(float(L)+sqrt(disc))
        assert 0<star<=2+1e-12
        if eta:
            assert star<2
        for bi in range(1,11):
            beta=Q(bi,5)
            M=[[1-beta,beta*eta*(s-1),-beta*eta*s],
               [Q(0),s,-s],[-beta*eta,beta*(s-1),s*(1-beta)]]
            a,b,c=coeffs_direct(M)
            assert a==beta*(1+s)-1-2*s
            assert b==s*(v*beta*beta-4*beta+s+2)
            assert c==s*(-v*beta*beta+(1+s)*beta-s)
            assert 1+a+b+c==beta*(1-s)**2
            F=2*s*v*beta*beta-L*beta+2*(1+s)**2
            assert -(-1+a-b+c)==F
            J=1-b+a*c-c*c
            Jclosed=((1-s)**3*(1+s)+beta*s*(1-s)**2*(2*s+3)
                    +beta**2*s*(1-s)*(1+s)**2
                    +v*(2*beta**2*s**2*(1-s)+beta**3*s*(1+s)*(2*s-1))
                    -beta**4*s**2*v**2)
            assert J==Jclosed
            if beta<=2:
                assert J>0
            checks+=7
        for factor in (0.22,0.66,0.96,1.04,1.3,2.1):
            beta=star*factor
            af=beta*(1+float(s))-1-2*float(s)
            bf=float(s)*(float(v)*beta*beta-4*beta+float(s)+2)
            cf=float(s)*(-float(v)*beta*beta+(1+float(s))*beta-float(s))
            radius=max(abs(z) for z in roots(af,bf,cf))
            if factor<1:
                assert radius<1-1e-8, (s,eta,beta,radius)
            else:
                assert radius>1+1e-8, (s,eta,beta,radius)
            checks+=1
        a=star*(1+float(s))-1-2*float(s)
        b=float(s)*(float(v)*star*star-4*star+float(s)+2)
        c=float(s)*(-float(v)*star*star+(1+float(s))*star-float(s))
        assert abs(-1+a-b+c)<1e-10
        checks+=1
print('VERIFY_OK',checks,'exact-and-spectral checks')
