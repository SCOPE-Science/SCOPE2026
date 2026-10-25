#!/usr/bin/env python3
"""Independent finite rational checks for two-spoke wheel resilience formulas.
The universal monotonicity/asymptotic claims require the written proof.
"""
from fractions import Fraction as F
from sympy import Matrix, Rational, sqrt, simplify

def wheel(n):
    N=n+1
    L=Matrix.zeros(N)
    for i in range(n):
        for a,b in [(0,i+1),(i+1,(i+1)%n+1)]:
            L[a,a]+=1; L[b,b]+=1; L[a,b]-=1; L[b,a]-=1
    return L

def kf(L):
    N=L.rows
    return simplify(N*((L+Matrix.ones(N,N)/N).inv().trace()-1))

num=0
r=(3-sqrt(5))/2
for n in range(3,14):
    N=n+1;L=wheel(n);A=3*Matrix.eye(n)
    for i in range(n):A[i,(i+1)%n]-=1;A[i,(i-1)%n]-=1
    G=A.inv();H=G*G
    rho=G[0,0];sigma=H[0,0]-Rational(1,N);alpha=1-rho
    assert alpha>0 and sigma>0
    d1=kf(L)
    T=L.copy();T[0,0]-=1;T[1,1]-=1;T[0,1]+=1;T[1,0]+=1
    single=simplify(kf(T)-d1)
    assert simplify(single-N*sigma/alpha)==0
    num+=1
    g0=(1+r**n)/(sqrt(5)*(1-r**n))
    assert simplify(g0-rho)==0
    num+=1
    for d in range(1,n//2+1):
        Gd=(r**d+r**(n-d))/(sqrt(5)*(1-r**n))
        Hd=Gd*(Rational(3,5)+(d*r**d+(n-d)*r**(n-d))/(sqrt(5)*(r**d+r**(n-d)))+n*r**n/(sqrt(5)*(1-r**n)))
        assert simplify(Gd-G[0,d])==0
        assert simplify(Hd-H[0,d])==0
        T=L.copy()
        for v in [1,d+1]:
            T[0,0]-=1;T[v,v]-=1;T[0,v]+=1;T[v,0]+=1
        damage=simplify(kf(T)-d1)
        c=G[0,d];t=H[0,d]-Rational(1,N)
        rank=simplify(2*N*(alpha*sigma+c*t)/(alpha**2-c**2))
        assert simplify(damage-rank)==0
        inter=simplify(damage-2*single)
        Y=simplify(alpha*t+sigma*c)
        assert simplify(inter-2*N*c*Y/(alpha*(alpha**2-c**2)))==0
        num+=4
    Ylast=simplify(alpha*(H[0,n//2]-Rational(1,N))+sigma*G[0,n//2])
    assert (Ylast>0 if n<=5 else Ylast<0)
    if n>=4:
        delta=[]
        for d in range(1,n//2+1):
            c=G[0,d];t=H[0,d]-Rational(1,N)
            delta.append(simplify(2*N*(alpha*sigma+c*t)/(alpha**2-c**2)))
        assert all(delta[0]>e for e in delta[1:])
        num+=len(delta)-1
    if n in {3,4,5,6,7}:
        expected={3:Rational(1,16),4:Rational(4,225),5:Rational(1,726),6:-Rational(51,2800),7:-Rational(165,6728)}[n]
        assert Ylast==expected
        num+=1
q=F(2,5);m=4
z=q**(2*m)
upper=(2*m+2)*2*q**m*((F(4+m,5))/(1-z)+(F(2*m,5)*z)/(1-z)**2)
assert upper==F(125000000000,152387956161) and upper<1
num+=1
print('VERIFY_OK',num,'independent exact wheel damages, Green entries, pair identities, sign cases; bound')
