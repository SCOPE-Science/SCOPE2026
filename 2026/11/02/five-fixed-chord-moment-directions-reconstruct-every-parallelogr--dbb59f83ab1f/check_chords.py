#!/usr/bin/env python3
"""Standalone exact and numerical tests of five-view parallelogram chord tomography.
The analytical theorem and reconstruction proof do not rely on finite tests.
"""
from fractions import Fraction as F
from itertools import product
from math import hypot

def dot(a,b): return a[0]*b[0]+a[1]*b[1]

def solve3(mat,vec):
    a=[[F(t) for t in row]+[F(v)] for row,v in zip(mat,vec)]
    for i in range(3):
        k=next(k for k in range(i,3) if a[k][i])
        a[i],a[k]=a[k],a[i]
        p=a[i][i]
        a[i]=[z/p for z in a[i]]
        for j in range(3):
            if j!=i:
                f=a[j][i]
                a[j]=[x-f*y for x,y in zip(a[j],a[i])]
    return tuple(a[i][-1] for i in range(3))

def valquad(v,c):
    x,y=v
    return c[0]*x*x+c[1]*x*y+c[2]*y*y

def coeff(v):
    x,y=v
    return (x*x,x*y,y*y)

# Four *distinct* unoriented rational directions have genuinely indistinguishable
# noncongruent parallelograms, despite their entire laws being identical.
A1=((F(2),F(0)),(F(0),F(1)))
A2=((F(6,5),F(4,5)),(F(-8,5),F(3,5)))
ambiguous_views=((1,1),(1,6),(1,-4),(3,-2))
assert len({F(y,x) for x,y in ambiguous_views})==4
assert dot(A1[0],A1[1])==0 and dot(A2[0],A2[1])==F(-36,25)
assert A1[0][0]*A1[1][1]-A1[0][1]*A1[1][0] == A2[0][0]*A2[1][1]-A2[0][1]*A2[1][0]==2
for v in ambiguous_views:
    assert sorted(abs(dot(row,v)) for row in A1)==sorted(abs(dot(row,v)) for row in A2)
print('EXACT_FOUR_VIEW_NONCONGRUENCE_AND_FULL_LAW_AMBIGUITY_PASSED')

# All quadratic candidate signs are checked exactly at FIVE prescribed directions.
# Every triple determines the coefficients of a binary quadratic.
views=((1,0),(0,1),(1,1),(1,2),(2,-1))
assert len({(F(y,x) if x else 'inf') for x,y in views})==5
A=((F(2),F(1)),(F(-1),F(3)))
S=[sum(dot(row,v)**2 for row in A) for v in views]
D=[abs(dot(A[0],v)**2-dot(A[1],v)**2) for v in views]
mat=[coeff(v) for v in views[:3]]
M=solve3(mat,S[:3]); assert all(valquad(v,M)==s for v,s in zip(views,S))
valid=set()
for signs in product((-1,1),repeat=5):
    N=solve3(mat,[signs[i]*D[i] for i in range(3)])
    if all(abs(valquad(v,N))==d for v,d in zip(views,D)):
        valid.add(N)
N_true=(A[0][0]**2-A[1][0]**2, 2*(A[0][0]*A[0][1]-A[1][0]*A[1][1]), A[0][1]**2-A[1][1]**2)
assert valid=={N_true,tuple(-x for x in N_true)},(valid,N_true)
assert M==(A[0][0]**2+A[1][0]**2,2*(A[0][0]*A[0][1]+A[1][0]*A[1][1]),A[0][1]**2+A[1][1]**2)
print('EXACT_FIVE_VIEW_BINARY_QUADRATIC_RECOVERY_PASSED')

# Direct offset-line clipping, independent of the uniform-plus-atom derivation.
def direct_moments(A,e,n=10000):
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    vertices=[]
    for signs in product((-1,1),repeat=2):
        x=(signs[0]*A[1][1]-signs[1]*A[0][1])/det
        y=(-signs[0]*A[1][0]+signs[1]*A[0][0])/det
        vertices.append((float(x),float(y)))
    vnorm=hypot(*e);ex,ey=(e[0]/vnorm,e[1]/vnorm)
    nx,ny=-ey,ex
    offsets=[nx*x+ny*y for x,y in vertices]
    lo,hi=min(offsets),max(offsets)
    total1=total2=0.0
    for i in range(n):
        t=lo+(hi-lo)*(i+0.5)/n
        lb,ub=-float('inf'),float('inf')
        for row in A:
            c=float(row[0])*nx+float(row[1])*ny
            q=float(row[0])*ex+float(row[1])*ey
            if abs(q)<1e-15:
                assert abs(c*t)<=1+1e-10
                continue
            t1=(-1-c*t)/q;t2=(1-c*t)/q
            lb=max(lb,min(t1,t2));ub=min(ub,max(t1,t2))
        seg=max(0.0,ub-lb)
        total1+=seg;total2+=seg*seg
    return total1/n,total2/n

def formula_moments(A,e):
    vnorm=hypot(*e)
    a,b=sorted((abs(float(dot(row,e)))/vnorm for row in A),reverse=True)
    assert a>0
    L=2/a
    p=(a-b)/(a+b)
    return L*(1+p)/2,L*L*(1+2*p)/3

for AA in (A1,A2,A):
    for e in ((1,0),(0,1),(1,1),(1,6),(1,-4),(3,-2),(2,3)):
        actual=direct_moments(AA,e)
        expect=formula_moments(AA,e)
        assert all(abs(x-y)<4e-6 for x,y in zip(actual,expect)),(AA,e,actual,expect)
print('INDEPENDENT_OFFSET_LINE_CLIPPING_MOMENTS_PASSED 21')

# Exact distribution has a uniform continuous component and a possible point mass.
# The first two moments invert its two unknown parameters everywhere on 0<=p<=1.
for p in (0,0.03,0.2,0.5,0.73,1):
    L=2.75
    mean=L*(1+p)/2
    second=L*L*(1+2*p)/3
    eta=(max(0.,1-3*second/(4*mean*mean)))**0.5
    pback=eta/(1-eta)
    assert abs(p-pback)<2e-7,(p,pback)
print('MOMENT_INVERSION_ENDPOINTS_AND_INTERIOR_PASSED')
print('ALL_CHECKS_PASSED')
