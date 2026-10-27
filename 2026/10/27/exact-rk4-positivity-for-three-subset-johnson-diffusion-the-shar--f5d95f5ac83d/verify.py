#!/usr/bin/env python3
"""Reproduce exact RK4 endpoint positivity identities for Johnson graphs J(n,3)."""
from itertools import combinations
from math import comb
import sympy as sp
import numpy as np

n,h=sp.symbols('n h', real=True)
d=3*(n-3)
# Distance-matrix multiplication in J(n,3), using intersection numbers.
b=lambda i:(3-i)*(n-3-i)
c=lambda i:i*i
a=lambda i:d-b(i)-c(i)
P=[{0:sp.Integer(1)}]
for order in range(4):
    nextp={i:sp.Integer(0) for i in range(4)}
    for j,coeff in P[-1].items():
        nextp[j]+=(a(j)-d)*coeff
        if j>0:nextp[j-1]+=b(j-1)*coeff
        if j<3:nextp[j+1]+=c(j+1)*coeff
    P.append({i:sp.expand(v) for i,v in nextp.items()})
actual={r:sp.expand(sum(h**m*P[m].get(r,0)/sp.factorial(m) for m in range(5))) for r in range(4)}
A=60*n-192;B=76*n*n-440*n+608;C=65*n**3-524*n*n+1328*n-1024
F=5*n**3-180*n*n+496*n-384
expected={
 1:h*(24-A*h+B*h*h-C*h**3)/24,
 2:h*h*(12+(-24*n+68)*h+(25*n*n-124*n+124)*h*h)/6,
 3:3*h**3*(2-(3*n-4)*h),
}
for r in (1,2,3):
    assert sp.expand(actual[r]-expected[r])==0, (r,sp.factor(actual[r]-expected[r]))
H3=sp.Integer(2)/(3*n-4)
assert sp.factor(expected[1].subs(h,H3)+2*F/(3*(3*n-4)**4))==0
assert sp.factor(3*A*C-B**2-4*(1481*n**4-16220*n**3+63712*n*n-103552*n+55040))==0
x=sp.symbols('x',nonnegative=True)
assert sp.expand((3*A*C-B**2).subs(n,x+6) - (5924*x**4+77296*x**3+366592*x*x+755264*x+572864))==0
assert sp.factor((-24*n+68)**2-48*(25*n*n-124*n+124)+16*(39*n*n-168*n+83))==0
assert sp.expand(F.subs(n,34+x)-(5*x**3+330*x*x+5596*x+4920))==0
z=sp.symbols('z')
assert sp.expand(F.subs(n,6+27*z) + 2808*(1-z)**3 + 3*12924*z*(1-z)**2 +3*44910*z*z*(1-z)+351*z**3)==0
assert sp.expand(24*(1-x+x*x/2-x**3/6+x**4/24)-((x*x-2*x)**2+8*(x*x-3*x+3)))==0

# Independent direct adjacency constructions and exact rational evaluations.
comparisons=0
for N in (6,7,8,9,10,11,12):
    verts=list(combinations(range(N),3)); size=len(verts)
    mat=np.zeros((size,size),dtype=np.int64)
    subsets=[set(v) for v in verts]
    for i in range(size):
        mat[i,i]=-3*(N-3)
        for j in range(i):
            if len(subsets[i]&subsets[j])==2:
                mat[i,j]=mat[j,i]=1
    powers=[np.eye(size,dtype=np.int64)]
    for i in range(4):powers.append(powers[-1]@mat)
    first=0
    for j in range(size):
        dist=3-len(subsets[first]&subsets[j])
        for val in (sp.Rational(1,5*N),sp.Rational(2,3*N-4),sp.Rational(1,3*(N-3))):
            direct=sum(sp.Rational(int(powers[k][first,j]))*val**k/sp.factorial(k) for k in range(5))
            predicted=actual[dist].subs({n:N,h:val})
            assert direct==predicted,(N,dist,val,direct,predicted)
            comparisons+=1
# Exact sign at the integer crossover and a direct root bracket.
assert F.subs(n,33)<0<F.subs(n,34)
assert expected[1].subs({n:33,h:sp.Rational(2,95)})>0
assert expected[1].subs({n:34,h:sp.Rational(2,98)})<0
print(f'VERIFY_OK: 3 symbolic distance-transition identities, 6 sign/threshold certificates, {comparisons} independent exact rational matrix entries, sharp n=34 switch')
