"""Exact rational and numerical checks for weighted tetrahedral up-Laplacian preconditioning.
Run: python3 weighted_tetra_check.py (Python 3 standard library only).
The analytic proof, not these finite checks, establishes universal assertions.
"""
from fractions import Fraction as Q
import math

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
FACES = [((1,2,3),1),((0,2,3),-1),((0,1,3),1),((0,1,2),-1)]

def boundary(face,sgn):
    i,j,k=face
    terms={(j,k):sgn,(i,k):-sgn,(i,j):sgn}
    return [Q(terms.get(e,0)) for e in EDGES]

B=[[boundary(face,sgn)[i] for face,sgn in FACES] for i in range(6)]
assert all(sum(B[i])==0 for i in range(6))
assert all(sum(B[i][j]*B[i][k] for i in range(6))==(3 if j==k else -1)
           for j in range(4) for k in range(4))

def mm(A,C):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*C)] for row in A]

def trans(A):
    return list(map(list,zip(*A)))

def lap(weights):
    return [[sum(B[i][k]*weights[k]*B[j][k] for k in range(4)) for j in range(6)] for i in range(6)]

def form(a):
    w=[a,Q(1),Q(1)/a,Q(1)]
    M=[[ (w[i] if i==j else Q(0))+w[3] for j in range(3)] for i in range(3)]
    B3=[row[:3] for row in B]
    return w,M,B3

def determinant3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def characteristic(A):
    tr=sum(A[i][i] for i in range(3))
    pair=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i,j in [(0,1),(0,2),(1,2)])
    return tr,pair,determinant3(A)

def jacobi3(A):
    A=[[float(y) for y in row] for row in A]
    for _ in range(150):
        i,j=max(((0,1),(0,2),(1,2)),key=lambda z:abs(A[z[0]][z[1]]))
        if abs(A[i][j])<1e-14: break
        theta=.5*math.atan2(2*A[i][j],A[j][j]-A[i][i])
        c,s=math.cos(theta),math.sin(theta)
        # Orthogonal rotation: columns (cos,-sin), (sin,cos)
        R=[[float(i==j) for j in range(3)] for i in range(3)]
        R[i][i]=c;R[j][j]=c;R[i][j]=s;R[j][i]=-s
        A=[[sum(R[k][x]*A[k][l]*R[l][y] for k in range(3) for l in range(3))
            for y in range(3)] for x in range(3)]
    return sorted(A[i][i] for i in range(3))

checks=0
for a in [Q(1),Q(1,2),Q(1,3),Q(1,10),Q(1,100),Q(1,1000),Q(1,10000),Q(1,1000000)]:
    w,M,B3=form(a)
    L=lap(w)
    fact=mm(mm(B3,M),trans(B3))
    assert fact==L;checks+=1
    # All original face columns in a single tetrahedral boundary cycle.
    assert determinant3(mm(trans(B3),B3))==16;checks+=1
    inherited=[w[0],w[1],w[2]]
    inherited_nonunit=Q(2)+a+1/a
    assert inherited_nonunit==1+sum(1/d for d in inherited);checks+=1
    # Jacobi-type retained-face reweighting.
    d=[M[i][i] for i in range(3)]
    # A = D^{-1}M is similar to the symmetric preconditioned matrix.
    A=[[M[i][j]/d[i] for j in range(3)] for i in range(3)]
    tr,pair,det=characteristic(A)
    t=a/(1+a)**2
    assert (tr,pair,det)==(Q(3),Q(5,2)-t,Q(1,2));checks+=1
    P=[[float(M[i][j])/math.sqrt(float(d[i]*d[j])) for j in range(3)] for i in range(3)]
    ev=jacobi3(P)
    assert all(x>0 for x in ev);checks+=1
    assert abs(sum(ev)-3)<1e-9;checks+=1
    assert abs(ev[0]*ev[1]*ev[2]-.5)<1e-9;checks+=1
    c=1/math.sqrt(2*(1+float(a)))
    low=(1+c)/(1-c)
    ratio=ev[2]/ev[0]
    assert ratio+1e-8>=low;checks+=1
    assert ratio<=6;checks+=1
    if a==Q(1,1000000):
        optimal_limit=3+2*math.sqrt(2)
        assert abs(ratio-optimal_limit)<1e-6;checks+=1
        assert abs(float(a)*float(inherited_nonunit)/ratio-(3-2*math.sqrt(2)))<1e-6;checks+=1
print('PASS:',checks,'tetrahedral exact rational identities / numerical spectral checks')
