"""Exact-rational tests for weighted Frobenius diagonal inverse fitting.

Run: python verify.py
Uses only the Python standard library. These tests supplement the analytic proof.
"""
from fractions import Fraction as F
from random import Random


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def solve3(M, b):
    den=det3(M)
    assert den != 0
    return [det3([[b[i] if j == col else M[i][j] for j in range(3)] for i in range(3)])/den for col in range(3)]


def squared(M):
    return [[v*v for v in row] for row in M]


def objective(M, x):
    n=len(x)
    return F(n,2) - sum(x) + sum(x[i]*M[i][j]*x[j] for i in range(n) for j in range(n))/2


checks=0
r,z=F(9,10),F(7,10)
R=[[F(1),r,r],[r,F(1),z],[r,z,F(1)]]
H=squared(R)
x=solve3(H,[F(1)]*3)
assert det3(R)==F(3,125) and det3(H)==F(45339,500000)
assert x == [-F(650,889),F(950,889),F(950,889)]
checks+=3
boundary=[F(0),1/(1+z*z),1/(1+z*z)]
assert objective(H,boundary)-objective(H,x)==F(4225,132461)
checks+=1

rng=Random(34921)
for k in range(350):
    a,b,c=(F(rng.randint(-89,89),100) for _ in range(3))
    R=[[F(1),a,b],[a,F(1),c],[b,c,F(1)]]
    if det3(R)<=0: continue
    H=squared(R); den=det3(H)
    assert den>0
    aa,bb,cc=a*a,b*b,c*c
    predicted=[(1-cc)*(1+cc-aa-bb)/den,
               (1-bb)*(1+bb-aa-cc)/den,
               (1-aa)*(1+aa-bb-cc)/den]
    observed=solve3(H,[F(1)]*3)
    assert observed==predicted
    assert sum(v<0 for v in observed)<=1
    assert sum(v<=0 for v in observed)<=1
    assert all(sum(H[i][j]*observed[j] for j in range(3))==1 for i in range(3))
    checks+=5

# Test a dense exact grid inside the sharp star phase boundaries.
for j in range(1,20):
    z=F(j,20)
    lo=(1+z*z)/2
    hi=(1+z)/2
    for i in range(1,30):
        # Affine interpolation: this parameter is r^2, not r.
        u=lo+(hi-lo)*F(i,30)
        H=[[F(1),u,u],[u,F(1),z*z],[u,z*z,F(1)]]
        out=solve3(H,[F(1)]*3)
        den=1+z*z-2*u*u
        formula=[(1+z*z-2*u)/den,(1-u)/den,(1-u)/den]
        assert out==formula and out[0]<0 and out[1]>0 and out[2]>0
        y=[F(0),1/(1+z*z),1/(1+z*z)]
        expected=(2*u-1-z*z)**2/(2*(1+z*z)*den)
        assert objective(H,y)-objective(H,out)==expected>0
        # The inactive-coordinate KKT condition has the correct sign.
        grad0=sum(H[0][j]*y[j] for j in range(3))-1
        assert grad0>0
        checks+=3

# Dimension two: arbitrary sign of correlation, but positive optimum.
for j in range(-99,100):
    a=F(j,100)
    u=a*a
    d1,d2=F(3,7),F(17,9)
    w=F(1,1+u)
    x1,x2=w/d1,w/d2
    assert x1>0 and x2>0
    assert d1*(d1*x1+u*d2*x2)==d1
    assert d2*(u*d1*x1+d2*x2)==d2
    checks+=3

print(f"PASS: {checks} exact-rational assertions / grouped checks; analytic proof required for universal quantifiers.")
