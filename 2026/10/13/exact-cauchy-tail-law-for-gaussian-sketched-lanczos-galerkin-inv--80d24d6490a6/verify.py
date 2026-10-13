#!/usr/bin/env python3
"""Exact-rational tests and numerical density checks for sketched Lanczos Galerkin."""
from fractions import Fraction as F
from random import Random
from math import sqrt, gamma, pi, log


def mm(A, B):
    return [[sum(x*y for x,y in zip(row, col)) for col in zip(*B)] for row in A]


def trans(A):
    return [list(col) for col in zip(*A)]


def inverse(A):
    n=len(A)
    E=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        t=next((j for j in range(i,n) if E[j][i]),None)
        if t is None:raise ZeroDivisionError('singular')
        E[i],E[t]=E[t],E[i]
        pivot=E[i][i];E[i]=[x/pivot for x in E[i]]
        for j in range(n):
            if j==i:continue
            fact=E[j][i]
            E[j]=[x-fact*y for x,y in zip(E[j],E[i])]
    return [row[n:] for row in E]


def det(A):
    n=len(A);B=[[F(v) for v in row] for row in A];ans=F(1)
    for i in range(n):
        t=next((j for j in range(i,n) if B[j][i]),None)
        if t is None:return F(0)
        if i!=t:B[i],B[t]=B[t],B[i];ans=-ans
        z=B[i][i];ans*=z
        for j in range(i+1,n):
            q=B[j][i]/z
            B[j]=[a-q*b for a,b in zip(B[j],B[i])]
    return ans


def vec(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]

def dot(u,v):return sum(a*b for a,b in zip(u,v))


def case(k,s,rand):
    n=k+1
    A=[[F(3 if i==j else 1 if abs(i-j)==1 else 0) for j in range(n)] for i in range(n)]
    T=[row[:k] for row in A[:k]]
    G=[[F(rand.randint(-4,4)) for _ in range(n)] for _ in range(s)]
    U=[row[:k] for row in G]
    W=mm(trans(U),U)
    try:Winv=inverse(W)
    except ZeroDivisionError:return False
    z=[row[k] for row in G]
    zeta=vec(trans(U),z)
    t=vec(Winv,zeta)
    Ti=inverse(T)
    a=vec(Ti,[F(int(i==k-1)) for i in range(k)])
    c=Ti[k-1][0]
    d=dot(a,t)
    B=mm(W,T)
    for i in range(k):B[i][k-1]+=zeta[i]
    assert det(B)==det(W)*det(T)*(1+d)
    if 1+d==0:return False
    coeff=vec(inverse(B),vec(W,[F(1)]+[F(0)]*(k-1)))
    assert coeff[-1]==c/(1+d)
    t_inv=vec(Ti,t)
    rhs=[Ti[i][0]-c*t_inv[i]/(1+d) for i in range(k)]
    assert coeff==rhs
    return True


def student_density_at_negative_one(nu,eta):
    # d = eta*T_nu/sqrt(nu)
    return gamma((nu+1)/2)/(gamma(nu/2)*sqrt(pi)*eta)*(1+eta**(-2))**(-(nu+1)/2)


def integrate_density(nu,eta,a,b,N=400):
    h=(b-a)/N
    val=0.
    for i in range(N+1):
        x=a+i*h
        y=gamma((nu+1)/2)/(gamma(nu/2)*sqrt(pi)*eta)*(1+x*x/(eta*eta))**(-(nu+1)/2)
        val+=(1 if i in (0,N) else 4 if i%2 else 2)*y
    return val*h/3


def main():
    rand=Random(20261010)
    n=0
    for k in (2,3,4):
        for s in (k,k+1,k+3,k+8):
            for i in range(150):
                n+=int(case(k,s,rand))
    assert n>1100,n
    tailchecks=0
    for k,detT,norm_a2 in [(2,F(8),F(10,64)),(3,F(21),F(0))]:
        if k==3:
            Ti=inverse([[F(3 if i==j else 1 if abs(i-j)==1 else 0) for j in range(3)] for i in range(3)])
            norm_a2=sum(Ti[i][2]**2 for i in range(3))
        c=abs(F((-1)**(k-1),1)/detT)
        for s in (k,k+2,k+6):
            nu=s-k+1;eta=sqrt(float(norm_a2))
            C=2*float(c)*student_density_at_negative_one(nu,eta)
            for R in (1000,5000):
                prob=integrate_density(nu,eta,-1-float(c)/R,-1+float(c)/R)
                assert abs(prob*R/C-1)<3e-5,(k,s,R,prob*R/C)
                tailchecks+=1
    print('VERIFY_OK rational_sketched_Lanczos_cases=',n,'density_tail_checks=',tailchecks)

if __name__=='__main__':main()
