"""Independent reproducible checks for the rotated-cube Minkowski volume law.
Uses only the Python standard library; finite checks supplement an analytic proof.
"""
from itertools import product, combinations
from fractions import Fraction as F
from math import cos, sin, sqrt, pi
import random


def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def dot(a,b): return sum(x*y for x,y in zip(a,b))


def matmul(a,b): return [[dot(row,col) for col in zip(*b)] for row in a]


def transpose(a): return list(map(list,zip(*a)))


def frobentry(a): return sum(abs(x) for row in a for x in row)


def zonovol(r):
    basis=[[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]
    cols=basis+transpose(r)
    return 8.*sum(abs(det(transpose([cols[i] for i in J]))) for J in combinations(range(6),3))


def rotation(omega):
    t=sqrt(dot(omega,omega))
    if t<1.e-16: return [[float(i==j) for j in range(3)] for i in range(3)]
    x,y,z=[v/t for v in omega]
    K=[[0.,-z,y],[z,0.,-x],[-y,x,0.]]
    K2=matmul(K,K)
    return [[float(i==j)+sin(t)*K[i][j]+(1-cos(t))*K2[i][j]
             for j in range(3)] for i in range(3)]

# Enumerate all 2^9 sign matrices and construct the unique maximizer of
# tr(S^T R) from S with distinct row lines, by rational polar factors.
nonparallel=[]
maxposes=set()
for flat in product((-1,1), repeat=9):
    s=[list(flat[i*3:(i+1)*3]) for i in range(3)]
    ps=[dot(s[i],s[j]) for i,j in ((0,1),(0,2),(1,2))]
    if any(abs(x)==3 for x in ps): continue
    nonparallel.append(s)
    t=(1,-ps[0],-ps[1])
    assert ps[2]==-t[1]*t[2]
    q=[[F(s[i][j],2)+F(t[i]*sum(t[k]*s[k][j] for k in range(3)),6)
        for j in range(3)] for i in range(3)]
    qtq=matmul(transpose(q),q)
    assert qtq==[[F(i==j) for j in range(3)] for i in range(3)]
    assert all(q[i][j]*s[i][j]>0 for i in range(3) for j in range(3))
    assert frobentry(q)==5
    assert abs(det(q))==1
    assert all(sorted(abs(q[i][j]) for j in range(3))==[F(1,3),F(2,3),F(2,3)] for i in range(3))
    if det(q)==1: maxposes.add(tuple(x for row in q for x in row))
assert len(nonparallel)==192
assert len(maxposes)==96

q0=[[(-F(1,3) if i==j else F(2,3)) for j in range(3)] for i in range(3)]
s0=[[(-1 if i==j else 1) for j in range(3)] for i in range(3)]
assert tuple(x for row in q0 for x in row) in maxposes
h=matmul(transpose(q0),s0)
assert h==[[F(5,3) if i==j else -F(1,3) for j in range(3)] for i in range(3)]
assert det(h)==4
assert sum(h[i][i] for i in range(3))==5
assert matmul(h,[[F(1)] for _ in range(3)])==[[F(1)] for _ in range(3)]

# Direct 20-minor zonotope volume versus the 9-entry closed formula.
random.seed(842005)
maxerr=0.
means=[]
for k in range(250):
    w=[random.gauss(0,1) for _ in range(3)]
    R=rotation(w)
    v1=zonovol(R)
    v2=16*(1+frobentry(R))
    maxerr=max(maxerr, abs(v1-v2))
    assert abs(v1-v2)<1.e-10
    assert 64-1.e-9<=v1<=96+1.e-9
    means.append(v1)
assert abs(zonovol([[float(v) for v in row] for row in q0])-96)<1.e-10
assert abs(zonovol([[float(i==j) for j in range(3)] for i in range(3)])-64)<1.e-10

# Local quadratic deficit around maximizer, in angle-axis coordinates:
# 5-||Q0 exp(omega_x)||_entry = (3|omega|^2+(omega.u)^2)/2 + O(|omega|^3), u=(1,1,1)/sqrt(3).
qf=[[float(x) for x in row] for row in q0]
local_max=[]
for scale in (0.015,0.0075,0.00375):
    relerrs=[]
    for k in range(500):
        w=[random.uniform(-scale,scale) for _ in range(3)]
        qr=matmul(qf,rotation(w))
        deficit=5-frobentry(qr)
        pred=(3*dot(w,w)+sum(w)**2/3)/2
        if pred>0: relerrs.append(abs(deficit-pred)/pred)
    local_max.append((scale,max(relerrs)))
assert all(e<0.09 for _,e in local_max)

# Haar SO(3) near-identity Lie-algebra density equals 1/(8 pi^2).
# Exact ellipsoid coefficient per each of 96 maximizers is
# vol({24(w1^2+w2^2)+32*w3^2<eps})/(8pi^2)
# = eps^(3/2)/(576 pi sqrt(2)); the total is eps^(3/2)/(6 pi sqrt(2)).
tail=1/(6*pi*sqrt(2))
large_moment=20*sqrt(10/pi)
print('nonparallel sign matrices',len(nonparallel))
print('SO(3) maximizing rotations',len(maxposes))
print('mean volume exact',88)
print('max direct-volume discrepancy',maxerr)
print('Hessian local relative errors',local_max)
print('sharp upper-volume tail coefficient',repr(tail))
print('high moment coefficient for entrywise L1',repr(large_moment))
print('ALL CHECKS PASSED')
