#!/usr/bin/env python3
"""Exact rational verification of a public-goods modal dispersion witness."""
from fractions import Fraction as Q

def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,Q(0))+v
    return {k:v for k,v in c.items() if v}

def mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            key=(i+k,j+l)
            c[key]=c.get(key,Q(0))+x*y
    return {k:v for k,v in c.items() if v}

def neg(a):return {k:-v for k,v in a.items()}
def poly(*terms):return {(i,j):Q(num,den) for i,j,num,den in terms}
def const(q):return {(0,0):q}
def evaluate(poly,z,q):return sum(v*z**i*q**j for (i,j),v in poly.items())
# variable z and squared wave number q, with a literal modal matrix M
z=poly((1,0,1,1)); q=poly((0,1,1,1))
M=[[add(neg(q),const(-Q(1,40))),const(-Q(1,40)),const(Q(431,400))],
   [const(-Q(1,40)),add(neg(mul(q,const(Q(1,10)))),const(-Q(1,40))),const(Q(541,400))],
   [const(Q(11)),const(Q(-10)),add(neg(mul(q,const(Q(1,10)))),const(-Q(21,20)))]]
A=[[add(z,neg(M[i][j])) if i==j else neg(M[i][j]) for j in range(3)] for i in range(3)]
def permutation_sign(p):return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
from itertools import permutations
p={}
for perm in permutations(range(3)):
    term=const(Q(permutation_sign(perm)))
    for i in range(3):term=mul(term,A[i][perm[i]])
    p=add(p,term)
coefficient=lambda power:{j:v for (i,j),v in p.items() if i==power}
a1={0:Q(11,10),1:Q(12,10)}
a2={0:Q(690,400),1:Q(475,400),2:Q(84,400)}
a3={0:Q(1155,8000),1:Q(98949,8000),2:Q(862,8000),3:Q(80,8000)}
for i,expect in [(3,{0:Q(1)}),(2,a1),(1,a2),(0,a3)]:assert coefficient(i)==expect,(i,coefficient(i),expect)
assert {i for (i,j) in p}=={0,1,2,3}
# Exact equilibrium checks.
u=v=Q(1,20);phi=Q(1)
Du=Q(1);Dv=Dphi=Q(1,10);gamma=Q(1,2);kappa=Q(10);delta=Q(1,20)
c=Q(21);ru=Q(431,20);rv=Q(541,20);mu_u=Q(1,2);mu_v=Q(27)
assert ru*phi-c-gamma*(u+v)-mu_u==0
assert rv*phi-gamma*(u+v)-mu_v==0
assert c*u-(kappa*(u+v)+delta)*phi==0
# Compute the cubic Hurwitz determinant from exact coefficient polynomials.
def univar_mul(a,b):
    d={}
    for i,x in a.items():
        for j,y in b.items():d[i+j]=d.get(i+j,Q(0))+x*y
    return d
h=univar_mul(a1,a2)
for j,cj in a3.items():h[j]=h.get(j,Q(0))-cj
assert h=={0:Q(14025,8000),1:Q(-71939,8000),2:Q(12386,8000),3:Q(1936,8000)}
value=lambda d,x:sum(v*x**i for i,v in d.items())
assert value(h,0)==Q(561,320)
assert value(h,1)==Q(-5449,1000)
assert value(h,4)==Q(48349,8000)
assert all(v>0 for coeff in (a1,a2,a3) for v in coeff.values())
print('PASS: equilibrium, modal determinant, positive coefficients, exact H and signs.')
print('All-wavenumber and uniqueness claims use proof by Descartes and Routh–Hurwitz, not enumeration.')
