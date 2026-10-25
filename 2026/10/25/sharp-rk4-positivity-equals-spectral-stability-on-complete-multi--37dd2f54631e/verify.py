#!/usr/bin/env python3
"""Independent exact checks for the RK4 complete-multipartite diffusion theorem.

No network access; requires SymPy.  The infinite-dimensional quantifiers
are handled in the accompanying mathematical proof, not by enumeration.
"""
from itertools import combinations
from math import factorial
from fractions import Fraction
import sympy as sp

z,h,p,q=sp.symbols('z h p q', positive=True)
R=lambda x: 1-x+x*x/sp.Integer(2)-x**3/sp.Integer(6)+x**4/sp.Integer(24)
N=p+q
A=sp.factor((p+q*R(N*h)-N*R(q*h))/(p*N))
formula= h*h*q*(12-4*h*(p+2*q)+h*h*(p*p+3*p*q+3*q*q))/24
assert sp.simplify(A-formula)==0
cross=sp.factor((1-R(N*h))/N)
assert sp.simplify(cross - h*(24-12*N*h+4*N*N*h*h-N**3*h**3)/24)==0
D=sp.factor((-4*(p+2*q))**2-4*(p*p+3*p*q+3*q*q)*12)
assert sp.simplify(D+16*(2*p*p+5*p*q+5*q*q))==0
assert sp.simplify(R(z)-((1-z/2)**2+z*z*((z-2)**2+2)/24))==0
phi=lambda zz:24-12*zz+4*zz**2-zz**3
assert phi(sp.Rational(27852,10000))>0 and phi(sp.Rational(27854,10000))<0
assert sp.expand(sp.diff(phi(z),z)+12-8*z+3*z*z)==0
assert sp.simplify((3*z*z-8*z+12)-(3*(z-sp.Rational(4,3))**2+sp.Rational(20,3)))==0


def partitions(n, minimum=1):
    if n==0:
        yield ()
    else:
        for k in range(minimum,n+1):
            for rem in partitions(n-k,k):
                yield (k,)+rem


def matmul(U,V):
    n=len(U)
    return [[sum((U[i][k]*V[k][j] for k in range(n)),Fraction())
             for j in range(n)] for i in range(n)]


def rk4(L,step):
    n=len(L)
    I=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    K=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    cur=I
    for k in range(1,5):
        cur=matmul(cur,L)
        term=(-step)**k/factorial(k)
        for i in range(n):
            for j in range(n):
                K[i][j]+=term*cur[i][j]
    return K


def make_graph(partition):
    N=sum(partition)
    who=sum(([a]*v for a,v in enumerate(partition)),[])
    L=[[Fraction(0) for j in range(N)] for i in range(N)]
    for i,j in combinations(range(N),2):
        if who[i]!=who[j]:
            L[i][i]+=1; L[j][j]+=1
            L[i][j]-=1; L[j][i]-=1
    return L, who

# A graph outside the claimed family shows norm-stability need not imply positivity.
Lpath=[[Fraction(1),-Fraction(1),Fraction(0),Fraction(0)],
       [-Fraction(1),Fraction(2),-Fraction(1),Fraction(0)],
       [Fraction(0),-Fraction(1),Fraction(2),-Fraction(1)],
       [Fraction(0),Fraction(0),-Fraction(1),Fraction(1)]]
assert rk4(Lpath,Fraction(3,4))[0][3]==-Fraction(9,1024)
assert phi(sp.Rational(11,4))>0
assert sp.simplify(11-3*(2+sp.sqrt(2)))>0

pairs=checks=0
for n in range(2,11):
    for part in partitions(n):
        if len(part)<2: continue
        L,who=make_graph(part)
        for ratio in [Fraction(1,2), Fraction(1), Fraction(2), Fraction(3)]:
            step=ratio/n
            K=rk4(L,step)
            assert all(sum(row)==1 for row in K)
            assert all(K[i][i]>0 for i in range(n))
            for i,j in combinations(range(n),2):
                if who[i]!=who[j]:
                    expected=Fraction(1,1)*cross.subs({p:part[who[i]],q:n-part[who[i]],h:sp.Rational(step)})
                    assert K[i][j]==expected
                    if ratio<=2:assert K[i][j]>0
                    if ratio==3:assert K[i][j]<0
                else:
                    pa=part[who[i]]; qb=n-pa
                    expected=formula.subs({p:pa,q:qb,h:sp.Rational(step)})
                    assert K[i][j]==expected and K[i][j]>0
                assert K[i][j]==K[j][i]
                pairs+=1
            checks+=1
print(f'VERIFY_OK symbolic spectral identities, exact positivity certificates, '
      f'{checks} complete multipartite direct rational RK4 matrices, {pairs} vertex-pair checks')
