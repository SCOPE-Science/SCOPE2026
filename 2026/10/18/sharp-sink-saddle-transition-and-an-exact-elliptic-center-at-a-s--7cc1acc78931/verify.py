#!/usr/bin/env python3
"""Finite exact checks for the symmetric three-dimensional piecewise-affine map.
The infinite-parameter and invariant-ellipse statements require the proof in RESULT.md.
Run with: python3 verify.py  (standard library only).
"""
from fractions import Fraction as F
from math import sqrt


def det3(m):
    return (m[0][0] * (m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1] * (m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2] * (m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def mv(a,v):
    return [sum(a[i][j]*v[j] for j in range(3)) for i in range(3)]


def T(a,b,v):
    x,y,z = v
    sx = 1 if x>=0 else -1
    sz = 1 if z>=0 else -1
    return [a*abs(x)+sz*y+1, b*(x+z), sx*y+a*abs(z)+1]


def branch_data(a,b):
    P = [[F(0),F(0),F(1)], [F(0),F(1),F(0)], [F(1),F(0),F(0)]]
    J = [[a,F(-1),F(0)], [b,F(0),b], [F(0),F(1),-a]]
    K = mm(P,J)
    M = mm(K,K)
    return P,J,K,M


def orbit(a,b):
    d = 1+a*a-2*a*b
    return [(1+2*b-a)/d,2*b/d,(1-2*b+a)/d]


def check_exact(a,b):
    P,J,K,M = branch_data(a,b)
    one=F(1)
    assert 0<b<1
    assert det3([[int(i==j)-M[i][j] for j in range(3)] for i in range(3)]) == (1+a*a-2*a*b)*(1+a*a+2*a*b)
    for lam in (-2,-1,0,1,2):
        assert det3([[F(lam)*(i==j)-K[i][j] for j in range(3)] for i in range(3)]) == F(lam)**3+a*a*lam-2*a*b
    u=orbit(a,b)
    v=mv(P,u)
    assert (u[0]>0 and u[2]<0)==(a<2*b-1)
    if a<2*b-1:
        assert v[0]<0<v[2]
        assert T(a,b,u)==v
        assert T(a,b,v)==u
        assert mv(M,[F(0),F(0),F(0)])==[0,0,0]
    return 1


n=0
A=[F(j,20) for j in range(-40,41,3)] + [F(-4,5),F(-5,4),F(-1),F(0),F(1,2)]
B=[F(j,20) for j in range(1,20,2)]
for a in A:
    for b in B:
        n+=check_exact(a,b)

# Three parameter types and an algebraically exact neutral point.
a,b=F(-4,5),F(1,5)
assert orbit(a,b)==[F(55,49),F(10,49),F(-5,49)]
assert a*a*(1+4*b*b)-1<0
assert F(-5,4)**2*(1+4*F(1,10)**2)-1>0

b=0.2
a=-5/sqrt(29)
s=2*a*b
assert abs(a*a+s*s-1)<1e-14
Kf=[[float(c) for c in row] for row in branch_data(a,b)[2]]

def sq(mat):
    return [[sum(mat[i][k]*mat[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]

I=[[float(i==j) for j in range(3)] for i in range(3)]
KK=sq(Kf)
q=[[KK[i][j]+s*Kf[i][j]+I[i][j] for j in range(3)] for i in range(3)]
Pc=[[I[i][j]-q[i][j]/(1+2*s*s) for j in range(3)] for i in range(3)]
v=[Pc[i][0] for i in range(3)]
Kv=[sum(Kf[i][j]*v[j] for j in range(3)) for i in range(3)]
assert max(abs(z) for z in v)>1e-5
# On the center plane K(v) = Kv and K(Kv) = -v-s Kv, and
# H(xi,eta)=xi^2-s xi eta+eta^2 is preserved by (xi,eta)->(-eta,xi-s eta).
KKv=[sum(Kf[i][j]*Kv[j] for j in range(3)) for i in range(3)]
assert max(abs(KKv[i]+v[i]+s*Kv[i]) for i in range(3))<1e-12
for xi,eta in [(0.1,0.3),(-1.1,0.4),(.5,-.7)]:
    lhs=xi*xi-s*xi*eta+eta*eta
    xi2,eta2=-eta,xi-s*eta
    rhs=xi2*xi2-s*xi2*eta2+eta2*eta2
    assert abs(lhs-rhs)<1e-12

# Every approximate trajectory in this local center plane remains in the prescribed
# two strict quadrants; this is a finite diagnostic, not the invariant-set proof.
u=[float(x) for x in orbit(a,b)]
for xi,eta in [(0.0001,0),(.00007,.00011),(-.00009,.00006)]:
    point=[u[j]+xi*v[j]+eta*Kv[j] for j in range(3)]
    for _ in range(64):
        assert point[0]>0>point[2]
        mid=T(a,b,point)
        assert mid[0]<0<mid[2]
        point=T(a,b,mid)

print(f'PASS: {n} exact rational parameter checks, 5 characteristic values each,')
print('       rational orbit identity and neutral-center quadratic invariance checks.')
