"""Independent exact finite checks and spectral-fiber spot checks for the stated theorem.
Run: python3 CHECK.py (Python standard library only).
Finite tests corroborate and do not replace the all-q proof.
"""
from fractions import Fraction as F
from math import sqrt, pi
from cmath import exp

def hat(t):
    return max(0., 1.-abs(t))

def zak(x,nu):
    return sum(hat(x-k)*exp(2j*pi*k*nu) for k in range(-5,6))

def fiber_extrema(q,x,nu):
    H=[[zak(x-2*s/q,nu+r/2)/sqrt(2) for s in range(q)] for r in (0,1)]
    aa=sum(abs(z)**2 for z in H[0]); dd=sum(abs(z)**2 for z in H[1]);
    ab=sum(H[0][s]*H[1][s].conjugate() for s in range(q))
    t=(aa+dd)/2; d=sqrt(((aa-dd)/2)**2+abs(ab)**2)
    return t-d,t+d

count=0
for q in range(3,32,2):
    m=(q-1)//2
    for z in (F(0),F(1,7),F(1,2),F(4,5),F(1)):
        u=[(z+2*j)/q for j in range(q)]
        v=[(z+2*j+1)/q for j in range(q)]
        A0=sum((e*e for e in u[:m+1]),F(0))+sum(((2-e)**2 for e in u[m+1:]),F(0))
        A1=sum((e*e for e in v[:m]),F(0))+sum(((2-e)**2 for e in v[m:]),F(0))
        B0=sum(((e-1)*(2-e) for e in u[m+1:]),F(0))
        B1=sum(((e-1)*(2-e) for e in v[m:]),F(0))
        w=(2*z-1)**2
        assert A0==F(q*q-1+3*z*z,3*q)
        assert A1==F(q*q-1+3*(z-1)**2,3*q)
        assert A0+A1==F(4*q*q-1+3*w,6*q)
        assert A0-A1==F(2*z-1,q)
        assert B0+B1==F(2*q*q+1-3*w,12*q)
        assert B0>=0 and B1>=0
        assert (2*q*q+1-3*w)**2+36*w-(5-2*q*q+3*w)**2==24*(q*q-1)
        count+=7
for q in (3,5,7,11):
    A=(q*q-1)/(6*q)
    B=(2*q*q+1+sqrt((q*q-1)**2+9))/(6*q)
    for x in (0,1/(2*q),1/q,0.23,0.5,0.83):
        for nu in (0,0.113,0.25,0.5,0.71):
            small,big=fiber_extrema(q,x,nu)
            assert small>=A-2e-10,(q,x,nu,small,A)
            assert big<=B+2e-10,(q,x,nu,big,B)
            count+=2
    assert abs(fiber_extrema(q,1/(2*q),0)[0]-A)<2e-10
    assert abs(fiber_extrema(q,0,0)[1]-B)<2e-10
    count+=2
print('PASS:',count,'supplementary assertions (exact polynomial identities and numerical Zak fibers).')
