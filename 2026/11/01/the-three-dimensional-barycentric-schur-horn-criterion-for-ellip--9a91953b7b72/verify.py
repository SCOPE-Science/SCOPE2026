#!/usr/bin/env python3
"""Self-contained finite checks for the three-dimensional barycentric criterion.
The universal equivalence is established by the analytic proof, not this program.
"""
import cmath
import math
import random
from fractions import Fraction


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],
            x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0])


def mul(C,x):
    return tuple(sum(C[i][j]*x[j] for j in range(3)) for i in range(3))


def quad(C,x,y):
    return dot(x,mul(C,y))


def polynomial(C,y):
    T=sum(C[i][i] for i in range(3))
    T2=sum(C[i][j]*C[j][i] for i in range(3) for j in range(3))
    a=quad(C,y,y)
    v=dot(mul(C,y),mul(C,y))
    return 9*a*a+2*T*a-12*v+2*T2-T*T


def tangent_basis(y):
    seed=min(((1.,0.,0.),(0.,1.,0.),(0.,0.,1.)),key=lambda z:abs(dot(z,y)))
    v=tuple(seed[i]-dot(seed,y)*y[i] for i in range(3))
    nv=math.sqrt(dot(v,v))
    e=tuple(z/nv for z in v)
    f=cross(y,e)
    return e,f


def tangent_invariants(C,y):
    e,f=tangent_basis(y)
    b1,b2=quad(C,e,y),quad(C,f,y)
    p=(quad(C,e,e)-quad(C,f,f))/2
    q=quad(C,e,f)
    return e,f,b1,b2,p,q


def build_frame(C,y):
    e,f,b1,b2,p,q=tangent_invariants(C,y)
    assert abs(p*p+q*q-2*(b1*b1+b2*b2)) < 1e-11
    if abs(b1)+abs(b2)+abs(p)+abs(q)<1e-12:
        theta=0.0
    else:
        z=-(p+1j*q)/(math.sqrt(2)*(b1-1j*b2))
        assert abs(abs(z)-1)<1e-11
        theta=cmath.phase(z)/3
    return [tuple(y[i]/math.sqrt(3)+math.sqrt(2/3)*(
            math.cos(theta+2*math.pi*j/3)*e[i]+
            math.sin(theta+2*math.pi*j/3)*f[i])
                for i in range(3)) for j in range(3)]


def check_frame(C,y):
    U=build_frame(C,y)
    tr=sum(C[i][i] for i in range(3))
    for i in range(3):
        assert abs(quad(C,U[i],U[i])-tr/3)<1e-12
        assert abs(dot(U[i],y)-1/math.sqrt(3))<1e-12
        for j in range(3):
            assert abs(dot(U[i],U[j])-(i==j))<1e-12
    return True


def main():
    checks=0
    C=((Fraction(1),0,0),(0,Fraction(2),0),(0,0,Fraction(3)))
    y2=(Fraction(1,6),Fraction(4,6),Fraction(1,6))
    a=sum(C[i][i]*y2[i] for i in range(3))
    v=sum(C[i][i]**2*y2[i] for i in range(3))
    T=sum(C[i][i] for i in range(3));T2=sum(C[i][i]**2 for i in range(3))
    assert 9*a*a+2*T*a-12*v+2*T2-T*T==0
    checks+=1
    for j,expect in enumerate((Fraction(1),Fraction(4),Fraction(1))):
        unit=tuple(Fraction(int(i==j)) for i in range(3))
        assert polynomial(C,unit)==expect
        checks+=1
    y=tuple(t/math.sqrt(6) for t in (1.,2.,1.))
    Cf=((1.,0.,0.),(0.,2.,0.),(0.,0.,3.))
    check_frame(Cf,y);checks+=1
    for weights,idx in (((1.,1.,4.),2),((2.,2.,2.),0)):
        M=tuple(tuple(weights[i] if i==j else 0. for j in range(3)) for i in range(3))
        z=tuple(float(i==idx) for i in range(3))
        assert abs(polynomial(M,z))<1e-12
        check_frame(M,z)
        checks+=1
    rng=random.Random(20261025)
    for _ in range(150):
        R=[[rng.uniform(-1,1) for j in range(3)] for i in range(3)]
        M=tuple(tuple(sum(R[k][i]*R[k][j] for k in range(3))+(i==j)
                 for j in range(3)) for i in range(3))
        v=[rng.gauss(0,1) for i in range(3)];l=math.sqrt(dot(v,v))
        z=tuple(t/l for t in v)
        e,f,b1,b2,p,q=tangent_invariants(M,z)
        # Difference of restricted eigenvalues squared is 4(p*p+q*q).
        direct=4*(p*p+q*q)-8*(b1*b1+b2*b2)
        assert abs(polynomial(M,z)-direct)<2e-11
        checks+=1
        # Independently evaluate the three harmonic deviations.
        theta=rng.uniform(-math.pi,math.pi)
        for j in range(3):
            t=theta+2*math.pi*j/3
            u=tuple(z[i]/math.sqrt(3)+math.sqrt(2/3)*(
                math.cos(t)*e[i]+math.sin(t)*f[i]) for i in range(3))
            lhs=1.5*(quad(M,u,u)-sum(M[i][i] for i in range(3))/3)
            rhs=math.sqrt(2)*(b1*math.cos(t)+b2*math.sin(t)) \
                 +p*math.cos(2*t)+q*math.sin(2*t)
            assert abs(lhs-rhs)<1e-11
            checks+=1
    print('PASS:',checks,'exact and numerical checks; analytic proof required for all dimensions/domain.')

if __name__=='__main__':main()
