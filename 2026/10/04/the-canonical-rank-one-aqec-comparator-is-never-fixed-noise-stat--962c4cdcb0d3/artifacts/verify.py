#!/usr/bin/env python3
import math
import numpy as np
from fractions import Fraction

def params(d,p):
    l1=1-p/(d*d-2); l4=(d*d-1+p)/(d*d); l5=(1-p)/(d*d)
    l2=((1-l1)*(d*d*l1-1))/(d*d*l4); l3=2*(1-l1)**2/(d*d*l4)
    a=math.sqrt(d*l4/(d*d-1)); b=math.sqrt(d*l5); g=(d+1-p)/(d*(d+1)); c=(b-a)/d
    th=math.atan2(math.sqrt(d-1)*c,a+c)
    return l1,l2,l3,l4,l5,a,b,g,th

def scalar(d,p,th):
    l1,l2,l3,l4,l5,a,b,g,_=params(d,p)
    w=(math.cos(th)+math.sqrt(d-1)*math.sin(th))/math.sqrt(d)
    T=(d-1)*a+a*math.cos(th)+(b-a)*w/math.sqrt(d)
    return l3+(l1-l3)*T*T/d+l2*(w-math.sqrt(l5)*T)**2/(d*l4)

def direct(d,p,th):
    l1,l2,l3,l4,l5,a,b,g,_=params(d,p); D=d*d
    psi=np.zeros(D,complex)
    for j in range(d): psi[j*d+j]=1/math.sqrt(d)
    pi=np.outer(psi,psi.conj()); Q=a*(np.eye(D)-pi)+b*pi
    V=np.zeros((D,d),complex); V[0,0]=math.cos(th)
    for j in range(1,d): V[j*d+j,0]=math.sin(th)/math.sqrt(d-1); V[j*d,j]=1
    assert np.linalg.norm(V.conj().T@V-np.eye(d))<1e-11
    dec=[]
    for r in range(d):
        R=np.zeros((d,D),complex)
        for j in range(d): R[j,j*d+r]=1
        dec.append(R)
    noise=[]
    for x in range(D):
        for y in range(D):
            K=np.zeros((D,D),complex); K[x,y]=math.sqrt(l3); noise.append(K)
    coef=l1-l3
    for s in range(d):
        J=np.zeros((D,d),complex)
        for j in range(d): J[j*d+s,j]=1
        for R in dec: noise.append(math.sqrt(coef)*J@R@Q)
    for i in range(d):
        J=np.zeros((D,d),complex)
        for j in range(d): J[j*d+i,j]=1
        C=Q@J
        for j in range(d):
            ket=np.zeros(D,complex); ket[i*d+j]=1
            E=(np.outer(ket,psi.conj())-math.sqrt(l5)*(C@dec[j]).conj().T)/math.sqrt(l4)
            noise.append(math.sqrt(l2)*E)
    return sum(abs(np.trace(R@K@V))**2 for R in dec for K in noise)/(d*d)

def derivative_formula(d,p):
    l1,l2,l3,l4,l5,a,b,g,th=params(d,p)
    wp=math.sqrt(l5/g); Tp=(d-1)*a+math.sqrt(g)
    wprime=math.sqrt(d-1)*a/(math.sqrt(d)*math.sqrt(g))
    return 2*l2*(wp-math.sqrt(l5)*Tp)*wprime/(d*l4)

def exact_identity(d,num,den):
    p=Fraction(num,den); D=Fraction(d,1)
    g=(D+1-p)/(D*(D+1)); a2=(D*D-1+p)/(D*(D*D-1))
    lhs=(1-g)**2-(D-1)**2*a2*g
    rhs=p*(D*D-1+p)/(D*(D+1)**2)
    assert lhs==rhs and rhs>0

def main():
    for d in (2,3,4):
        for p in (0.1,0.37,0.8):
            *_,th=params(d,p)
            assert abs(scalar(d,p,th)-direct(d,p,th))<3e-10
            assert derivative_formula(d,p)>0
    for d in range(2,16):
        for q in ((1,10),(1,3),(4,5)): exact_identity(d,*q)
    print('VERIFY_OK')
if __name__=='__main__': main()
