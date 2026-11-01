#!/usr/bin/env python3
"""Exact integer/rational certificate for the centered ball maximal norm on the triangular-prism graph."""
from fractions import Fraction
from itertools import permutations, product
from math import sqrt

N=6
V=range(N)
EDGES = {(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)}
EDGES |= {(b,a) for a,b in tuple(EDGES)}
D=[]
for src in V:
    distance=[N+1]*N
    distance[src]=0
    queue=[src]
    for i in queue:
        for j in V:
            if (i,j) in EDGES and distance[j]>distance[i]+1:
                distance[j]=distance[i]+1
                queue.append(j)
    D.append(tuple(distance))
assert all(sorted(set(row)) == [0,1,2] for row in D)
assert all(sum(d==1 for d in row)==3 for row in D)
ROWS=[]
for i in V:
    choices=[]
    for r in range(3):
        ball=[j for j in V if D[i][j]<=r]
        assert len(ball) in (1,4,6) and 12%len(ball)==0
        choices.append(tuple(12//len(ball) if j in ball else 0 for j in V))
    ROWS.append(choices)

def selected_matrix(c):
    return [ROWS[i][c[i]] for i in V]

def gram(T):
    return [[sum(T[k][i]*T[k][j] for k in V) for j in V] for i in V]

def positive_definite_bareiss(M):
    """Unpivoted fraction-free LDL: positive pivots iff all leading minors are positive."""
    M=[list(row) for row in M]
    old=1
    for k in V:
        p=M[k][k]
        if p<=0:
            return False,k
        for i in range(k+1,N):
            for j in range(k+1,N):
                z=p*M[i][j]-M[i][k]*M[k][j]
                assert z%old==0
                M[i][j]=z//old
        old=p
    return True,N

exception=[]
strict=0
for c in product(range(3), repeat=N):
    A=selected_matrix(c)
    G=gram(A)
    # 1044 I - 5 A^T A = 720(29/20 I - (A/12)^T(A/12)).
    F=[[1044*int(i==j)-5*G[i][j] for j in V] for i in V]
    ok,step=positive_definite_bareiss(F)
    if ok:
        strict+=1
    else:
        assert step==5
        exception.append(c)
assert strict==723 and len(exception)==6
base=(0,1,2,1,0,2)
assert base in exception
orbit=set()
for pi in permutations(range(3)):
    for flip in (0,1):
        c=[None]*N
        for i in V:
            gi=pi[i%3]+3*((i//3)^flip)
            c[gi]=base[i]
        orbit.add(tuple(c))
assert set(exception)==orbit
assert len(orbit)==6
for c in exception:
    peaks=[i for i in V if c[i]==0]
    assert len(peaks)==2 and D[peaks[0]][peaks[1]]==2
    assert sorted(c)==[0,0,1,1,2,2]

def mult(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in V) for j in V] for i in V]

def charpoly_integer(M):
    # Faddeev-LeVerrier exact characteristic coefficients, monic, descending.
    B=[[int(i==j) for j in V] for i in V]
    coefficients=[1]
    for k in range(1,N+1):
        C=mult(M,B)
        tr=sum(C[i][i] for i in V)
        assert tr%k==0
        ck=-tr//k
        coefficients.append(ck)
        B=[[C[i][j]+ck*int(i==j) for j in V] for i in V]
    assert all(v==0 for row in B for v in row)
    return coefficients

def poly_product(*factors):
    p=[1]
    for factor in factors:
        q=[0]*(len(p)+len(factor)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(factor):
                q[i+j]+=a*b
        p=q
    return p

A=selected_matrix(base)
G=gram(A)
expected=poly_product([1,0],[1,0],[1,-144],[1,-18],[1,-246,7488])
assert charpoly_integer(G)==expected
# A^T A has eigenvalues 144 times the roots of
# lambda^2 (lambda-1) (lambda-1/8) (72 lambda^2-123 lambda+26).
assert 72*Fraction(29,20)**2-123*Fraction(29,20)+26<0
# Invariant positive vector v=(1,a,a,a,1,a). Using the two row formulas:
# (B^T B v)_{0,4}=(49+17a)/36;
# (B^T B v)_{1,2,3,5}=(17+25a)/72.
# Hence 34a^2+73a-17=0 and a=(sqrt(7641)-73)/68.
a=(sqrt(7641)-73)/68
lam=(123+sqrt(7641))/144
assert 0<a<1 and lam>29/20
assert abs((49+17*a)/36-lam)<1e-13
assert abs((17+25*a)/72-lam*a)<1e-13
x=[1,a,a,a,1,a]
for i in V:
    values=[sum(ROWS[i][r][j]*x[j] for j in V)/12 for r in range(3)]
    assert values[base[i]]>max(v for r,v in enumerate(values) if r!=base[i])+1e-5
print('CERTIFICATE_OK selections=729 strict=723 exceptional=6 distance_two_pairs=6 characteristic=exact')
print('SQUARED_NORM',lam, 'NORM', sqrt(lam), 'LOW_AMPLITUDE',a)
