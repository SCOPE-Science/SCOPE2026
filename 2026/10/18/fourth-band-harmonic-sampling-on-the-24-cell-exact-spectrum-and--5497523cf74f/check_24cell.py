"""Exact, standalone checks for fourth-band harmonic sampling on the 24-cell.

Only Python's standard library is needed. This is finite corroboration;
the accompanying proof establishes the statements in all claimed cases.
"""
from fractions import Fraction
from itertools import product
from math import prod

N = 24
nodes = []
for i in range(4):
    for s in (-1, 1):
        v = [0]*4
        v[i] = 2*s
        nodes.append(tuple(v))
for s in product((-1,1), repeat=4):
    nodes.append(tuple(s))
assert len(nodes)==N and len(set(nodes))==N

def us(l, x):
    if l==0: return Fraction(1)
    a,b = Fraction(1), 2*x
    if l==1: return b
    for _ in range(1,l):
        a,b = b, 2*x*b-a
    return b

def kernel(L):
    return [[sum((j+1)*us(j,Fraction(sum(a*b for a,b in zip(x,y)),4)) for j in range(L+1))
             for y in nodes] for x in nodes]

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def subtract_scalar(A,t):
    return [[a-(t if i==j else 0) for j,a in enumerate(row)] for i,row in enumerate(A)]

def rank(M):
    a = [[Fraction(z) for z in row] for row in M]
    n=len(a)
    lead=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(lead,n) if a[i][col]), None)
        if pivot is None: continue
        a[lead],a[pivot]=a[pivot],a[lead]
        t=a[lead][col]
        a[lead]=[v/t for v in a[lead]]
        for i in range(lead+1,n):
            if a[i][col]:
                z=a[i][col]
                a[i]=[v-z*w for v,w in zip(a[i],a[lead])]
        lead+=1
        if lead==n: break
    return lead

Ks = [kernel(L) for L in range(5)]
assert [rank(K) for K in Ks] == [1,5,14,22,24]
K=Ks[4]
bydot={}
for x in nodes:
    for y in nodes:
        dot=Fraction(sum(a*b for a,b in zip(x,y)),4)
        bydot.setdefault(dot, K[nodes.index(x)][nodes.index(y)])
assert bydot == {Fraction(-1):15, Fraction(-1,2):-2, Fraction(0):3,
                 Fraction(1,2):-6, Fraction(1):55}, bydot
I=eye(N)
polyprod=I
for e in (24,48,64,120):
    polyprod=matmul(polyprod,subtract_scalar(K,e))
assert not any(v for row in polyprod for v in row)
assert sum(K[i][i] for i in range(N))==1320
assert sum(z*z for row in K for z in row)==(5*24**2+8*48**2+9*64**2+2*120**2)
# Polynomial inverse for the uniformly normalized Gram G=K/24.
G=[[Fraction(z,24) for z in row] for row in K]
G2=matmul(G,G)
G3=matmul(G,G2)
Ginv=[[-Fraction(3,80)*G3[i][j]+Fraction(2,5)*G2[i][j]
       -Fraction(23,16)*G[i][j]+Fraction(83,40)*I[i][j]
       for j in range(N)] for i in range(N)]
assert matmul(G,Ginv)==I
# Flat extremal eigenvectors: constant and primitive-cube-root colored corners.
# Instead of complex arithmetic, use Q(omega), omega^2=-omega-1.
const=[1]*N
assert [sum(G[i][j]*const[j] for j in range(N)) for i in range(N)]==const
# corner color 1,omega or omega^2, encoded in basis (1,omega).
phases=[(1,0)]*8+[(0,1) if prod(s)==1 else (-1,-1)
                        for s in product((-1,1),repeat=4)]
for i in range(N):
    a=sum(G[i][j]*phases[j][0] for j in range(N))
    b=sum(G[i][j]*phases[j][1] for j in range(N))
    assert (a,b)==(5*phases[i][0],5*phases[i][1])
print('PASS: 24 nodes; ranks (1,5,14,22,24); exact 4-factor kernel polynomial;')
print('      normalized Gram eigenvalues 1[5], 2[8], 8/3[9], 5[2];')
print('      inverse polynomial and flat endpoint eigenvectors checked.')
