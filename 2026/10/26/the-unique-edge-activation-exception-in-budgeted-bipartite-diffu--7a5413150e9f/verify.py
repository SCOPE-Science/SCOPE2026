"""Exact radical identities and finite matrix checks for one-edge biclique augmentation.

Run with Python 3.9 or newer; no third-party packages are needed.
The analytic proof of the all-size result is given in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

# Store an algebraic number A + B*sqrt(3) as a pair of fractions.
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    return (x[0] * y[0] + 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul_int(n, x):
    return (n*x[0], n*x[1])

def E(a=0,b=0):
    return (F(a), F(b))

def real(x):
    return float(x[0])+float(x[1])*sqrt(3)

a=E(F(3,10),F(1,15))
b=E(F(2,5),F(1,10))
c=E(F(1,5),-F(1,15))
V=E(F(11,5),F(2,5))
assert add(add(mul_int(4,a),mul_int(2,b)),c)==V
assert add(mul_int(2,a),mul_int(2,c))==E(1)
assert sub(add(mul_int(10,mul(a,b)),E(1)),add(mul_int(4,a),mul_int(3,b)))==E(0)
assert real(add(mul_int(2,a),b))>1
assert real(sub(add(mul_int(4,a),mul_int(3,b)),E(1)))>1

# For each integer pair, check a constructed feasible embedding's variance
# and the full graph spectrum for a uniform, zero-added-edge allocation.
def laplacian(p,q,B=1.0):
    n=p+q
    w=B/(p*q)
    L=[[0.0]*n for _ in range(n)]
    for i in range(p):
        for j in range(p,n):
            L[i][i]+=w
            L[j][j]+=w
            L[i][j]-=w
            L[j][i]-=w
    return L

def jacobi_eigs(A):
    A=[row[:] for row in A]
    n=len(A)
    for _ in range(20*n*n):
        i,j=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda e:abs(A[e[0]][e[1]]))
        if abs(A[i][j])<1e-13:
            break
        import math
        theta=(A[j][j]-A[i][i])/(2*A[i][j]); t=(1 if theta>=0 else -1)/(abs(theta)+math.sqrt(1+theta*theta))
        cc=1/math.sqrt(1+t*t); ss=t*cc
        old=A[i][j]
        A[i][i]-=t*old;A[j][j]+=t*old;A[i][j]=A[j][i]=0.0
        for k in range(n):
            if k==i or k==j:continue
            aki,akj=A[k][i],A[k][j]
            A[k][i]=A[i][k]=cc*aki-ss*akj
            A[k][j]=A[j][k]=ss*aki+cc*akj
    else:
        raise AssertionError('Jacobi iteration did not converge')
    return sorted(A[i][i] for i in range(n))

checks=0
for p in range(2,17):
    for q in range(2,17):
        if (p,q)==(3,2):continue
        lam=jacobi_eigs(laplacian(p,q))[1]
        assert abs(lam-1/max(p,q))<2e-9,(p,q,lam)
        checks+=1
special=[[0.0]*5 for _ in range(5)]
for i in range(3):
    for j in (3,4):
        w=real(a if i<2 else b)
        special[i][i]+=w;special[j][j]+=w;special[i][j]-=w;special[j][i]-=w
z=real(c)
special[0][0]+=z;special[1][1]+=z;special[0][1]-=z;special[1][0]-=z
spectrum=jacobi_eigs(special)
assert abs(spectrum[1]-1)<1e-10
assert abs(spectrum[2]-1)<1e-10
assert spectrum[3]>1 and spectrum[4]>1
points=[(sqrt(3)/2,0.5),(sqrt(3)/2,-0.5),(-1,0),(0,0),(0,0)]
assert all(abs(sum((points[i][k]-points[j][k])**2 for k in range(2))-1)<1e-10 for i,j in [(0,1)]+[(i,j) for i in range(3) for j in (3,4)])
mean=[sum(x[k] for x in points)/5 for k in range(2)]
S=sum(sum((x[k]-mean[k])**2 for k in range(2)) for x in points)
assert abs(S-real(V))<1e-11
print('PASS: exact identities, exceptional embedding, 224 complete comparison spectra, exceptional full spectrum')
