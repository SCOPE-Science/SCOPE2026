"""Exact finite checks and numerical lattice-kernel diagnostics for Radau IIA heat stepping.

Requires Python 3.9+ standard library. Run: python verify.py
This checker supplements, but does not replace, the stated analytic proof.
"""
from fractions import Fraction as F
from cmath import sqrt, phase
from math import cos

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def matadd(a,b,sa=1,sb=1):
    return [[sa*a[i][j]+sb*b[i][j] for j in range(len(a))] for i in range(len(a))]

def inverse(a):
    n=len(a)
    aug=[a[i][:]+eye(n)[i] for i in range(n)]
    for i in range(n):
        k=next(k for k in range(i,n) if aug[k][i])
        aug[i],aug[k]=aug[k],aug[i]
        pivot=aug[i][i]
        aug[i]=[x/pivot for x in aug[i]]
        for j in range(n):
            if j!=i and aug[j][i]:
                v=aug[j][i]
                aug[j]=[aug[j][c]-v*aug[i][c] for c in range(2*n)]
    return [row[n:] for row in aug]

def heat_generator(n):
    q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        q[i][i]=F(-2)
        q[i][(i+1)%n]+=1
        q[i][(i-1)%n]+=1
    return q

def radau(n,h):
    q=heat_generator(n)
    I=eye(n)
    q2=matmul(q,q)
    # R(hQ) = (6I+2hQ) (6I-4hQ+h^2 Q^2)^{-1}.
    denominator=matadd(matadd(I,q,6,-4*h),q2,1,h*h)
    numerator=matadd(I,q,6,2*h)
    return matmul(numerator,inverse(denominator))

coeff=[F(1), F(1)]
for k in range(2,9):
    coeff.append(F(2,3)*coeff[-1]-F(1,6)*coeff[-2])
assert coeff[:7]==[F(1),F(1),F(1,2),F(1,6),F(1,36),-F(1,108),-F(7,648)]

checks=0
for n in range(3,15):
    for h in (F(1,10000), F(1000000)):
        P=radau(n,h)
        assert all(sum(row)==1 for row in P)
        assert all(P[i][j]==P[(i+1)%n][(j+1)%n] for i in range(n) for j in range(n))
        assert all(P[i][j]==P[j][i] for i in range(n) for j in range(n))
        if h==F(1,10000):
            if n<=9:
                assert all(x>0 for row in P for x in row),n
            else:
                assert P[0][5]<0,n
        else:
            assert all(x>0 for row in P for x in row),n
        checks+=n*n

# Every sampled infinite-lattice kernel changes sign at least once.
# It is not a proof for arbitrary h; that follows from the nonreal characteristic root.
tests=[]
for h in (0.001,0.1,1.0,5.0,50.0):
    a=h*(1+1j/2**.5)/3
    q=(1+2*a-sqrt(1+4*a))/(2*a)
    C=(.5-1j*2**.5)/sqrt(1+4*a)
    ks=[2*(C*q**m).real for m in range(120)]
    negative=[m for m,x in enumerate(ks) if x<0]
    assert abs(q)<1 and abs(q.imag)>1e-12
    assert negative
    assert abs(ks[0]+2*sum(ks[1:80])-1)<1e-8 if h<5 else True
    tests.append((h,negative[0],ks[negative[0]]))
print('VERIFY_OK',checks,'exact rational matrix entries; sign-change examples:',tests)
