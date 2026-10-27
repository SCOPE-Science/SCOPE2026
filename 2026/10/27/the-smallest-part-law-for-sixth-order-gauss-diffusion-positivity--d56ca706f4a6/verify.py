"""Exact arithmetic checks for a three-stage Gauss diffusion theorem.

Requires SymPy 1.12+. Checks scalar certificates, spectral projector formulas,
and independent rational inverses on small complete multipartite graphs.
"""
from itertools import combinations_with_replacement, product
from fractions import Fraction
import sympy as sp

x = sp.symbols('x', real=True)
P = 120-60*x+12*x*x-x**3
Q = 120+60*x+12*x*x+x**3
r = P/Q
g = (1-r)/x
assert sp.cancel(g - 2*(x*x+60)/Q) == 0
assert sp.cancel(sp.diff(r,x) + 24*((x*x-15)**2+375)/Q**2) == 0
assert sp.cancel(sp.diff(g,x) + 2*(x**4+120*x*x+1200*x+3600)/Q**2) == 0
assert sp.expand((P+Q) - 24*(x*x+10)) == 0
assert sp.expand((Q-P) - 2*x*(x*x+60)) == 0
assert sp.series(r-sp.exp(-x),x,0,7).removeO() == 0

def as_graph(parts):
    n=sum(parts)
    grp=[i for i,m in enumerate(parts) for _ in range(m)]
    L=sp.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            if grp[i]!=grp[j]:
                L[i,i]+=1
                L[j,j]+=1
                L[i,j]=L[j,i]=-1
    return L,grp

def R(z):
    return (120-60*z+12*z*z-z**3)/(120+60*z+12*z*z+z**3)

def G(z):
    return 2*(z*z+60)/(120+60*z+12*z*z+z**3)

def formula(n,m,h,i,j,same_part):
    if i!=j and not same_part:
        return h*G(n*h)
    if i!=j:
        return (n-m)*h*(G((n-m)*h)-G(n*h))/m
    return sp.Rational(1,n)+(sp.Rational(1,m)-sp.Rational(1,n))*R(n*h)+(1-sp.Rational(1,m))*R((n-m)*h)

num_graphs=num_entries=0
for n in range(2,10):
    for num_parts in range(2,n+1):
        for parts in combinations_with_replacement(range(1,n),num_parts):
            if sum(parts)!=n:continue
            L,grp=as_graph(parts)
            for h in (sp.Rational(1,5),sp.Rational(1,1),sp.Rational(7,1)):
                A=h*L
                den=120*sp.eye(n)+60*A+12*A*A+A*A*A
                nom=120*sp.eye(n)-60*A+12*A*A-A*A*A
                T=den.inv()*nom
                assert T == T.T
                for i in range(n):
                    assert sum(T[i,j] for j in range(n))==1
                    for j in range(n):
                        m=parts[grp[i]]
                        expected=formula(n,m,h,i,j,grp[i]==grp[j])
                        assert sp.cancel(T[i,j]-expected)==0,(parts,h,i,j,T[i,j],expected)
                        if i!=j:assert T[i,j]>0,(parts,h,i,j,T[i,j])
                        num_entries+=1
                for a,b in zip(sorted(set(parts)),sorted(set(parts))[1:]):
                    assert formula(n,a,h,0,0,True)<formula(n,b,h,0,0,True)
            num_graphs+=1
for parts, target in [((2,2,2),sp.Rational(-66473,957799)),((3,3),sp.Rational(1999,166291))]:
    L,_=as_graph(parts)
    A=4*L
    T=(120*sp.eye(sum(parts))+60*A+12*A*A+A*A*A).inv()*(120*sp.eye(sum(parts))-60*A+12*A*A-A*A*A)
    assert T[0,0]==target
assert num_graphs == 87 and num_entries == 14925
print(f'VERIFY_OK scalar derivative and positivity certificates; {num_graphs} graphs; {num_entries} exact matrix-entry identities; exact stochasticity, smallest-part ordering, and two six-vertex signs')
